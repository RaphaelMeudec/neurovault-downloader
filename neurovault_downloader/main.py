import time
from nilearn.datasets import fetch_neurovault_ids

from neurovault_downloader.asyncio_downloader import asyncio_download_neurovault
from neurovault_downloader.collection_url_downloader import (
    collection_page_download,
    parallel_collection_page_download_neurovault,
)

collection_ids = [5412, 5317, 5472, 5299]

start_time = time.time()
fetch_neurovault_ids(collection_ids=collection_ids, data_dir="nilearn_dl")
end_time = time.time()
print(f"Nilearn {end_time - start_time}")

start_time = time.time()
collection_page_download(collection_ids=collection_ids)
end_time = time.time()
print(f"Collection page {end_time - start_time}")

start_time = time.time()
parallel_collection_page_download_neurovault(collection_ids=collection_ids, n_jobs=4)
end_time = time.time()
print(f"Parallel collection page {end_time - start_time}")

# start_time = time.time()
# asyncio_download_neurovault(collection_ids=collection_ids, semaphore_limit=4)
# end_time = time.time()
# print(f"Asyncio {end_time - start_time}")
