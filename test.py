import json
import xmltodict
from json2xml import json2xml
from json2xml.utils import readfromurl, readfromstring, readfromjson

with open("About.xml") as xml_file:
    data_dict = xmltodict.parse(xml_file.read())
    json_data = json.dumps(data_dict)


print(json_data)
print(json2xml.Json2xml(json_data, wrapper="all", pretty=True, attr_type=False).to_xml())