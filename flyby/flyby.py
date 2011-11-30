'''
Created on 29/nov/2011

@author: gionata
'''
from mayavi import  mlab
import pyproj
from tiffDb.tiffDb import tiffDb
from TiffReader.TiffReader import TiffReader
import numpy
#self.proj=pyproj.Proj('+proj=stere +lon_0=%4.1f%s +lat_ts=%4.1fn +lat_0=%4.1f +ellps=WGS84' % (abs(lon0),s,lat0,lat0))
class flyby(object):
    '''
    classdocs
    '''

    def __init__(self,start,end,maxd=5000.,n=100):
        '''
        Constructor
        '''
        self.start=start
        self.end=end
        self.lopath=numpy.linspace(start[0], end[0], n)
        self.lapath=numpy.linspace(start[1], end[1], n)
        self.set_proj()
        self.tile=TiffReader(lon=self.lopath[0],lat=self.lapath[0])
        self.tile.readit()
        for i in range(n):
                if not self.tile==TiffReader(lon=self.lopath[i],lat=self.lapath[i]):
                        self.tile=TiffReader(lon=self.lopath[i],lat=self.lapath[i])
                        self.tile.readit()
                if not hasattr(self,'mesh'):
                        lo,la,z=self.tile.subset(rect=None, around=(self.lopath[i],self.lapath[i],maxd))
                        x,y=self.proj(lo,la)
                        x=x-x.mean()
                        y=y-y.mean()
                        self.mesh=mlab.mesh(x,y,z,scalars=z,vmax=1500.,vmin=0.)
                        mlab.view(180.,45.,maxd,numpy.array([x.max(),0,z.max()]))
                else:
                        lo,la,self.mesh.mlab_source.z=self.tile.subset(rect=None, around=(self.lopath[i],self.lapath[i],maxd))
                        self.mesh.mlab_source.scalars=self.mesh.mlab_source.z
                        mlab.view(180.,45.,5*x.max(),numpy.array([x.max(),0,self.mesh.mlab_source.z.max()]))
                mlab.draw()
                
    def set_proj(self):
        self.proj=pyproj.Proj('+proj=stere +lon_0=%4.1f +lat_ts=%4.1fn +lat_0=%4.1f +ellps=WGS84' % (self.start[0],self.start[1],self.start[1]))