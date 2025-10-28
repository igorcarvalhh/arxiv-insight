# 🧠 ArxivInsight

> *Resumos claros de pesquisas complexas.*

## 📘 Visão geral

O **ArxivInsight** é uma ferramenta que utiliza o **Azure OpenAI** para gerar **resumos não técnicos** de artigos científicos publicados no [arXiv.org](https://arxiv.org).

O objetivo do projeto é **tornar o conhecimento científico mais acessível** — traduzindo textos técnicos em explicações simples, envolventes e compreensíveis por qualquer pessoa interessada em ciência e tecnologia.

## 🚀 Funcionalidades principais

* 🔗 Entrada via **link ou ID do arXiv**
* 🧾 Extração automática de **título, autores e resumo original**
* 🧠 Geração de **resumo não técnico** via **Azure OpenAI (GPT)**
* 🌍 Resultados claros e acessíveis, destacando:

  * O problema que o estudo resolve
  * A ideia principal da solução
  * O impacto e a importância prática

## 🧩 Arquitetura geral

```
arxiv.org → extração de dados → Azure OpenAI → resumo não técnico → exibição
```

### Componentes

* **Backend (Python)** – responsável por buscar artigos no arXiv e enviar o texto ao modelo.
* **Azure OpenAI** – modelo GPT configurado para gerar resumos simplificados.
* **API (FastAPI ou Flask)** – fornece endpoints para consumo via navegador ou integração externa.
* **Frontend opcional** – interface simples (React, Streamlit ou HTML) para facilitar o uso.

## ⚙️ Instalação e uso

### 1. Clonar o repositório

```bash
git clone https://github.com/<seu-usuario>/ArxivInsight.git
cd ArxivInsight
```

### 2. Criar e ativar um ambiente virtual

```bash
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

### 4. Configurar variáveis de ambiente

Crie um arquivo `.env` com as seguintes chaves:

```
AZURE_OPENAI_API_KEY=<sua-chave-do-azure>
AZURE_ENDPOINT=<seu-endpoint-do-azure>
DEPLOYMENT_NAME=<nome-do-modelo>
```

### 5. Executar o servidor

Se estiver usando **FastAPI**:

```bash
uvicorn main:app --reload
```

A API ficará disponível em:
➡️ `http://127.0.0.1:8000`

## 🧠 Exemplo de uso

### Endpoint

`POST /summarize`

### Corpo da requisição:

```json
{
  "arxiv_id": "2403.12345"
}
```

### Resposta esperada:

```json
{
  "title": "Sketch2BIM: A Multi-Agent Human-AI Collaborative Pipeline...",
  "authors": ["Abir Khan Ratul", "Sanjay Acharjee", "..."],
  "technical_summary": "This study introduces a multi-agent pipeline...",
  "non_technical_summary": "O estudo apresenta uma nova forma de transformar plantas desenhadas à mão em modelos 3D, combinando pessoas e inteligência artificial..."
}
```

## 📚 Tecnologias utilizadas

* **Python 3.10+**
* **FastAPI** (ou Flask)
* **Requests** + **BeautifulSoup4**
* **Azure OpenAI Service**
* **Dotenv**
* **Uvicorn**

## 🧭 Roadmap futuro

* [ ] Suporte a múltiplos idiomas (português, inglês, espanhol)
* [ ] Interface web interativa (React/Streamlit)
* [ ] Resumos técnicos e não técnicos lado a lado
* [ ] Curadoria automática de artigos por área
* [ ] Integração com Zotero, Notion e Obsidian

## 💡 Motivação

A maioria das pesquisas publicadas em plataformas como o arXiv é escrita em linguagem altamente técnica.
O **ArxivInsight** busca quebrar essa barreira — ajudando estudantes, educadores e curiosos a entender *o que a ciência está fazendo agora*, sem precisar de formação específica na área.

## 🤝 Contribuição

Contribuições são bem-vindas!
Siga os passos:

1. Faça um fork do projeto
2. Crie uma branch (`git checkout -b feature/nome-da-feature`)
3. Faça o commit (`git commit -m "Adiciona nova feature"`)
4. Envie para o repositório remoto (`git push origin feature/nome-da-feature`)
5. Abra um Pull Request 🎉

## 📄 Licença

Distribuído sob a licença **MIT**.
Consulte o arquivo `LICENSE` para mais informações.

## 🌟 Exemplo visual (futuro)

> *Um painel simples exibindo o resumo não técnico e o resumo original lado a lado.*

```
┌──────────────────────────────┬──────────────────────────────┐
│        Resumo original       │       Resumo não técnico     │
│  Texto do paper técnico...   │  Explicação simples e clara  │
└──────────────────────────────┴──────────────────────────────┘
```
