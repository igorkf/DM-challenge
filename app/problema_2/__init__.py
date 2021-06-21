import json


with open('app/problema_2/data.json', 'r') as f:
    data = json.loads(f.read())


for x in data:
    x['volume_max'] = x['largura_max'] * \
        x['altura_max'] * x['espessura_max']

data = sorted(data, key=lambda k: (
    k['plataforma'], k['volume_max']))

plataformas = sorted({x['plataforma'] for x in data})
