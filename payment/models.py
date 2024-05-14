import uuid
from sqlalchemy import UUID, Column, DECIMAL, DateTime, ForeignKey, String, func

from database import Base


class Transactions(Base):
    __tablename__ = 'transactions'
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    tryout_id = Column(UUID(as_uuid=True), ForeignKey("tryout.id", ondelete="SET NULL"), nullable=True)
    user_id = Column(UUID(as_uuid=True), ForeignKey("user.id", ondelete="SET NULL"), nullable=True)

    amount = Column(DECIMAL(10, 2), nullable=False)
    status = Column(String)

    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
