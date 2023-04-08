import xml.etree.ElementTree as ET

tree = ET.parse('dados.xml')
root = tree.getroot()

for row in root.iter('row'):
    dia = row.find('dia').text
    valor = row.find('valor').text
    print(f"dia: {dia}, valor: {valor}")

