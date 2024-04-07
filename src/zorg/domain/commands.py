"""Zorg commands."""

from dataclasses import dataclass
from pathlib import Path

from .types import Message


@dataclass(frozen=True)
class Command(Message):
    """A zorg command."""


@dataclass(frozen=True)
class EditCommand(Command):
    """Command to open one or more zorg files using an editor."""

    zettel_dir: Path
    paths: list[Path]
    keep_alive_file: Path
    vim_commands: list[str]
