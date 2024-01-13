from domain.type import Type


class Tree:

    def __init__(self, id, year_planted, coords, type):
        if id<0:
            self.__id = -1
        else:
            self.__id = id

        if year_planted<0:
            self.__year_planted = -1
        else:
            self.__year_planted = year_planted

        self.__coords = coords

        self.__type = type  # from class Type

    def id_getter(self):
        return self.__id

    def year_planted_getter(self):
        return self.__year_planted

    def coords_getter(self):
        return self.__coords

    def type_getter(self):
        return self.__type

    def type_first_three(self):
        return str(self.__type)[7:10]

    def id_setter(self,id=-1):
        if id<0:
            print("Not an available id!")
        else:
            self.__id=id

    def year_setter(self,year=0):
        if year < 0:
            print("Not an available year!")
        else:
            self.__year_planted = year

    def coords_setter(self,coords=[]):
        self.__coords = coords

    def type_setter(self,type):
        self.__type=type

    def read_tree(self):
        id = int(input("Id: "))
        year = int(input("Year: "))
        xcoord = int(input("X Coord: "))
        ycoord = int(input("Y Coord: "))
        self.__type.read_type()

        self.id_setter(id)
        self.year_setter(year)
        self.coords_setter([xcoord,ycoord])

    def __str__(self):
        if self.type_getter().available_origin(self.type_getter().origin_getter()):
            return ("Tree with id "+str(self.__id)+", planted in "+str(self.__year_planted)
                + ", with coords:"+str(self.__coords)+", of type "+str(self.__type))
        else:
            return ""

    def __eq__(self,other):
        return (
                self.__type!=other.__type and self.__coords==other.__coords
                and self.__year_planted==other.__year_planted
        )



#tree=Tree(-1,-1,[1],type)
#tree.read_tree()
#print(str(tree))