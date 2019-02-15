#######################################################
# Title:	csvToDict
#
# Descr:	Convert CSV file to Python Dictionary
#
# Author:	Tarllark
#
# Team:		Successful Story
#######################################################

import csv
import pprint

statistics = {}; #Dictionary

def toDict(file):
	with open(file) as in_file:
		dataset = csv.reader(in_file)
		#dataset = next(reader, None)
		print('Beginning conversion')
		first_line = True
		#statistics = {row[0]:{row[1]:{row[2]:{row[3]:row[4]for row in dataset}for row in dataset}for row in dataset} for row in dataset}
		for row in dataset:
			if not(first_line):
				if not(row[0] in statistics):
					statistics[row[0]] = {row[1]:{row[2]:{row[3]:row[4]}}}
				if not(row[1] in statistics):
					statistics[row[0]][row[1]] = {row[2]:{row[3]:row[4]}}
				if not(row[2] in statistics):
					statistics[row[0]][row[1]][row[2]] = {row[3]:row[4]}
				if not(row[3] in statistics):
					statistics[row[0]][row[1]][row[2]][row[3]] = row[4]
			else:
				first_line = False;
				
		
		pprint.pprint(statistics)
		print('Done converting')
	
def verifyData(DataSet, OriginFile):
	dataReader = csv.reader(open(OriginFile))
	lineCounter  = 0
	for row in dataReader:
		print("Line: ")
		print(lineCounter)
		if(lineCounter != 0):
			if not(row[0] in DataSet):
				print (row[0])
				print (DataSet)
				return 'false 1'
			elif not(row[1] in DataSet[row[0]]):
				print (row[1])
				print (DataSet[row[0]])
				return 'false 2'
			elif not(row[2] in DataSet[row[0]][row[1]]):
				print (row[2])
				print (DataSet[row[0]][row[1]])
				return 'false 3'
			elif not(row[3] in DataSet[row[0]][row[1]][row[2]]):
				print (row[3])
				print (DataSet[row[0]][row[1]][row[2]])
				return 'false 4'
			elif not(row[4] in DataSet[row[0]][row[1]][row[2]][row[3]]):
				print (row[4])
				print (DataSet[row[0]][row[1]][row[2]][row[3]])
				return 'false 5'
		lineCounter += 1
	return true

if __name__ == '__main__':
	file = './befkbhalderstatkode.csv'
	toDict(file)
	print("Verifying data")
	verified = verifyData(statistics, file)
	print("Verification done\nIdentical data:")
	print(verified)