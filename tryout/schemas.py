from typing import List
from pydantic import BaseModel

class OptionModuleParams(BaseModel):
    content: str
    isTrue: bool
    optionOrder: int

class QuestionModuleParams(BaseModel):
    content: str
    questionOrder: int
    options: List[OptionModuleParams]

class CreateModuleParams(BaseModel):
    title: str
    moduleOrder: int
    questions: List[QuestionModuleParams]

class CreateTryoutParams(BaseModel):
    title: str
    price: float
    status: str
    startedAt: str
    endedAt: str
    modules: List[CreateModuleParams]
