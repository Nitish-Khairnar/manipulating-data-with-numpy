# --------------
import numpy as np
from collections import Counter

data= np.genfromtxt(path,dtype = str, delimiter= ",", skip_header=1)
# Not every data format will be in csv there are other file formats also.
# This exercise will help you deal with other file formats and how toa read it.

# Number of unique matches 
print("the no of uniques matches ",np.unique(data[:,0]).size)


 # How many matches were held in total we need to know so that we can analyze further       statistics keeping that in mind.
print("the no of matched held ",np.unique(data[:,0]).size)
# Number of unique teams
team1=data[:,3]
team2=data[:,4]
print("unique teams are ", np.unique(np.concatenate((team1, team2))).shape[0])
 # this exercise deals with you getting to know that which are all those six teams that   played in the tournament.

# Sum of all extras
print(" The sum of all extras ", np.sum(data[:,-6].astype(np.int64)))
# An exercise to make you familiar with indexing and slicing up within data.

# Delivery number when a given player got out

# Get the array of all delivery numbers when a given player got out. Also mention the wicket type.
print("When plater got out", [ (j,k) for i,j,k in zip(data[:,-3], data[:,-12], data[:,-2]) if len(i)>0])
# Number of times Mumbai Indians won the toss
print(np.unique(data[data[:,5]=='Mumbai Indians'][:,0]).shape[0])
# this exercise will help you get the statistics on one particular team

# Filter record where batsman scored six and player with most number of sixex
Dict1=Counter(data[data[:,-7].astype(np.int64)==6][:,-10])
for key, val in Dict1.items():
    if val==max(Dict1.values()):
        print("The batsman with max sixes are ",key,val)
# An exercise to know who is the most aggresive player or maybe the scoring player 







