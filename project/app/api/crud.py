from typing import List, Optional

from app.models.pydantic import SummaryPayloadSchema, SummaryPayloadSchemaText, SummaryResponseSchemaText
from app.models.tortoise import TextSummary
from app.summarizer import generate_summary_from_text


async def post(payload: SummaryPayloadSchema) -> int:
    summary = TextSummary(
        url=payload.url,
        summrary="",
    )
    await summary.save()
    return summary.id


async def post_text(payload: SummaryPayloadSchemaText) -> SummaryResponseSchemaText:

    summary_text = await generate_summary_from_text(text=payload.text)

    summary = TextSummary(
        url=' ',
        summrary=summary_text,
    )
    await summary.save()

    response_object = {
        "id": summary.id,
        "text": payload.text,
        "summary": summary.summrary,
    }

    return response_object


async def get(id: int) -> Optional[dict]:
    summary = await TextSummary.filter(id=id).first().values()
    if summary:
        return summary
    return None


async def get_all() -> List:
    summaries = await TextSummary.all().values()
    return summaries


async def delete(id: int) -> int:
    summary = await TextSummary.filter(id=id).first().delete()
    return summary


async def put(id: int, payload: SummaryPayloadSchema) -> Optional[dict]:
    summary = await TextSummary.filter(id=id).update(
        url=payload.url, summrary=payload.summary
    )
    if summary:
        updated_summary = await TextSummary.filter(id=id).first().values()
        return updated_summary
    return None
