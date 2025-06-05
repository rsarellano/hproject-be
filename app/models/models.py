from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from database import Base

class Questions(Base)

    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    question_text = Column(String, index=True)
    is_correct = Column(Boolean, default=False)
    

    class Choice(Base):
        __tablename__ = "choices"

        id = Column(Integer, primary_key=True, index=True)
        choice_text = Column(String, index=True)
        is_correct = Column(Boolean, default=False)
        question_id = Column(Integer, ForeignKey("questions.id"))
        
        
    class Answer(Base):
        __tablename__ = "answers"

        id = Column(Integer, primary_key=True, index=True)
        answer_text = Column(String, index=True)
        question_id = Column(Integer, ForeignKey("questions.id"))
        
        
