from typing import List
from decimal import Decimal

from fastapi import FastAPI, HTTPException, Query, Depends

from .problema_1 import fibo
from .problema_2 import data, plataformas

app = FastAPI(docs_url=None)


@app.get('/fibonacci/{n}')
async def fibonacci(n: int):
    '''
    Encontra o n-ésimo elemento (considerando 0 como primeiro elemento) da sequência
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


@app.get('/transporte')
async def transporte(
    largura: List[Decimal] = Query(...),
    altura: List[Decimal] = Query(...),
    espessura: List[Decimal] = Query(...),
    peso: List[Decimal] = Query(...)
):
    '''
    Encontra melhor veículo para transportar uma lista de itens, agrupado por plataforma.
    '''

    if not len(set(len(x) for x in [largura, altura, espessura, peso])) == 1:
        raise HTTPException(
            status_code=422,
            detail='Um ou mais itens possuem quantidade diferente de características.'
        )

    volume_total = sum(
        [x * y * z for x, y, z in zip(largura, altura, espessura)])
    peso_total = sum(peso)

    result = []
    for plataforma in plataformas:
        try:
            veiculo_ideal = list(filter(
                lambda x: volume_total <= x['volume_max'] and peso_total <= x['peso_max'] and x['plataforma'] == plataforma, data))[0]
        except IndexError:
            veiculo_ideal = None

        veiculo_ideal = {x[0]: x[1]
                         for x in veiculo_ideal.items() if x[0] != 'plataforma'}

        obj = {
            'plataforma': plataforma,
            'volume_total': volume_total,
            'peso_total': peso_total,
            'veiculo_ideal': veiculo_ideal,
        }
        result.append(obj)

    return result
