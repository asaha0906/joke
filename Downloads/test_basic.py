import joke_generator

def test_get_joke_returns_string():
    joke = joke_generator.get_joke()
    assert isinstance(joke, str)
    assert len(joke.strip()) > 0
