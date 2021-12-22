import logging
import nltk
from newspaper import Article, fulltext

from app.models.tortoise import TextSummary

logging.basicConfig(level=logging.INFO)


async def generate_summary(summary_id: int, url: str) -> None:
    article = Article(url)
    article.download()
    article.parse()

    try:
        nltk.data.find("tokenizers/punkt")
    except LookupError:
        nltk.download("punkt")
    finally:
        article.nlp()

    summary = article.summary

    await TextSummary.filter(id=summary_id).update(summrary=summary)


async def generate_summary_from_text(text: str) -> str:
    html = f'''
    <!DOCTYPE html>
    <html>
    <body>
    <p>
    {text}
    </p>
    </body>
    </html>
    '''
    logging.info(f"text: {text}")
    logging.info(f"html: {html}")
    logging.info(f"fulltext(html, 'en'): {fulltext(html, 'en')}")


    article = Article(url = 'https://qrspace.io')
    article.set_html(html)
    article.parse()

    try:
        nltk.data.find("tokenizers/punkt")
    except LookupError:
        nltk.download("punkt")
    finally:
        article.nlp()

    t = fulltext(html, 'en').nlp()
    summary = article.summary
    tags = article.tags

    logging.info(f" text: {t}")
    logging.info(f" tags: {tags}")
    logging.info(f"summary text: {summary}")

    return summary

