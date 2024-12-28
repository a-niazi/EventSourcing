from abc import ABC, abstractmethod


class RepositoryInterface(ABC):
    @abstractmethod
    def save(self, aggregate):
        pass

    @abstractmethod
    def get(self, aggregate_id: str):
        pass

    @abstractmethod
    def delete(self, aggregate_id: str):
        pass
