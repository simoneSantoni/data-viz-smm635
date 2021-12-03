# %% import libraries
from collections import Counter
import pandas as pd
import geopandas as gp
from geopy.geocoders import Nominatim
import statsmodels.api as sm
import statsmodels.formula.api as smf
import contextily as cx
import seaborn as sns

# %% read data
employer_data = (
    "https://data.london.gov.uk/download/gender-pay-gaps/"
    "42ab9dc1-08f5-4536-927d-ad4bfa59660a/"
    "pay-gaps-london-employers.csv"
)
df = pd.read_csv(employer_data, skiprows=1)
df.set_index("EmployerName", inplace=True)

# %% geolocating companies
# pass a custom user agent
geolocator = Nominatim(user_agent="my_user_agent")
# get locations
# --+ to iterate
employers = df.index
adresses = df.loc[:, "Address"].to_list()
# --+ my data
coords = {}
# --+ ... and loop
for i, j in zip(employers, adresses):
    clean_str = j.replace("\n|\t", " ").replace("  ", " ")
    try:
        location = geolocator.geocode(clean_str)
        if (location.latitude is not None) & (location.longitude is not None):
            coords[i] = {
                "Lat": location.latitude,
                "Long": location.longitude,
            }
        else:
            pass
    except:
        print("Not finding a match!?")

# %% does gender pay gap change across industries?
# create covariates by manipulating SIC codes
# --+ remove obs with null values
df = df.loc[df["SicCodes"].notnull()]
# --+ 2 digit SIC codes
df.loc[:, "SicCodes_twod"] = df["SicCodes"].str[0:2]
# --+ business diversification
df.loc[:, "divers"] = [Counter(item)[","] + 1 for item in df.loc[:, "SicCodes"]]

# %% OLS estimation
# does gender pay gap change across industries and companies?
model1 = "DiffMeanHourlyPercent ~ C(SicCodes_twod)"
res = smf.ols(formula=model1, data=df).fit()
print(res.summary())
model2 = "DiffMeanHourlyPercent ~ C(divers) + C(EmployerSize) + C(SicCodes_twod)"
res = smf.ols(formula=model2, data=df.loc[df["EmployerSize"] != "Not Provided"]).fit()
print(res.summary())

# %% does gender pay gap change across different areas of the city?
# get a geopandas df
# --+ a bit of data wrangling
df = pd.merge(
    df, pd.DataFrame(coords).T, left_index=True, right_index=True, how="inner"
)
# --+ and there we go
gdf = gp.GeoDataFrame(df, geometry=gp.points_from_xy(df.Long, df.Lat))
# --+ check the coordinate reference systemm
gdf.crs

# %% visualization
"""
Contextily helper function
==========================

We define a small helper function that uses
`contextily <https://github.com/darribas/contextily>`__ to add a map
as background to an existing plot: 
"""


def add_basemap(ax, zoom):
    xmin, xmax, ymin, ymax = ax.axis()
    basemap, extent = cx.bounds2img(xmin, ymin, xmax, ymax, zoom=zoom)
    ax.imshow(basemap, extent=extent, interpolation="bilinear")
    # restore original x/y limits
    ax.axis((xmin, xmax, ymin, ymax))


# %%
gdf_wm = gdf.set_crs(epsg=3857)

# %%
ax = gdf_wm.plot(color="red", figsize=(9, 9))
cx.add_basemap(ax, zoom=10)

# %%
from contextily import Place
madrid = Place("London")
ax = madrid.plot()

# %%
