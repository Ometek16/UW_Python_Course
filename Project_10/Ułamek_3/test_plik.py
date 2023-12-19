import pytest
from unittest.mock import patch
from Ułamek import Ułamek

@pytest.fixture
def sample_fraction():
    return Ułamek(3, 4)  

@patch('builtins.open', create=True)
def test_save_and_read_from_file(mock_open, sample_fraction):
    mock_file = mock_open.return_value.__enter__.return_value

    content = []
    mock_file.write.side_effect = lambda s: content.append(s)

    sample_fraction.save_to_file('test_path')

    expected_content = '3/4'  
    assert content == [expected_content]

    mock_file.read.side_effect = lambda: expected_content

    loaded_fraction = Ułamek.read_from_file('test_path')

    assert loaded_fraction == sample_fraction
