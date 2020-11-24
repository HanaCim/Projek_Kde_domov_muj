import pandas as pd

souradnice = pd.read_csv("geometry.csv", encoding="utf-8", low_memory=False)

#vytvoření dataframe s lat a lng
souradnice['new_col'] = range(1, len(souradnice) + 1)
lat = souradnice.loc[souradnice["data"] > 40]
lng = souradnice.loc[souradnice["data"] < 20]
lat.rename(columns={'data': 'lat'}, inplace = True)
lng.rename(columns={'data': 'lng'}, inplace = True)

#merge dataframe zastavek s lat a lng podle 'json_parentid')
hriste = pd.read_csv("playgrounds.csv", encoding="utf-8", low_memory=False)
hriste_slat = pd.merge(hriste, lat, on='JSON_parentId')
hriste_latlng = pd.merge(hriste_slat, lng, on='JSON_parentId')

hriste_final = hriste_latlng[["lat","lng","properties_url"]]
print(hriste_final)

hriste_final.to_csv("hriste_final.csv")