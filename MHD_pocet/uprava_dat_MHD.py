import pandas as pd

souradnice = pd.read_csv("MHD_souradnice.csv", encoding="utf-8", low_memory=False)

# rozdělení lat a lng do dvou sloupců
souradnice['new_col'] = range(1, len(souradnice) + 1)
lat = souradnice.loc[souradnice["data"] > 40]
lng = souradnice.loc[souradnice["data"] < 20]
lat.rename(columns={'data': 'lat'}, inplace = True)
lng.rename(columns={'data': 'lng'}, inplace = True)

#merge dataframe zastavek s lat a lng podle 'json_parentid')
zastavky = pd.read_csv("MHD_zastavky.csv", encoding="utf-8", low_memory=False)
souradnice['ID'] = range(1, len(souradnice) + 1)
zastavky_slat = pd.merge(zastavky, lat, on='JSON_parentId')
zastavky_latlng = pd.merge(zastavky_slat, lng, on='JSON_parentId')
print(zastavky_latlng)

#vypuštění nepotřebných sloupců a řádků s prázdnými hodnotami
zastavky_final= zastavky_latlng.drop(zastavky_latlng.columns[[0,1,2,3,4,5,6,7,8,10,11,12,13,14,16,18]], axis=1)
bez_nul = zastavky_final.dropna(subset = ['properties_stop_name'])

#vypuštění duplikátů pro potřeby datasetu
bez_duplikatu = bez_nul.drop_duplicates(subset=['properties_stop_name'])
bez_duplikatu.to_csv("zastavky_final.csv")
print(bez_duplikatu)
