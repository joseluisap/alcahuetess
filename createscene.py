"""
Created on Thu Apr 19 11:55:16 2012

@author: Jose
"""

import sys,os,numpy,scipy,shelve

class scene2D:
    def __init__(self):
        """Creates a scence"""
    def findPoints(self,coordinatesXY,amplitudeXY,eta,platform):
        ndimXY=numpy.ndim(coordinatesXY)
        ndimA=numpy.ndim(amplitudeXY)
        
        shapeXY=numpy.shape(coordinatesXY)
        shapeA=numpy.shape(amplitudeXY)
        
        sizeXY=numpy.size(coordinatesXY)
        sizeA=numpy.size(amplitudeXY)
        
        if ndimXY != ndimA or shapeXY != shapeA or sizeXY != sizeA:
            raise IOError,\
                "Arrays coordinatesXY and amplitudeXY must have the same dimensions"
        
        self.coordinatesRA=numpy.empty(shapeXY)
        self.amplitudeRA=numpy.empty(shapeA)
        self.coordinatesRA[:,0]=numpy.sqrt((coordinatesXY[:,0]-platform.Vr*eta)**2+\
                                           coordinatesXY[:,1]**2+platform.H**2)
        self.coordinatesRA[:,1]=numpy.arcsin(coordinatesXY[:,1]/self.coordinatesRA[:,0])
        self.amplitudeRA=amplitudeXY
def RLowSquint(eta,R0,Vr):
    return(R0+Vr**2*eta**2/(2*R0))