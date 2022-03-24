import io
import requests
from pathlib import Path

import joblib
import numpy as np
import zipfile


def _download_collection(collection_id, target_dir):
    url = format_neurovault_download_url(collection_id)

    response = requests.get(url)
    assert response.status_code == 200
    data = response.content

    zipfile.ZipFile(io.BytesIO(data)).extractall(target_dir)


def _download_collections(collection_ids, target_dir):
    [_download_collection(collection_id, target_dir) for collection_id in collection_ids]


def format_neurovault_download_url(collection_id):
    return f"https://neurovault.org/collections/{collection_id}/download"


def collection_page_download(collection_ids):
    target_dir = Path(__file__).parent / "collection_page_dl"
    target_dir.mkdir(exist_ok=True)

    _download_collections(collection_ids=collection_ids, target_dir=target_dir)


def parallel_collection_page_download_neurovault(collection_ids, n_jobs=1):
    target_dir = Path(__file__).parent / "collection_page_dl"
    target_dir.mkdir(exist_ok=True)

    splits = np.array_split(collection_ids, n_jobs)

    joblib.Parallel(n_jobs=n_jobs)(
        joblib.delayed(_download_collections)(
            urls,
            target_dir=target_dir,
        ) for urls in splits
    )
