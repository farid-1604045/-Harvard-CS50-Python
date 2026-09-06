from src.hello import hello

def test_default():
    assert hello("Alice") == "hello, Alice"  # This will return "hello, Alice"

def test_argument():
    for name in ["Alice", "Bob", "Charlie"]:
        assert hello(name) == f"hello, {name}"  # This will return "hello, Alice", "hello, Bob", and "hello, Charlie"