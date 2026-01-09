from app.entropy import calculate_entropy

def test_entropy_positive():
    assert calculate_entropy("Abc123!") > 0
