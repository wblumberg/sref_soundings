from netCDF4 import Dataset
import numpy as np
from pylab import *

run_hour = '21'
yyyymmdd = '20131204'
sref_data = 'http://nomads.ncep.noaa.gov:9090/dods/sref/sref' + yyyymmdd + '/'
latitude = 35.7
longitude = 197
members = 'sref_memberlist'
time_idx = 0

member_file = open(members, 'r')
#print member_file.readlines()

#hghprs
#
firstrun = 0
lat_idx = 0
lon_idx = 0
pres = None
for line in member_file.readlines():
    membername = line.rstrip()
    dap_link = sref_data + membername + run_hour + 'z'
    print dap_link
    d = Dataset(dap_link)
    #print d.variables.keys()
    if firstrun == 0:
        lat = d.variables['lat'][:]
        lon = d.variables['lon'][:]
        pres = d.variables['lev'][:]
        lat_idx = np.argmin(np.abs(latitude - lat))
        lon_idx = np.argmin(np.abs(longitude - lon))
    height = d.variables['hgtprs'][time_idx, :, lat_idx, lon_idx]
    height = height * 9.81
    temp = d.variables['tmpprs'][time_idx, :, lat_idx, lon_idx]
    plot(temp, height)
    d.close()
show()
