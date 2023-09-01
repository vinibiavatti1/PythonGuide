from abc import ABC, abstractmethod


class IBuilding(ABC):

    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def build(self) -> None:
        pass


class GoldMine(IBuilding):

    def __init__(self) -> None:
        self.name = "Gold Mine"

    def get_name(self) -> str:
        return self.name

    def build(self) -> None:
        print(f"{self.name} is building")
