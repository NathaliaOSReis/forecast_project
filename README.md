# <p align="center">🌤️ Forecast Project - Previsão do Tempo Interativa

<p align="center">
<img src="https://badgen.net/badge/STATUS/CONCLUÍDO/green?icon=github" alt="Status Badge"/>
  <img src="https://badgen.net/badge/Version/1.0.0/blue?icon=github" alt="Version Badge"/>
</p>

## ⚙️Versão

Atualmente está disponível a **Versão 1.0.0** do presente projeto, disponibilizada em Abril/2025.

## 📝 Descrição
Este é um projeto simples e amigável para consultar a previsão do tempo de forma visual e acessível. O sistema utiliza uma interface web feita com Streamlit e uma API local em FastAPI, permitindo que o usuário digite o nome de uma cidade e visualize a previsão de temperatura e precipitação por hora.

## 📋 🧠 Como Funciona?
1. O usuário digita o nome de uma cidade.
2. A interface consulta a latitude e longitude da cidade usando Nominatim(ferramenta de geocodificação e geocodificação reversa para dados do OpenStreetMap (OSM)).
3. A API recebe as coordenadas e consulta a previsão do tempo usando a Open-Meteo(serviço que fornece dados e previsões meteorológicas, acessíveis através de APIs).
4. Os dados são processados e exibidos em gráficos interativos e tabelas.

## 👀 Preview da Aplicação
![Gif da aplicação Forecast](./assets/clima_api_teste.gif)

## ⚙️ Tecnologias Utilizadas

