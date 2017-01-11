#!/usr/bin/evn python 
#coding:utf-8 
  
try: 
  import xml.etree.cElementTree as ET 
except ImportError: 
  import xml.etree.ElementTree as ET 
import sys 
  
try: 
  tree = ET.parse("country.xml")     #��xml�ĵ� 
  #root = ET.fromstring(country_string) #���ַ�������xml 
  root = tree.getroot()         #���root�ڵ�  
except Exception, e: 
  print "Error:cannot parse file:country.xml."
  sys.exit(1) 
print root.tag, "---", root.attrib  
for child in root: 
  print child.tag, "---", child.attrib 
  
print "*"*10
print root[0][1].text   #ͨ���±���� 
print root[0].tag, root[0].text 
print "*"*10
  
for country in root.findall('country'): #�ҵ�root�ڵ��µ�����country�ڵ� 
  rank = country.find('rank').text   #�ӽڵ��½ڵ�rank��ֵ 
  name = country.get('name')      #�ӽڵ�������name��ֵ 
  print name, rank 
     
#�޸�xml�ļ� 
for country in root.findall('country'): 
  rank = int(country.find('rank').text) 
  if rank > 50: 
    root.remove(country) 
  
tree.write('output.xml') 