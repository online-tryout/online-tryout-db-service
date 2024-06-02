from typing import List
from pydantic import BaseModel

import uuid

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
    
class GetOptionModuleParams(BaseModel):
    id: uuid.UUID
    content: str
    isTrue: bool
    optionOrder: int

class GetQuestionModuleParams(BaseModel):
    id: uuid.UUID
    content: str
    questionOrder: int
    options: List[GetOptionModuleParams]

class GetModuleParams(BaseModel):
    id: uuid.UUID
    title: str
    moduleOrder: int
    questions: List[GetQuestionModuleParams]

class GetTryoutParams(BaseModel):
    id: uuid.UUID
    title: str
    price: float
    status: str
    startedAt: str
    endedAt: str
    modules: List[GetModuleParams]
    
class TryoutResponse(BaseModel):
    tryouts: List[GetTryoutParams]
    message: str
