import json

with open("dados.json", encoding= 'utf-8') as meu_json:
   dados = json.load(meu_json)

for i in dados:
   print('No dia', i['dia'], 'entrou em caixa o valor de: ', i['valor'])

