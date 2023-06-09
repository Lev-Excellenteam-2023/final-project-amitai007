import pytest
from helpers.pptx_helper import parse_presentation, extract_text

import unittest

@pytest.fixture
def sample_presentation_path():
    return "path/to/sample.pptx"

def test_parse_presentation(sample_presentation_path):
    slides = parse_presentation(sample_presentation_path)
    # Perform assertions to check the correctness of the parsed slides

def test_extract_text():
    # Create a sample slide with text boxes
    # Call the extract_text function on the sample slide
    # Perform assertions to check the correctness of the extracted text

