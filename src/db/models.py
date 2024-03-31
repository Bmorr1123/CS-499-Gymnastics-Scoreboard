from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column, declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.types import LargeBinary, Float


class Models(DeclarativeBase):
    pass


class School(Models):
    __tablename__ = "school"
    school_id: Mapped[int] = mapped_column(primary_key=True)
    school_name: Mapped[str] = mapped_column(String(30))
    school_logo: Mapped[Optional[str]] = mapped_column(LargeBinary)


class Event(Models):
    __tablename__ = "event"
    event_id: Mapped[int] = mapped_column(primary_key=True)
    event_name: Mapped[str] = mapped_column(String(30))
    event_location: Mapped[Optional[str]] = mapped_column(String(30))
    event_date: Mapped[Optional[str]] = mapped_column(String(30))


class Gymnast(Models):
    __tablename__ = "gymnast"
    gymnast_id: Mapped[int] = mapped_column(primary_key=True)
    school_id: Mapped[School] = mapped_column(ForeignKey(School.school_id))
    first_name: Mapped[str] = mapped_column(String(30))
    last_name: Mapped[str] = mapped_column(String(30))
    major: Mapped[str] = mapped_column(String(30))
    classification: Mapped[str] = mapped_column(String(30))
    gymnast_picture: Mapped[Optional[str]] = mapped_column(LargeBinary)
    # Leaving this here as an example for later
    # addresses: Mapped[List["Address"]] = relationship(
    #     back_populates="user", cascade="all, delete-orphan"
    # )
    def __repr__(self) -> str:
        return f"Gymnast(gymnast_id={self.gymnast_id!r}, first_name={self.first_name!r}, last_name={self.last_name!r}, major={self.major!r}, classification={self.classification!r})"


class Lineup(Models):
    __tablename__ = "lineup"
    lineup_id: Mapped[int] = mapped_column(primary_key=True)
    school_id: Mapped[School] = mapped_column(ForeignKey(School.school_id))
    event_id: Mapped[Event] = mapped_column(ForeignKey(Event.event_id))
    apparatus_name: Mapped[str] = mapped_column(String(30))

    def __repr__(self) -> str:
        return f"Lineup(lineup_id={self.lineup_id!r}, school_id={self.school_id!r}, event_id={self.event_id!r}, apparatus_name={self.apparatus_name!r})"


class LineupEntry(Models):
    __tablename__ = "lineup_entry"
    lineup_entry_id: Mapped[int] = mapped_column(primary_key=True)
    lineup_id: Mapped[int] = mapped_column(ForeignKey(Lineup.lineup_id))
    gymnast_id: Mapped[int] = mapped_column(ForeignKey(Gymnast.gymnast_id))
    score: Mapped[float] = mapped_column(Float)
    status: Mapped[str] = mapped_column(String(30))

    def __repr__(self) -> str:
        return f"LineupEntry(lineyp_entry_id={self.lineup_entry_id!r}, gymnast_id={self.gymnast_id!r}, lineup_id={self.lineup_id!r}, score={self.score!r}, status={self.status!r})"


class Judge(Models):
    __tablename__ = "judge"
    judge_id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(30))
    last_name: Mapped[str] = mapped_column(String(30))
    event_id: Mapped[int] = mapped_column(ForeignKey(Event.event_id))
    apparatus_name: Mapped[str] = mapped_column(String(30))

# class Address(Models):
#     __tablename__ = "address"
#     id: Mapped[int] = mapped_column(primary_key=True)
#     email_address: Mapped[str]
#     user_id: Mapped[int] = mapped_column(ForeignKey("user_account.id"))
#     user: Mapped["User"] = relationship(back_populates="addresses")
#     def __repr__(self) -> str:
#         return f"Address(id={self.id!r}, email_address={self.email_address!r})"