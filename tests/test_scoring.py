from app.scoring import rating_from_score

def test_rating():
    assert rating_from_score(90) == "VERY STRONG"
