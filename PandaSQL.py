# ================== install:
# pip install pandasql
# conda install pandasql

# ================== Libraries: 
# for pandasql 
# import pandasql as ps

# related 
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# sns.set()



# ================== Important SQL Commands:
# SELECT - extracts data from a database
# UPDATE - updates data in a database
# DELETE - deletes data from a database
# INSERT INTO - inserts new data into a database
# CREATE DATABASE - creates a new database
# ALTER DATABASE - modifies a database
# CREATE TABLE - creates a new table
# ALTER TABLE - modifies a table
# DROP TABLE - deletes a table
# CREATE INDEX - creates an index (search key)
#  DROP INDEX - deletes an index


# ==================  Methods:
# Load: 
df_shootings = pd.read_csv('shootings.csv')
df_states = pd.read_csv('shootings_states.csv')


# Comment 
"""
/comment/
"""

# SELECT 
ps.sqldf("""
SELECT id, 
       date 
FROM df_shootings 
LIMIT 2
""")

ps.sqldf("""
SELECT *
FROM df_shootings 
WHERE state = 'VT'
""")

# WHERE
ps.sqldf("""
SELECT date
FROM df_shootings 
WHERE state = 'VT'
""")

ps.sqldf("""
SELECT *
FROM df_shootings 
WHERE state = 'KS' AND ( 
              arms_category = 'Unarmed' 
              OR 
              arms_category = 'Other unusual objects'
              )
""")


# ORDER BY
ps.sqldf("""
SELECT *
FROM df_shootings 
ORDER BY age DESC, 
         date DESC
LIMIT 10
""")


# GROUP BY
ps.sqldf("""
SELECT gender,
       COUNT(*)
FROM df_shootings 
GROUP BY gender
""")

ps.sqldf("""
SELECT date,
       COUNT(*)
FROM df_shootings 
GROUP BY date
ORDER BY COUNT(*) DESC
LIMIT 5
""")


# MIN AVG MAX
ps.sqldf("""
SELECT threat_level,
       MIN(age),
       AVG(age), 
       MAX(age)
FROM df_shootings 
GROUP BY threat_level
""")

# HAVING
ps.sqldf("""
SELECT race,
       flee,
       COUNT(*)
FROM df_shootings 
GROUP BY race, 
         flee
HAVING COUNT(*) > 75
ORDER BY flee, race
""")


# CAST SUM AS
ps.sqldf("""
SELECT race,
       CAST(SUM(signs_of_mental_illness) AS FLOAT) / COUNT(*) AS ratio,
       SUM(signs_of_mental_illness) AS signs_of_mental_illness_count,
       COUNT(*) AS total_count
FROM df_shootings 
GROUP BY race
ORDER BY ratio DESC
""")

ps.sqldf("""
         Points +100 AS discounts_factors
         Or As 'discounts factors' 
         """)


# STRFTIME
query46 = ps.sqldf("""
SELECT STRFTIME('%Y', date) AS year,
       flee,
       CAST(SUM(signs_of_mental_illness) AS FLOAT) / COUNT(*) AS ratio
FROM df_shootings 
GROUP BY year, flee
ORDER BY year ASC
""")

query46


# pivot_table plot
ax = query46.pivot_table(index='year', columns='flee', values='ratio') \
            .plot(title='Ratio of mental illness over time by flee method', figsize=(16, 4))


# INNER JOIN 
ps.sqldf("""
SELECT region,
       COUNT(*)
FROM df_shootings 
INNER JOIN df_states ON df_shootings.state = df_states.state
GROUP BY region
""")

# INNER JOIN WHERE LIKE OR
ps.sqldf("""
SELECT state_long,
       COUNT(*)
FROM df_shootings 
INNER JOIN df_states ON df_shootings.state = df_states.state
WHERE df_states.state_long LIKE 'New%'
OR df_states.state_long LIKE 'North%'
GROUP BY df_states.state
""")


# INNER JOIN USING 
ps.sqldf("""
SELECT city,
       df_states.state_long,
       COUNT(*)
FROM df_shootings 
INNER JOIN df_states USING (state)
WHERE df_states.region = 'south'
GROUP BY city
ORDER BY COUNT(*) DESC
LIMIT 10
""")

