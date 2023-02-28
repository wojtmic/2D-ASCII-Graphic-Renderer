class cell():
    def __init__(self,type="air",icon=".",x=0,y=0):
        self.type = type
        self.icon = icon
        self.x = x
        self.y = y
    def getIcon(self):
        return self.icon
    def getX(self):
        return self.x
    def getY(self):
        return self.y

def getCell(x,y):
    for celll in cells:
        for xfind in range(x):
            for yfind in range(y):
                if celll.getX() == xfind and celll.getY() == yfind:
                    return celll

cells = []

height = 5
width = 5 + 1

for y in range(height):
    for x in range(width):
        if y == 3 and x == 3:
            cells.append(cell(x=x,y=y,icon="x",type="debug"))
        else:
            cells.append(cell(x=x,y=y))

for y in range(height):
    for x in range(width):
        if getCell(x,y) != None:
            print(getCell(x,y).getIcon(),end="")
    print("")
