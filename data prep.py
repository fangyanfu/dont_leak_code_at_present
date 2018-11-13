# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 12:25:01 2018

@author: Irina
"""

# import required libraries
import pandas as pd
import numpy as np


training = pd.read_csv('training.csv', encoding='cp1252')
training.head()

test = pd.read_csv('test.csv',encoding='cp1252')
test.head()


# Data Clearance training dataset
training.drop(['BESTELL_ID','OBS_ID','WGH1_ID','WGH3_ID','WGH4_ID','DIVISION_DESC_SORT','WGH4_DESC','BEWERTUNG'],axis=1,inplace=True)
test.drop(['BESTELL_ID','OBS_ID','WGH1_ID','WGH3_ID','WGH4_ID','DIVISION_DESC_SORT','WGH4_DESC','BEWERTUNG'],axis=1,inplace=True)

training['BRAND_ID'].fillna(0,inplace=True)
training['PREIS_DISCOUNT'].fillna(0,inplace=True)

training['NEW_ITEM_FLG'].fillna(0,inplace=True)
training['AIRING_23_FLG'].fillna(0,inplace=True)
training['AIRING_456_FLG'].fillna(0,inplace=True)
training['AIRING_23_FLG'].replace(1,2,inplace=True)
training['AIRING_456_FLG'].replace(1,4,inplace=True)
training['AIRING']=training['NEW_ITEM_FLG']+training['AIRING_23_FLG']+training['AIRING_456_FLG']
training.drop(['NEW_ITEM_FLG','AIRING_23_FLG','AIRING_456_FLG'],axis=1,inplace=True)

training['WGH3_DESC'].replace('WGH-Stufe Eigenmarken',0,inplace=True)
training['WGH3_DESC'].replace('WGH-Stufe Marken National',1,inplace=True)


#DUMMIES FARBE - DUMMIES COLOR GROUPED
training['FARBE'].replace(['SILBERGRAU','GRAU','ANTHRAZIT','GRAU MELANGE','ANTHRAZIT MELANGE','HELLGRAU',
'STEINGRAU','DUNKELGRAU','STONE'],1,inplace=True)
training['FARBE'].replace(['SCHWARZ'],2,inplace=True)
training['FARBE'].replace(['BLAU','GRAUBLAU','JEANSBLAU','DENIMBLAU','TÜRKIS'],3,inplace=True)
training['FARBE'].replace(['LEO'],4,inplace=True)
training['FARBE'].replace(['PINK','DAHLIA','FUCHSIA','MAGENTA','HIMBEERE','FLAMINGO'],5,inplace=True)
training['FARBE'].replace(['GRÜN','OLIV','PETROL','KHAKI','PISTAZIE','SCHILFGRÜN','SEEGRÜN','OLIVE MELANGE','OLIVE'],6,inplace=True)
training['FARBE'].replace(['BEERE','BROMBEERE','PFLAUME','AUBERGINE','LILA','VIOLETT'],7,inplace=True)
training['FARBE'].replace(['BRAUN','ROST','COGNAC','ROST','BRONZE','SCHLAMM'],8,inplace=True)
training['FARBE'].replace(['GOLD'],9,inplace=True)
training['FARBE'].replace(['SILBER','SILBER MELANGE'],10,inplace=True)
training['FARBE'].replace(['DUNKELBLAU','MARINE','NACHTBLAU','INDIGO','SAPHIRBLAU','NAVYBLAU','NAVY'],11,inplace=True)
training['FARBE'].replace(['BORDEAUX','BURGUND','WEINROT','DUNKELROT','KAMIN'],12,inplace=True)
training['FARBE'].replace(['BUNT','HELLBRAUN/GRAU','GOLD/BEIGE','SCHWARZ/WEIß','BLAU/WEIß','ROSÉ/BLAU','ROT/NAVY',
                            'SCHWARZ/GOLD','SCHWARZ/SILBER','HAHNENTRITT','SCHWARZ/CREME'],14,inplace=True)
training['FARBE'].replace(['SAND','ROSENHOLZ','MAUVE','BEIGE','BEIGE MELANGE','CAMEL','NUDE'],14,inplace=True)
training['FARBE'].replace(['MINT'],15,inplace=True)
training['FARBE'].replace(['PUDER','ROSÉ','ALTROSA','ROSA'],16,inplace=True)
training['FARBE'].replace(['CREME','WEIß','WOLLWEIß','OFFWHITE','CHAMPAGNER'],17,inplace=True)
training['FARBE'].replace(['DUNKELBRAUN'],18,inplace=True)
training['FARBE'].replace(['ROT','ROYAL','RUBINROT','PURPUR'],19,inplace=True)
training['FARBE'].replace(['DUNKELGRÜN','FLASCHENGRÜN','SMARAGD'],20,inplace=True)
training['FARBE'].replace(['RAUCHBLAU','HELLBLAU','PASTELLBLAU','EISBLAU'],21,inplace=True)
training['FARBE'].replace(['LACHS','KORALLE','ORANGE','DUNKEL GRAPEFRUIT','TERRACOTTA'],22,inplace=True)
training['FARBE'].replace(['TAUPE','HELLBRAUN'],23,inplace=True)
training['FARBE'].replace(['GELB'],24,inplace=True)


training['PREISKLASSE_DESC']=training['PREISKLASSE_DESC'].str[:2]
training['PREISKLASSE_DESC']=training['PREISKLASSE_DESC'].convert_objects(convert_numeric=True)


# DATE and WEEKDAY
training['SHOW_DATUM']=pd.to_datetime(training['SHOW_DATUM'])
training['DAY_OF_WEEK'] = training['SHOW_DATUM'].dt.day_name()
training["DAY_OF_WEEK"] = training["DAY_OF_WEEK"].astype('category')
training.dtypes
training["DAY_OF_WEEK"] = training["DAY_OF_WEEK"].cat.codes
training.head()



# AMOUNT TOTAL
training['TOTAL_AMOUNT']=training['MENGE_ECOM']+training['MENGE_CALL']

# KANAL - CHANNEL
training["KANAL"] = training["KANAL"].astype('category')
training.dtypes
training["KANAL"] = training["KANAL"].cat.codes
training.head()


# WG_DESC
training["WG_DESC"] = training["WG_DESC"].astype('category')
training.dtypes
training["WG_DESC"] = training["WG_DESC"].cat.codes
training.head()

#WGH1_DESC
training["WGH1_DESC"] = training["WGH1_DESC"].astype('category')
training.dtypes
training["WGH1_DESC"] = training["WGH1_DESC"].cat.codes
training.head()

#GROESSE - SIZE
training["GROESSE"] = training["GROESSE"].astype('category')
training.dtypes
training["GROESSE"] = training["GROESSE"].cat.codes
training.head()


# PREIS LABEL DESC
training["PREIS_LABEL_DESC"] = training["PREIS_LABEL_DESC"].astype('category')
training.dtypes
training["PREIS_LABEL_DESC"] = training["PREIS_LABEL_DESC"].cat.codes
training.head()



#Objects into numeric Values
training['FAKTOR']=training['FAKTOR'].convert_objects(convert_numeric=True)
training['FARBE']=training['FARBE'].convert_objects(convert_numeric=True)
training['TOTAL_AMOUNT']=training['TOTAL_AMOUNT'].convert_objects(convert_numeric=True)
training['PREIS_DISCOUNT']=training['PREIS_DISCOUNT'].convert_objects(convert_numeric=True)
training['WG_DESC']=training['WG_DESC'].convert_objects(convert_numeric=True)


# Info data
info = training.info()
description = training.describe()
