import csv
import os
import sys

def readCSV(csvFile):
	res =[]
	csvReader = csv.reader(csvFile)
	for row in csvReader:
		res.append(row)
	return res

def getCommonColumnIndex(read,commonColumn):
	commonColumnIndex = -1
	l = len(read[0])
	for i in range(0,l):
		if (read[0][i] == commonColumn):
			commonColumnIndex = i

	if (commonColumnIndex == -1):
		raise Exception("common Column doesn't exist")

	return commonColumnIndex



def mapAllColumnsToCommonColumn(read,commonColumnIndex):

	map={}
	
	l = len(read)
	for i in range(1,l):

		key = read[i][commonColumnIndex]
		if key not in map:
			temp=[]
			temp.append(read[i])
			map[key]=temp
			
		else:
			print "duplicate rows are existing"
			
			'''Handled duplicate rows by using list of list'''


			map[key].append(read[i])
	
	return map


def sameColumnsInBothCsv(read1,read2):

	same=[]

	l1=len(read1[0])
	l2=len(read2[0])

	for i in range(0,l1):
		for j in range(0,l2):
			if (read1[0][i]==read2[0][j]):
				same.append(j)
		
	return same

def merge(map1,map2,same,read1,read2):
	res=[]

	temp = read1[0]
	for j in range(0,len(read2[0])):
		if j not in same:
			temp.append(read2[0][j])

	res.append(temp)

	for key in map2:
		if key in map1:

			p=len(map1[key])
			q=len(map2[key])

			for j in range(0,p):

				for k in range(0,q):
					temp=(map1[key][j][:])
					for l in range(0,len(map2[key][k])):
					 	if l not in same:
					 		temp.append(map2[key][k][l]) 
					 	
					res.append(temp)

	#print res
	return res

def get_csv_filenames(path):
	suffix=".csv"
	filenames=os.listdir(path)
	return [ filename for filename in filenames if filename.endswith(suffix) ]

def mergeAll(listOfCsv,commonColumnName):
	if(len(listOfCsv)==0):
		raise Exception("No CSV files found!!")
	f1 = open(listOfCsv[0])
	read1 = readCSV(f1)

	for i in range(1,len(listOfCsv)):
		f2 = open(listOfCsv[i])
		read2 = readCSV(f2)
		
		commonColumnIndex1 = getCommonColumnIndex(read1,commonColumnName)
		commonColumnIndex2 = getCommonColumnIndex(read2,commonColumnName)

		map1=mapAllColumnsToCommonColumn(read1,commonColumnIndex1)
		map2=mapAllColumnsToCommonColumn(read2,commonColumnIndex2)

		same=sameColumnsInBothCsv(read1,read2)
		read1=merge(map1,map2,same,read1,read2)
		

	return read1

def writeOutputCsv(read):
	with open('output.csv', 'wb') as fp:
	    writer = csv.writer(fp, delimiter=',')
	    writer.writerows(read)



# give path here, default is current directory
path = os.getcwd()
if (len(sys.argv)==1):
	raise Exception("Please give the common Column Name in command line!")
commonColumnName = sys.argv[1]

listOfCsv = get_csv_filenames(path)
output=mergeAll(listOfCsv, commonColumnName)
writeOutputCsv(output)
