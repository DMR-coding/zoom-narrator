#!/usr/bin/env bash

set -euxo pipefail

poetry run flake8 .
poetry run black --check .
poetry run mypy .