from abc import ABC, abstractmethod
from typing import Dict

class ReportGenerator(ABC):
    def generate_report(self, data: Dict[str, int]) -> str:
        data_to_format = self.collect_data(data)
        formatted_data = self.format_data(data_to_format)
        return self.generate_file(formatted_data)

    @abstractmethod
    def collect_data(self, data: Dict[str, int]) -> Dict[str, str]:
        pass

    @abstractmethod
    def format_data(self, data: Dict[str, str]) -> str:
        pass

    @abstractmethod
    def generate_file(self, data: str) -> str:
        pass
