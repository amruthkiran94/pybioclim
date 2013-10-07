from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
from config import ul, lr
from get_data import get_dataset


def draw_map(file, map=None, show=True):
    '''Use Matplotlib's basemap to generate a map of a given BIOCLIM data 
    file.

    You can supply a Basemap object (in any projection) as the optional 
    keyword argument "map." If none is provided, the default Miller 
    projection will be used.'''

    data = get_dataset(file)
    lats = np.linspace(ul[0], lr[0], data.RasterYSize, endpoint=False)
    lons = np.linspace(ul[1], lr[1], data.RasterXSize, endpoint=False)

    values = data.ReadAsArray()    
    values = np.ma.masked_where(values==-9999, values)

    plt.figure()
    plt.title(file)
    if map is None: map = Basemap(projection='mill',lon_0=0)
    map.drawcoastlines(linewidth=1)
    map.drawcountries(linewidth=1)
    map.drawstates(linewidth=0.5)

    x, y = np.meshgrid(lons, lats)
    data = np.zeros(x.shape)
            
    map.pcolormesh(x, y, data=values, latlon=True, cmap=plt.cm.OrRd)
    cbar = plt.colorbar()
    
    if show: plt.show()