### 🛠️ Linguagens e Frameworks<br>
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![FastAPI](https://img.shields.io/badge/FastAPI-000000?style=for-the-badge&logo=fastapi&logoColor=green) ![Streamlit](https://img.shields.io/badge/Streamlit-E34F26?style=for-the-badge&logo=streamlit&logoColor=white) 

- **Python 3.12** — Linguagem utilizada no desenvolvimento da aplicação.
- **FastAPI** — Para construção da API de previsão
- **Streamlit** — Para a interface gráfica do usuário
### 🌐 APIs Utilizadas <br>
![Open-Meteo](https://img.shields.io/badge/Open%20Meteo-F7B93E?style=for-the-badge&logo=openmeteo&logoColor=black) ![Nominatim](https://img.shields.io/badge/Nominatim-1A73E8?style=for-the-badge&logo=nominatim&logoColor=black)

- **Open-Meteo API** — Para a consulta de dados meteorológicos.
- **Nominatim (OpenStreetMap)** — Para geolocalização de cidades.

## ✅ Pré-requisitos
Antes de rodar a aplicação, você precisa ter:

- Python 3.10 ou superior instalado

- pip (instalador de pacotes Python) funcionando

- Ambiente virtual (opcional, mas recomendado)

## 🔐 Configuração das Variáveis de Ambiente e Credenciais Sigilosas

O projeto utiliza variáveis de ambiente para armazenar configurações sensíveis e credenciais. Para configurá-las:

1. **Crie um arquivo `.env` na raiz do projeto** (um arquivo de exemplo `.env.example` está disponível como referência)

2. **Adicione as seguintes variáveis ao arquivo `.env`**:
```
# Configurações da API Open-Meteo
OPENMETEO_URL=https://api.open-meteo.com/v1/forecast

# Configurações do servidor FastAPI
API_HOST=127.0.0.1
API_PORT=8000

# Credenciais e chaves de API (mantenha estas informações sigilosas)
API_KEY=sua_chave_api_secreta_aqui
API_SECRET=seu_segredo_api_aqui
DATABASE_URL=mysql://usuario:senha@localhost:3306/nome_do_banco
JWT_SECRET=chave_jwt_muito_secreta_e_longa

# Variáveis de ambiente para serviços externos
WEATHER_API_KEY=sua_chave_api_clima_aqui
MAPS_API_KEY=sua_chave_api_mapas_aqui
```

3. **Boas práticas para manter credenciais seguras**:
   - O arquivo `.env` já está no `.gitignore` para proteger suas credenciais
   - **NUNCA** compartilhe ou cometa seu arquivo `.env` no repositório
   - **NUNCA** armazene credenciais diretamente no código-fonte
   - Ao adicionar novas variáveis de ambiente, atualize também o `.env.example` (sem valores reais)
   - Em ambientes de produção, considere usar serviços de gerenciamento de segredos como:
     - AWS Secrets Manager
     - HashiCorp Vault
     - Docker Swarm Secrets ou Kubernetes Secrets
   - Para projetos em equipe, compartilhe credenciais por canais seguros (não por e-mail ou mensagens)
   - Considere rotacionar chaves e segredos periodicamente

4. **Uso com Docker**:
   - O `docker-compose.yml` está configurado para carregar automaticamente as variáveis do arquivo `.env`
   - As variáveis são injetadas nos contêineres durante a inicialização
   - Para adicionar novas variáveis, atualize o arquivo `docker-compose.yml` conforme necessário

## 🛠 Como Abrir e Executar Esse Projeto

### Método 1: Execução Local (sem Docker)

1. **Clone o repositório**:
```
git clone https://github.com/seu-usuario/forecast_project.git
cd forecast_project
```

2. **(Opcional) Crie e ative um ambiente virtual**:
* No Windows
```
python -m venv venv
venv\Scripts\activate
```
* No Linux
```
python3 -m venv venv
source venv/bin/activate
```

3. **Instale as dependências**:
```
pip install -r requirements.txt
```

4. **Configure as variáveis de ambiente**:
```
# Crie um arquivo .env na raiz do projeto (use .env.example como referência)
```

5. **Inicie a API (FastAPI)**:
```
uvicorn api.main:app --reload
```
- A API estará disponível em: ```http://127.0.0.1:8000```
- Você pode acessar a documentação automática da API em: ```http://127.0.0.1:8000/docs```

6. **Em outro terminal, execute a interface (Streamlit)**:
```
streamlit run app_streamlit.py
```
- A interface abrirá automaticamente em seu navegador em: ```http://localhost:8501```

### Método 2: Execução com Docker (recomendado)

1. **Clone o repositório**:
```
git clone https://github.com/seu-usuario/forecast_project.git
cd forecast_project
```

2. **Construa e inicie os containers**:
```
docker-compose up -d --build
```

3. **Acesse as aplicações**:
- API FastAPI: ```http://localhost:8000```
- Documentação da API: ```http://localhost:8000/docs```
- Interface Streamlit: ```http://localhost:8501```

4. **Para parar os containers**:
```
docker-compose down
```

### 💡 Dicas Extras
- Se a interface não abrir automaticamente, copie o link mostrado no terminal (geralmente ```http://localhost:8501```) e cole no navegador.
- Para parar a aplicação local, pressione ```CTRL+C``` nos terminais.
- No Docker, você pode visualizar os logs com ```docker-compose logs -f``` ou ```docker-compose logs -f [serviço]``` para um serviço específico.
- Se estiver usando Docker e precisar reiniciar apenas um serviço: ```docker-compose restart [serviço]```
## 🏗️ Arquitetura da Aplicação

- Usuário acessa o app → Streamlit

- Streamlit envia nome da cidade → Geocodifica com Nominatim

- Com as coordenadas → faz uma requisição POST ao FastAPI (/forecast)

- FastAPI consulta a Open-Meteo e retorna os dados

- Streamlit exibe o resultado

![Arquitetura_da Aplicacao](./assets/fluxograma_da_aplicacao.png)

## 📂 Estrutura do Projeto
### Estrutura de Diretórios: 

```
forecast_project/
├── api/                           # Contém a lógica da API FastAPI.
│    └── main.py                   # Código principal da API.
├── assets/
│    ├── clima_api_teste.gif       # Gif mostrando o projeto em execução.
│    └── fluxograma_da_aplicacao.png  # Arquitetura da aplicação.
├── .dockerignore                  # Arquivos a serem ignorados pelo Docker
├── .env                           # Arquivo de variáveis de ambiente (não versionado)
├── .env.example                   # Exemplo de configuração de variáveis de ambiente
├── Dockerfile                     # Instruções para construção da imagem Docker
├── docker-compose.yml             # Configuração dos serviços Docker
├── README.md                      # Documentação do projeto.
├── app_streamlit.py               # Interface web com Streamlit.
├── LICENSE                        # Arquivo de licença proprietária do projeto.
└── requirements.txt               # Lista de dependências do projeto.
```

## ⚖️ Licença
Este projeto é protegido por uma Licença Proprietária. Todos os direitos reservados.

O uso, modificação e distribuição deste software são estritamente proibidos sem a autorização.

<img src="https://badgen.net/badge/License/Proprietary License/gray?icon=github" alt="Status Badge"/>

## 👩‍💻 Responsável Pelo Projeto

[<img loading="lazy" src="https://avatars.githubusercontent.com/u/101699095?v=4" width=115><br><sub>Nathalia Reis</sub>](https://github.com/NathaliaOSReis)





