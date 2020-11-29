import pandas as pd
import csv

realitky=pd.read_csv("in/tables/sreality_clean.csv",encoding="utf-8", low_memory=False)
zsjd=pd.read_csv("in/tables/zsj_d_dwh.csv",encoding="utf-8", low_memory=False)
obce=pd.read_csv("in/tables/cast_obce_dwh.csv",encoding="utf-8", low_memory=False)
prodej_prumer=pd.read_csv("in/tables/prodej_prumer.csv",encoding="utf-8", low_memory=False)
pronajem_prumer=pd.read_csv("in/tables/pronajem_prumer.csv",encoding="utf-8", low_memory=False)

#odstraneni vsech null hodnot
realitky.dropna(subset = ['price'],inplace=True)

#změna datového typu u ceny
realitky['price'] = realitky['price'].astype(int)

#osekani sloupcu zdrojovych tabulek
zsjd_kod= zsjd.loc[:, ["kod_zsj_d","kod_cast_obec"]]
obce_kod=obce.loc[:, ["kod_cast_obec","upper_name"]]

#inner join realitek kodu zsjd
realitky_zsjd=pd.merge(realitky,zsjd_kod,on='kod_zsj_d')
#realitky_zsjd.to_csv("realitky_zsjd.csv")

#inner join s obcemi
realitky_uj=pd.merge(realitky_zsjd,obce_kod,on='kod_cast_obec' )

#realitky_uj.to_csv("realitky_uj.csv")

#změna datového typu
realitky_uj['kod_zsj_d'] = realitky_uj['kod_zsj_d'].astype(str)
#doplnění nul do 7 míst
realitky_uj['kod_zsj_d'] = realitky_uj['kod_zsj_d'].apply(lambda x: x.zfill(7))


#vyfiltrujeme pouze Prahu
realitky_praha = realitky_uj[realitky_uj.apply(lambda row: row['upper_name'].lower() == 'praha', axis=1)]

realitky_praha.index.names=['id']


realitky_praha.to_csv("out/tables/realitky_praha.csv")
#realitky_praha.info()

#-----------------------------------------------------------------------------------------
#změna datového typu u ceny
prodej_prumer['price'] = prodej_prumer['price'].astype(int)

#inner join prodeje kodu zsjd
prodej_prumer_zsjd=pd.merge(prodej_prumer,zsjd_kod,on='kod_zsj_d')


#inner join s obcemi
prodej_prumer_zsjd_uj=pd.merge(prodej_prumer_zsjd,obce_kod,on='kod_cast_obec' )


#změna datového typu
prodej_prumer_zsjd_uj['kod_zsj_d'] = prodej_prumer_zsjd_uj['kod_zsj_d'].astype(str)
#doplnění nul do 7 míst
prodej_prumer_zsjd_uj['kod_zsj_d'] = prodej_prumer_zsjd_uj['kod_zsj_d'].apply(lambda x: x.zfill(7))


#vyfiltrujeme pouze Prahu
prodej_prumer_praha = prodej_prumer_zsjd_uj[prodej_prumer_zsjd_uj.apply(lambda row: row['upper_name'].lower() == 'praha', axis=1)]

prodej_prumer_praha.index.names=['id']

prodej_prumer_praha.to_csv("out/tables/prodej_prumer_praha.csv")

#prodej_prumer_praha.info()
#----------------------------------------------------------------------------------------------
#změna datového typu u ceny
pronajem_prumer['price'] = pronajem_prumer['price'].astype(int)

#inner join pronajmu kodu zsjd
pronajem_prumer_zsjd=pd.merge(pronajem_prumer,zsjd_kod,on='kod_zsj_d')


#inner join s obcemi
pronajem_prumer_zsjd_uj=pd.merge(pronajem_prumer_zsjd,obce_kod,on='kod_cast_obec' )


#změna datového typu
pronajem_prumer_zsjd_uj['kod_zsj_d'] = pronajem_prumer_zsjd_uj['kod_zsj_d'].astype(str)
#doplnění nul do 7 míst
pronajem_prumer_zsjd_uj['kod_zsj_d'] = pronajem_prumer_zsjd_uj['kod_zsj_d'].apply(lambda x: x.zfill(7))


#vyfiltrujeme pouze Prahu
pronajem_prumer_zsjd_uj_praha = pronajem_prumer_zsjd_uj[pronajem_prumer_zsjd_uj.apply(lambda row: row['upper_name'].lower() == 'praha', axis=1)]

pronajem_prumer_zsjd_uj_praha.index.names=['id']

pronajem_prumer_zsjd_uj_praha.to_csv("out/tables/pronajem_prumer_praha.csv")
#pronajem_prumer_zsjd_uj_praha.info()

