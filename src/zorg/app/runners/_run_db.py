"""Contains runners for the 'zorg db' command."""

from pathlib import Path
import sys

from logrus import Logger
from tqdm import tqdm

from ...service.compiler import walk_zorg_file
from ...storage.sql.session import ZorgSQLSession
from ..config import DbCreateConfig
from ._runners import runner


logger = Logger(__name__)


@runner
def run_db_create(cfg: DbCreateConfig) -> int:
    """Runner for the 'db create' command."""
    zorg_files = []
    total_num_notes = 0
    total_num_todos = 0
    _prep_sqlite_db_for_create(cfg.database_url)
    with ZorgSQLSession(cfg.database_url) as session:
        for zo_path in tqdm(
            sorted(cfg.zettel_dir.rglob("*.zo"), key=lambda p: p.name),
            desc="Reading notes from zorg files",
            file=sys.stdout,
        ):
            logger.info("Starting to walk zorg file", zorg_file=zo_path.name)
            zorg_file = walk_zorg_file(zo_path)
            num_notes = len(zorg_file.notes)
            num_todos = len(
                [note for note in zorg_file.notes if note.todo_payload]
            )
            total_num_notes += num_notes
            total_num_todos += num_todos
            logger.info(
                "Finished walking zorg file",
                zorg_file=zo_path.name,
                num_notes=num_notes,
                num_todos=num_todos,
            )
            session.repo.add(zorg_file)
            zorg_files.append(zorg_file)
        logger.info(
            "Finished reading zettel org directory",
            num_files=len(zorg_files),
            num_notes=total_num_notes,
            num_todos=total_num_todos,
        )
        session.commit()
    return 0


def _prep_sqlite_db_for_create(database_url: str) -> None:
    sqlite_prefix = "sqlite:///"
    if database_url.startswith(sqlite_prefix):
        db_path = Path(database_url[len(sqlite_prefix) :])
        db_path.parent.mkdir(exist_ok=True, parents=True)
        if db_path.exists():
            logger.info("Deleting existing zorg database.", db_path=db_path)
            db_path.unlink()
