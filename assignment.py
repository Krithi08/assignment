import csv
import json

def make_json(csvFilePath, jsonFilePath):
	data = {}
	with open(csvFilePath, encoding='utf-8') as csvf:
		csvReader = csv.DictReader(csvf)
	
		for rows in csvReader:
			key = rows['parental level of education']
			data[key] = rows

	with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
		jsonf.write(json.dumps(data, indent=4))
		
csvFilePath = r'C:\Users\ASUS\Documents\StudentsPerformance.csv'
jsonFilePath = r'Names.json'

make_json(csvFilePath, jsonFilePath)
