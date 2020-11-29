import pandas as pd
import csv
#nacteni zrdojove tabulky
realitky=pd.read_csv("in/tables/sreality_input_area_mapper.csv",encoding="utf-8")


#změna datového typu
realitky['kod_zsj_d'] = realitky['kod_zsj_d'].astype(str)
#doplnění nul do 7 míst
realitky['kod_zsj_d'] = realitky['kod_zsj_d'].apply(lambda x: x.zfill(7))

#print(realitky)

#odstraneni null hodnot
realitky.dropna(subset = ['price'],inplace=True)

#vyfiltrovani pouze bytu
byty=realitky[realitky["type"].str.contains("apartment", na=False, case=False)]


byty.to_csv("out/tables/sreality_clean.csv", index=False)


#dataframe pro prodej bytu
prodej_bytu =  realitky[
    realitky["type"].str.contains("apartment", na=False, case=False)
    & realitky["offer_type"].str.contains("sale", na=False, case=False)
]

#dataframe pro pronajem bytu
pronajem_bytu = realitky[
    realitky["type"].str.contains("apartment", na=False, case=False)
    & realitky["offer_type"].str.contains("rent", na=False, case=False)
]

#nastaveni limitu pro zobrazovani inzeratu prodeje
limit_prodej=prodej_bytu[(prodej_bytu['price']>=1000000)&(prodej_bytu['price']!=0)]
# print(limit_prodej)


#nastaveni limitu pro zobrazovani inzeratu pronajmu
limit_pronajem=pronajem_bytu[(pronajem_bytu['price']>=3500) & (pronajem_bytu['price']<=500000)&(pronajem_bytu['price']!=0)]
# print(limit_pronajem)

#df na prumernou cenu prodeje
prodej_prumer = limit_prodej.loc[:, [ "local_unique_id", "price", "living_area","kod_zsj_d","lat","lng"]]
prodej_prumer["prumer"] = prodej_prumer.price / prodej_prumer.living_area
# print(prodej_prumer )

#změna datového typu
prodej_prumer['kod_zsj_d'] = prodej_prumer['kod_zsj_d'].astype(str)
#doplnění nul do 7 míst
prodej_prumer['kod_zsj_d'] = prodej_prumer['kod_zsj_d'].apply(lambda x: x.zfill(7))

prodej_prumer.to_csv("out/tables/prodej_prumer.csv", index=False)

#df na prumernou cenu prnonajmu
pronajem_prumer = limit_pronajem.loc[:, [ "local_unique_id", "price", "living_area","kod_zsj_d","lat","lng"]]
pronajem_prumer["prumer"] = pronajem_prumer.price / pronajem_prumer.living_area

#změna datového typu
pronajem_prumer['kod_zsj_d'] = pronajem_prumer['kod_zsj_d'].astype(str)
#doplnění nul do 7 míst
pronajem_prumer['kod_zsj_d'] = pronajem_prumer['kod_zsj_d'].apply(lambda x: x.zfill(7))

#nastaveni limitu pro prumerny pronajem
limit_pronajem=pronajem_prumer[pronajem_prumer["prumer"]<=2500]
#print(limit_pronajem)

limit_pronajem.to_csv("out/tables/pronajem_prumer.csv", index=False)
