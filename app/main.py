from fastapi import FastAPI, HTTPException

from .problema_1 import fibo


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

    return list(fibo(n + 1))[-1]
