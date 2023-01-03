
class TestTool():
    def __init__(self) -> None:
        pass

    def assertEqual(self, value1, value2):
        if value1 == value2:
            print("PASS")
            return True
        else:
            print("FAIL")
            return False
