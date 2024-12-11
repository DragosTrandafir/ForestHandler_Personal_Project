from ForestHandler.domain.tree import Tree
from ForestHandler.domain.type import Type
import matplotlib.pyplot as plt


class TreeRepo:
    # Each tree should have a unique id!

    colors = ["burlywood", "forestgreen", "pink", "mediumseagreen", "olivedrab", "darkgreen", "limegreen", "green",
              "lightslategray", "yellowgreen"]

    def __init__(self):
        self.__trees=[]

    def get_trees(self):
        return self.__trees

    def get_colors(self):
        return self.colors

    def set_trees(self, vl):
        self.__trees = vl

    def read_tree_repo(self):
        tree=Tree(1,1906,[1,1],Type(("Baobab", "Madagascar")))
        try:
            tree.read_tree()
        except ValueError as valueError:
            raise ValueError(valueError)
        return tree

    def __str__(self):
        s=""
        for i in range (0,len(self.__trees)):
            if str(self.__trees[i])!="":
                s += str(self.__trees[i]) + "\n"
        return s

    # 1
    def add_tree(self,tree):
        if tree.id_getter()>=0 and tree.year_planted_getter()>=0:
            self.__trees.append(tree)

    # 3
    def insert_tree(self,tree,index):
        if index<0 or index>=len(self.__trees):
            print("Not an available index!")
        else:
            if tree.id_getter() >= 0 and tree.year_planted_getter() >= 0:
                self.__trees.insert(index,tree)

    # 4
    def delete_tree(self,index):
        if index<0 or index>=len(self.__trees):
            print("Not an available index!")
        else:
            del self.__trees[index]

    def type_of_tree_by_index(self,index):
        if 0 <= index < len(self.__trees):
            type=self.__trees[index].type_getter()
            return type
        return Type(("",""))

    def two_trees_same_type(self,type):
        c=0
        for i in range(0,len(self.__trees)):
            if type==self.__trees[i].type_getter():
                c+=1
        if c>=2:
            return True
        return False

    # 5
    def delete_tree_ByType(self,type):
        for i in range(len(self.__trees)-1,-1,-1):
            if self.__trees[i].type_getter()==type:
                del self.__trees[i]

    # 6
    def delete_tree_years(self,year1,year2):
        for i in range(len(self.__trees)-1,-1,-1):
            if year1 <= self.__trees[i].year_planted_getter() <= year2:
                del self.__trees[i]

    def get_types_of_tree_by_years(self,year1,year2):
        types=[]
        for i in range(len(self.__trees)-1,-1,-1):
            if year1 <= self.__trees[i].year_planted_getter() <= year2:
                types.append(self.__trees[i].type_getter())
        return types

    # 7. Get all trees having the coordinates in a certain range
    def coords_range(self,xcoord1,xcoord2,ycoord1,ycoord2):
        s=""
        for elem in self.__trees:
            if xcoord1<=elem.coords_getter()[0]<=xcoord2 and ycoord1<=elem.coords_getter()[1]<=ycoord2:
                s+= str(elem) + "\n"
        return s

    # 8. Get all trees planted between 2 given years
    def years_range(self,year1,year2):
        s=""
        for i in range(len(self.__trees) - 1, -1, -1):
            if year1 <= self.__trees[i].year_planted_getter() <= year2:
                s += str(self.__trees[i])+"\n"
        return s

    # 9. Sort the trees by year (ascending)
    def sort_by_year(self):
        list=sorted(self.__trees, key=lambda x:x.year_planted_getter())
        s = ""
        for i in range(0, len(list)):
            if str(list[i]) != "":
                s += str(list[i]) + "\n"
        return s

    # 10. Filter the tree repository to get only trees with even or odd id
    def filter_id(self,parity):
        if parity=="odd":
            list1=list(filter(lambda x:x.id_getter()%2!=0, self.__trees))
            s = ""
            for i in range(0, len(list1)):
                if str(list1[i]) != "":
                    s += str(list1[i]) + "\n"
            return s
        elif parity=="even":
            list1 = list(filter(lambda x: x.id_getter() % 2 == 0, self.__trees))
            s = ""
            for i in range(0, len(list1)):
                if str(list1[i]) != "":
                    s += str(list1[i]) + "\n"
            return s
        else:
            print("Unavailable input!")

    # 11
    def oldest_tree(self):
        if len(self.__trees)<1:
            return "No oldest tree"
        else:
            oldest=self.__trees[0].year_planted_getter()
            index=0
            for i in range(1,len(self.__trees)):
                if self.__trees[i].year_planted_getter()<oldest:
                    oldest = self.__trees[i].year_planted_getter()
                    index = i
            return str(self.__trees[index])

    # 12
    def trees_at_least_2_types(self):
        index = 0
        s=""
        for i in range(0,len(self.__trees)-1):
            c=0
            for j in range(i+1,len(self.__trees)):
                if self.__trees[i] == self.__trees[j]:
                    c+=1
                    index = i
            if c>=1:
                s += str(self.__trees[index])+"\n"
        return s

    # 13 . Delete all trees that overlap (only the first of each is kept)
    def delete_overlapping(self):
        for i in range(len(self.__trees)-2,-1,-1):
            for j in range(len(self.__trees)-1,i,-1):
                if self.__trees[i].coords_getter() == self.__trees[j].coords_getter():
                    del self.__trees[j]


    # 14
    def update_tree_by_index_repo(self, index):
        if index<0 or index>=len(self.__trees):
            print("Not an available index/id!")
        else:
            tree = Tree(-1, -1, [1], Type(("", "")))
            tree.read_tree()
            self.__trees[index]=tree

    # 15
    def get_index_by_id(self,id):
        for i in range(0,len(self.__trees)):
            if self.__trees[i].id_getter() == id:
                return i
        return -1

    def update_tree_by_id_repo(self,id):
        index = self.get_index_by_id(id)
        self.update_tree_by_index_repo(index)

    # 16. Get a visual representation of the repository
    def repository_representation(self,trees):
        fig, ax = plt.subplots()
        for tree in trees:
            x = tree.coords_getter()[0]
            y = tree.coords_getter()[1]
            if tree.type_first_three() == "Bao":
                marker = "o"
                color = "burlywood"
            elif tree.type_first_three() == "Map":
                marker = "^"
                color = "forestgreen"
            elif tree.type_first_three() == "Sak":
                marker = "s"
                color = "pink"
            elif tree.type_first_three() == "Euc":
                marker = "p"
                color = "mediumseagreen"
            elif tree.type_first_three() == "Oli":
                marker = "*"
                color = "olivedrab"
            elif tree.type_first_three() == "Pin":
                marker = "h"
                color = "darkgreen"
            elif tree.type_first_three() == "Eur":
                marker = "1"
                color = "limegreen"
            elif tree.type_first_three() == "Nor":
                marker = "2"
                color = "green"
            elif tree.type_first_three() == "Sil":
                marker = "3"
                color = "lightslategray"
            elif tree.type_first_three() == "Que":
                marker = "4"
                color = "yellowgreen"
            else:
                marker = "."
                color = "green"

            ax.scatter(x, y, marker=marker, color=color, s=70)

        ax.set_xlabel('X coordinates')
        ax.set_ylabel('Y coordinates')
        ax.set_title('Visual representation of the repository')

        plt.show()

    def repository_representation_general(self):
        self.repository_representation(self.__trees)

    # 17. Get all trees having the coordinates in a certain range (graphic)
    def repository_representation_coords_range(self, xcoord1, xcoord2, ycoord1, ycoord2):
        repoCopy=list(filter(lambda elem:xcoord1 <= elem.coords_getter()[0] <= xcoord2 and ycoord1 <= elem.coords_getter()[1] <= ycoord2 ,self.__trees))
        self.repository_representation(repoCopy)

    # 18. Get all trees planted between 2 given years (graphic)
    def repository_representation_years_range(self,year1,year2):
        repoCopy=list(filter(lambda elem:year1 <= elem.year_planted_getter() <= year2,self.__trees))
        self.repository_representation(repoCopy)

    # 19. Get a pie chart with all the types
    def type_appearences(self,type):
        nr=0
        for tree in self.__trees:
            if tree.type_getter()==type:
                nr+=1
        return nr

    # 20. Get a bar chart with number of trees planted in intervals of 20 years
    def oldest_year(self):
        if len(self.__trees)<1:
            print("Not an available operation!")
        else:
            oldest=self.__trees[0].year_planted_getter()
            index=0
            for i in range(1,len(self.__trees)):
                if self.__trees[i].year_planted_getter()<oldest:
                    oldest = self.__trees[i].year_planted_getter()
                    index = i
            return self.__trees[index].year_planted_getter()

    def intervals_bar_chart(self):
        oldest_year=self.oldest_year()
        bar_counter=[]
        bar_years=[]
        for i in range(oldest_year,2025,20): # present year + 20
            nr=0
            bar_years.append(i)
            for tree in self.__trees:
                if i<=tree.year_planted_getter()<i+20:
                    nr+=1
            bar_counter.append(nr)

        fig, ax= plt.subplots()
        for i in range(0,len(bar_years)):
            bar_years[i] = str(bar_years[i])+"-"+str(bar_years[i]+20)

        ax.set_xlabel("Intervals of 20 years in which trees are planted")
        ax.set_ylabel("Number of trees")
        ax.set_title('Bar chart with distribution of trees in year intervals')
        ax.bar(bar_years,bar_counter,color=self.colors)
        plt.show()












'''
treeRepo=TreeRepo()
tree=treeRepo.read_tree_repo()
treeRepo.add_tree(tree)
tree=treeRepo.read_tree_repo()
treeRepo.add_tree(tree)
print(str(treeRepo))
'''