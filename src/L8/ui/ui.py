from abc import abstractmethod, ABC


class UI(ABC):

    @abstractmethod
    def initialize_ui(self):
        raise NotImplementedError

    @abstractmethod
    def input(self):
        raise NotImplementedError

    @abstractmethod
    def output(self):
        raise NotImplementedError
