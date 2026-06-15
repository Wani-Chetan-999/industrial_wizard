#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

# --- WINDOWS GLOBAL ONNX/CHROMADB CRASH BYPASS ---
# We create a fake onnxruntime module in sys.modules before anything else imports it.
# This completely intercepts ChromaDB's internal installation checks.
class FakeORTModule:
    class InferenceSession:
        def __init__(self, *args, **kwargs): pass
    @staticmethod
    def get_device(): return "CPU"

sys.modules["onnxruntime"] = FakeORTModule

# Clean root module resolution pathing for Windows envs
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# -------------------------------------------------

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'industrial_wizard.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()