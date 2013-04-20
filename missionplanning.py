"""
Created on Thu Apr 19 11:55:16 2012

@author: Jose
"""

import sys,os,numpy,scipy
from scipy import constants

class selectionOfPRF:
    def __init__(self):
        """Helps to select the PRF value, given the length of the pulse and the receive\
        protect window extension"""
    def checkValue(self,Pulse,scene2D):
        startRxWindow=numpy.mod(2*scene2D.Rmin*Pulse.Fa/constants.c)/Pulse.Fa,1)
        endRxWindow=numpy.mod(2*scene2D.Rmax*Pulse.Fa/constants.c)/Pulse.Fa,1)
        startRxInterpulsePosition=numpy.floor(2*scene2D.Rmin*Pulse.Fa/constants.c)
        endRxInterpulsePosition=numpy.floor(2*scene2D.Rmax*Pulse.Fa/constants.c)
        if startRxWindow > Pulse.Tr+Pulse.Trp or endRxWindow < 1/Pulse.F-Pulse.Trp \
            or startRxInterpulsePosition != endRxInterpulsePosition:
                print("The value of the PRF is not well suited to the radar gating window")
                return(1)
        else:
                print("The value of the PRF is well suited to the radar gating window")
                return(0)
                
        