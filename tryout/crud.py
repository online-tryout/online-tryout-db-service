from sqlalchemy.orm import Session
from tryout import models, schemas
from sqlalchemy import desc
from auth import crud

import uuid
from dateutil import parser

def create_tryout(db: Session, tryout_params: schemas.CreateTryoutParams):
    try:
        # Create tryout instance
        tryout = models.Tryout(
            title=tryout_params.title,
            price=tryout_params.price,
            status=tryout_params.status,
            started_at=parser.isoparse(tryout_params.startedAt),
            ended_at=parser.isoparse(tryout_params.endedAt)
        )
        db.add(tryout)
        db.commit()
        db.refresh(tryout)

        # Create modules
        for module_params in tryout_params.modules:
            module = models.Module(
                title=module_params.title,
                tryout_id=tryout.id,
                module_order=module_params.moduleOrder
            )
            db.add(module)
            db.commit()
            db.refresh(module)

            # Create questions
            for question_params in module_params.questions:
                question = models.Question(
                    content=question_params.content,
                    module_id=module.id,
                    question_order=question_params.questionOrder
                )
                db.add(question)
                db.commit()
                db.refresh(question)

                # Create options
                for option_params in question_params.options:
                    option = models.Option(
                        content=option_params.content,
                        question_id=question.id,
                        is_true=option_params.isTrue,
                        option_order=option_params.optionOrder
                    )
                    db.add(option)
                    db.commit()
                    db.refresh(option)

        return tryout
    except Exception as e:
        db.rollback()
        raise ValueError(crud.handle_exception(e))

def get_all_tryouts(db: Session):
    tryouts = db.query(models.Tryout).order_by(desc(models.Tryout.updated_at)).all()
    return [serialize_tryout(tryout) for tryout in tryouts]

def serialize_tryout(tryout: models.Tryout) -> schemas.CreateTryoutParams:
    return schemas.GetTryoutParams(
        id=tryout.id,
        title=tryout.title,
        price=float(tryout.price),
        status=tryout.status,
        started_at=tryout.started_at.isoformat(),
        ended_at=tryout.ended_at.isoformat(),
        modules=[
            serialize_module(module) for module in tryout.modules
        ]
    )

def serialize_module(module: models.Module):
    return schemas.GetModuleParams(
        id=module.id,
        title=module.title,
        module_order=module.module_order,
        questions=[
            serialize_question(question) for question in module.questions
        ]
    )

def serialize_question(question: models.Question):
    return schemas.GetQuestionModuleParams(
        id=question.id,
        content=question.content,
        question_order=question.question_order,
        options=[
            serialize_option(option) for option in question.options
        ]
    )

def serialize_option(option: models.Option):
    return schemas.GetOptionModuleParams(
        id=option.id,
        content=option.content,
        is_true=option.is_true,
        option_order=option.option_order
    )

def get_tryout(db: Session, tryout_id: uuid.UUID):
    tryout = db.query(models.Tryout).filter(models.Tryout.id == tryout_id).first()
    return serialize_tryout(tryout)

def get_module_by_id(db: Session, id: uuid.UUID):
    module = db.query(models.Module).filter(models.Module.id == id).first()
    return serialize_module(module=module)