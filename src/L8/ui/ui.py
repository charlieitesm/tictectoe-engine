from abc import abstractmethod, ABC


class UI(ABC):

    @abstractmethod
    def initialize_ui(self):
        raise NotImplementedError

    @abstractmethod
    def input(self, message: str):
        raise NotImplementedError

    @abstractmethod
    def output(self, message: str):
        raise NotImplementedError


class ConsoleUI(UI):

    def initialize_ui(self):
        print("Initializing console UI")

    def input(self, message: str):
        input(f"{message}: ")

    def output(self, message: str):
        print(message)

