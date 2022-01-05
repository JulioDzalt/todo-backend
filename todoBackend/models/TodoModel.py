from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from ..db.db import Base

class TodoModel(Base):

    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)

    # def __init__(self, title, description): #Constructor
    #     self.title = title
    #     self.description = description
