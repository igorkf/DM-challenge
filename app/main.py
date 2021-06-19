from fastapi import FastAPI, Request, HTTPException, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from .problema_1 import fibo
from .problema_2 import plataformas, Transporte


app = FastAPI()
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

    return list(fibo(n + 1))[-1]


@app.get('/transporte', response_class=HTMLResponse)
async def show_vehicle_options(request: Request, model: Transporte = Depends()):
    for x in plataformas:
        if model.largura <= x['largura_max'] and model.altura <= x['altura_max'] and model.espessura <= x['espessura_max'] and model.peso <= x['peso_max']:
            x['possui_requisitos'] = 'Sim'
        else:
            x['possui_requisitos'] = 'Não'

    context = {
        'request': request,
        'plataformas': plataformas,
        'model': model
    }

    return templates.TemplateResponse('index.html', context=context)
