from datetime import datetime, timedelta

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


class Weekdays:
    def __init__(self):
        today = datetime.today()
        self._weekdays = (today + timedelta(days=day_offset)
                          for day_offset in range(7))

    def next(self):
        try:
            weekday_date = next(self._weekdays)
        except StopIteration:
            return None
        weekday_info = {
            'date': weekday_date,
            'tasks': tasks_get_by_date(weekday_date)
        }
        return weekday_info


def init_db():
    Base.metadata.create_all(engine)


def tasks_get_by_date(date):
    session = Session()
    tasks = session.query(Task).\
        filter(Task.deadline == date.strftime("%Y-%m-%d")).all()
    if len(tasks) == 0:
        return None
    return tasks


def tasks_get_today():
    return tasks_get_by_date(datetime.today())


def tasks_get_all():
    session = Session()
    tasks = session.query(Task).order_by(Task.deadline).all()
    session.close()
    if len(tasks) == 0:
        return None
    return tasks


def tasks_get_missed():
    session = Session()
    tasks = session.query(Task).\
        filter(Task.deadline < datetime.today().date()).all()
    if len(tasks) == 0:
        return None
    return tasks



def task_create(task_data):
    session = Session()
    _task = Task(**task_data)
    session.add(_task)
    session.commit()


def task_delete(task):
    session = Session()
    session.delete(task)
    session.commit()
