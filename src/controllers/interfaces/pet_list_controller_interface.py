from abc import ABC, abstractmethod

from typing import Dict

class PetsListControllerInterface(ABC):
    
    @abstractmethod
    def list(self) -> Dict:
        pass