from typing import Optional

import asyncclick as click

from . import audio, captions, zoom


@click.command()
@click.argument(
    "audio_path",
    required=True,
    type=click.Path(exists=True),
)
@click.option(
    "-c",
    "--captions",
    "caption_path",
    required=False,
    default=None,
    help="Manually specify captions file.",
    type=click.Path(exists=True),
)
@click.option(
    "-k",
    "--key",
    required=True,
    prompt=True,
    help="Zoom captioning API key (URL). Will prompt if not specified.",
)
async def main(audio_path: str, key: str, caption_path: Optional[str]):
    if not caption_path:
        caption_path = captions.probe(audio_path)
    if not caption_path:
        raise click.ClickException(
            "Couldn't find caption file, please specify manually."
        )

    caption_file = captions.load(caption_path)

    with audio.play(audio_path):
        async with zoom.open_zoom_session(key) as session:
            async for event in captions.timed_captions(caption_file):
                session.send_caption(event.plaintext)


if __name__ == "__main__":
    # execute only if run as a script
    main()
