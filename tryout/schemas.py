from typing import List
from pydantic import BaseModel

import uuid

class OptionModuleParams(BaseModel):
    content: str
    is_true: bool
    option_order: int

class QuestionModuleParams(BaseModel):
    content: str
    question_order: int
    options: List[OptionModuleParams]

class CreateModuleParams(BaseModel):
    title: str
    module_order: int
    questions: List[QuestionModuleParams]

class CreateTryoutParams(BaseModel):
    title: str
    price: float
    status: str
    started_at: str
    ended_at: str
    modules: List[CreateModuleParams]
    
class GetOptionModuleParams(BaseModel):
    id: uuid.UUID
    content: str
    is_true: bool
    option_order: int

class GetQuestionModuleParams(BaseModel):
    id: uuid.UUID
    content: str
    question_order: int
    options: List[GetOptionModuleParams]

class GetModuleParams(BaseModel):
    id: uuid.UUID
    title: str
    module_order: int
    questions: List[GetQuestionModuleParams]

class GetTryoutParams(BaseModel):
    id: uuid.UUID
    title: str
    price: float
    status: str
    started_at: str
    ended_at: str
    modules: List[GetModuleParams]
    
class TryoutResponse(BaseModel):
    tryouts: List[GetTryoutParams]
    message: str
