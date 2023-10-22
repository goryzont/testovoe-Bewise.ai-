from fastapi import FastAPI

from core.question.routers import router as router_question

app = FastAPI(
    title="Вопросы для викторины"
)

app.include_router(router_question)
