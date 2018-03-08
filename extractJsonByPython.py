#This is used for json extract file from local disk
import json
 
data=json.load(open('jsonsamplefile.json'))
 

# output is 
# {u'test': {u'unitTestd': u'jasmin'}, 
# u'maps':[{u'country': u'Nepal', u'city': u'Kathmandu'},{u'country': u'UK', u'city': u'Houston'}],
# u'_comment': u'Map is list ', u'Habbit': u'Program', 
# u'Hobby': {u'badHabbit': u'lapwithwork'}}
print("json---",data) 

#extract specific data from json is 
print("Extract only hobby--",data["Hobby"])   # output :: ('Extract only hobby--', {u'badHabbit': u'lapwithwork'})

print("extract from map list--",data["maps"])# output :: ('extract from map list--', [{u'country': u'Nepal', u'city': u'Kathmandu'}, {u'country': u'UK', u'city': u'Houston'}])


print("extract country from map list first list--",data["maps"][0]["country"]) # [0] indicate the  first position of list in map json format .. output ::  ('extract country from map list first position--', u'Nepal')

print("extract country from map list second list--",data["maps"][1]["country"]) # [1] indicate the  Second position of list in map json format  output :: ('extract country from map list Second position--', u'UK')



## this can be done by python3 like this 

with open('jsonsamplefile.json', encoding='utf-8') as data_file:
    data = json.loads(data_file.read())

#output :: {'_comment': 'Map is list ', 
# 'maps': [{'country': 'Nepal', 'city': 'Kathmandu'},
#  {'country': 'UK', 'city': 'Houston'}], 
# 'Habbit': 'Program', 
# 'test': {'unitTestd': 'jasmin'},
#  'Hobby': {'badHabbit': 'lapwithwork'}}

#in this output you can see the elimination of (u'test') to 'test' this is in python3 filename.py
print (data) 


#dump json 
json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])


print (json.dumps("\"foo\bar")) #output : "\"foo\bar"

print(json.dumps([1,2,3,{'4': 5, '6': 7}], separators=(',',':'))) #output [1,2,3,{"4":5,"6":7}]


#output 
# {
#   "4": 5,
#   "6": 7
# } 

print (json.dumps({'4': 5, '6': 7}, sort_keys=True,indent=4, separators=(',', ': ')))

