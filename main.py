import os
import runpy
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent
SCRIPT = PROJECT_DIR / "evacodev2.py"


def main():
    # evacodev2.py uses relative paths for eva-data.json and the output PNG,
    # so run it from the project directory regardless of where main is launched.
    os.chdir(PROJECT_DIR)
    runpy.run_path(str(SCRIPT), run_name="__main__")


if __name__ == "__main__":
    main()
