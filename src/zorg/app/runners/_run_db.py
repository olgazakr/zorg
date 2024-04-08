"""Contains runners for the 'zorg db' command."""

from logrus import Logger

from ...domain import commands
from ...service import messagebus
from ...storage.sql.session import SQLSession
from ..config import DbCreateConfig
from ._runners import runner


logger = Logger(__name__)


@runner
def run_db_create(cfg: DbCreateConfig) -> int:
    """Runner for the 'db create' command."""
    session = SQLSession(cfg.database_url, should_delete_existing_db=True)
    messagebus.handle([commands.CreateDBCommand(cfg.zettel_dir)], session)
    return 0
