from enum import Enum


class GameMode(Enum):
    LOCAL = "local"
    CLIENT = "client"
    SERVER = "server"


class TypeOfUI(Enum):
    CONSOLE = "console"
