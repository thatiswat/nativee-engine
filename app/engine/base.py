from abc import ABC
from abc import abstractmethod


class Pipeline(ABC):

    @abstractmethod
    async def run(
        self,
        context,
    ):
        ...