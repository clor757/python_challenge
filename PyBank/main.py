# In[1]:




# CHENGYEE LOR
import os
import csv

csvpath = os.path.join('..', 'Desktop', 'budget_data.csv')

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)

    # Set our variables to 0 in order to store certain values
    net_total = 0
    total_month = 0
    prev1 = 0
    
    # Allows us to append our results from our loops to an empty list
    change = []
    Bank = []
    
    # Read each row of data after the header
    for row in csvreader:
        
        # Appends each row in our file to our list called Bank
            # Allows us to refer back to a list called Bank
        Bank.append(row)
        
        # For each row (excluding the header) in our file, performs a counter to add 1
        total_month = total_month + 1
        
        # Adds up each value in each row for Profits/Losses
        net_total = net_total + int(row[1])
        
        # First, takes the value of prev1 minus the value of the second column of the row which the loop is on
        # Second, appends the results of this into our list called change
        # Third, Stores the previous row into variable prev1
        if int(row[1]) != prev1:
            x = int(row[1])-prev1
            change.append(x)
            prev1 = int(row[1])
            
    # Give our variable prev2 and inital value and a place to store our results
    prev2 = 0
    
    # For each index in change, if the current row of the loop is greater than the previous row
    #then it is stored into prev2. Once we find our greatest value in change, we look for the index number of this greatest
    #value and assign it to the variable a
    for x in change:
        if x > prev2:
            prev2=x
            a=change.index(prev2)
                    
    # For each index in change, if the current row of the loop is greater than the previous row
    #then it is stored into prev3. Once we find our smallest value in change, we look for the index number of this smallest
    #value and assign it to the variable b
    prev3 = 0
    for x in change:
        if x < prev3:
            prev3=x
            b=change.index(prev3)

        # Calculate the average change by using the first value of profits/lossses to the last value
        # Note: we must perform total_month-1 to account for comparing each row of profits/losses to the next row
        average_change = (int(Bank[85][1])-int(Bank[0][1]))/(total_month-1)

# Good ole print function to save the day
print("Financial Analysis           \n----------------------------           \nTotal Months: " + str(total_month) + 
         "\nNet Total: $" + str(net_total) +
         "\nAverage Change: $" + str("{0:.2f}".format(average_change)) +
         "\nGreatest Increase in Profits: " + str(Bank[a][0]) + " ($" + str(prev2) +")" 
         "\nGreatest Decrease in Profits: " + str(Bank[b][0]) + " ($" + str(prev3) +")"  +
         "\n----------------------------" )

path = "/home"
output_path = os.path.join(path,"User/Desktop", "Financial Analysis.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
f=open("PyBank_Chengyee.txt", 'w+')

f.write("Financial Analysis           \n----------------------------           \nTotal Months: " + str(total_month) + 
         "\nNet Total: $" + str(net_total) +
         "\nAverage Change: $" + str("{0:.2f}".format(average_change)) +
         "\nGreatest Increase in Profits: " + str(Bank[a][0]) + " ($" + str(prev2) +")" 
         "\nGreatest Decrease in Profits: " + str(Bank[b][0]) + " ($" + str(prev3) +")"  +
         "\n----------------------------")
f.close()

