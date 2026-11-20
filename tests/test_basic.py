"""Basic project smoke tests."""
from src import config

def test_directories():
    assert config.DATA_DIR.exists()
    assert config.RAW_DATA_DIR.exists()
    assert config.PROCESSED_DATA_DIR.exists()
