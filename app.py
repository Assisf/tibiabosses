import requests
import json

API_SERVER = 'https://api.tibiadata.com'
INPUT_BOSSES = './input/bosses.txt'
OUTPUT_BOSSES = './output/output_bosses.txt'

# SELECIONANDO O MUNDO
# world = input("Select your world")
api_url = f'/v3/killstatistics/Issobra'
response = requests.get(API_SERVER + api_url).json()

#LAÇO CHECAR PARA CADA BOSS
races = {}
for entry in response['killstatistics']['entries']:
    races[entry['race']] = entry

bossesfile = open(INPUT_BOSSES, "r")
bosses = json.loads(bossesfile.read())
 
for boss in bosses:
    del boss['qualquer']
    if boss['name'] in races:
        if(races[boss['name']]['last_day_killed'] > 0):
            print('Achou ontem: ' + boss['name'])
            boss['days_until_killed'].append(boss['last_day_killed'])
            boss['last_day_killed'] = 0
        else:
            boss['last_day_killed'] += 1
    else:
        boss['last_day_killed'] += 1

bossesfile = open(INPUT_BOSSES, 'w')
bossesfile.write(json.dumps(bosses, indent=4, sort_keys=True))
bossesfile.close()

#ESCREVER NO ARQUIVO DE SAIDA