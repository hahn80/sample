#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import annotations
from pyarrow.feather import read_feather, write_feather
import pandas as pd


def read_arrow(file_path: str, columns=list[str]) -> pd.DataFrame:
    return read_feather(file_path, columns=columns)


def write_arrow(df: pd.DataFrame, file_path: str, batch_size: int = 1000):
    write_feather(df, file_path, chunksize=batch_size)
