import time
from pathlib import Path
from typing import Iterable, Optional, Union

import asyncio
import click
from tqdm.auto import tqdm


async def _download_file(url, target_dir, semaphore):
    async with semaphore:
        print(url)
        await asyncio.sleep(3)

async def _download_files(urls, target_dir):
    semaphore = asyncio.Semaphore(5)

    download_tasks = [_download_file(url, target_dir, semaphore) for url in urls]

    await asyncio.gather(*download_tasks)


def download() -> None:
    target_dir = Path(__file__).parent

    kwargs = {
        "urls": [f"Hello {index}" for index in range(10)],
        "target_dir": ".",
    }
    asyncio.run(_download_files(**kwargs))


@click.command()
def download_cli():
    """Download datasets from OpenNeuro."""
    download()


if __name__ == "__main__":
    download_cli()
