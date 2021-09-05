# Api Globocard

Esse projeto é uma API web desenvolvida com Python e MongoDB para ser utilizada na criação de cards e tags. Com objetivo de ser utilizada em conjunto com uma interface gráfica para a criação de Cards de conteúdo esportivos(Insights) para o desafio Globo. A descrição de todas as rotas pode ser encontrada ao iniciar em modo desenvolvedor.

Acessando a url(padrão) http://localhost:5000 diretamente no navegador ou, [clicando aqui](https://api-globo-card.herokuapp.com/) para visualizar online. 
É possível efetuar testes em cada rota e analisar cada uma especificamente.

Essa api está hospedada no Heroku e utilizando o método de deploy automático e utilizando o Mongo DB Atlas.

Você pode acessar e testar seu funcionamento em modo de produção [clicando aqui](https://api-globo-card.herokuapp.com/)


> É necessário ter o Python 3.x instalado e o Mongo DB instalado e executando. Ou utilizar Docker.

## Requerimentos:

- Python 3.x
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
7. Crie um arquivo .env na pasta raíz do projeto e insira os seguintes campos:

        #MONGO_HOST É A CHAVE RESPONSÁVEL PELO ENDEREÇO DO SERVIÇO MONGO DB
        #UTILIZE localhost PARA TESTES LOCAIS E 0.0.0.0 PARA UTILIZAÇÃO COM DOCKER
        MONGO_HOST=localhost
        #NOME DA COLEÇÃO
        MONGO_DB_NAME=globocards
        #A PORTA PADRÃO DESSE PROJETO É 5000. VOCÊ PODE ALTERAR A PORTA AO DESCOMENTAR A LINHA ABAIXO E ALTERAR A PORTA.
        #PORT=5000
        #PARA UTILIZAR O PROJETO EM MODO PRODUÇÃO E CONECTAR COM INSTÂNCIAS DE MONGO DB EXTERNOS, ALTERE A CHAVE PRODUCTION=0 PARA PRODUCTION=1
        PRODUCTION=0
        #URL DE ACESSO PARA O AMBIENTE DE TESTE: mongodb+srv://globocard:globocard@cluster0.8iywx.mongodb.net/globocard?retryWrites=true&w=majority
        #UTILIZE O MONGODB COMPASS. A senha é globocard.
        #ESSA INSTÂNCIA DO MONGO DB ATLAS É TEMPORÁRIA E SERÁ DESATIVADA DENTRO DE 15 DIAS.
        #CONFIGURE A URL DO MONGO_DB_ATLAS NA CHAVE MONGO_DB_ATLAS.
        MONGO_DB_ATLAS=NONE

8. Ainda com o terminal aberto, execute o comando <b>python start.py</b>
9. Acesse http://localhost:5000 para acessar a documentação do swagger e visualizar todas as rotas da api.

## Primeiros passos(Docker)
1. Acesse o guia de instação do mongodb e instale a opção correspondente ao seu sistema operacional [clique aqui para acessar](https://docs.mongodb.com/guides/server/install/).
2. Acesse o guia de instação do Mongo Compass para instalar e facilitar a visualização de dados de forma visual. [clique aqui para acessar](https://www.mongodb.com/try/download/compass)
3. Clone esse repositório em um local de fácil localização
4. Acesse a pasta raíz do projeto clonado.
5. Crie um arquivo .env na pasta raíz do projeto e insira os seguintes campos:

        #MONGO_HOST É A CHAVE RESPONSÁVEL PELO ENDEREÇO DO SERVIÇO MONGO DB
        #UTILIZE localhost PARA TESTES LOCAIS E 0.0.0.0 PARA UTILIZAÇÃO COM DOCKER
        MONGO_HOST=0.0.0.0
        #NOME DA COLEÇÃO
        MONGO_DB_NAME=globocards
        #A PORTA PADRÃO DESSE PROJETO É 5000. VOCÊ PODE ALTERAR A PORTA AO DESCOMENTAR A LINHA ABAIXO E ALTERAR A PORTA.
        #PORT=5000
        #PARA UTILIZAR O PROJETO EM MODO PRODUÇÃO E CONECTAR COM INSTÂNCIAS DE MONGO DB EXTERNOS, ALTERE A CHAVE PRODUCTION=0 PARA PRODUCTION=1
        PRODUCTION=0
        #URL DE ACESSO PARA O AMBIENTE DE TESTE: mongodb+srv://globocard:globocard@cluster0.8iywx.mongodb.net/globocard?retryWrites=true&w=majority
        #UTILIZE O MONGODB COMPASS. A senha é globocard.
        #ESSA INSTÂNCIA DO MONGO DB ATLAS É TEMPORÁRIA E SERÁ DESATIVADA DENTRO DE 15 DIAS.
        #CONFIGURE A URL DO MONGO_DB_ATLAS NA CHAVE MONGO_DB_ATLAS.
        MONGO_DB_ATLAS=NONE


6. Abra um terminal na raíz do projeto.
7. Execute o comando docker-compose up. Aguarde o Docker configurar o ambiente.
8. Acesse http://localhost:5000 para acessar a documentação do swagger e visualizar todas as rotas da api.



