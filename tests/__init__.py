import os
import tempfile
from contextlib import contextmanager
import json


@contextmanager
def temp_files(num_files):
    temp_file_paths = []
    try:
        for _ in range(num_files):
            temp_file = tempfile.NamedTemporaryFile(delete=False)
            temp_file_paths.append(temp_file.name)
            temp_file.close()
        yield temp_file_paths
    finally:
        for path in temp_file_paths:
            os.remove(path)


def load_json(fname: str) -> dict:
    with open(fname, encoding="utf-8") as fh:
        return json.load(fh)
