plataformas = [
    {
        'fabricante': 'Lala',
        'veiculo': 'Moto',
        'largura_max': 35,
        'altura_max': 40,
        'espessura_max': 30,
        'peso_max': 20
    },
    {
        'fabricante': 'Lala',
        'veiculo': 'Fiorino',
        'largura_max': 188,
        'altura_max': 133,
        'espessura_max': 108,
        'peso_max': 500
    },
    {
        'fabricante': 'Lala',
        'veiculo': 'Carreto',
        'largura_max': 300,
        'altura_max': 180,
        'espessura_max': 200,
        'peso_max': 1500
    },
    {
        'fabricante': 'Ogi',
        'veiculo': 'Moto',
        'largura_max': 52,
        'altura_max': 36,
        'espessura_max': 52,
        'peso_max': 20
    },
    {
        'fabricante': 'Ogi',
        'veiculo': 'SUV',
        'largura_max': 125,
        'altura_max': 80,
        'espessura_max': 60,
        'peso_max': 200
    }
]

for x in plataformas:
    x['volume_max'] = x['largura_max'] * x['altura_max'] * x['espessura_max']
