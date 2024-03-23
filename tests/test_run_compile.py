"""Tests for the zorg project's 'compile' CLI command."""

from __future__ import annotations

import itertools as it
from pathlib import Path
from typing import Iterator

from _pytest.capture import CaptureFixture
from pytest import mark, param
from syrupy.assertion import SnapshotAssertion as Snapshot

from . import common as c


params = mark.parametrize


def _get_all_zo_paths() -> list[Path]:
    tests_dir = Path(__file__).parent
    data_dir = tests_dir / "data"
    examples_dir = tests_dir.parent / "examples"
    return sorted(
        path
        for path in it.chain(
            _get_zo_path_iter(data_dir), _get_zo_path_iter(examples_dir)
        )
        if not path.stem.endswith("_tmpl")
    )


def _get_zo_path_iter(src_dir: Path) -> Iterator[Path]:
    for zo_path in src_dir.rglob("*.zo"):
        yield zo_path


@params(
    "zo_path",
    [param(zo_path, id=zo_path.stem) for zo_path in _get_all_zo_paths()],
)
def test_compile(
    main: c.MainType,
    capsys: CaptureFixture,
    tmp_path: Path,
    snapshot: Snapshot,
    zo_path: Path,
) -> None:
    """Test that the all *.zo test data files compile as expected."""
    zettel_dir = tmp_path / "org"
    argv = [
        "--dir",
        str(zettel_dir),
        "compile",
        str(zo_path),
    ]
    exit_code = main(*argv)

    assert exit_code == 0
    capture = capsys.readouterr()
    assert capture.out == snapshot