'''
Created on 29/nov/2011

@author: gionata
'''
from glob import glob
dir= __file__.split('/')[0]
class tiffDb(object):
    '''
    tiles directory provides a set of tiles wich name specify the origin onf the tif images
    16 bit integers data.
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.files=glob(dir+'/tiles/*/*dem.tif')
        self.set_coordinates()
    
    def set_coordinates(self):
        from numpy import zeros,array
        self.rect=list()
        for f in self.files:
                fil=f.split('/')[-1].split('.')[0].split('_')[1]
                fil=fil.replace('W','_-')
                fil=fil.replace('E','_+')
                fil=fil.replace('N','+')
                fil=fil.replace('S','-')
                lat,lon=fil.split('_')
                lat=float(lat)
                lon=float(lon)
                self.rect.append(array([lon,lon+1.,lat,lat+1.]))
    def file_from_coordinate(self,lon,lat):
        for i in range(len(self.rect)):
                if lon>=self.rect[i][0] and lon<=self.rect[i][1] and lat>=self.rect[i][2] and lat<=self.rect[i][3]:
                   return(self.files[i],self.rect[i])
    