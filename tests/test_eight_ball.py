from oracle.eight_ball import get_eight_ball, responses
    
#test function
def test_fortune_cookie():
    result = get_eight_ball()
    assert result in responses

def test_fortune_is_string():
    result = get_eight_ball()
    assert isinstance(result, str)

def test_fortunes_not_empty():
    result = get_eight_ball()
    assert result != ""

def test_random():
    results = {get_eight_ball() for _ in range(100)}
    assert len(results) > 1