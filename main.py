from fastapi import FastAPI

from problema_1 import fibo


app = FastAPI()


@app.get('/fibonacci/{n}')
async def fibonacci(n: int):
    '''
    Escolhe o n-ésimo elemento (considerando 0 como primeiro elemento) da sequência
    de Fibonacci, dado um número maior ou igual a 0.
    '''
    return list(fibo(n + 1))[-1]
