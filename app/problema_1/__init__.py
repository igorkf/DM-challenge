def fibo(n):
    '''
    Gera a sequência de Fibonacci até o n-ésimo termo (considerando 0 como primeiro elemento).
    '''
    a, b = 0, 1

    for i in range(n):
        yield a
        (a, b) = (b, a + b)
