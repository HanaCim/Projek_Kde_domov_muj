import pandas as pd 
original=pd.read_csv("ms_2.csv",encoding="utf-8")

#vyfiltrovani sloupcu pomoci loc a prejmenovani pomoci rename
final=original.loc[:,["name","result/1","result/2","result/5"]]
final.rename(columns={"name":"název","result/1":"typ školy","result/2":"adresa","result/5":"stránky školy"}, inplace=True)

#odstraneni duplikatu kombinace nazev a adresa
final.drop_duplicates(subset=['název','adresa'])

final.info()
final.to_csv("ms_input.csv")

#pocet unique values in adresa
unique_address = final.adresa.nunique()
print(unique_address)

#pocet unique values in nazev
unique_nazev = final.název.nunique()
print(unique_nazev)

adresy=final.loc[:,"adresa"]
adresy.to_csv("adresy_ms.csv")

#nacteni souboru s coordinates
coordinates_dirty=pd.read_csv("ms_coordinates.csv", encoding="utf-8")
coordinates_dirty.info()

#ocisteni pouze na sloupce co potrebuju a prejmenovani
coordinates_clean=coordinates_dirty.loc[:,["query","latitude","longitude"]]
coordinates_clean.rename(columns={"query":"adresa","latitude":"lat","longitude":"lng"}, inplace=True)
coordinates_clean.to_csv("ms_coordinates_clean.csv")

#spojeni clean coordinates a puvodniho souboru ms_input.csv
ms_komplet=pd.merge(final,coordinates_clean,on='adresa')

#odstraneni duplikatu zaznamu podle kombinace nazev a adresa
ms_komplet.drop_duplicates(subset=['název','adresa'],keep = False, inplace = True)

#prejmenovani kategorii
ms_komplet.replace(["Obecně","Státní"],["Soukromá","Veřejná"], inplace=True)


ms_komplet.info()

ms_komplet.to_csv("ms_komplet.csv", index=False)

# final.info()

