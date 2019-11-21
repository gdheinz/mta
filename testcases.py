import xml.etree.ElementTree as ET

class _TestCase(object):
  
  def __init__(self, label, count):
    self.label = label
    self.count = count
    #self.found = False
    
  
class TestCases(object):
  def __init__(self, testcases_xml):
    
    self.testcases = []
    root = ET.parse(testcases_xml)
    
    for country in root.findall('warning'):
      count = country.find('count').text
      name = country.find('name').text
      self.testcases.append(_TestCase(name, count))

