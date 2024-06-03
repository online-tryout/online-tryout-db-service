from sqlalchemy import Column, DateTime, func, String, Integer, ForeignKey, Text, Boolean, DECIMAL
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship, backref
import uuid

from database import Base

class Tryout(Base):
    __tablename__ = "tryout"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String, nullable=False)
    price = Column(DECIMAL(10, 2), nullable=False)
    status = Column(String, nullable=False)
    started_at = Column(DateTime(timezone=True), nullable=False)
    ended_at = Column(DateTime(timezone=True), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

    modules = relationship("Module", backref="tryout", cascade="all, delete")

class TryoutInstance(Base):
    __tablename__ = "tryoutinstance"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    tryout_id = Column(UUID(as_uuid=True), ForeignKey("tryout.id", ondelete="CASCADE"), nullable=False)
    user_id = Column(UUID(as_uuid=True), ForeignKey("user.id", ondelete="CASCADE"), nullable=False)
    status = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

class Module(Base):
    __tablename__ = "module"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String, nullable=False)
    tryout_id = Column(UUID(as_uuid=True), ForeignKey("tryout.id", ondelete="CASCADE"), nullable=False)
    module_order = Column(Integer)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

    questions = relationship("Question", backref="module", cascade="all, delete")

class ModuleInstance(Base):
    __tablename__ = "moduleinstance"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    module_id = Column(UUID(as_uuid=True), ForeignKey("module.id", ondelete="CASCADE"), nullable=False)
    tryout_instance_id = Column(UUID(as_uuid=True), ForeignKey("tryoutinstance.id", ondelete="CASCADE"), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

class Question(Base):
    __tablename__ = "question"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    content = Column(Text, nullable=False)
    module_id = Column(UUID(as_uuid=True), ForeignKey("module.id", ondelete="CASCADE"), nullable=False)
    question_order = Column(Integer)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

    options = relationship("Option", backref="question", cascade="all, delete")

class Option(Base):
    __tablename__ = "option"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    content = Column(Text, nullable=False)
    question_id = Column(UUID(as_uuid=True), ForeignKey("question.id", ondelete="CASCADE"), nullable=False)
    is_true = Column(Boolean, nullable=False, default=False)
    option_order = Column(Integer)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

class Answer(Base):
    __tablename__ = "answer"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    question_id = Column(UUID(as_uuid=True), ForeignKey("question.id", ondelete="CASCADE"), nullable=False)
    option_id = Column(UUID(as_uuid=True), ForeignKey("option.id", ondelete="CASCADE"), nullable=False)
    module_instance_id = Column(UUID(as_uuid=True), ForeignKey("moduleinstance.id", ondelete="CASCADE"), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
