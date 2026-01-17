from dagster import Definitions
from .assets import data_pipeline

defs = Definitions(assets=[data_pipeline])
