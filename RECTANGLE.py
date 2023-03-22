# Simple Rectangle data structure.
# Helper function for Bnuuy drivers to seamlessly communicate.
#      By L3pu5, L3pu5_Hare
#
# A simple Python wrapper for the ILI4988 driver bound to the SPI interface IM[2:0] 101 for chipsets such as
# those ubuqituous ones on Aliexpress.

class RECTANGLE():
    x = 0
    y = 0
    xf = 0
    yf = 0
    width = 0
    height = 0
    
    def __str__(self):
        return f"({self.x}, {self.y} -> {self.xf}, {self.yf} : {self.width} x {self.height} => {self.width*self.height} :: BUFF => {self.width*self.height*2})"

    def __init__(self, xi, yi, xf, yf):
        #FORCE lowerbound corners, xy
        if(xf < xi):
            self.x = xf
            self.xf = xi
        else:
            self.x = xi
            self.xf = xf
        if(yf < yi):
            self.y = yf
            self.yf = yi
        else:
            self.y = yi
            self.yf = yf
        self.width = self.xf-self.x
        self.height = self.yf-self.y

    def from_bounds(xi, yi, xf, yf):
        return RECTANGLE(xi, yi, xf, yf)
    
    def from_dimensions(xi, yi, width, height):
        return RECTANGLE(xi, yi, xi+width, yi+height)