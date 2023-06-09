import pytest
from helpers.gpt_helper import generate_explanation

@pytest.fixture
def sample_prompt():
    return "This is a sample prompt."

def test_generate_explanation(sample_prompt):
    explanation = generate_explanation(sample_prompt)
    # Perform assertions to check the correctness of the generated explanation
