#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""

import os
import sys
from flask import Flask

app = Flask(__name__)

def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gettingstarted.settings")
    try:
        from django.core.management import execute_from_command_line
        @app.route('/api', methods=['GET'])
        def hello():
            return "<h1>Hello world!</h1>"
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
