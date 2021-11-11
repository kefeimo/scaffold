import hello

def test_hello_add():
    assert 3 == hello.add(1, 2)
# print("test")

def test_hello_add_fail():
    assert 6 == hello.add(1, 2)