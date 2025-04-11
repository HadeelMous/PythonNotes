# """
# @author: Hadeel Moustafa
# Matplotlib Notes 
# """
# #################################
# # 0. library: 
# #################################
# from operator import imod
# import IPython
# from IPython.lib.display import YouTubeVideo
# from matplotlib import pyplot as plt, style


# #################################
# # 1. CurvePlot:
# #################################

# # ax
# plt.gca()  -> get current axes

# example
# plt.plot([1, 2, 3, 4], [10, 20, 25, 30])
# ax = plt.gca()
# plt.show()

# # Cordenates:
# x1 = [ls]
# y1 = [ls]   

# # figure size
# plt.figure(figsize=(8, 8))

# # Plot command:
# plt.plot(x1,y1,'abbrToColor',label="string",linewidth=nr)

# # same graph
# x2 = [ls]
# y2 = [ls]
# plt.plot(x2,y2,'abbrToColor',label="string",linewidth=nr)    


# # abbrToColor: A string that specifies both the color and style of the line 
# color
# """
# green   =   'g' 
# blue    =   'c' 
# black   =   'k' 
# pink    =   'm' 
# red     =   'r'
# or
# color   =   'tab:gray'
# """

# style
# """
# '-': Solid line (default)
# '--': Dashed line
# '-.': Dash-dot line
# ':': Dotted line
# """

# Markers
# """
#'o': Circle
#'s': Square
#'^': Triangle
# """

# # Shaded for error
# A shaded region between two curves is commonly used to visualize uncertainty or error margins around a plot line.
# plt.fill_between(x, y1, y2) 
# plt.fill_between(xs, y-std, y+std, color='blue', alpha=0.2, label='±1 std dev')


# # vertical line
# plot a vertical line at a fixed x-coordinate, spanning from a lower y-coordinate (y_low) to a higher y-coordinate (y_high)
# plt.plot([x_fix, x_fix], [y_low,y_high], c="black")

# # horizontal line
# plot a horizontal line at a fixed y-coordinate (y_fix), spanning from a left x-coordinate (x_left) to a right x-coordinate (x_right)
# plt.plot([x_left, x_right], [y_fix,y_fix], c="black")

# # line 
# plot a straight line between two points
# plt.plot([x1,x2], [y1,y2], c="black")

# # write inside the figure:
# x_where=2
# y_where=5
# plt.annotate(s="$\mu$",xy=(x_where + 0.1 , y_where + 0.1), size=20)

# # title
# plt.title("$Latex$ string")

# # curve and axis info:
# plt.ylabel("string")
# plt.xlabel("string")

# # ticks
# set where the ticks should appear (positions) and what labels should be displayed at those tick positions
# plt.xticks(ticks=bins, labels=labels)
# plt.xticks(x, str_lst,rotation='vertical')
# plt.yticks(y, str_lst,rotation='vertical')
# """
# ticks = np.arange(start, stop, step) same as np.arange(0,len(Data.select_dtypes(exclude=object).columns),1) 
# ax.set_xticks(ticks)
# ax.set_yticks(ticks)
# ax.set_xticklabels(['Zip', 'LAT.', 'LONG.', 'Injured','killed', 'Response', 'Year', 'Month', 'Day', 'Hour','Minute', 'S.L.M.', 'Pre.', 'S.F.','S. D.', 'F.S.H.', 
# """



# # log(y)
# set the y-axis to a logarithmic scale, which is useful when working with data spanning several orders of magnitude. 
# plt.yscale('log')

# # show label    
# A legend helps identify different lines, markers, or elements in your plot by associating them with labels.
# plt.legend()                                                 

# # Squares
# adds grid lines to the plot, making it easier to read and interpret the data. 
# plt.grid(True,color='k')

# # Show the plot
# plt.show()                                                       


# #################################
# # 2. scatterPlot: 
# #################################
# #cordenates:
# x1 = [ls]
# y1 = [ls]   
    
# # plot command:
# used to display individual data points without connecting them with lines where Each Point is Independent
# plt.scatter(x,y,alpha=0.1,color='abbrToColor',marker="abbrToMarker")    
# plt.plot(): Creates a line plot, which is typically used to show trends over time or continuous data, connecting data points with lines           



# or
# ax = plt.axes()

# ax.scatter(data.sepal_length, data.sepal_width)

# # Label the axes
# ax.set(xlabel='Sepal Length (cm)',
#        ylabel='Sepal Width (cm)',
#        title='Sepal Length vs Width');
# #################################
# # 3. BarGraph: 
# #################################
# # cordenates:
# x = [ls]
# y = [ls]   
    
# # plot command:
# plt.bar(x,y)
# plt.bar(x, y, color='purple', edgecolor='black', linewidth=1.5, width=0.6)

