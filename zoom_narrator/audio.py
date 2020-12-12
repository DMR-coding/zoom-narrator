from contextlib import AbstractContextManager
import subprocess


def play(path) -> AbstractContextManager:
    return subprocess.Popen(f"ffplay -nodisp -autoexit '{path}'", shell=True)
