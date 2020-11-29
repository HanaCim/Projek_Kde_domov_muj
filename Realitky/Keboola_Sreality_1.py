#importovani zdrojove tabulky
import pandas as pd
import csv
tabulka_cela=pd.read_csv("in/tables/dataset-items.csv",index_col="data_localUniqueId",encoding="utf-8", low_memory=False)

#vyberu pouze sloupce co potrebuje pro dalsi ucely
tabulka_export= tabulka_cela.loc[:, ["data_address","data_countryCode", "data_gpsCoord_lat", "data_gpsCoord_lon","data_livingArea", "data_price", "data_title", "data_type", "data_offerType", "data_url"]]

# prejmenuju si headery vsech sloupcu
tabulka_export.rename(columns={"data_address":"address","data_countryCode":"Country", "data_gpsCoord_lat":"lat", "data_gpsCoord_lon":"lng","data_livingArea":"living_area", "data_price":"price", "data_title":"title", "data_type":"type", "data_offerType":"offer_type","data_url":"url"}, inplace=True)

#odstraneni duplikatu na zaklade kombinace address-livingarea-price
bez_duplikatu=tabulka_export.drop_duplicates(subset=['address','living_area', 'price'])

#prejmenovani indexoveho sloupce
bez_duplikatu.index.names=['local_unique_id']
                          
bez_duplikatu.to_csv("out/tables/realitky_input.csv")