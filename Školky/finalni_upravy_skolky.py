import pandas as pd 
skolky=pd.read_csv("skolky_praha.csv", low_memory=False)
skolky.info()

#odstraneni mezer ve sloupci s odkazem na webovky
skolky['stranky_skoly'] = skolky['stranky_skoly'].str.strip()

#unikatni hodnoty adresa a nazvy (pouze pocet, kontrola duplikatu)
adresy = skolky.adresa.nunique()
nazvy = skolky.nazev.nunique()
print(adresy)
print(nazvy)

#ocisteni nepotrebnych sloupcu
ciste_skolky=skolky.drop(['kod_cast_obec', 'upper_name'], axis=1)


#změna datového typu
ciste_skolky['kod_zsj_d'] = ciste_skolky['kod_zsj_d'].astype(str)
#doplnění nul do 7 míst
ciste_skolky['kod_zsj_d'] = ciste_skolky['kod_zsj_d'].apply(lambda x: x.zfill(7))

#prejmenovani sloupce s indexem
ciste_skolky.index.names=['id']

ciste_skolky.info()

ciste_skolky.to_csv("skolky.csv")
