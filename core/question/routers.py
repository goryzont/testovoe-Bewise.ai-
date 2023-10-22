from fastapi import APIRouter, Depends
from sqlalchemy import insert, text
from sqlalchemy.ext.asyncio import AsyncSession
from requests import get

from core.database import get_async_session
from .schemas import Question
from .models import question

router = APIRouter(
    prefix='/question',
    tags=["Question"]
)


@router.post("/")
async def add_question(quantity_questions: int, session: AsyncSession = Depends(get_async_session)) -> Question:
    quantity_questions = quantity_questions
    url = f"https://jservice.io/api/random?count={quantity_questions}"
    data = get(url).json()
    questions = [Question(id_question=quest["id"],
                          question=quest["question"],
                          answer=quest["answer"],
                          created_at=quest["created_at"][0:len(quest["created_at"]) - 1]) for quest in data]
    last = None  # запоминаем последний вопрос
    for quest in questions:   # type: Question
        info = text(f"SELECT id_question FROM questions WHERE id_question={quest.id_question}")
        result = await session.execute(info)
        check = result.fetchone()
        if check is None:
            stmt = insert(question).values(**quest.model_dump())
            await session.execute(stmt)
            await session.commit()
            last = dict(quest)  # Если он есть
        else:
            last = None  # Если его нет
            continue
    return last