# Adding Values on Top of Bars
#for i in range(len(x)):
#    plt.text(i, values[i] + 1, str(values[i]), ha='center')
  
# #################################
# # 4. hist:
# #################################
# L = [lst]
# plt.hist(L, bins=100, density=True)


# data is the csv file, then you do a hist for all features in one plot
# ax = data.plot.hist(bins=25, alpha=0.5)
# ax.set_xlabel('Size (cm)');

# To create x separate plots, use Pandas `.hist` method
# axList = data.hist(bins=25)

# # Add some x- and y- labels to first column and last row
# for ax in axList.flatten():
#     if ax.is_last_row():
#         ax.set_xlabel('Size (cm)')
        
#     if ax.is_first_col():
#         ax.set_ylabel('Frequency')

# #################################
# # 5. multiple plots:
# #################################
# # enumerate 
# # https://stackoverflow.com/questions/12319796/dynamically-add-create-subplots-in-matplotlib
# # Set figure para
# Tot  = len(repos_file_names.keys())
# Cols = 2
# # Compute Rows required
# Rows = Tot // Cols 
# Rows += Tot % Cols
# # Create a Position index (The Position of each subplot)
# Position = range(1,Tot + 1)
# # Create main figure
# fig = plt.figure( figsize = (Cols*4, Rows*4)) # Adjust figure size based on number of subplots
# plt.subplots_adjust(hspace=0.25) # Adjust space between subplots
# fig.suptitle(f'File Distribution for Multiple Repositories', fontsize=10) # Super title for the whole figure

# # Loop (Loop through each repository to create pie charts)
# for k in range(Tot):
# or 
# for k, (repo, files) in enumerate(repos_file_names.items()):
# Get the corresponding file sizes for each repo
#     sizes = file_sizes[repo]
#     labels = files
#     ax = fig.add_subplot(Rows,Cols,Position[k])
#     ax.pie(sizes, labels=labels, autopct='%1.0f%%', pctdistance=1.1, labeldistance=1.2, startangle=90)
#     ax.set(title=f'{repo}', fontsize=12)
# plt.show()


    
# example 2
#x = np.arange(0, 10, 0.1)
#y = [np.sin(x), np.cos(x), np.tan(x), np.sqrt(x)]

# Create a figure with 2 rows and 2 columns of subplots
#fig, axs = plt.subplots(#nr_row, #nr_col, figsize=(15, 20), sharex=True)
#fig, axs = plt.subplots(2, 2, figsize=(10, 8))
#fig.suptitle('Trigonometric Functions', fontsize=16)

# Titles for each subplot
#titles = ['Sine', 'Cosine', 'Tangent', 'Square Root']

# Loop through each subplot and plot different data
#for i, ax in enumerate(axs.flat):
#    ax.plot(x, y[i], 'r-', linewidth=2)  # Line plot in each subplot
#    ax.set_title(titles[i])  # Add title to each subplot
#    ax.set_xlabel('X-axis')
#    ax.set_ylabel('Y-axis')
    
# Add text annotation inside each subplot
#    ax.text(0.5, 0.5, titles[i], fontsize=12, transform=ax.transAxes, 
#            ha='center', color='blue')

# Adjust y-axis limit for the tangent plot to avoid extreme values
#    if titles[i] == 'Tangent':
 #       ax.set_ylim(-10, 10)

# Adjust layout to prevent overlap
#plt.tight_layout(rect=[0, 0, 1, 0.95])

  
# Summary 
# fig, axs = plt.subplots(#nr_row, #nr_col, figsize=(15, 20), sharex=True)
# fig.suptitle('super-title', fontsize=20)
# for i,ax in enumerate(axs.flat):
#     ax.set(title='sub-title')
#     plt.plot(x[i],x[i],'abbrToColor',label="string",linewidth=nr,ax=ax)

# # more function for the subplots (ax in the for loop above) 
# axs[i].text(-0.3, y[i].max()*1.1, 'crime', fontsize=16) #writing in the subplot
# axs[i].set_ylim(0, counts.max()*1.4)
# axs[i].set_ylabel('Crime count')
# axs[i].set_xlabel('Weekdays')
# axs[i].set_xticklabels(counts.index, rotation=-10)





# #################################
# # 6. Style:
# #################################
# from matplotlib import style
# style.use("ggplot")    #have more muted colors and uses a solid grid background.                                        

# import seaborn as sns
# sns.set() #modern feel with a lighter background and softer grid lines.

# #################################
# # 7. Jitter plot
# #################################
# import seaborn as sns # for jitter plot
# plt.figure(figsize=(8, 8))
# sns.stripplot(data_WL['Time'].values, jitter=True, edgecolor='none', alpha=.50 ,color='k').set_title('Robbery\nJan to Jul\n13:00-14:00')
# plt.show()


