from abc import ABC, abstractmethod

class Encryption(ABC):
    @abstractmethod
    def hash_password(self,pasword:str) -> str:
        pass
    @abstractmethod
    def verify(self,password:str,hashed:str)-> bool:
        pass

class 
class EncryptionFactory:
    @staticmethod
    def get_encryption_strategy(strategy_type:str) -> Encryption:
