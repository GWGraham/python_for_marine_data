""" Example process workflow to import, tidy, transform, explore, visualise and model a dataset
	Week 1 of MRes Python for Marine Science tutorials

	Deliberately scrappy so we can improve (make more pythonic and refactor) in class!

"""

# imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
import cartopy.crs as ccrs
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
import cartopy.io.img_tiles as cimgt
from geopy.distance import vincenty
import statsmodels.api as sm

# lOAD data
pt=pd.read_csv('data/CPR/14013_buffers_cpr.txt',sep='\t',parse_dates=[1],index_col=1)
tk=pd.read_csv('data/CPR/PR_1215.csv',parse_dates=[7],index_col=7)

# TIDY data
# find row in tk that's before pt start:
tk_s=tk.index[tk.index<=pt.index[0]][-1]
tk_e=tk.index[(tk.index>=pt.index[-1])][0]
tk_sub=tk[(tk.index>=tk_s) & (tk.index<=tk_e)]
# merge
tk_pt=pt.join(tk_sub,how='outer')

# TRANSFORM data
# interpolate tk to match pt
tk_interp=tk_pt.interpolate(method='linear')

# fix up column names
cols=tk_interp.columns
cols_s=[col.strip() for col in cols]
tk_interp.columns=cols_s

# EXPLORE data
# plot map
ax = plt.axes(projection=ccrs.PlateCarree())
#ax.set_extent([-6,0,47,52])
ax.stock_img()
ax.coastlines(resolution='10m',color='black',linewidth=1)
gl = ax.gridlines(draw_labels=True)
gl.xlabels_top = gl.ylabels_right = False
gl.xformatter = LONGITUDE_FORMATTER
gl.yformatter = LATITUDE_FORMATTER
x=tk_interp['LON']
y=tk_interp['LAT']
plt.plot(x,y,'r')
#plt.show()

# plot timeseries
fig1,ax1=plt.subplots(4,1,sharex=True)
tk_interp.plot(kind='line',y='Temperature',ax=ax1[0])
tk_interp.plot(kind='line',y='Salinity',ax=ax1[1])
tk_interp.plot(kind='line',y='Fluoro',ax=ax1[2])
tk_interp.plot(kind='line',y='Light',ax=ax1[3])

# scatter_matrix
fig2=plt.figure()
ax2=fig2.add_subplot(111)
scatter_matrix(pt)

# closer look
fig3=plt.figure()
ax3=fig3.add_subplot(111)
pt.plot.scatter(x='Light',y='Temperature',ax=ax3)

# MODEL
ind=pt['Light']>60
x=sm.add_constant(pt[ind]['Light']) # to capture intercept in model
model = sm.OLS(pt[ind]['Temperature'],x)
results = model.fit()
print(results.summary())
print('Parameters: {}'.format(results.params))
print('{0}: {1}'.format('R2',results.rsquared))

fig4=plt.figure()
ax4=fig4.add_subplot(111)
pt[ind].plot.scatter(x='Light',y='Temperature',ax=ax4)
ax4.plot(pt[ind]['Light'], results.fittedvalues, 'r--.', label="OLS")

# time average to reduce noise and improve linear model
x2=pt[ind].resample('5T').mean()

fig4=plt.figure()
ax4=fig4.add_subplot(111)
x2.plot.scatter(x='Light',y='Temperature',Color='g',ax=ax4)

x=sm.add_constant(x2['Light'])
model = sm.OLS(x2['Temperature'],x)
results = model.fit()
print(results.summary())
print('Parameters: {}'.format(results.params))
print('{0}: {1}'.format('R2',results.rsquared))



