from abc import abstractmethod, ABC


class Board(ABC):

    def __init__(self):
        self.current_state = []

    @abstractmethod
    def init_board(self):
        raise NotImplementedError

    @abstractmethod
    def to_string(self):
        raise NotImplementedError
