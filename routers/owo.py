from fastapi import APIRouter
from pydantic import BaseModel
from pyowo import owo


class OwOResponse(BaseModel):
    text: str


router = APIRouter()

@router.get("/{content}")
async def get_owo(content: str) -> OwOResponse:
    return {"text": owo(content)}
