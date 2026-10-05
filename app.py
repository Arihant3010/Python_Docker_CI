def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5
    print("Test Passed: 2 + 3 = 5")

if __name__ == "__main__":
    print("Running Python Application...")
    test_add()
    print("Application executed successfully!")