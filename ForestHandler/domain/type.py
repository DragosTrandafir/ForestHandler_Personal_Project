
class Type:

    origins = [
        ("Baobab", "Madagascar"),
        ("Maple", "Canada"),
        ("Sakura", "Japan"),
        ("Eucalyptus", "Australia"),
        ("Olive", "Mediterranean"),
        ("Pine", "United States"),
        ("European beech " ,"Romania"),
        ("Norway spruce" ,"Romania"),
        ("Silver fir" ,"Romania"),
        ("Quercus" ,"Romania")
    ]

    def __init__(self ,origin):
        if self.available_origin(origin):
            self.__origin = origin
        else:
            raise ValueError("Not an available origin for type!")

    def available_origin(self ,origin):
        for origin1 in self.origins:
            if origin1==origin:
                return True
        return False

    def origin_getter(self):
        return self.__origin

    def origin_setter(self ,origin):
        if self.available_origin(origin):
            self.__origin = origin
        else:
            raise ValueError("Not an available origin for type!")

    def read_type(self):
        name =input("Name: ")
        country =input("Country: ")
        try:
            self.origin_setter((name ,country))
        except ValueError as valueError:
            raise ValueError(valueError)

    def __str__(self):
        if self.available_origin(self.origin_getter()):
            return "Type:  " +self.__origin[0] +" from  " +self.__origin[1]

    def __eq__(self, other):
        return(
            self.__origin == other.__origin
        )

# type=Type(("Eucalyptus", "Australia"))
# print(str(type))
