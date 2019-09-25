"""Python utils."""

import code  # code.interact(local=dict(globals(), **locals()))
import os
from typing import List, Tuple, Dict, Set, Any, Optional, Callable


def read(path: str) -> str:
    """Returns contents of file at `path`, leading/trailing whitespace stripped."""
    with open(path, 'r') as f:
        return f.read().strip()


def write(path: str, contents: str, info_print: bool = True) -> None:
    """Writes contents to path, makes dirs if needed, prints info msg w/ path."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        f.write(contents)
    if info_print:
        print('Wrote {} chars to "{}"'.format(len(contents), path))


def main() -> None:
    # This would be for testing out code only.
    pass


if __name__ == "__main__":
    main()
