#Gianpaolo Pittis

import random

Unsorted_List = []

for x in range(100):
	Unsorted_List.append(random.randint(0, 10000))
	
print(Unsorted_List)

escape_variable = False

while escape_variable == False:
	corrections = 0
	for y in range(len(Unsorted_List)-1):
		if Unsorted_List[y] > Unsorted_List[y+1]:
			temp = Unsorted_List[y]
			Unsorted_List[y] = Unsorted_List[y+1]
			Unsorted_List[y+1] = temp
			corrections = corrections + 1
	if corrections == 0:
		escape_variable = True

sorted_list = Unsorted_List
print("")
print(sorted_list)