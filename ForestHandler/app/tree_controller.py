from ForestHandler.infrastructure.tree_repo import TreeRepo
from ForestHandler.infrastructure.type_repo import TypeRepo
from ForestHandler.domain.tree import Tree
from ForestHandler.domain.type import Type
import matplotlib.pyplot as plt


class TreeCtrl:
    def __init__(self,treeRepo,typeRepo):
        self.__treeRepo=treeRepo
        self.__typeRepo=typeRepo

    def treeRepo_getter(self):
        return self.__treeRepo

    def typeRepo_getter(self):
        return self.__typeRepo

    def treeRepo_setter(self,tr):
        self.__treeRepo=tr

    def typeRepo_setter(self,tr):
        self.__typeRepo=tr

    def __str__(self):
        return str(self.__treeRepo)+"\n"+str(self.__typeRepo)

    # read a tree
    def read_tree_ctrl(self):
        treeRepo=TreeRepo()
        try:
            tree=treeRepo.read_tree_repo()
        except ValueError as valueError:
            raise ValueError(valueError)
        return tree

    def read_type_ctrl(self):
        typeRepo=TypeRepo()
        try:
            type=typeRepo.read_type_repo()
        except ValueError as valueError:
            raise ValueError(valueError)
        return type

    # 1. Add a tree to the forest
    def add_tree_type(self,tree):
        try:
            self.__treeRepo.add_tree(tree)
            if not self.__typeRepo.contains(tree.type_getter()):
                self.__typeRepo.add_type(tree.type_getter())
        except ValueError as valueError:
            raise ValueError(valueError)



    # 3. Insert a tree to the library
    def insert_tree_type(self,tree,index):
        try:
            self.__treeRepo.insert_tree(tree,index)
            if not self.__typeRepo.contains(tree.type_getter()):
                self.__typeRepo.add_type(tree.type_getter())
        except ValueError as valueError:
            raise ValueError(valueError)

    # 4. Delete a tree from the forest
    def delete_tree_type(self,index):
        try:
            if not self.__treeRepo.two_trees_same_type(self.__treeRepo.type_of_tree_by_index(index)):
                self.__typeRepo.delete_types(self.__treeRepo.type_of_tree_by_index(index))
            self.__treeRepo.delete_tree(index)
        except ValueError as valueError:
            raise ValueError(valueError)

    # 5 . Delete all trees of a given type
    def delete_treeByType(self,type):
        self.__typeRepo.delete_types(type)
        self.__treeRepo.delete_tree_ByType(type)

    # 6 . Delete all trees planted between 2 given years
    def delete_tree_type_between_years(self,year1,year2):
        if year1>year2:
            year1,year2=year2,year1
        for type in self.__treeRepo.get_types_of_tree_by_years(year1,year2):
            if not self.__treeRepo.two_trees_same_type(type):
                self.__typeRepo.delete_types(type)
        self.__treeRepo.delete_tree_years(year1,year2)

    # 7. Get all trees having the coordinates in a certain range
    def coords_range_ctrl(self,xcoord1,xcoord2,ycoord1,ycoord2):
        return self.__treeRepo.coords_range(xcoord1,xcoord2,ycoord1,ycoord2)

    # 8. Get all trees planted between 2 given years
    def years_range_ctrl(self,year1,year2):
        return self.__treeRepo.years_range(year1,year2)

    # 9
    def sort_by_year_ctrl(self):
        return self.__treeRepo.sort_by_year()

    # 10
    def filter_id_ctrl(self, parity):
        try:
            return self.__treeRepo.filter_id(parity)
        except ValueError as valueError:
            raise ValueError(valueError)

    # 11 . Determine the oldest tree
    def oldest_tree_repo(self):
        try:
            r=self.__treeRepo.oldest_tree()
            return r
        except ValueError as valueError:
            raise ValueError(valueError)

    # 12 . Determine all the trees which are the same, excepting their type
    def trees_at_least_2_types_ctrl(self):
        s=self.__treeRepo.trees_at_least_2_types()
        return s

    # 13 . Delete all trees that overlap (only the first of each is kept)
    def delete_overlapping_ctrl(self):
        self.__treeRepo.delete_overlapping()

    # 14 . Update tree at index
    def update_tree_by_index_ctrl(self, index):
        try:
            if not self.__treeRepo.two_trees_same_type(self.__treeRepo.type_of_tree_by_index(index)):
                self.__typeRepo.delete_types(self.__treeRepo.type_of_tree_by_index(index))
            self.__treeRepo.update_tree_by_index_repo(index)
            if not self.__typeRepo.contains(self.__treeRepo.type_of_tree_by_index(index)):
                self.__typeRepo.add_type(self.__treeRepo.type_of_tree_by_index(index))
        except ValueError as valueError:
            raise ValueError(valueError)

    # 15 . Update tree by id
    def update_tree_by_id_ctrl(self, id):
        try:
            index_where_to_update = self.__treeRepo.get_index_by_id(id)
            if not self.__treeRepo.two_trees_same_type(self.__treeRepo.type_of_tree_by_index(index_where_to_update)):
                self.__typeRepo.delete_types(self.__treeRepo.type_of_tree_by_index(index_where_to_update))
            self.__treeRepo.update_tree_by_id_repo(id)
            if not self.__typeRepo.contains(self.__treeRepo.type_of_tree_by_index(index_where_to_update)):
                self.__typeRepo.add_type(self.__treeRepo.type_of_tree_by_index(index_where_to_update))
        except ValueError as valueError:
            raise ValueError(valueError)

    # 16. Get a visual representation of the repository
    def repository_representation_general_ctrl(self):
        self.__treeRepo.repository_representation_general()

    # 17. Get all trees having the coordinates in a certain range (graphic)
    def coords_range_representation_ctrl(self, xcoord1, xcoord2, ycoord1, ycoord2):
        self.__treeRepo.repository_representation_coords_range(xcoord1, xcoord2, ycoord1, ycoord2)

    # 18. Get all trees planted between 2 given years (graphic)
    def repository_representation_years_range_ctrl(self, year1, year2):
        self.__treeRepo.repository_representation_years_range(year1, year2)

    # 19. Get a pie chart with all the types
    def types_bar_ctrl(self):
        fig, ax = plt.subplots(figsize=(9, 5))
        parts = []
        for type in self.__typeRepo.get_types():
            number=self.__treeRepo.type_appearences(type)
            parts.append(number)
        ax.set_title('Pie chart with all the types of the repository')
        labels=self.__typeRepo.get_types_special()
        colors=self.__treeRepo.get_colors()
        ax.pie(parts, labels=labels, colors=colors, autopct='%.2f %%', pctdistance=0.7)
        plt.show()

    # 20. Get a bar chart with number of trees planted in intervals of 20 years
    def intervals_bar_chart_ctrl(self):
        self.__treeRepo.intervals_bar_chart()
