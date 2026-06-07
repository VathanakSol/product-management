from abc import ABC, abstractmethod

class Base(ABC):

    def __init__(self, id, name):
        self.__id = id
        self.__name = name

    @property
    def get_id(self):
        return self.__id
    
    @property
    def get_name(self):
        return self.__name
    
    @get_name.setter
    def set_name(self, value):
        self.__name = value

    @abstractmethod
    def display(self):
        pass

    