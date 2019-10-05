#!/usr/bin/env python
# coding: utf-8
# In[50]:


import os
import csv

csvpath = os.path.join('..', 'Desktop', 'election_data.csv')

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    
    # Creates an empty list called poll to store our data from our csv file
    poll = []
    
    # Creates a counter to find the total votes
    totalv = 0
    
    # Creates an empty list called name to store all of the candidates for the poll
    name = []
    
    # Creates counters to find the total amount of votes for each candidates
    Kv = 0
    Cv = 0
    Lv = 0
    Ov = 0
    
    # Loops through each row in our csv file
    for row in csvreader:
        
        # Appends each row into our empty list called poll
        poll.append(row)
        
        # If the row value in our 2 column is not in our name list, it will add the value(name) into our list
        if row[2] not in  name:
            name.append(row[2])
            
        # Finds the total amount of votes for each candidate
        if row[2] == name[0]:
            Kv = Kv + 1
        elif row[2] == name[1]:
            Cv = Cv + 1
        elif row[2] == name[2]:
            Lv = Lv + 1
        elif row[2] == name[3]:
            Ov = Ov + 1
    
    # The length of our list called poll will ensure us to find the total amounts of votes
    Totalv = len(poll)
    
    # Calculates the percentage of votes for each candidate
    Kp = (Kv/ Totalv)*100
    Cp = (Cv/ Totalv)*100
    Lp = (Lv/ Totalv)*100
    Op = (Ov/ Totalv)*100
    
    # Creates a list of our percentages
    Cand =[Kp,Cp,Lp,Op]
    
    # Sets our Winner variable as 0 in order to find the largest value in our list Cand
    Winner = 0
    
    # For each percentage in our list Cand, our if statement finds the largest value within the list and stores it in our Winner variable
    for x in Cand:
        if x > Winner:
            Winner = x
            
    # Depending on the value of our Winner variable, we will be able to pair is with its corresponding candidate name
    if Winner == Kp:
        Winner = name[0]
    elif Winner == Cp:
        Winner = name[1]
    elif Winner == Lp:
        Winner = name[2]
    elif Winner == Op:
        Winner = name[3]

# Prints our results according to the style given
print("Election Results           \n-------------------------           \nTotal Votes: " + str(Totalv) + 
         "\n-------------------------"
         "\nKhan: " + str("{0:.3f}".format(round(Kp))) + "% (" + str(Kv) + ")" +
         "\nCorrey: " + str("{0:.3f}".format(round(Cp))) + "% (" + str(Cv) + ")" +
         "\nLi: " + str("{0:.3f}".format(round(Lp))) + "% (" + str(Lv) + ")" +
         "\nO'Tooley: " + str("{0:.3f}".format(round(Op))) + "% (" + str(Ov) + ")" +
         "\n-------------------------" + 
         "\nWinner: " + Winner +
         "\n-------------------------"
)

# Sets our path to home
path = "/home"

# By using path, our os.path.join will create our txt file on the user's desktop
output_path = os.path.join(path,"User/Desktop", "Election Results.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
    # Note: 'w+' allows us to create the txt file on the user's desktop if the desktop does not have PyPoll_Chengyee.txt file on it
f=open("PyPoll_Chengyee.txt", 'w+')

# Writes our reults in the txt file
f.write("Election Results           \n-------------------------           \nTotal Votes: " + str(Totalv) + 
         "\n-------------------------"
         "\nKhan: " + str("{0:.3f}".format(round(Kp))) + "% (" + str(Kv) + ")" +
         "\nCorrey: " + str("{0:.3f}".format(round(Cp))) + "% (" + str(Cv) + ")" +
         "\nLi: " + str("{0:.3f}".format(round(Lp))) + "% (" + str(Lv) + ")" +
         "\nO'Tooley: " + str("{0:.3f}".format(round(Op))) + "% (" + str(Ov) + ")" +
         "\n-------------------------" + 
         "\nWinner: " + Winner +
         "\n-------------------------"
)

# Closes our txt file
f.close()


# In[ ]:




