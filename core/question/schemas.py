from datetime import datetime

from pydantic import BaseModel


class Question(BaseModel):
    id_question: int
    question: str
    answer: str
    created_at: datetime


