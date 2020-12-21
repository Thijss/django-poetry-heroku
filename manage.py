"""Django's command-line utility for administrative tasks."""
import sys
from pathlib import Path

import environ
from django.core.management import execute_from_command_line

BASE_DIR = Path(__file__).resolve().parent


def main():
    """Run administrative tasks."""
    env = environ.Env()
    env.read_env(str(BASE_DIR / ".env"))

    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
