# Neurovault Downloader

This repository is an experiment on how we can improve
download time of Neurovault in Nilearn.

Running the main script, we compare several approach:

- Nilearn `nilearn.datasets.fetch_neurovault_ids` current main
- A downloader that uses the `/collections/{collection_id}/download` endpoint
  from Neurovault, and allows to download a collection as a zip file (instead 
  iterate downloading each image from the collection as Nilearn is currently
  doing)
- A parallel version of the zip downloader

Running the `main.py`, we see that:

- downloading the collection as a zip already benefits largely compared
  to Nilearn (55s vs 98s)
- adding parallelism in the download is helpful (4 jobs = 12s)
