import pytest
from utils import save_json, remove_whitespace, clean_text


@pytest.fixture
def sample_data():
    return {"key": "value"}


def test_save_json(tmpdir, sample_data):
    file_path = tmpdir.join("output.json")
    save_json(str(file_path), sample_data)
    # Perform assertions to check if the JSON file was saved correctly


def test_remove_whitespace():
    text = "  This is  a   test  text.  "
    cleaned_text = remove_whitespace(text)
    # Perform assertions to check if the whitespace was removed correctly


def test_clean_text():
    text = "   This \n   is \n\na \n test  \n text.   \n"
    cleaned_text = clean_text(text)
    # Perform assertions to check if the text was cleaned correctly
