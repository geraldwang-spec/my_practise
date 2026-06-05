from datetime import datetime, timedelta, timezone
import sqlite3
from pathlib import Path
from sqlalchemy import Integer, String, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy.sql.functions import now

class Base(DeclarativeBase):
    pass

class UserModule(Base):
    __tablename__:str = "login"
    id:Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username:Mapped[str] = mapped_column(String, unique=True, nullable=False)
    passwd:Mapped[str] = mapped_column(String, nullable=False)
    mail: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    name: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    mail_ready: Mapped[bool] = mapped_column(Integer, nullable=False, default=False)
    account_created:Mapped[datetime] = mapped_column(
        nullable= False, 
        default=lambda: datetime.now(timezone.utc))
    mail_check_time:Mapped[datetime] = mapped_column(
        unique=False,
        default=lambda: datetime.now(tz=timezone.utc).replace(microsecond=0)+timedelta(minutes=15)
    ) 

class DatabaseManager:
    def __init__(self, db_url:str = "sqlite:///login.db") -> None:
        self._engine = create_engine(db_url, echo=False)
    

