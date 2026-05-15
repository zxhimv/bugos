"""Source-tree import shim for ``python -m bugos.cli``.

The packaged project uses a ``src/`` layout. This small local shim lets the
module command run from a checkout without installing anything or contacting a
package index.
"""

from __future__ import annotations

from pathlib import Path

_SRC_PACKAGE = Path(__file__).resolve().parents[1] / "src" / "bugos"
if _SRC_PACKAGE.is_dir():
    __path__.append(str(_SRC_PACKAGE))

__version__ = "0.1.0"
