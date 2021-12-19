from pydantic import AnyHttpUrl, BaseModel


class SummaryPayloadSchema(BaseModel):
    url: AnyHttpUrl


class SummaryResponseSchema(SummaryPayloadSchema):
    id: str


class SummaryUpdatePayloadSchema(SummaryPayloadSchema):
    summary: str
