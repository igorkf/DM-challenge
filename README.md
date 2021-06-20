# DM-challenge

Foi implementada uma API para resolver 2 problemas.

## Problema 1   

Encontre o n-ésimo elemento (considerando 0 como primeiro elemento) da sequência de Fibonacci, dado um número maior ou igual a 0.

Exemplo de uso:   
- /fibonacci/10 

## Problema 2

Encontre o melhor veículo para transportar uma lista de itens, agrupado por plataforma.

Exemplo de uso (passando 2 itens):
- /transporte?largura=200&largura=5&altura=12&altura=0.3&espessura=6.6&espessura=10.3&peso=1.6&peso=2.3

## Extra

...

## Como utilizar a API
Clone o repositório:   
```
git clone https://github.com/igorkf/DM-challenge.git
```

Dentro do repositório, construa a imagem do Docker:
```
docker build -t my_api .
```

Defina o container:
```
docker run --name my_container -p 8000:8000 my_api
```

Acesse http://localhost:8000/ e teste as rotas.   