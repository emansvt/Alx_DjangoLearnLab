<<<<<<< HEAD
#!/usr/bin/env python
=======
#!/usr/bin/env python3
>>>>>>> 8bb8dda1a481287b184dd5feb1ec3e7f69e36ec3
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
<<<<<<< HEAD
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "social_media_api.settings")
=======
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'social_media_api.settings')
>>>>>>> 8bb8dda1a481287b184dd5feb1ec3e7f69e36ec3
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


<<<<<<< HEAD
if __name__ == "__main__":
=======
if __name__ == '__main__':
>>>>>>> 8bb8dda1a481287b184dd5feb1ec3e7f69e36ec3
    main()
