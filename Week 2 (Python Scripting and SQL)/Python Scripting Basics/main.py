print(f"Name of this file (main.py) is {__name__}")

def test_func_success():
    print("hi test success\n")

def test_func_fail():
    print("hi test fail\n")

if __name__ == '__main__':
    print("\nSince '__name__' == '__main__' ")
    test_func_success()


if __name__ != '__main__':
    print("\nSince '__name__' != '__main__' ")
    test_func_fail()