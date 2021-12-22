from pydantic import AnyHttpUrl, BaseModel


class SummaryPayloadSchema(BaseModel):
    url: AnyHttpUrl


class SummaryPayloadSchemaText(BaseModel):
    text: str


class SummaryResponseSchema(SummaryPayloadSchema):
    id: int


class SummaryResponseSchemaText(SummaryPayloadSchemaText):
    summary: str
    id: int


class SummaryUpdatePayloadSchema(SummaryPayloadSchema):
    summary: str
