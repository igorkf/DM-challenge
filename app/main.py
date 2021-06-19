from pathlib import Path
import json

from fastapi import FastAPI, Request, HTTPException, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from .problema_1 import fibo
from .problema_2 import Transporte


BASE_DIR = Path(__file__).parent.parent.absolute()

app = FastAPI()
app.mount(
    '/static',
    StaticFiles(directory=BASE_DIR / 'app/static'),
    name='static'
)
templates = Jinja2Templates(directory='app/templates')


@app.get('/fibonacci/{n}')
async def fibonacci(n: int):
    '''
    Escolhe o n-ésimo elemento (considerando 0 como primeiro elemento) da sequência
    de Fibonacci, dado um número maior ou igual a 0.
    '''
    if n < 0:
        raise HTTPException(
            status_code=422,
            detail='Escolha um número maior ou igual a 0.'
        )
    elif n > 2e5:
        raise HTTPException(
            status_code=422,
            detail='Opa...vai com calma.'
        )

    return list(fibo(n))[-1]


@app.get('/transporte', response_class=HTMLResponse)
async def transporte(request: Request, model: Transporte = Depends()):
    '''
    Calcula quais opções de transporte suportam uma mercadoria de acordo
    com as características da mercadoria, além de mostrar o custo benefício.   
    '''

    with open('app/problema_2/data.json', 'r') as f:
        data = json.loads(f.read())

    for x in data:
        x['volume_max'] = x['largura_max'] * \
            x['altura_max'] * x['espessura_max']
        x['possui_requisitos'] = 'Não'
        x['nivel_de_custo'] = None

    sorted_data = sorted(data, key=lambda k: (
        k['plataforma'], k['volume_max']))
    plataformas = sorted({x['plataforma'] for x in sorted_data})

    for plataforma in plataformas:
        i = 0
        for x in sorted_data:
            if x['plataforma'] == plataforma and model.largura <= x['largura_max'] and model.altura <= x['altura_max'] and model.espessura <= x['espessura_max'] and model.peso <= x['peso_max']:
                x['possui_requisitos'] = 'Sim'
                i += 1
                x['nivel_de_custo'] = i

    context = {
        'request': request,
        'plataformas': plataformas,
        'data': sorted_data,
        'model': model
    }

    return templates.TemplateResponse('index.html', context=context)
