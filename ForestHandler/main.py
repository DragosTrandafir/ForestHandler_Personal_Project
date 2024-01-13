from infrastructure.tree_repo import TreeRepo
from infrastructure.type_repo import TypeRepo
from domain.tree import Tree
from domain.type import Type
from app.tree_controller import TreeCtrl
from ui.user import UI

type1=Type(("Baobab", "Madagascar"))
type2=Type(("Maple", "Canada"))
type3=Type(("Sakura", "Japan"))
type4=Type(("Eucalyptus", "Australia"))
type5=Type(("Olive", "Mediterranean"))
type6=Type(("Pine", "United States"))
type7=Type(("European beech ", "Romania"))
type8=Type(("Norway spruce", "Romania"))
type9=Type(("Silver fir", "Romania"))
type10=Type(("Quercus", "Romania"))


tree1=Tree(101,1934,[2,5],type1)
tree2=Tree(102,1999,[22,5],type1)
tree3=Tree(103,2003,[9,1],type1)
tree4=Tree(104,1999,[23,5],type1)


tree5=Tree(105,1939,[8,23],type2)
tree6=Tree(106,2004,[24,25],type2)
tree7=Tree(107,2001,[9,14],type2)

tree8=Tree(108,1998,[11,5],type3)
tree9=Tree(109,1937,[2,15],type3)
tree10=Tree(110,1989,[21,5],type3)
tree11=Tree(111,2013,[19,1],type3)
tree12=Tree(112,2015,[1,5],type3)

tree13=Tree(113,1938,[1,2],type4)
tree14=Tree(114,1997,[3,5],type4)
tree15=Tree(115,2012,[4,1],type4)
tree16=Tree(116,2020,[5,5],type4)

tree17=Tree(117,1940,[11,22],type7)
tree18=Tree(118,1941,[3,13],type7)
tree19=Tree(119,2021,[13,13],type7)
tree20=Tree(120,2023,[1,1],type7)

tree21=Tree(121,1934,[21,0],type5)
tree22=Tree(122,1999,[2,0],type5)
tree23=Tree(123,2003,[9,0],type5)
tree24=Tree(124,1999,[23,0],type5)

tree25=Tree(125,1939,[8,0],type6)
tree26=Tree(126,2004,[24,21],type6)
tree27=Tree(127,2001,[0,14],type6)

tree28=Tree(128,1998,[0,5],type8)
tree29=Tree(129,1937,[0,15],type8)
tree30=Tree(130,1989,[22,5],type8)
tree31=Tree(131,2013,[19,0],type8)
tree32=Tree(132,2015,[11,5],type8)

tree33=Tree(133,1938,[0,2],type9)
tree34=Tree(134,1997,[3,0],type9)
tree35=Tree(135,2012,[0,1],type9)
tree36=Tree(140,2023,[1,10],type9)

tree37=Tree(137,1941,[7,22],type10)
tree38=Tree(138,1941,[3,8],type10)
tree39=Tree(139,2022,[9,13],type10)
tree40=Tree(141,2023,[1,10],type10)
tree41=Tree(142,1941,[3,8],type9)

tree42=Tree(143,1999,[18,18],type1)
tree43=Tree(144,1999,[18,19],type2)
tree44=Tree(145,1999,[19,18],type3)
tree45=Tree(146,1999,[17,16],type4)
tree46=Tree(147,1999,[17,17],type5)
tree47=Tree(148,1999,[16,17],type6)
tree48=Tree(149,1999,[2,23],type7)
tree49=Tree(150,1999,[1,24],type8)
tree50=Tree(151,1999,[3,22],type9)
tree51=Tree(152,1956,[1,22],type10)


treeR=TreeRepo()
typeR=TypeRepo()
ctrl=TreeCtrl(treeR,typeR)


for i in range(1, 52):
    tree_object = globals()[f'tree{i}']
    ctrl.add_tree_type(tree_object)

ui=UI(ctrl)
ui.start()

