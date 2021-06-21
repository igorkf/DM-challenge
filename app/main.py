from typing import List
from decimal import Decimal

from fastapi import FastAPI, HTTPException, Query, Body, Depends

from .problema_1 import fibo
from .problema_2 import data, plataformas
from .auth.model import UserLoginSchema
from .auth.auth_handler import signJWT, USER
from .auth.auth_bearer import JWTBearer


app = FastAPI(
    title='DM-challenge',
    description='Uma API implementada com FastAPI, que possui autenticação JWT, para resolver dois problemas interessantes.',
    redoc_url=None
)


users = [USER]


def check_user(data: UserLoginSchema):
    for user in users:
        if user['email'] == data.email and user['password'] == data.password:
            return True
    return False


@app.post('/user/login', tags=['user'])
async def user_login(user: UserLoginSchema = Body(...)):
    '''
    Verifica credenciais do usuário e retorna um token JWT para autorizar rotas protegidas caso
    o usuário esteja autorizado a usar a API.
    '''
    if check_user(user):
        return signJWT(user.email)
    raise HTTPException(
        status_code=403,
        detail='Email ou senha incorretos.'
    )


@app.get('/fibonacci/{n}', tags=['problema 1'], dependencies=[Depends(JWTBearer())])
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


@app.get('/transporte', tags=['problema 2'], dependencies=[Depends(JWTBearer())])
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
            detail='Um ou mais itens possuem quantidades diferentes de características.'
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
