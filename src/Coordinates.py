def addtoCoordinate(c, x, y, z, k):
    return (c[0]+x,c[1]+y,c[0]+z,c[1]+k)
    
class Coordinates():
    dinosaur = (160, 423)
    d = dinosaur
    replayBtn = (d[0]+180,d[1])
    flyingdino = addtoCoordinate(d, 60, -10, 100, -5)
    g = addtoCoordinate(d, 85, -55, 98, -43)
    c1 = 15
    c2 = 0
    #c3 = [100, 120, 120, 130, 130, 170, 210, 350]
    c4 = 25
    
class times():
    jumplen = [0.18, 0.18, 0.18, 0.17, 0.17, 0.17, 0.17, 0.17]
    lendlen = [0.15, 0.15, 0.14, 0.13, 0.12, 0.12, 0.11, 0.10]
    ducklen = [0.02, 0.018, 0.017, 0.015, 0.010, 0.010, 0.010, 0.010]
    timepassed = [10.0, 20.0, 30.0, 40.0, 70.0, 85.0, 100.0, 1000.0]
