from typing import List

from fastapi import FastAPI, HTTPException, Query, Depends

from .problema_1 import fibo
from .problema_2 import data, plataformas

app = FastAPI()


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
    largura: List[float] = Query(...),
    altura: List[float] = Query(...),
    espessura: List[float] = Query(...),
    peso: List[float] = Query(...)
):
    '''
    Encontra melhor veículo para transportar uma lista de itens, agrupado por plataforma.
    '''

    if not len(set(len(x) for x in [largura, altura, espessura, peso])) == 1:
        raise HTTPException(
            status_code=422,
            detail='Um ou mais itens possuem quantidade diferente de características.'
        )

    # TODO: usar volume em vez de medidas totais

    larg_total = sum(largura)
    alt_total = sum(altura)
    esp_total = sum(espessura)
    peso_total = sum(peso)

    result = []
    for plataforma in plataformas:
        obj = {}

        try:
            veiculo_ideal = list(filter(lambda x: larg_total <= x['largura_max'] and alt_total <= x['altura_max'] and esp_total <= x['espessura_max'] and peso_total <= x['peso_max'] and x['plataforma'] == plataforma, data))[0]
            print(veiculo_ideal)
        except IndexError:
            veiculo_ideal = {}

        veiculo_ideal = {x[0]: x[1] for x in veiculo_ideal.items() if x[0] != 'plataforma'}

        obj['plataforma'] = plataforma
        obj['largura_total'] = larg_total
        obj['altura_total'] =  alt_total
        obj['espessura_total'] = esp_total
        obj['peso_total'] = peso_total
        obj['veiculo_ideal'] = veiculo_ideal
        result.append(obj)

    return result
