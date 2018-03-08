# import packages

import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import pandas as pd

# ask for filename, add extension

inputFileName = input ('Enter the filename:\n')
outputFileName = inputFileName + ".csv"

# read in ais data to DataFrame:
ais_df=pd.read_csv(outputFileName,skiprows=1,parse_dates=[0],names=['Timestamp','Source','Speed','','AISLon','AISLat','loglon','loglat','Course'])
ais_df['Timestamp']=pd.to_datetime(ais_df['Timestamp'].str.strip('(UTC)'),yearfirst=True)

logformlons=ais_df.loc[pd.notnull(ais_df['loglon']),'loglon'].values
logformlats=ais_df.loc[pd.notnull(ais_df['loglat']),'loglat'].values

# define maximum and minimum latitudes and longitudes using DataFrame columns and .max() | .min() methods
        
latsupperlimit = ais_df['AISLat'].max()+1
latslowerlimit = ais_df['AISLat'].min()-1
lonsupperlimit = ais_df['AISLon'].max()+1
lonslowerlimit = ais_df['AISLon'].min()-1

# set the projection, resolution and map extent

ax = plt.axes(projection=ccrs.PlateCarree())
ax.set_extent([lonslowerlimit, lonsupperlimit, latslowerlimit, latsupperlimit])
ax.coastlines(resolution='10m', color='black')

# add background map elements

#land_10m = cfeature.NaturalEarthFeature('physical', 'land', '10m', edgecolor='face', facecolor=cfeature.COLORS['land'])
#ax.add_feature(land_10m)

# add features Christina Aguilera September 2002 style

#ax.add_feature(cfeature.LAKES)
#ax.add_feature(cfeature.RIVERS)
#ax.add_feature(cfeature.OCEAN)
#ax.add_feature(cfeature.BORDERS)
#ax.add_feature(cfeature.COASTLINE)

# add features Christina Aguilera November 2002 style

'''url = 'https://map1c.vis.earthdata.nasa.gov/wmts-geo/wmts.cgi'
#layer = 'VIIRS_CityLights_2012'
layer = 'BlueMarble_ShadedRelief_Bathymetry'
ax = plt.axes(projection=ccrs.PlateCarree())
ax.set_extent([lonslowerlimit, lonsupperlimit, latslowerlimit, latsupperlimit])
ax.add_wmts(url, layer)'''

# add gridlines and labels

gl = ax.gridlines(draw_labels=True, color='none', crs=ccrs.PlateCarree())
gl.xlabels_top=False
gl.ylabels_left=False

# plot dataset 1 using DataFrame columns, set line / marker color + size

plt.plot(ais_df['AISLon'], ais_df['AISLat'], color='g', marker='.', linewidth=1, transform=ccrs.PlateCarree())

# plot dataset 2, set line / marker color + size

plt.plot(logformlons, logformlats, color='red', marker='o', linewidth=1, transform=ccrs.PlateCarree())

# add title from filename

title_string = "CPR tow " + inputFileName
plt.title(title_string, y=1.08)

# add legend

log_form_legend = mlines.Line2D([], [], color='r', linewidth=1, marker='o', label='log form')
ais_legend = mlines.Line2D([], [], color='g', linewidth=1, marker='.', label='AIS')
plt.legend(handles=[ais_legend, log_form_legend])

# display the map

plt.show()