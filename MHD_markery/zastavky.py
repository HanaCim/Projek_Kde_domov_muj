import pandas as pd

data = pd.read_csv("zastavky_open.csv", encoding="utf-8", low_memory=False, index_col=5)

#výběr potřebných sloupců
zastavky = data[['latitude',"longitude","highway","name","railway","station"]]

#doplnění kategorií do jednoho sloupce
zastavky.railway.fillna(zastavky.station, inplace=True)
zastavky.highway.fillna(zastavky.railway, inplace=True)
del zastavky['station']
del zastavky['railway']


#přejmenování hodnot
zastavky['highway'] = zastavky['highway'].replace(['bus_stop','tram_stop','subway_entrance','station','elevator'],['autobus','tramvaj','metro','vlak','metro'])

print(zastavky)
#unique = zastavky.highway.unique()
#print(unique)
zastavky.to_csv('zastavky_mark.csv')