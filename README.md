# DM-challenge

Foi implementada uma API para resolver 2 problemas independentes.   

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

### Documentação   
Acesse http://localhost:8000/docs    
Teste as rotas pela própria documentação.   

## Problemas

### Problema 1
Encontre o n-ésimo elemento (considerando 0 como primeiro elemento) da sequência de Fibonacci, dado um número maior ou igual a 0.   
- /fibonacci/{n} 

### Problema 2
Encontre o melhor veículo para transportar uma lista de itens, agrupado por plataforma.   
- /transporte

OBS.: cada parâmetro pode receber uma lista de valores. Teste na documentação e veja como a API monta a *query string*.     


## Extra

