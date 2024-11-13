# """
# @author: Hadeel Moustafa
# Numpy notes
# """

# #################################
# # to learn NumPy
# #################################
# Introduction to NumPy Course | DataCamp


# #################################
# # libraries:
# #################################
# import numpy as np

# #################################
# # universal functions:
# #################################
# See numpy universal functions

# #################################
# # build:
# #################################
# # format 
# v=np.array([v0,..,vn])
# v=np.array(ls)
# v=np.zeros(Nr) ->  np.zeros((3,2))
# v=np.ones(Nr) 
# v=np.empty(Nr)
# v=np.random.random(Nr)
# v=np.arange(Nr)   

# # linspace:
# v=np.linspace(startNr,endNr,nr_Of_Elements_Within_The_Interval)  

# # range of steps
# v=np.arange(start=2,stop=17,step=4)                             

# # random array 
# v=np.random.randint(maxNr,size=nr)

# #################################
# # print:
# #################################
# print(type(v))
# print(array.shape)
# print(array.dtype)

# #################################
# # slicing 
# #################################

# # get
# v[index]
# v[-1]

# # range slicing
# v[sartIndex:endIndex]

# # step slicing
# v[0::2] """ start:end:step """

# # conditional slicing
# v[v arithmeticLogicalOperator nr]

# example
# v = np.array([10, 20, 30, 40, 50])
# v[v>20]




# #################################
# # math:
# #################################
# # arithmetic operations element wise  
# v1 arithmeticOperator v2

# example
# Create two NumPy arrays
# Addition: v1 + v2
# Subtraction: v1 - v2
# Multiplication: v1 * v2
# Division: v1 / v2
# Exponentiation: v1 ** 2
# Modulus: v1 % 2


# # arithmeticLogical element wise
# v arithmeticLogicalOperator nr  

# example
# Needs only one NumPy array
# Logical Greater Than: v > nr
# Logical Less Than: v < nr
# Logical Equal To: v == nr
# Logical Not Equal To: v != nr
# Logical AND: (v > 2) & (v < 5)
# Logical OR: (v < 2) | (v > 4)
# Logical NOT: ~(v > nr)

# # dot product
# v1 @ v2 or np.dot(v1, v2)

# # min/max value 
# np.max(v)
# np.min(v)

# # index of max/min value
# np.argmax(v)
# np.argmin(v)                                        

# # return sum/product of elements 
# np.sum(v) """ also used to count true"""
# np.prod(v)

# # sin/cos
# np.sin(v)
# np.cos(v)

# # Stat:
# np.mean(v)  #The mean (or average)
# np.var(v) #The variance measures the average squared deviation from the mean. 
# np.std(v) #The standard deviation measures the amount of variation or dispersion in the array -> std= sqr(Variance)



# # Transpose
# v[::-1]    #This syntax reverses the array along its last axis. 
             # For a 1D array, it reverses the order of the elements. 
             # For a 2D array, it reverses the rows of the array, but the columns remain in their original order.
# v.t

# #################################
# # Diminsions
# #################################

# # length 
# len(v)

# # get diminsions 
# v.shape

# # change to one colomn Matrix 
# v.shape=(len(v),1)
#or
# v_new = v.reshape(-1, 1)




# # reshape 
# v.reshape(2,2)                                                 



# #################################
# # More
# #################################
# np.where(condition, replaceValueIfTrue, replaceValueIfFalse)

# example
# v = np.array([1, 4, 6, 8, 10])
# np.where(v > 5, 99, 0)
# [ 0  0 99 99 99]

# #################################
# # Matrixs: (use the arrays commands) see exer0
# #################################

# # build 
# M=np.array([[rowArray0],..,[rowArrayN]])

# # slicing 
# M[startRow:endRow,startCol:endCol] 
# M[::2,::2] """ start:end:step """

# # get the shape  
# M.shape 

# # Transpose
# M.T 

# # inverse
# np.linalg.inv(v)
