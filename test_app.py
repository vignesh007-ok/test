import pytest
from app import calculate_bill

def test_standard_calculation():
    assert calculate_bill(10.0, 5) == 50.0
    assert calculate_bill(0.0, 5) == 0.0

def test_invalid_inputs():
    with pytest.raises(ValueError):
        calculate_bill(-5.0, 2)
    with pytest.raises(ValueError):
        calculate_bill(10.0, 0)
