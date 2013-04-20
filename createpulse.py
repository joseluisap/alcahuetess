"""
Created on Thu Apr 19 11:55:16 2012

@author: Jose
"""
import sys,os,numpy,scipy
import shelve
import antenna,createscene

TrDefault = 2.5e-6;  # Transmitted pulse duration (s)
TrpDefault = 2.5e-6;  # Transmitted pulse duration (s)
KrDefault = 20e12; # FM rate of transmitted pulse chirp (Hz/s)
f0Default = 5.3e9 # Carrier frequency (Hz)
FrDefault = 60e6 # Range sampling rate (Hz)
FaDefault = 100 # Azimuth sampling rate or PRF (Hz)


class Pulse:
	def __init__(self,filename,Tr=TrDefault,Trp=TrpDefault,Kr=KrDefault,\
				f0=f0Default,Fr=FrDefault,Fa=FaDefault,mode='store'):
		"""Initialize parameters that characterize the pulse"""
		self.Tr = Tr
		self.Kr = Kr
		self.f0 = f0
		self.Fr = Fr
		self.Fa = Fa
		if mode == 'store':
			# stores data in a file
			database=shelve.open(filename)
			database['Tr'] = self.Tr
			database['Kr'] = self.Kr
			database['f0'] = self.f0
			database['Fr'] = self.Fr
			database['Fa'] = self.Fa
		database.close()
	def wr(self,t,dt):
		if abs(t) < dt:
			return(1.0)
		else:
			return(0.0)
	def signalRx(self,A0,tau,eta,etac,tn,coordinatesXY,amplitudeXY,platform,case='Low squint'):
		antennaInUse=antenna()
		antennaPattern=antennaInUse.pattern(eta,etac)
		
		scene=createscene()
		#R=RLowSquint(eta,)
		scene=createscene.scene2D()
		for 
			scene.findPoints(coordinatesXY,amplitudeXY,eta,platform)
			RA=scene.coordinatesRA
		
#		if case == 'Low squint':
#			R=
#		etaStart=0
#		etaStop=
#		for eta in xrange(etaStart,etaStop,etaStep)
		self.st=A0*self.wr(tau-2*R(eta)/c)*antennaPattern*\
		numpy.exp(-4j*2*numpy.pi*self.f0*R(eta)/c)*\
		numpy.exp(1j*numpy.pi*self.Kr*(tau-2*R(eta)/c))