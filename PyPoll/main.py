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
    
    poll = []
    totalv = 0
    
    name = []
    
    Kv = 0
    Cv = 0
    Lv = 0
    Ov = 0
    
    for row in csvreader:
        poll.append(row)
        if row[2] not in  name:
            name.append(row[2])
        if row[2] == "Khan":
            Kv = Kv + 1
        elif row[2] == "Correy":
            Cv = Cv + 1
        elif row[2] == "Li":
            Lv = Lv + 1
        elif row[2] == "O'Tooley":
            Ov = Ov + 1
            
    Totalv = len(poll)
    
    Kp = (Kv/ Totalv)*100
    Cp = (Cv/ Totalv)*100
    Lp = (Lv/ Totalv)*100
    Op = (Ov/ Totalv)*100
    
    Cand =[Kp,Cp,Lp,Op]
    Winner = 0
    for x in Cand:
        if x > Winner:
            Winner = x
    if Winner == Kp:
        Winner = name[0]
    elif Winner == Cp:
        Winner = name[1]
    elif Winner == Lp:
        Winner = name[2]
    elif Winner == Op:
        Winner = name[3]
    
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

path = "/home"
output_path = os.path.join(path,"User/Desktop", "Election Results.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
f=open("PyPoll_Chengyee.txt", 'w+')

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
f.close()


# In[ ]:




