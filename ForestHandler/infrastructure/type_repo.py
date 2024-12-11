from ForestHandler.domain.type import Type
from ForestHandler.infrastructure.tree_repo import TreeRepo
import matplotlib.pyplot as plt


class TypeRepo:
    def __init__(self):
        self.__types=[]

    def get_types(self):
        return self.__types

    def get_types_special(self):
        lst=[]
        for type in self.__types:
            lst.append(str(type)[6:])
        return lst



    def set_types(self,vl):
        self.__types=vl

    def __str__(self):
        s = ""
        for i in range(0,len(self.__types)):
            if str(self.__types[i])!="":
                s += str(self.__types[i]) + "\n"
        return s

    def read_type_repo(self):
        try:
            type=Type(("Baobab", "Madagascar"))
            type.read_type()
        except ValueError as valueError:
            raise ValueError(valueError)

        return type

    def contains(self,type):
        for elem in self.__types:
            if elem==type:   # WHAT DOES IT MEAN TO COMPARE TWO TYPES? => type module, __eq__ method
                return True
        return False

    # 1
    def add_type(self,type):
        self.__types.append(type)

    # 4
    def delete_types(self,type):
        for i in range(len(self.__types)-1,-1,-1):
            if self.__types[i]==type:
                del self.__types[i]










'''
typesInitial=TypeRepo()
type1 = typesInitial.read_type_repo()
typesInitial.add_type(type1)
type1 = typesInitial.read_type_repo()
typesInitial.add_type(type1)
print(str(typesInitial))
'''


