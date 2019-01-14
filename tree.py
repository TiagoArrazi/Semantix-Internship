import xml.etree.ElementTree as ET

xml_string = '''<?xml version="1.0"?>
<data>
    <country name="Liechtenstein">
        <rank>1</rank>
        <year>2008</year>
        <gdppc>141100</gdppc>
        <neighbor name="Austria" direction="E"/>
        <neighbor name="Switzerland" direction="W"/>
    </country>
    <country name="Singapore">
        <rank>4</rank>
        <year>2011</year>
        <gdppc>59900</gdppc>
        <neighbor name="Malaysia" direction="N"/>
    </country>
    <country name="Panama">
        <rank>68</rank>
        <year>2011</year>
        <gdppc>13600</gdppc>
        <neighbor name="Costa Rica" direction="W"/>
        <neighbor name="Colombia" direction="E"/>
    </country>
</data>
'''

tree = ET.fromstring(xml_string)
countries = tree.iter('country')
for country in countries:
    for rank in country.iter('rank'):
        country.remove(rank)

print(xml_string)

new_xml = ET.tostring(tree, encoding='utf8', method='xml').split(b'\n')
for line in new_xml:
    print(line)

