#Lab5 - Cybersecurity Programming
#parsexml.py

import sys
import xml.etree.ElementTree as ET
from xml.dom.minidom import parseString
import json
import xmltodict

if(sys.argv[1] == "-h" or sys.argv[1] == "--help"):
    print("USAGE: python3 {} inputfile.xml".format(sys.argv[0]))

    sys.exit()

fileToParse = sys.argv[1]
print('File to Parse: {}'.format(fileToParse))
tree = ET.ElementTree(file=fileToParse)
print("*****")
print("Tree Root:")
root = tree.getroot()
print("root tag: {}, root attribute: {}".format(root.tag, root.attrib))


