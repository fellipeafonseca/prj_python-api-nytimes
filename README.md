# 🗞️ NYTimes News API

Microserviço responsável por **receber, validar e persistir notícias do New York Times** em um banco de dados PostgreSQL.  
Este serviço faz parte de uma arquitetura baseada em **microsserviços**, sendo consumido por um scraper independente.

---

## 📌 Visão Geral

Esta API foi desenvolvida com foco em:

- Arquitetura limpa
- Separação de responsabilidades
- Boas práticas de mercado
- Containerização com Docker
- Pronta para escalar e integrar com outros serviços

O scraper é responsável apenas pela **coleta dos dados**, enquanto esta API cuida de:

- Validação
- Persistência
- Exposição de endpoints REST

---

## 🏗️ Arquitetura

[ Scraper (Selenium / Playwright) ]
|
v
[ FastAPI ]
|
v
[ PostgreSQL ]


- O scraper envia os dados via HTTP (POST)
- A API valida e persiste os dados
- O banco roda isolado em container Docker

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.11**
- **FastAPI**
- **SQLAlchemy**
- **PostgreSQL**
- **Docker & Docker Compose**
- **Pydantic**
- **Uvicorn**

---

## 📁 Estrutura do Projeto

api/
├── app/
│ ├── main.py # Inicialização da aplicação
│ ├── database.py # Conexão com o banco
│ ├── models.py # Modelos ORM
│ ├── schemas.py # Schemas de validação
│ ├── crud.py # Regras de persistência
│ └── routes.py # Endpoints da API
├── Dockerfile
├── requirements.txt
└── .env


---

## ⚙️ Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
DATABASE_URL=postgresql://postgres:postgres@db:5432/nytimes
⚠️ Em ambientes produtivos, recomenda-se o uso de Docker Secrets ou ferramentas de gerenciamento de segredos.

▶️ Como Executar o Projeto
Pré-requisitos
Docker

Docker Compose

Subindo os containers
docker compose up --build
🌐 Acessos
API:

http://localhost:8000
Documentação automática (Swagger):

http://localhost:8000/docs
📤 Endpoint Principal
Criar uma notícia
POST /news

{
  "title": "Example News Title",
  "category": "Technology",
  "url": "https://www.nytimes.com/example",
  "published_at": "2025-01-10T10:00:00"
}
🧪 Validação e Persistência
Todos os dados são validados via Pydantic

As tabelas são criadas automaticamente na inicialização

URLs são únicas para evitar duplicidade de notícias

🔐 Segurança (Evolução planejada)
Autenticação via JWT

Docker Secrets

Controle de acesso por serviço

🚀 Próximos Passos
Integração com Playwright

Autenticação JWT

Evitar duplicidade de notícias

Logs estruturados

Monitoramento e métricas

👨‍💻 Autor
Projeto desenvolvido para fins de portfólio profissional, demonstrando habilidades em:

Backend Python

APIs REST

Docker

Arquitetura de microsserviços