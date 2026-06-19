#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import annotations
import pytest
import pandas as pd
from faker import Faker
from pathlib import Path

from titan.sample import read_arrow, write_arrow


@pytest.mark.skip(reason="Generate data for testing")
def fake_data(num_records: int = 10):
    fake = Faker()

    data = {
        "name": [fake.name() for _ in range(num_records)],
        "age": [fake.random_int(min=18, max=80) for _ in range(num_records)],
        "location": [fake.city() for _ in range(num_records)],
        "salary": [
            round(fake.random_number(digits=5, fix_len=True), 2)
            for _ in range(num_records)
        ],
        "education": [
            fake.random_element(
                elements=["High School", "Bachelor's", "Master's", "PhD"]
            )
            for _ in range(num_records)
        ],
    }

    df = pd.DataFrame(data)
    return df


def test_arrow_io(tmp_path: Path):
    df = fake_data(num_records=10)
    arrow_file = str(tmp_path / "fake.arrow")
    write_arrow(df, arrow_file)
    new_df = read_arrow(arrow_file, columns=["name", "age", "salary"])
    assert isinstance(new_df, pd.DataFrame)
    assert len(new_df) == 10
    print(new_df)
