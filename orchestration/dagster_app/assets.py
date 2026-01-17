import subprocess
from dagster import asset

@asset
def data_pipeline():
    subprocess.check_call(["dvc", "repro"])
