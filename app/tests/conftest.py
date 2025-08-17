# app/tests/conftest.py
import sys
import os

# add project root to sys.path so "import app" works
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
