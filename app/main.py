from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from .problema_1 import fibo
from .problema_2 import plataformas


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
async def show_vehicle_options(request: Request):
    context = {
        'request': request,
        'plataformas': plataformas
    }
    return templates.TemplateResponse('index.html', context=context)
