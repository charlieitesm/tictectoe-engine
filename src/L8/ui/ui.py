from abc import abstractmethod, ABC


class UI(ABC):

    def __init__(self):
        self.initialize_ui()

    @abstractmethod
    def initialize_ui(self):
        raise NotImplementedError

    @abstractmethod
    def input(self, message: str) -> str:
        raise NotImplementedError

    @abstractmethod
    def output(self, message: str):
        raise NotImplementedError


class ConsoleUI(UI):

    def __init__(self):
        super().__init__()

    def initialize_ui(self):
        print("Initializing console UI")

    def input(self, message: str) -> str:
        return input(f"{message}: ")

    def output(self, message: str):
        print(message)

