def fibo(n):
    '''
    Gera a sequência de Fibonacci até o n-ésimo termo (considerando 0 como primeiro elemento).
    '''
    a, b = 0, 1

    for _ in range(n + 1):
        yield a
        (a, b) = (b, a + b)
