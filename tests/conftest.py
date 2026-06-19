import pytest
from tempfile import TemporaryDirectory
from pathlib import Path


@pytest.fixture(scope="module")
def tmp_path():
    """Create a temporary directory that auto-cleans up."""
    with TemporaryDirectory() as tmpdir:
        yield Path(tmpdir)
