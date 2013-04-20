"""
Created on Thu Apr 19 11:55:16 2012

@author: Jose
"""
import sys,os,numpy,scipy,shelve

HDefault = 12e3 # Platform height (m)
VrDefault = 150 # Effective radar velocity (m/s)
thetarcDefault = 25*numpy.pi/180 # Beam squint angle (rad)

class Platform:
    def __init__(self,filename,H=HDefault,Vr=VrDefault,\
                 thetarc=thetarcDefault,mode='store'):
        """Initialize parameters that characterize the platform"""
        self.H=H
        self.Vr=Vr
        self.thetarc=thetarc
        if mode == 'store':
            # stores data in a file
            database=shelve.open(filename)
            database['H'] = self.H
            database['Vr'] = self.Vr
            database['thetarc'] = self.thetarc
        database.close()
        