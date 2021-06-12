from tkinter import *

Camera = [60,600,600,0,0,0]
Points = []
Cubes = []

fen_princ = Tk()
fen_princ.title("Test en 3d")
fen_princ.geometry("600x600")

Canvas = Canvas(fen_princ, width=500, height=500, bg='white',borderwidth=0, highlightthickness=0)
Canvas.pack()


def MakeAPoint(x,y,z):
    P = [x,y,z]
    Points.append(P)

def MakeCube(x,y,z,Size):
    C = []
    Face = [x - Size, y + Size, z + Size, x + Size, y + Size, z + Size, x + Size, y - Size, z + Size, x - Size, y - Size, z + Size]
    C.append(Face)
    Face = [x - Size, y + Size, z - Size, x + Size, y + Size, z - Size, x + Size, y - Size, z - Size, x - Size, y - Size, z - Size]
    C.append(Face)
    Face = [x - Size, y + Size, z - Size, x + Size, y + Size, z - Size, x + Size, y + Size, z + Size, x - Size, y + Size, z + Size]
    C.append(Face)
    Face = [x - Size, y - Size, z - Size, x + Size, y - Size, z - Size, x + Size, y - Size, z + Size, x - Size, y - Size, z + Size]
    C.append(Face)
    Face = [x - Size, y - Size, z - Size, x - Size, y + Size, z - Size, x - Size, y + Size, z + Size, x - Size, y - Size, z + Size]
    C.append(Face)
    Face = [x + Size, y - Size, z - Size, x + Size, y + Size, z - Size, x + Size, y + Size, z + Size, x + Size, y - Size, z + Size]
    C.append(Face)
    
    Cubes.append(C)

def NewFrame():
    for Point in Points:
        PosXR = Point[0] - Camera[3]
        PosYR = Point[1] - Camera[4]
        PosZR = Point[2] - Camera[5]

        PosXS = (Camera[0] / PosZR) * PosXR
        PosYS = (Camera[0] / PosZR) * PosYR
        
        if PosXS <= Camera[1] and PosYS <= Camera[2]:
            Canvas.create_rectangle(PosXS - 5 + 300,PosYS - 5 + 300,PosXS + 6 + 300,PosYS + 6 + 300)

    for Face in Cubes:
        for Point in Face:
            print(Point)
            PointAXR = Point[0] - Camera[3]
            PointAYR = Point[1] - Camera[4]
            PointAZR = Point[2] - Camera[5]

            PosAXS = (Camera[0] / PointAZR) * PointAXR
            PosAYS = (Camera[0] / PointAZR) * PointAYR

            PointBXR = Point[3] - Camera[3]
            PointBYR = Point[4] - Camera[4]
            PointBZR = Point[5] - Camera[5]

            PosBXS = (Camera[0] / PointBZR) * PointBXR
            PosBYS = (Camera[0] / PointBZR) * PointBYR

            PointCXR = Point[6] - Camera[3]
            PointCYR = Point[7] - Camera[4]
            PointCZR = Point[8] - Camera[5]

            PosCXS = (Camera[0] / PointCZR) * PointCXR
            PosCYS = (Camera[0] / PointCZR) * PointCYR

            PointDXR = Point[9] - Camera[3]
            PointDYR = Point[10] - Camera[4]
            PointDZR = Point[11] - Camera[5]

            PosDXS = (Camera[0] / PointDZR) * PointDXR
            PosDYS = (Camera[0] / PointDZR) * PointDYR

            PosAXS = int(PosAXS)
            PosAYS = int(PosAYS)

            PosBXS = int(PosBXS)
            PosBYS = int(PosBYS)

            PosCXS = int(PosCXS)
            PosCYS = int(PosCYS)

            PosDXS = int(PosDXS)
            PosDYS = int(PosDYS)

            print(PosAXS)
            print(PosDXS)

            Canvas.create_polygon(PosAXS + 300,PosAYS + 300,PosBXS + 300,PosBYS + 300,PosCXS + 300,PosCYS + 300,PosDXS + 300,PosDYS + 300)

            
MakeCube(4,0,8,3)
MakeCube(-4,0,8,3)
NewFrame()
fen_princ.mainloop()

        
