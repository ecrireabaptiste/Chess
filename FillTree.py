# import xmlparser
# Python XML Parsing
import xml.etree.ElementTree as ET
root = ET.parse('sample.xml').getroot()
tag = root.tag
print(tag)

# get all attributes
attributes = root.attrib
print(attributes)

# extract a particular attribute
year = attributes.get('year')
print('year : ',year)

# iterate over all the nodes with tag name - holiday
for holiday in root.findall('holiday'):
    print(holiday)
    
# iterate over child nodes
for holiday in root.findall('holiday'):

    # get all attributes of a node
    attributes = holiday.attrib
    print(attributes)

    # get a particular attribute
    type = attributes.get('type')
    print(type)
    
# iterate over all nodes
for holiday in root.findall('holiday'):

    # access element - name
    name = holiday.find('name').text
    print('name : ', name)

    # access element - date
    date = holiday.find('date').text
    print('date : ', date)
    
# iterate over all nodes
for holiday in root.findall('holiday'):

    # access element - name
    name = holiday.find('name').text
    print('name : ', name)

    # access element - date
    date = holiday.find('date').text
    print('date : ', date)
