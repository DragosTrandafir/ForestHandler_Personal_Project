from app.tree_controller import TreeCtrl


class UI:
    def __init__(self, data):
        self.__data = data

    def printMenu(self):
        s = ""
        s += ("MENU:\n\t1. Add a tree to the forest\n\t2. Get all trees and types (console)\n\t3. Insert a tree to the forest\n"
              + "\t4. Delete a tree from the forest\n\t5. Delete all trees of a given type\n"
              + "\t6. Delete all trees planted between 2 given years\n"
              + "\t7. Get all trees having the coordinates in a certain range (console)\n"
              + "\t8. Get all trees planted between 2 given years (console)\n"
              + "\t9. SORTING options (not ready yet) \n"
              + "\t10. FILTER options (not ready yet) \n"
              + "\t11. Determine the oldest tree \n"
              + "\t12. Determine trees which are the same, excepting their type\n"
              + "\t13. Delete all trees that overlap (only the first of each is kept)\n"
              + "\t14. Update tree by index\n"
              + "\t15. Update tree by id\n"
              + "\t16. Get a visual representation of the repository \n"
              + "\t17. Get all trees having the coordinates in a certain range (graphic)\n"
              + "\t18. Get all trees planted between 2 given years (graphic)\n"
              + "\t19. Get a pie chart with all the types\n"
              + "\t20. Get a bar chart with number of trees planted in intervals of 20 years\n"
              + "\t0. STOP\n")
        return s

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
        tree = self.__data.read_tree_ctrl()
        return tree

    def read_type_ui(self):
        type = self.__data.read_type_ctrl()
        return type

    def start(self):
        stop = False
        while not stop:
            print(self.printMenu())
            option = self.readOption()
            if option == 1:
                tree = self.read_tree_ui()
                self.__data.add_tree_type(tree)
                print(str(self.__data))
            elif option == 2:
                print(str(self.__data))
            elif option == 3:
                tree = self.read_tree_ui()
                index = self.readIndex()
                self.__data.insert_tree_type(tree,index)
                print(str(self.__data))
            elif option == 4:
                index = self.readIndex()
                self.__data.delete_tree_type(index)
                print(str(self.__data))
            elif option == 5:
                type = self.read_type_ui()
                self.__data.delete_treeByType(type)
                print(str(self.__data))
            elif option == 6:
                year1 = self.readYear()
                year2 = self.readYear()
                self.__data.delete_tree_type_between_years(year1,year2)
                print(str(self.__data))
            elif option==7:
                xcoord1= self.readCoordX()
                xcoord2 = self.readCoordX()
                ycoord1 = self.readCoordY()
                ycoord2 = self.readCoordY()
                print(self.__data.coords_range_ctrl(xcoord1, xcoord2, ycoord1, ycoord2))
            elif option == 8:
                year1 = self.readYear()
                year2 = self.readYear()
                print(self.__data.years_range_ctrl(year1, year2))
            elif option == 11:
                print(self.__data.oldest_tree_repo())
            elif option == 12:
                print(self.__data.trees_at_least_2_types_ctrl())
            elif option == 13:
                self.__data.delete_overlapping_ctrl()
                print(str(self.__data))
            elif option == 14:
                index = self.readIndex()
                self.__data.update_tree_by_index_ctrl(index)
                print(str(self.__data))
            elif option == 15:
                id = self.readId()
                self.__data.update_tree_by_id_ctrl(id)
                print(str(self.__data))
            elif option == 16:
                self.__data.repository_representation_general_ctrl()
            elif option == 17:
                xcoord1 = self.readCoordX()
                xcoord2 = self.readCoordX()
                ycoord1 = self.readCoordY()
                ycoord2 = self.readCoordY()
                self.__data.coords_range_representation_ctrl(xcoord1, xcoord2, ycoord1, ycoord2)
            elif option == 18:
                year1 = self.readYear()
                year2 = self.readYear()
                self.__data.repository_representation_years_range_ctrl(year1, year2)
            elif option == 19:
                self.__data.types_bar_ctrl()
            elif option == 20:
                self.__data.intervals_bar_chart_ctrl()
            elif option == 0:
                stop = True
            else:
                print("Option does not exist!")
