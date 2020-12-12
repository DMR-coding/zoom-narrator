import asyncio
import os
from typing import Optional, AsyncGenerator

import pysubs2

CAPTIONS_EXTENSION = ".ass"


def probe(audio_path: str) -> Optional[str]:
    audio_name = _root_name(audio_path)
    audio_dir = os.path.dirname(audio_path)

    for file in os.listdir(audio_dir):
        if _root_name(file) == audio_name and file.endswith(CAPTIONS_EXTENSION):
            return os.path.join(audio_dir, file)

    return None


def load(path: str) -> pysubs2.SSAFile:
    return pysubs2.load(path)


def dump(captions: pysubs2.SSAFile) -> None:
    for event in captions.events:
        print(f"{event.start/1000:05}: {event.text}")


async def timed_captions(captions: pysubs2.SSAFile) -> AsyncGenerator[(int, str)]:
    for index, event in enumerate(captions):
        prev_start = captions[index - 1].start if index > 0 else 0
        event_delta = event.start - prev_start
        await asyncio.sleep(event_delta / 1000)
        yield event


def _root_name(path):
    return os.path.basename(path).split(".", 1)[0]
