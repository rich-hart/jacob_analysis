import matplotlib.pyplot as plt

DATA_FILE_PATH = './Bimodal_Data.csv'






# laod and save the data as a list of values

with open(DATA_FILE_PATH) as file:
    data = []
    for line in file:
        entries = line.split(',')
        first_entry = entries[0]
        try:
            value = float(first_entry)
        except ValueError:
            value = None
        if value is not None:
            data.append(value)







# sort the list of values
data.sort()
data_copy = data[:]

y_diff_list = []


#remove the first value from the list

y_1 = data.pop(0)                                

#####################################################
# Jacob: this is where the weird trend in your      #
# dataset comes from.  What the 'while' function is #
# doing is finding the difference between every     #
# value in your sorted data set and saving those    #
# values into a new list.  Then those values are    #
# plotted.  There is a clear pattern dataset        #
# which I can't explain.  Maybe you can.            #
#####################################################
while data:
    y_2 = data.pop(0)                             
    y_diff_list.append(abs((float(y_2)-float(y_1)))) 
    y_1=y_2                                  



max_y_diff = max(y_diff_list)

# ALso not that in the diffdataset the max value in the 
# difference list is MUCH greater than the limits
# of the plot that is shown. 

print("max value in the difference list: "+str(max_y_diff))


plt.ylim(0,.2)    
plt.plot(y_diff_list,'bo')

plt.show()

