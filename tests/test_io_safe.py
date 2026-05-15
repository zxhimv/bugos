from pathlib import Path

import pytest

from bugos.io_safe import SafeIOError, read_text, resolve_safe, write_text


def test_resolve_safe_blocks_traversal(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    outside = tmp_path.parent / "outside_bugos_io.txt"
    outside.write_text("outside", encoding="utf-8")
    try:
        with pytest.raises(SafeIOError):
            resolve_safe("../outside_bugos_io.txt")
    finally:
        outside.unlink(missing_ok=True)


def test_read_write_text_stays_inside_workspace(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    write_text("nested/local.txt", "local")
    assert read_text("nested/local.txt") == "local"
    assert Path("nested/local.txt").exists()
