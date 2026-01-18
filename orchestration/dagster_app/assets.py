import subprocess
from pathlib import Path

from dagster import asset, AssetExecutionContext

REPO_ROOT = Path(__file__).resolve().parents[2]

@asset
def data_pipeline(context: AssetExecutionContext):
    # Run DVC pipeline from repo root
    proc = subprocess.run(
        ["dvc", "repro"],
        cwd=str(REPO_ROOT),
        text=True,
        capture_output=True,
    )

    # Show DVC + script prints in Dagster logs
    if proc.stdout:
        context.log.info(proc.stdout)

    if proc.returncode != 0:
        if proc.stderr:
            context.log.error(proc.stderr)
        raise RuntimeError(f"dvc repro failed with code {proc.returncode}")

    return "dvc repro completed"
