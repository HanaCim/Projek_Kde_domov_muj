import pandas as pd

#načtení souborů s datovými typy u potřebných sloupců
zastavky=pd.read_csv("zastavky_sregiony.csv",encoding="utf-8", low_memory=False, dtype= {'kod_zsj_d': str})
zsjd=pd.read_csv("zsj_d_dwh.csv",encoding="utf-8", low_memory=False, dtype= {'kod_zsj_d': str,'kod_cast_obec': str })
obce=pd.read_csv("cast_obec_dwh.csv",encoding="utf-8", low_memory=False, dtype= {'kod_cast_obec': str})

#osekani sloupcu zdrojovych tabulek
zsjd_kod= zsjd.loc[:, ["kod_zsj_d","kod_cast_obec"]]
obce_kod=obce.loc[:, ["kod_cast_obec","upper_name"]]

#inner join podle kodu zsjd
zastavky_zsjd=pd.merge(zastavky,zsjd_kod,on='kod_zsj_d')


#inner join s obcemi
zastavky_uj=pd.merge(zastavky_zsjd,obce_kod,on='kod_cast_obec' )

#vyfiltrujeme pouze Prahu
zastavky_praha = zastavky_uj[zastavky_uj.apply(lambda row: row['upper_name'].lower() == 'praha', axis=1)]

print(zastavky_praha)
zastavky_praha.to_csv("zastavky_praha.csv")
