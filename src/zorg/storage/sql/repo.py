"""Contains the Repo class."""

from __future__ import annotations

from eris import ErisResult, Ok
from logrus import Logger
from potoroo import QueryRepo
from sqlmodel import Session, select

from . import models as sql
from ...domain.messages.events import NewZorgNotesEvent
from ...domain.models import OrZorgQuery, ZorgFile
from .converters import ZorgFileConverter


logger = Logger(__name__)


class SQLRepo(QueryRepo[int, ZorgFile, OrZorgQuery]):
    """Repo that stores zorg notes in sqlite database."""

    def __init__(
        self,
        session: Session,
    ) -> None:
        self._session = session
        self._converter = ZorgFileConverter(session)

        self.seen: list[ZorgFile] = []

    def add(
        self, zorg_file: ZorgFile, /, *, key: int = None
    ) -> ErisResult[int]:
        """Adds a new file to the DB.

        Returns a unique identifier that has been associated with this file.
        """
        del key
        self._seen_zorg_file(zorg_file)
        _add_zorg_ids(zorg_file)
        sql_zorg_file = self._converter.from_entity(zorg_file)
        self._session.add(sql_zorg_file)
        return Ok(sql_zorg_file.id)

    def remove(
        self, zorg_file: ZorgFile, /  # noqa: W504
    ) -> ErisResult[ZorgFile | None]:
        """Remove a file from the DB."""
        self._session.delete(self._converter.from_entity(zorg_file))
        return Ok(zorg_file)

    def get(self, key: int) -> ErisResult[ZorgFile | None]:
        """Retrieve a file from the DB."""
        stmt = select(sql.ZorgFile).where(sql.ZorgFile.id == int(key))
        results = self._session.exec(stmt)
        sql_zorg_file = results.first()
        if sql_zorg_file:
            zorg_file = self._converter.to_entity(sql_zorg_file)
            self._seen_zorg_file(zorg_file)
            return Ok(zorg_file)
        else:
            return Ok(None)

    def get_by_query(self, query: OrZorgQuery) -> ErisResult[list[ZorgFile]]:
        """Get file(s) from DB by using a query."""
        del query
        result: list[ZorgFile] = []
        for zorg_file in result:
            self._seen_zorg_file(zorg_file)
        return Ok(result)

    def all(self) -> ErisResult[list[ZorgFile]]:
        """Returns all zorg notes contained in the underlying SQL database."""
        stmt = select(sql.ZorgFile)
        result: list[ZorgFile] = []
        for sql_zorg_file in self._session.exec(stmt).all():
            zorg_file = self._converter.to_entity(sql_zorg_file)
            self._seen_zorg_file(zorg_file)
        return Ok(result)

    def _seen_zorg_file(self, zorg_file: ZorgFile) -> None:
        if str(zorg_file.path) not in set(str(zf.path) for zf in self.seen):
            self.seen.append(zorg_file)


def _add_zorg_ids(zorg_file: ZorgFile) -> None:
    new_notes = []
    for note in zorg_file.notes:
        if note.zorg_id is None:
            logger.debug("Found new zorg note", zorg_note=note)
            zorg_id = "991231#XX"
            note.zorg_id = zorg_id
            new_notes.append(note)
    if new_notes:
        zorg_file.events.append(
            NewZorgNotesEvent(
                zorg_file_path=zorg_file.path, new_notes=new_notes
            )
        )
