# 🧠 ArxivInsight

> *Transforme papers complexos em resumos claros e acessíveis.*

## 😵‍💫 O problema

Você já tentou entender um artigo como

> **“Attention Is All You Need”**
> ou qualquer outro paper do [arXiv.org](https://arxiv.org)?

Esses estudos são fundamentais para a ciência moderna — mas, para quem não domina o jargão técnico, eles soam como outro idioma.

Muitas vezes, tudo o que queremos é **entender a essência**:

* O que esse estudo realmente faz?
* Por que ele é importante?
* Como ele pode impactar o mundo real?

Mas a barreira da linguagem científica torna isso difícil.
Foi por isso que nasceu o **ArxivInsight**.

## 💡 A solução

O **ArxivInsight** é uma ferramenta de **linha de comando (CLI)** que utiliza o **Azure OpenAI** para **traduzir papers técnicos do arXiv em resumos não técnicos e acessíveis**.

Basta colar o ID de um artigo — e o ArxivInsight gera um resumo que qualquer pessoa pode entender.

Ele não simplifica demais, mas **explica com clareza**, destacando:

* 🧩 **O problema** que o estudo aborda
* 💡 **A ideia principal** da solução
* 🌍 **O impacto prático** das descobertas

## ⚙️ Como funciona

| Etapa                 | Descrição                                                                      |
| --------------------- | ------------------------------------------------------------------------------ |
| **1️⃣ Entrada**       | Você fornece o ID do artigo do arXiv.                                  |
| **2️⃣ Extração**      | O ArxivInsight busca automaticamente o título, autores e resumo técnico.       |
| **3️⃣ Interpretação** | O Azure OpenAI (modelo GPT) reescreve o texto em linguagem clara e simples. |
| **4️⃣ Exibição**      | O resumo é exibido diretamente no terminal, pronto para leitura.               |

🧠 Em resumo: ele é o seu **tradutor pessoal de papers científicos**.

## 🧭 Exemplo rápido

> Exemplo: tentar entender “Attention Is All You Need”

```bash
python arxivinsight.py 1706.03762
```

📤 **Saída esperada:**

```
📘 Título: Attention Is All You Need

🎓 Autores: Ashish Vaswani,Noam Shazeer,Niki Parmar,Jakob Uszkoreit,Llion Jones,Aidan N. Gomez,Lukasz Kaiser,Illia Polosukhin

🧩 Resumo não técnico:
Um novo estudo propõe uma abordagem inovadora para melhorar a forma como as máquinas traduzem textos de um idioma para outro. Tradicionalmente, esses sistemas eram complexos e demorados, utilizando técnicas que envolviam redes neurais com múltiplas camadas. O problema que o estudo aborda é a necessidade de tornar esse processo mais eficiente, tanto em termos de tempo quanto de qualidade na tradução. A solução apresentada pelos pesquisadores é uma nova estrutura chamada Transformer, que se baseia apenas em mecanismos de atenção. Isso significa que o modelo consegue focar nas partes mais relevantes do texto de entrada, sem precisar das técnicas mais complicadas que eram usadas antes. Como resultado, o Transformer não só produz traduções de melhor qualidade, mas também é mais rápido para ser treinado. Os resultados foram impressionantes: o modelo alcançou novas marcas de qualidade em traduções do inglês para o alemão e do inglês para o francês, superando os melhores modelos existentes de forma significativa. Além disso, o Transformer mostrou que também pode ser aplicado com sucesso em outras tarefas de linguagem, como a análise de estruturas de frases. O impacto prático desse estudo é grande. Com essa nova abordagem, as máquinas poderão traduzir textos com mais precisão e em menos tempo, o que pode beneficiar desde tradutores profissionais até a utilização de serviços de tradução em plataformas online, tornando a comunicação entre diferentes idiomas mais acessível e eficiente.

link: https://arxiv.org/pdf/1706.03762
```

## ⚙️ Instalação

### 1️⃣ Clone o repositório

```bash
git clone https://github.com/igorcarvalhh/arxiv-insight.git
cd arxiv-insight
```

### 2️⃣ Crie e ative o ambiente virtual

```bash
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows
```

### 3️⃣ Instale as dependências

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure o acesso ao Azure

Crie um arquivo `.env` na raiz com suas credenciais:

```
AZURE_OPENAI_API_KEY=<sua-chave>
AZURE_ENDPOINT=<seu-endpoint>
DEPLOYMENT_NAME=<modelo>
```

## ▶️ Uso

### Modo básico

```bash
python arxivinsight.py <arxiv_id>
```

### Exemplo

```bash
python arxivinsight.py https://arxiv.org/abs/2403.12345
```

### Execução via terminal

![CLI Example](https://fakeimg.pl/800x200/1e1e1e/e8e8e8?text=python+arxivinsight.py+1706.03762\&font=consolas)

### Saída formatada

![Output Example](https://fakeimg.pl/800x350/222/eee?text=Resumo+gerado+no+terminal\&font=consolas)

## 🧰 Tecnologias usadas

* 🐍 **Python 3.14**
* ☁️ **Azure OpenAI (gpt-4o-mini)**
* 🔍 **BeautifulSoup4** — para coletar texto do arXiv
* ⚙️ **Requests** — para buscar artigos
* 🔐 **python-dotenv** — para gerenciar chaves

## 🤝 Contribua

Quer participar?

1. Faça um fork 🍴
2. Crie uma branch (`git checkout -b feature/nova-feature`)
3. Faça o commit e o push 🚀
4. Abra um Pull Request

## 📄 Licença

Distribuído sob a licença **MIT**.
Consulte o arquivo `LICENSE` para mais detalhes.
