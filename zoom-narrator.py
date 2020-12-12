from zoom_narrator import audio, captions, zoom
import asyncclick as click


@click.command()
@click.option(
    "-f",
    "--file",
    "file_path",
    help="Audio file to play.",
    required=True,
    type=click.Path(exists=True),
)
@click.option(
    "-k",
    "--key",
    required=True,
    prompt=True,
    help="Zoom captioning API key (URL)",
)
async def main(file_path: str, key: str):
    captionpath = captions.probe(file_path)
    if not captionpath:
        raise ValueError("Couldn't find caption file, please specify manually.")

    caption_file = captions.load(captionpath)

    with audio.play(file_path):
        async with zoom.open_zoom_session(key) as session:
            async for event in captions.timed_captions(caption_file):
                session.send_caption(event.plaintext)


if __name__ == "__main__":
    # execute only if run as a script
    main()