# OUTER JOIN
"""
Select *
From customers c
Left join orders 
On c.customer_id = o.customer_id
Order by c.customer_id 

# so even though the customer do not have an order it will show all the result as you ask for all results in the customer table 
If you write right instead then you will get all the results from orders table
"""


# CASE
ps.sqldf("""
SELECT COUNT(*),
       CASE 
              WHEN STRFTIME('%m', date) < '07' THEN 'first'
              ELSE 'last'
       END first_or_last
FROM df_shootings
GROUP BY first_or_last
""")


# WITH CROSS JOIN
ps.sqldf("""
WITH first_six AS (
       SELECT COUNT(*) AS count,
              STRFTIME('%m', date) AS month
       FROM df_shootings
       WHERE month < '07'
), 
last_six AS (
       SELECT COUNT(*) AS count,
              STRFTIME('%m', date) AS month
       FROM df_shootings
       WHERE month >= '07'
)

SELECT first_six.count AS first_six_count,
       last_six.count AS last_six_count

FROM first_six CROSS JOIN last_six
""")


# IN ROUND ||

"""
Where State='av' or State= 'mn' or State ='bv'
Is the same as
Where State In ('av', 'mn', 'bv') 
"""
                
ps.sqldf("""
WITH first_three AS (
       SELECT state,
              COUNT(*) AS count,
              AVG(age) AS avg_age
       FROM df_shootings
       WHERE STRFTIME('%Y', date) IN ('2015', '2016', '2017')
       GROUP BY state
), 
last_three AS (
       SELECT state,
              COUNT(*) AS count,
              AVG(age) AS avg_age
       FROM df_shootings
       WHERE STRFTIME('%Y', date) IN ('2018', '2019', '2020')
       GROUP BY state
)

SELECT state_long,
       ROUND(first_three.avg_age, 2) || ' (' || first_three.count || ')' AS '2015 to 2017',
       ROUND(last_three.avg_age, 2) || ' (' || last_three.count || ')' AS '2018 to 2020'
FROM first_three

INNER JOIN last_three USING (state)

INNER JOIN df_states USING (state)

WHERE first_three.count > 40 AND last_three.count > 40

ORDER BY state
""")

clean_transactions\
       .groupBy(['company', 'year', 'quarter'])\
       .agg(f.sum('price').alias('purchases'))





# ================== NAME:

"""
Gives the name that start with b 
Where last_name like 'b%' 
'%b%' have a b in the name 


_ = one character 
So '__y' = two characters and then y


Where last_name REGEXP 'b' 
By using REGEXP you don't need to add %
And you Can search for multiple variables 
REGEXP 'field | mac '


REGEXP '[gim]e' the name includes ge,ie or me
[a-h] = a to h

"""

# ================== MATH:
""" 
points >1000 and points<3000 
the same as 
Where points between 1000 and 3000
"""

"""
Here we got the one that do not have number 
Where phone is null 
"""

"""
Limit 10 give the first 10 results 
Limit 6,3 don’t show the first 6 and give the next three so 7-9
"""


"""
Remove duplicate values from a specified result set and only return the unique values
SELECT DISTINCT Country FROM Customers
"""

"""
By using the DISTINCT keyword in a function called COUNT, we can return the number of different countries.
SELECT COUNT(DISTINCT Country) FROM Customers;
"""

"""
Sort the products from highest to lowest price:
ORDER BY Price DESC;
"""

# ================== ADD/EXISTS DATA:
"""
Insert into products (name, quantity_in_stock, unit)
Values ('product1', 10, 6)
        ('product2', 10, 2)
        ('product3', 11, 5)
"""


"""
Make a new table where you copy sth from one table to another 

Create table orders_archived 
Select * 
from orders 
Where order_date < '1990-01-01'
"""

"""
The following SQL statement lists the number of customers in each country. Only include countries with more than 5 customers:
SELECT COUNT(CustomerID), Country
FROM Customers
GROUP BY Country
HAVING COUNT(CustomerID) > 5;
"""

"""
The EXISTS operator is used to test for the existence of any record in a subquery.

SELECT column_name(s)
FROM table_name
WHERE EXISTS
(SELECT column_name FROM table_name WHERE condition)
"""
# ================== UpDATE/DELETE DATA:

"""
Update invoices 
Set payment_total = 10, payment_date= '2019-01-01'
Where invoice_id =1
"""

"""
DELETE Statement
DELETE FROM Customers WHERE CustomerName='Alfreds Futterkiste'
"""
