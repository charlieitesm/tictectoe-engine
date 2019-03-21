from abc import abstractmethod, ABC


class Board(ABC):

    def __init__(self):
        self.current_state = []

    @abstractmethod
    def init_board(self): # pragma: no cover
        raise NotImplementedError

    @abstractmethod
    def __str__(self) -> str: # pragma: no cover
        raise NotImplementedError
