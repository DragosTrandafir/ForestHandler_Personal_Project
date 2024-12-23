from ForestHandler.app.tree_controller import TreeCtrl

add_tree_option=1
get_all_trees_and_types_console_option=2
insert_tree_option=3
delete_tree_option=4
delete_all_trees_of_type_option=5
delete_all_trees_between_2_years_option=6
get_all_trees_with_coordinates_range_option=7
get_all_trees_between_2_years_option=8
sort_all_trees_by_year_option=9
filter_trees_by_id_option=10
oldest_tree_option=11
similar_trees_excepting_type_option=12
delete_overlapping_trees_option=13
update_tree_by_index_option=14
update_tree_by_id_option=15
visual_representation_option=16
get_all_trees_with_coordinates_range_graphic_option=17
get_all_trees_between_2_years_graphic_option=18
get_bar_char_with_all_types_option=19
get_bar_chart_number_trees_planted_in_intervals_of_20_years_option=20
stop_option=0

class UI:
    def __init__(self, data):
        self.__data = data

    def printMenu(self):
        menu_string = ""
        menu_string += (f"MENU:\n\t{add_tree_option}. Add a tree to the forest\n"+
                        f"\t{get_all_trees_and_types_console_option}. Get all trees and types (console)\n"
                        +f"\t{insert_tree_option}. Insert a tree to the forest\n"
              + f"\t{delete_tree_option}. Delete a tree from the forest\n"
                        + f"\t{delete_all_trees_of_type_option}. Delete all trees of a given type\n"
              + f"\t{delete_all_trees_between_2_years_option}. Delete all trees planted between 2 given years\n"
              + f"\t{get_all_trees_with_coordinates_range_option}. Get all trees having the coordinates in a certain "
                f"range (console)\n"
              + f"\t{get_all_trees_between_2_years_option}. Get all trees planted between 2 given years (console)\n"
              + f"\t{sort_all_trees_by_year_option}. Sort the trees by year (ascending) \n"
              + f"\t{filter_trees_by_id_option}. Filter the tree repository so as to get only trees with even or odd "
                f"id\n"
              + f"\t{oldest_tree_option}. Determine the oldest tree \n"
              + f"\t{similar_trees_excepting_type_option}. Determine trees which are the same, excepting their type\n"
              + f"\t{delete_overlapping_trees_option}. Delete all trees that overlap (only the first of each is kept)\n"
              + f"\t{update_tree_by_index_option}. Update tree by index\n"
              + f"\t{update_tree_by_id_option}. Update tree by id\n"
              + f"\t{visual_representation_option}. Get a visual representation of the repository \n"
              + f"\t{get_all_trees_with_coordinates_range_graphic_option}. Get all trees having the coordinates in a "
                f"certain range (graphic)\n"
              + f"\t{get_all_trees_between_2_years_graphic_option}. Get all trees planted between 2 given years ("
                f"graphic)\n"
              + f"\t{get_bar_char_with_all_types_option}. Get a pie chart with all the types\n"
              + f"\t{get_bar_chart_number_trees_planted_in_intervals_of_20_years_option}. Get a bar chart with number of "
                f"trees planted in intervals of 20 years\n"
              + f"\t{stop_option}. STOP\n")
        return menu_string

    def readOption(self):
        option = int(input("Read an option: "))
        return option

    def readId(self):
        id = int(input("Read an id: "))
        return id

    def readIndex(self):
        index = int(input("Read an index: "))
        return index

    def readYear(self):
        year = int(input("Read a year: "))
        return year

    def readCoordX(self):
        coord = int(input("Read coordinate x: "))
        return coord

    def readCoordY(self):
        coord = int(input("Read coordinate y: "))
        return coord

    def read_tree_ui(self):
        tree = self.__data.read_tree()
        return tree

    def read_type_ui(self):
        type = self.__data.read_type()
        return type

    def start(self):
        stop = False
        while not stop:
            print(self.printMenu())
            option = self.readOption()
            if option == add_tree_option:
                try:
                    tree = self.read_tree_ui()
                    self.__data.add_tree_type(tree)
                except ValueError as value_error:
                    print(value_error)
            elif option == get_all_trees_and_types_console_option:
                print(str(self.__data))
            elif option == insert_tree_option:
                try:
                    tree = self.read_tree_ui()
                    index = self.readIndex()
                    self.__data.insert_tree_type(tree,index)
                except ValueError as value_error:
                    print(value_error)
            elif option == delete_tree_option:
                try:
                    index = self.readIndex()
                    self.__data.delete_tree_type(index)
                except ValueError as value_error:
                    print(value_error)
            elif option == delete_all_trees_of_type_option:
                try:
                    type_delete_all_trees_of_type = self.read_type_ui()
                    self.__data.delete_treeByType(type_delete_all_trees_of_type)
                except ValueError as value_error:
                    print(value_error)
            elif option == delete_all_trees_between_2_years_option:
                try:
                    year1 = self.readYear()
                    year2 = self.readYear()
                    self.__data.delete_tree_type_between_years(year1,year2)
                except ValueError as value_error:
                    print(value_error)
            elif option == get_all_trees_with_coordinates_range_option:
                try:
                    xcoord1= self.readCoordX()
                    xcoord2 = self.readCoordX()
                    ycoord1 = self.readCoordY()
                    ycoord2 = self.readCoordY()
                    print(self.__data.coords_range(xcoord1, xcoord2, ycoord1, ycoord2))
                except ValueError as value_error:
                    print(value_error)
            elif option == get_all_trees_between_2_years_option:
                try:
                    year1 = self.readYear()
                    year2 = self.readYear()
                    print(self.__data.years_range(year1, year2))
                except ValueError as value_error:
                    print(value_error)
            elif option == sort_all_trees_by_year_option:
                print(self.__data.sort_by_year())
            elif option == filter_trees_by_id_option:
                try:
                    parity=input("Choose between odd or even: ")
                    print(self.__data.filter_id(parity))
                except ValueError as value_error:
                    print(value_error)
            elif option == oldest_tree_option:
                try:
                    print(self.__data.oldest_tree())
                except ValueError as value_error:
                    print(value_error)
            elif option == similar_trees_excepting_type_option:
                print(self.__data.trees_at_least_2_types())
            elif option == delete_overlapping_trees_option:
                self.__data.delete_overlapping()
            elif option == update_tree_by_index_option:
                try:
                    index = self.readIndex()
                    self.__data.update_tree_by_index(index)
                except ValueError as value_error:
                    print(value_error)
            elif option == update_tree_by_id_option:
                try:
                    id_update_by_id = self.readId()
                    self.__data.update_tree_by_id(id_update_by_id)
                except ValueError as value_error:
                    print(value_error)
            elif option == visual_representation_option:
                self.__data.repository_representation_general()
            elif option == get_all_trees_with_coordinates_range_graphic_option:
                xcoord1 = self.readCoordX()
                xcoord2 = self.readCoordX()
                ycoord1 = self.readCoordY()
                ycoord2 = self.readCoordY()
                self.__data.coords_range_representation(xcoord1, xcoord2, ycoord1, ycoord2)
            elif option == get_all_trees_between_2_years_graphic_option:
                year1 = self.readYear()
                year2 = self.readYear()
                self.__data.repository_representation_years_range(year1, year2)
            elif option == get_bar_char_with_all_types_option:
                self.__data.types_bar()
            elif option == get_bar_chart_number_trees_planted_in_intervals_of_20_years_option:
                self.__data.intervals_bar_chart()
            elif option == stop_option:
                stop = True
            else:
                print("Option does not exist!")
