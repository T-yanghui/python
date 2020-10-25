#解析Json文件
import json
jsonFile = open ('D:/code/python/ClassDemo/conf_classTime.json','r',encoding='UTF-8')
jsonString = json.load(jsonFile)
for name in jsonString:
	print(name['classTime'])
