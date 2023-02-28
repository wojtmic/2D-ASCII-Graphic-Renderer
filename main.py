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

height = 10
width = 10

def getCell(x,y):
    for celll in cells:
        for xfind in range(height):
            for yfind in range(width):
                if celll.getX() == x and celll.getY() == y:
                    return celll

cells = []

for y in range(height):
    for x in range(width):
        if y == 0 and x == 0:
            cells.append(cell(type="glob",icon="G",x=x,y=y))
        else:
            cells.append(cell(x=x,y=y))

for y in range(height):
    for x in range(width):
        if getCell(x,y) != None:
            print(getCell(x,y).getIcon(),end="")
    print("")
