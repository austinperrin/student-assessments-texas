from __future__ import annotations

import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


def run(script_name: str) -> int:
    script_path = REPO_ROOT / "scripts" / script_name
    result = subprocess.run([sys.executable, str(script_path)], cwd=REPO_ROOT)
    return result.returncode


def main() -> int:
    checks = [
        "validate_mappings.py",
        "validate_docs.py",
    ]

    for check in checks:
        exit_code = run(check)
        if exit_code != 0:
            return exit_code

    print("All repository validation checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

