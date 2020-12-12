# zoom-narrator
Play audio while streaming its closed captions to Zoom

## Prerequisites
This application relies on `ffmpeg` (specifically, `ffplay`) to play audio at the command line. The user is responsible
for ensuring this utility is installed and on the `PATH`.

## Developing
Environment and prerequisites are managed by `poetry`. See https://python-poetry.org/docs/#installation to get started with poetry.

To run the application:
* In the top level of the repository, run `poetry install`.
* Invoke the application with `poetry run python zoom-narrator.py`

## Installing
There is not currently a production installation procedure; please use the instructions under 'Developing' above.