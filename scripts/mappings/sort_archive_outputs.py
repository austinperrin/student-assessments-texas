from __future__ import annotations

import sys

from lib.tea_assessment_sorter import OUTPUT_MODE_ARCHIVE, main


if __name__ == "__main__":
    raise SystemExit(main([*sys.argv[1:], "--output-mode", OUTPUT_MODE_ARCHIVE]))
