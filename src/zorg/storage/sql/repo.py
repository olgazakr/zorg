"""Contains the Repo class."""

from __future__ import annotations

from eris import ErisResult, Ok
from logrus import Logger
from potoroo import QueryRepo
from sqlmodel import Session, select

from . import converters, models as sql
from ...domain.models import OrZorgQuery, ZorgFile


logger = Logger(__name__)


class ZorgSQLRepo(QueryRepo[str, ZorgFile, OrZorgQuery]):
    """Repo that stores zorg notes in sqlite database."""

    def __init__(
        self,
        session: Session,
    ) -> None:
        self._session = session

    def add(self, note: ZorgFile, /, *, key: str = None) -> ErisResult[str]:
        """Adds a new note to the DB.

        Returns a unique identifier that has been associated with this note.
        """
        del key
        self._session.add(note)
        # TODO(bugyi): Add ID generation logic here, which should add an event to the message bus.
        return Ok("")

    def remove(
        self, note: ZorgFile, /  # noqa: W504
    ) -> ErisResult[ZorgFile | None]:
        """Remove a note from the DB."""
        self._session.delete(note)
        return Ok(note)

    def get(self, key: str) -> ErisResult[ZorgFile | None]:
        """Retrieve a note from the DB."""
        stmt = select(sql.ZorgFile).where(sql.ZorgFile.id == int(key))
        results = self._session.exec(stmt)
        sql_zorg_file = results.first()
        if sql_zorg_file:
            return Ok(converters.sql_file_to_model(sql_zorg_file))
        else:
            return Ok(None)

    def get_by_query(self, query: OrZorgQuery) -> ErisResult[list[ZorgFile]]:
        """Get note(s) from DB by using a query."""
        del query
        return Ok([])

    def all(self) -> ErisResult[list[ZorgFile]]:
        """Returns all zorg notes contained in the underlying SQL database."""
        stmt = select(sql.ZorgFile)
        return Ok([
            converters.sql_file_to_model(sql_note)
            for sql_note in self._session.exec(stmt).all()
        ])