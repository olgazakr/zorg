"""Contains the init_zoq_file() function."""

import datetime as dt
from functools import partial
import itertools as it
from pathlib import Path


def init_zoq_file(zoq_path: Path, query_results: str) -> None:
    """Initialize the provided *.zoq file.

    Arguments:
    ----------
    zoq_path: The path of the *.zoq file we are going to initialize.
    query_string: The execution results of this SWOG query will be used to
      populate the provided *.zoq file.
    """
    date_spec = dt.datetime.now().strftime("%Y-%m-%d at %H:%M:%S")
    stats_line_start = "# Saved query generated on"
    zoq_lines = zoq_path.read_text().split("\n")
    old_header_lines = it.takewhile(
        partial(_is_zoq_header_line, stats_line_start), zoq_lines
    )
    old_header = "\n".join(old_header_lines)
    stats_line = f"{stats_line_start} {date_spec}."
    maybe_hash_line = "" if old_header.endswith("#") else "#\n"
    zoq_contents = (
        f"{old_header}\n{maybe_hash_line}{stats_line}\n\n{query_results}"
    )
    with zoq_path.open("w") as f:
        f.write(zoq_contents)


def _is_zoq_header_line(end_marker: str, line: str) -> bool:
    return line.startswith("#") and not line.startswith(end_marker)
