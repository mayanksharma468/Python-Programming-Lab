def swapList(list):
	get = list[-1], list[0]
	list[0], list[-1] = get
	
	return list
newList = [12, 35, 9, 56, 24]
print(swapList(newList))
