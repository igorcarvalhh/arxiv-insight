import os, re
import argparse
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from openai import AzureOpenAI

def get_arxiv_data(arxiv_id):
    url = f"https://arxiv.org/abs/{arxiv_id}"
    pdf_url = f"https://arxiv.org/pdf/{arxiv_id}"

    response = requests.get(url)
    if response.status_code != 200:
        return None

    soup = BeautifulSoup(response.text, "html.parser")

    title = soup.find("h1", class_="title").get_text(strip=True).replace("Title:", "")
    authors = soup.find("div", class_="authors").get_text(strip=True).replace("Authors:", "")
    abstract = soup.find("blockquote", class_="abstract").get_text(strip=True).replace("Abstract:", "")

    return {
        "id": arxiv_id,
        "title": title,
        "authors": authors,
        "abstract": abstract,
        "pdf_url": pdf_url
    }

def summarize_paper(title, abstract):
    load_dotenv()
    
    try:
        client = AzureOpenAI(
            api_key=os.getenv("AZURE_OPENAI_API_KEY"),
            azure_endpoint=os.getenv("AZURE_ENDPOINT"),
            api_version="2024-05-01-preview"
        )

        prompt = f"""
        Faça um resumo não técnico do texto a seguir, explicando de forma simples o que o estudo faz, por que ele é importante e o que foi descoberto. Evite jargões técnicos e termos. Use uma linguagem acessível para um público geral, como se fosse uma matéria de revista de ciência ou tecnologia. Destaque: O problema que o estudo resolve; Como ele resolve (de forma geral, sem detalhes técnicos); Os resultados e o impacto prático. 

        Título: {title}

        Resumo técnico:
        {abstract}
        """

        response = client.chat.completions.create(
            model=os.getenv("DEPLOYMENT_NAME"),
            messages=[
                {"role": "system", "content": "Você é um assistente que gera resumos claros e acessíveis de artigos científicos."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=500
        )

        summary = response.choices[0].message.content.strip()
        return re.sub(r'\s+', ' ', summary)

    except Exception as e:
        return f"Erro ao gerar resumo: {e}"

def main():
    parser = argparse.ArgumentParser(
        description="🧠 ArxivInsight — transforme papers do arXiv em resumos claros e acessíveis."
    )
    parser.add_argument("paper_id", help="ID ou link do paper no arXiv (ex: 1706.03762 ou https://arxiv.org/abs/1706.03762)")
    args = parser.parse_args()

    paper_data = get_arxiv_data(args.paper_id)

    if not paper_data:
        print("❌ Não foi possível obter os dados do artigo.")
        return

    summary = summarize_paper(
        title=paper_data["title"],
        abstract=paper_data["abstract"]
    )

    output = f"""
📘 Título: {paper_data["title"]}

🎓 Autores: {paper_data["authors"]}

🧩 Resumo não técnico:
{summary}

link: {paper_data['pdf_url']}"""
    print(output)

if __name__ == "__main__":
    main()