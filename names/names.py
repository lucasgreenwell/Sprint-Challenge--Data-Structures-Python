import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates =  [] # Return the list of duplicates in this data structure

#5.97 seconds
# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

#1.51 seconds
for i in range(len(names_1)):
    if names_1[i] in names_2:
        duplicates.append(names_1[i])



end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

#duplicates = set(names_1).intersection(names_2)
##Not sure how fast you want it to go but i was able to get it down to .003 seconds and running in linear time based on the length of the two lists
## O(len(list1) + len(list2))