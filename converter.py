inputFile = open("input.txt", "r")

for line in inputFile:
	data = line[5:len(line)]
	data = data.replace(")", "")
	data = data.replace(" \n", "")
	
	noteInfo = data.split(",")
	if len(noteInfo) == 3:
		noteInfo.append(2)
	else:
		noteInfo.append(1)

	for i in range(len(noteInfo)):
		noteInfo[i] = str(noteInfo[i])

	if len(noteInfo) == 3:
		temp = noteInfo[2]
		noteInfo[2] = noteInfo[0]
		noteInfo[0] = temp
	else:
		temp = noteInfo[3]
		noteInfo[3] = noteInfo[0]
		noteInfo[0] = temp

		temp = noteInfo[2]
		noteInfo[2] = noteInfo[3]
		noteInfo[3] = temp
	
	print("{" + str(', '.join(noteInfo) + "}, "))
