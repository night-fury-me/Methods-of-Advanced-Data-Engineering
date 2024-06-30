from logger import BaseLogger

class MockLogger(BaseLogger):
    def __init__(self) -> None:
        super().__init__()