# #################################
# # Examples: 
# #################################

# """ 1 """
# plt.figure(figsize=(8,6)) # define the figure size 
# #plt.title('Title Needed') # Having a title is always needed for plots :) 
# plt.ylabel('$E_{1D} - E_{bulk}$  (eV/atom)')
# plt.xlabel('$s_{0} + s_{01} + s_{1}$') # The '$' signs allow to use latex formated string

# plt.xlim([0.5, 1]) # Set x-axis range 
# ax = plt.gca() # Take the plot needed to play with xticks 
# bins = np.arange(0.5, 1.05, 0.1) # Define the bins - Here we have as a max limit 1.05 to include 1 
# bins_labels = [str(np.round(i,1)) for i in bins] # Define the bins as list of string items - Here we do round to 1 dec to prevent having to many decimals in the plot due to machine error  
# ax.set_xticks(bins) # This is our xticks
# ax.set_xticklabels(bins_labels) # This is what we want to show instead of our xticks (Here by chance the replaced one and xticks are the same but in general this could be any list of string that have the same size as our xticks)

# inds  = np.digitize(x,bins) # Return the indices (place) of the bins to which each value from input array x belongs
# means = [np.mean(y[inds==i]) for i in list(set(inds))] # Calculate the means ask if needed 
# stds   = [np.std(y[inds==i], ddof=1) for i in list(set(inds))] # Calculate the std ask if needed
# delta = bins[1]-bins[0] # to center of each bin 
# mid_bins = bins - delta/2 # Center of each bin
# mid_bins = mid_bins[1:] # need to be deleted since it is less than the left bordar of the first bin

# plt.plot(x,y,'bo',markersize=2) # Plot x vs y values
# plt.errorbar(mid_bins, means, stds, linestyle='None', marker='o', color='r') # Plot mean and standard deviation
# plt.grid(True) # squares in the plot 
# plt.savefig('Title Needed') # save to same directory 
# plt.show() 


# """ 2 density """
# def Visual_Histogram(x, n_bins = 10):
#     bins = np.linspace(min(x), max(x), n_bins + 1)    
#     weights = np.ones(len(x))/len(x)
#     plt.hist(x, n_bins, weights=weights, ec='black') # ec short for "edgecolor"
#     plt.title("Density Histogram")
#     plt.xlabel("Classes")
#     plt.xticks(ticks=bins, labels=[str(xi) for xi in np.round(bins,2)])
#     plt.ylabel("Density")
#     plt.show()
# Visual_Histogram(x, n_bins = 10)



# def density_Histogram(x, n_bins = 10, figsize=(10,6), title= "Density Histogram", xlabel= 'Classes', ylabel='Density', xticks=False):
#     plt.figure(figsize=figsize)
#     n_bins = n_bins
#     bins = np.linspace(min(x), max(x), n_bins + 1)    
#     weights = np.ones(len(x))/len(x)
#     plt.hist(x, n_bins, weights=weights, ec='black') # ec short for "edgecolor"
#     plt.title(title)
#     plt.xlabel(xlabel)
#     if xticks : plt.xticks(ticks=bins, labels=[str(xi) for xi in np.round(bins,2)])
#     plt.ylabel(ylabel)
#     plt.show()


# from IPython import YouTubeVideo
# YouTubeVideo()


# """ 3 """
# # Build the plot
# fig, ax = plt.subplots(figsize=(10,6))
# ax.bar(crimes, means, yerr=stds, align='edge', width=0.8, alpha=0.5, ecolor='black', capsize=5)
# ax.set_ylabel('Mean')
# ax.set_xlabel('Crime')
# ax.set_xticks(range(len(crimes)))
# ax.set_xticklabels(crimes,rotation=90)
# ax.set_title('Crime per year by category')

# # Build the plot
# plt.figure(figsize=(10,6))
# plt.bar(crimes, 
#         means,
#         width=0.9,
#         alpha=0.5, 
#         color='green',
#         label='mean')
# plt.errorbar(crimes, 
#         means,
#         yerr= stds, 
#         ecolor='black', 
#         capsize=3,
#         fmt='none',
#         label='std')
# plt.xticks(crimes, crimes, rotation='vertical')
# plt.ylabel('Mean')
# plt.xlabel('Crime')
# plt.title('Crime per year by category')
# plt.legend()
# plt.show()



# """ more """
# import matplotlib as mpl
# mpl.rcParams.update(mpl.rcParamsDefault)

# from matplotlib.pyplot import style
# style.use('ggplot')

# %matplotlib inline

# from IPython.display import display
# from IPython import get_ipython
# get_ipython().run_line_magic('matplotlib', 'inline')


# ax = plt.gca()
