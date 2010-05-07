from buedastatus.model.meta import Base
from datetime import datetime
from sqlalchemy import Column, String, Integer, TIMESTAMP

class Status(Base):
    __tablename__ = 'status'
    id = Column(Integer, primary_key=True)
    status = Column(String(255))
    time = Column(TIMESTAMP, default=datetime.now)
