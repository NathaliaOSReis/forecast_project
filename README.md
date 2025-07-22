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

## 🛠 Como Abrir e Executar Esse Projeto

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
4. **Inicie a API (FastAPI)**:
```
uvicorn api.main:app --reload

```
- A API estará disponível em: ```http://127.0.0.1:8000```

- Você pode acessar a documentação automática da API em: ```http://127.0.0.1:8000/docs```

5. **Em outro terminal, execute a interface (Streamlit)**:
* Se estiver com o ambiente virtual ativado ainda
```
streamlit run app_streamlit.py

```
* A interface abrirá automaticamente em seu navegador em: ```http://localhost:8501```


### 💡 Dicas Extras
Se a interface não abrir automaticamente, copie o link mostrado no terminal (geralmente ```http://localhost:8501```) e cole no navegador.

Para parar a aplicação, pressione ```CTRL+C``` nos dois terminais.
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