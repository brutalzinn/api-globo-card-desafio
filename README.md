# Api Globocard

Esse projeto é uma API web desenvolvida com Python e MongoDB para ser utilizada na criação de cards e tags. Com objetivo de ser utilizada em conjunto com uma interface gráfica para a criação de Cards de conteúdo esportivos(Insights) para o desafio Globo. A documentação dessa api pode ser encontrada ao iniciar em modo desenvolvedor, e acessando a url(padrão) http://localhost:5000 diretamente no navegador ou [clicando aqui](https://api-globo-card.herokuapp.com/). É possível efetuar testes em cada rota e analisar cada uma especificamente.
Essa api está hospedada no Heroku e utilizando o método de deploy automático.
Você pode acessar e testar seu funcionamento em modo de produção [clicando aqui](https://api-globo-card.herokuapp.com/)


## Requerimentos:

- Python 3x
- Mongo DB

## Bibliotecas utilizadas:

- aniso8601
- attrs
- click
- dnspython
- Flask
- Flask-Cors
- Flask-PyMongo
- flask-restx
- itsdangerous
- Jinja2
- jsonschema
- MarkupSafe
- pymongo
- pyrsistent
- python-dotenv
- pytz1
- six0
- Unidecode
- Werkzeug



## Primeiros passos(padrão)
1. Acesse o guia de instação do mongodb e instale a opção correspondente ao seu sistema operacional [clique aqui para acessar](https://docs.mongodb.com/guides/server/install/).
2. Acesse o guia de instação do Mongo Compass para instalar e facilitar a visualização de dados de forma visual. [clique aqui para acessar](https://www.mongodb.com/try/download/compass)
3. Clone esse repositório em um local de fácil localização
4. Acesse a pasta raíz do projeto clonado.
5. Abra um terminal na raíz do projeto.
6. Execute o comando <b>pip install -r requirements.txt</b> para baixar todas as dependências.
7. Crie um arquivo .env no local escolhido e insira os seguintes campos:

        #COMENTE A LINHA ABAIXO PARA RODAR ESSE PROJETO COM DOCKER
        MONGO_HOST=localhost
        MONGO_DB_NAME=globocards
        #VOCÊ PODE DESCOMENTAR A LINHA ABAIXO PARA ALTERAR A PORTA.
        #PORT=5000
        #PARA UTILIZAR O PROJETO EM MODO PRODUÇÃO, ALTERE A CHAVE PRODUCTION=0 PARA PRODUCTION=1
        #E CONFIGURE A URL DO MONGO_DB_ATLAS NA CHAVE MONGO_DB_ATLAS.
        #URL DE ACESSO PARA O AMBIENTE DE TESTE: mongodb+srv://globocard:globocard@cluster0.8iywx.mongodb.net/globocard?retryWrites=true&w=majority
        #UTILIZE O MONGODB COMPASS. A senha é globocard.
        #ESSA INSTÂNCIA DO MONGO DB ATLAS É TEMPORÁRIA E PODE SER DESATIVADA SEM AVISO PRÉVIO.
        PRODUCTION=0
        MONGO_DB_ATLAS=NONE
8. Ainda com o terminal aberto, execute o comando <b>python start.py</b>
9. Acesse http://localhost:5000 para acessar a documentação do swagger e visualizar todas as rotas da api.

## Primeiros passos(Docker)
1. Acesse o guia de instação do mongodb e instale a opção correspondente ao seu sistema operacional [clique aqui para acessar](https://docs.mongodb.com/guides/server/install/).
2. Acesse o guia de instação do Mongo Compass para instalar e facilitar a visualização de dados de forma visual. [clique aqui para acessar](https://www.mongodb.com/try/download/compass)
3. Clone esse repositório em um local de fácil localização
4. Acesse a pasta raíz do projeto clonado.
5. Crie um arquivo .env no local escolhido e insira os seguintes campos:

        MONGO_DB_NAME=globocards
        #VOCÊ PODE DESCOMENTAR A LINHA ABAIXO PARA ALTERAR A PORTA.
        #PORT=5000
        #PARA UTILIZAR O PROJETO EM MODO PRODUÇÃO, ALTERE A CHAVE PRODUCTION=0 PARA PRODUCTION=1
        #E CONFIGURE A URL DO MONGO_DB_ATLAS NA CHAVE MONGO_DB_ATLAS.
        #URL DE ACESSO PARA O AMBIENTE DE TESTE: mongodb+srv://globocard:globocard@cluster0.8iywx.mongodb.net/globocard?retryWrites=true&w=majority
        #UTILIZE O MONGODB COMPASS. A senha é globocard.
        #ESSA INSTÂNCIA DO MONGO DB ATLAS É TEMPORÁRIA E PODE SER DESATIVADA SEM AVISO PRÉVIO.
        PRODUCTION=0
        MONGO_DB_ATLAS=NONE
6. Abra um terminal na raíz do projeto.
7. Execute o comando docker-compose up. Aguarde o Docker configurar o ambiente.
8. Acesse http://localhost:5000 para acessar a documentação do swagger e visualizar todas as rotas da api.



