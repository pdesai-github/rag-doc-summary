from abc import abstractmethod, ABC
from langchain_core.documents import Document

class DocumentReader(ABC):

    @abstractmethod
    def read(self, file_path: str) -> list[Document]:
        pass