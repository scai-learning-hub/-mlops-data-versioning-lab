import hashlib
from pathlib import Path

from dagster import (
    Definitions,
    AssetSelection,
    define_asset_job,
    sensor,
    RunRequest,
    SkipReason,
    ScheduleDefinition,
)

from .assets import data_pipeline

REPO_ROOT = Path(__file__).resolve().parents[2]
PARAMS_PATH = REPO_ROOT / "params.yaml"


def file_hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


dvc_job = define_asset_job(
    name="dvc_repro_job",
    selection=AssetSelection.assets(data_pipeline),
)


@sensor(job=dvc_job, minimum_interval_seconds=10)
def params_change_sensor(context):
    if not PARAMS_PATH.exists():
        return SkipReason("params.yaml not found")

    h = file_hash(PARAMS_PATH)

    if context.cursor == h:
        return SkipReason("params.yaml unchanged")

    context.update_cursor(h)
    return RunRequest(
        run_key=h,
        tags={"trigger": "params.yaml_changed"},
    )




repro_every_2_min_schedule = ScheduleDefinition(
    name="repro_every_2_min_schedule",
    job=dvc_job,
    cron_schedule="*/2 * * * *",
    execution_timezone="Asia/Kolkata",
)


defs = Definitions(
    assets=[data_pipeline],
    jobs=[dvc_job],
    sensors=[params_change_sensor],
    schedules=[repro_every_2_min_schedule],
)
