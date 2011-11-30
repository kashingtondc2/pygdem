'''
Created on 29/nov/2011

@author: gionata
'''
from tiffDb.tiffDb import tiffDb
import skimage.io as image
image.use_plugin('freeimage')
db=tiffDb()
from numpy import *
class TiffReader(object):
    '''
    classdocs
    '''
    def __init__(self,file=None,lon=None,lat=None):
        '''
        Constructor
        '''
        self.dd=30.
        if not file is None:
                self.file=file
                self.readit()
        else:
                if not lon is None and not lat is None:
                        self.file,self.rect=db.file_from_coordinate(lon,lat)
    def __eq__(self,B):
        return self.file==B.file
                    
    def readit(self):
        self.im=image.imread(self.file)
        self.lon=self.rect[0]+linspace(0,1,3601)
        self.lat=self.rect[2]+linspace(0,1,3601)
        self.Lon,self.Lat=meshgrid(self.lon,self.lat)
        self.darc=self.lon[1]-self.lon[0]
    def subset(self,rect=None,around=None):
        if not rect is None:
                ilo=nonzero(self.lon>=rect[0] and self.lon<=rect[1])[0][[0,-1]]
                ila=nonzero(self.lat>=rect[2] and self.lat<=rect[3])[0][[0,-1]]                
        elif not around is None:
                lo0=around[0]
                la0=around[1]
                ilo0=int((lo0-self.rect[0])/self.darc)
                ila0=int((la0-self.rect[2])/self.darc)
                dist=int(around[2]/30)
                ilo=(max(0,ilo0-dist),min(3601,ilo0+dist))
                ila=(max(0,ila0-dist),min(3601,ila0+dist))
        elif around is None and rect is None: return False
        return (self.Lon[ilo[0]:ilo[1]+1,ila[0]:ila[1]+1],self.Lat[ilo[0]:ilo[1]+1,ila[0]:ila[1]+1],self.im[ilo[0]:ilo[1]+1,ila[0]:ila[1]+1])
                
                