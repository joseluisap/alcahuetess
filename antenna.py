"""
Created on Thu Apr 19 11:55:16 2012

@author: Jose
"""

import sys,os,numpy,scipy,shelve

antennaTypeDefault='Isotropic'
isotropic={'beamwidthAzimuth',numpy.pi/4,'beamwidthElevation',numpy.pi/4}

class antenna:
    def __init__(self,antennaType=antennaTypeDefault):
        """Initialize parameters"""
        self.type=type
    def pattern(self,azimuth,elevation):
        if self.type == 'Isotropic':
            if (numpy.abs(azimuth) < isotropic['beamwidthAzimuth']\
               and numpy.abs(elevation) < isotropic['beamwidthElevation']):
                self.wa=1.0
            else:
                self.wa=0.0
            
        