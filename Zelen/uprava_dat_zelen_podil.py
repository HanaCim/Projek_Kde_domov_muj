import pandas as pd

podily = pd.read_csv(r"C:\Digitalni_akademie\projekt\data_openstreetmaps\podil.csv", encoding="utf-8", low_memory=False)
admin = pd.read_csv(r"C:\Digitalni_akademie\CleverMaps\g7s7vtet7ottgbnv\2020-11-20_23-39-14\data\cast_obec_dwh.csv", encoding="utf-8", low_memory=False, dtype= {'kod_cast_obec': str})
slouceny = pd.merge(admin, podily, on='nazev')
zelen_podily = slouceny[['kod_cast_obec',"nazev","podil","upper_name"]]
print(zelen_podily)
zelen_podily.drop(zelen_podily[zelen_podily['upper_name'] != 'Praha'].index, inplace = True) 
print(zelen_podily)
zelen_podily.to_csv('zelen_podil.csv')