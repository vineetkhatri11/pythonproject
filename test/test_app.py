from app import index

def test_index():
    print(index())
    assert index() == "Hello, World!"

test_index()
