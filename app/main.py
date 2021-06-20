from typing import List

from fastapi import FastAPI, HTTPException, Query, Depends

from .problema_1 import fibo
from .problema_2 import data, plataformas

app = FastAPI()


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

    if any(len(lst) != largura for lst in [altura, espessura, peso]):
        raise HTTPException(
            status_code=422,
            detail='Algum dos itens possui quantidade diferente de características.'
        )

    result = []
    for plataforma in plataformas:
        obj = {}
        obj['plataforma'] = plataforma

        itens = []
        for i, (lar, alt, esp, pes) in enumerate(zip(largura, altura, espessura, peso), start=1):
            try:
                veiculo_ideal = list(filter(lambda x: lar <= x['largura_max'] and alt <= x['altura_max'] and esp <= x['espessura_max'] and pes <= x['peso_max'] and x['plataforma'] == plataforma, data))[0]
                print(veiculo_ideal)
            except IndexError:
                veiculo_ideal = {}
            item = {
                'id': i,
                'largura': lar,
                'altura': alt,
                'espessura': esp,
                'peso': pes,
                'veiculo_ideal': veiculo_ideal
            }
            itens.append(item)
            obj['itens'] = itens

        result.append(obj)

    return result
