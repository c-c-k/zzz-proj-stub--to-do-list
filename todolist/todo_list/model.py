from datetime import datetime

from sqlalchemy import (
    create_engine, Column, String, Integer, Date)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DB_URI = "sqlite:///todo.db?check_same_thread=False"
engine = create_engine(DB_URI)
Session = sessionmaker(bind=engine)

Base = declarative_base()


class Task(Base):
    __tablename__ = "task"

    id = Column(Integer, primary_key=True)
    task = Column(String)
    deadline = Column(Date, default=datetime.today())

    def __repr__(self):
        return self.task


class Tasks:
    def __init__(self, tasks):
        self._tasks_iterator = iter(tasks)

    def next(self):
        try:
            task = next(self._tasks_iterator)
        except StopIteration:
            task = None
        return task


def init_db():
    Base.metadata.create_all(engine)


def tasks_get_all():
    session = Session()
    tasks = session.query(Task).all()
    if len(tasks) == 0:
        return None
    return tasks


def task_create(task_data):
    session = Session()
    _task = Task(**task_data)
    session.add(_task)
    session.commit()
