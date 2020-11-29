import pandas as pd 

#nacteni zdrojovych souboru
skolky=pd.read_csv("skolky_regiony.csv",encoding="utf-8", low_memory=False)
zsjd=pd.read_csv("zsj_d_dwh.csv",encoding="utf-8", low_memory=False)
obce=pd.read_csv("cast_obec_dwh.csv",encoding="utf-8", low_memory=False)

#osekani sloupcu zdrojovych tabulek
zsjd_kod= zsjd.loc[:, ["kod_zsj_d","kod_cast_obec"]]
obce_kod=obce.loc[:, ["kod_cast_obec","upper_name"]]

#inner join skolek a kodu zsjd
skolky_zsjd=pd.merge(skolky,zsjd_kod,on='kod_zsj_d')


#inner join s obcemi
skolky_uj=pd.merge(skolky_zsjd,obce_kod,on='kod_cast_obec' )


#vyfiltrujeme pouze Prahu
skolky_praha = skolky_uj[skolky_uj.apply(lambda row: row['upper_name'].lower() == 'praha', axis=1)]

#změna datového typu
skolky_praha['kod_zsj_d'] = skolky_praha['kod_zsj_d'].astype(str)

#doplnění nul do 7 míst
skolky_praha['kod_zsj_d'] = skolky_praha['kod_zsj_d'].apply(lambda x: x.zfill(7))

#prejmenovani sloupcu mala pismena
skolky_praha.rename(columns={"Nazev":"nazev","Typ_skoly":"typ školy","Adresa":"adresa","Stranky_skoly":"stranky_skoly"}, inplace=True)

skolky_praha.to_csv("skolky_praha.csv",index=False)
skolky_praha.info()