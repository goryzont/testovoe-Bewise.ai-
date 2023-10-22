from sqlalchemy import Table, Column, Integer, String, TIMESTAMP, MetaData

metadata = MetaData()

question = Table(
    "questions",
    metadata,
    Column("id_question", Integer, primary_key=True),
    Column("question", String),
    Column("answer", String),
    Column("created_at", TIMESTAMP),
)
