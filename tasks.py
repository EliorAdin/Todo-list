from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import json

# הגדרת בסיס הנתונים
engine = create_engine('sqlite:///task_journal.db', echo=True)
Base = declarative_base()


# הגדרת מודל Task
class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(Text)
    start_date = Column(String)
    end_date = Column(String)
    status = Column(String)
    subtasks = Column(Text)  # JSON string
    notes = Column(Text)  # JSON string

    def __repr__(self):
        return f"<Task(title='{self.title}', status='{self.status}')>"


# יצירת הטבלה
Base.metadata.create_all(engine)

# יצירת סשן
Session = sessionmaker(bind=engine)
session = Session()
