import io
from pathlib import Path

import aiohttp
import asyncio
import zipfile

SEMAPHORE_LIMIT = 2

async def _download_collection(collection_id, target_dir, semaphore):
    url = format_neurovault_download_url(collection_id)

    async with semaphore:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                assert resp.status == 200
                data = await resp.read()

        zipfile.ZipFile(io.BytesIO(data)).extractall(target_dir)


async def _download_collections(collection_ids, target_dir, semaphore_limit):
    semaphore = asyncio.Semaphore(semaphore_limit)

    download_tasks = [_download_collection(collection_id, target_dir, semaphore) for collection_id in collection_ids]

    await asyncio.gather(*download_tasks)


def format_neurovault_download_url(collection_id):
    return f"https://neurovault.org/collections/{collection_id}/download"


def asyncio_download_neurovault(collection_ids, semaphore_limit=SEMAPHORE_LIMIT):
    target_dir = Path(__file__).parent / "asyncio_dl"
    target_dir.mkdir(exist_ok=True)

    asyncio.run(_download_collections(collection_ids=collection_ids, target_dir=target_dir, semaphore_limit=semaphore_limit))

