import pandas as pd

wkt = pd.read_csv("zelen_bound.csv", encoding="utf-8", low_memory=False)
data = pd.read_csv("zelen_wkt.csv", encoding="utf-8", low_memory=False)

#slouceni dataframe
slouceny = pd.merge(wkt, data, on='wkt')
zelen= slouceny[['id_x',"x_min","y_min","x_max","y_max","name","landuse","leisure","natural"]]

#doplnění kategorií do jednoho sloupce
zelen.natural.fillna(zelen.leisure, inplace=True)
zelen.landuse.fillna(zelen.natural, inplace=True)
del zelen['leisure']
del zelen['natural']
#unique = zelen.landuse.unique()

#přejmenování hodnot
zelen['landuse'] = zelen['landuse'].replace(['forest','wood','orchard','village_green','recreation_ground', 'grass','playground'],['les','les','sad','park','park', 'louka','hřiště'])
zelen.landuse.fillna('-',inplace=True)
zelen.name.fillna('-',inplace=True)
print(zelen)

zelen.to_csv('zelen_dwh.csv', index=False)