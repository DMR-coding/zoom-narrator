# zoom-narrator [![Build Status](https://travis-ci.com/DMR-coding/zoom-narrator.svg?branch=main)](https://travis-ci.com/DMR-coding/zoom-narrator)
Play audio while streaming its closed captions to Zoom.

## Prerequisites
The user is responsible for providing a working Python environment for this application. If you need help with this step, see [the PythonWiki beginner's guide](https://wiki.python.org/moin/BeginnersGuide/Download).

Additionally, this application relies on `ffmpeg` (specifically, `ffplay`) to play audio at the command line. The user is responsible
for ensuring this utility is installed and on the `PATH`.

## Installing
At the command line, type `pip install zoom-narrator`.

## Using 
* [Enable closed captioning for your Zoom account](https://support.zoom.us/hc/en-us/articles/207279736-Managing-and-viewing-closed-captioning#h_4cb4e874-d574-4e40-ab12-7d8fae1f71cc).
* Start your zoom meeting and [share your computer audio](https://it.umn.edu/services-technologies/how-tos/zoom-share-device-sound-during-screen#sharing-music-or-computer-audio-only).
* [Start closed captioning and copy the API token](https://support.zoom.us/hc/en-us/articles/207279736-Managing-and-viewing-closed-captioning#h_45f95867-9c71-4acd-888f-5a1475b4cd8e).
* Invoke this application: `zoom-narrator path/to/audio`.
  * You can optionally specify the path to a captions file at the command line with `-c` / `--captions`. If not specified, the application will look for a file with the same name as the audio and a known captioning file extension.
  * You can optionally provide the API key at the command line with `-k` / `--key`.

## Developing
Environment and prerequisites are managed by `poetry`. See https://python-poetry.org/docs/#installation to get started with poetry.

* To create an environment and install prerequisites, run `poetry install` in the top level of the repository.
* Invoke the application with `poetry run zoom-narrator`.
* Build packages with `poetry build`.

