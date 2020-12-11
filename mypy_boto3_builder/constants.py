"""
Constants and paths.
"""
from pathlib import Path

# Master module name
LEGACY_MODULE_NAME = "mypy_boto3"
MODULE_NAME = "boto3_stubs"

# PyPI module name
LEGACY_PYPI_NAME = "mypy-boto3"
PYPI_NAME = "boto3-stubs"

# Random region to initialize services
DUMMY_REGION = "us-west-2"

# Jinja2 templates for boto3-stubs
TEMPLATES_PATH = Path(__file__).parent / "templates"

# Static *.pyi files for boto3-stubs
BOTO3_STUBS_STATIC_PATH = Path(__file__).parent / "boto3_stubs_static"

# Boto3 stubs module name
BOTO3_STUBS_NAME = "boto3-stubs"

# Max line length for boto3 docs
LINE_LENGTH = 100

# type defs module name
TYPE_DEFS_NAME = "type_defs"
