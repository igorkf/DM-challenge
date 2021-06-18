# DM-challenge
Data Machina challenge 

## Problema 1   

## Problema 2

## Extra

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

Acesse http://localhost:8000/

### Rotas disponíveis:
- fibonacci/{n}

