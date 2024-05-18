from sqlalchemy.orm import Session
from tryout import models, schemas
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

def get_tryout(db: Session, tryout_id: uuid.UUID):
    return db.query(models.Tryout).filter(models.Tryout.id == tryout_id).first()
