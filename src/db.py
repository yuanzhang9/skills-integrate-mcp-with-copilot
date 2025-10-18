from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()

class Activity(Base):
    __tablename__ = 'activities'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(String)
    schedule = Column(String)
    max_participants = Column(Integer)
    participants = relationship('Participant', back_populates='activity')

class Participant(Base):
    __tablename__ = 'participants'
    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    activity_id = Column(Integer, ForeignKey('activities.id'))
    activity = relationship('Activity', back_populates='participants')

# Database setup
DATABASE_URL = "sqlite:///./school.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)
