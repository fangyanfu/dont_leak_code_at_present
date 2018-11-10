# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 12:06:28 2018

@author: Irina
"""

training = pd.read_csv('training.csv', encoding='cp1252')
training.head()

test = pd.read_csv('test.csv',encoding='cp1252')
test.head()




# Data Clearance training dataset
training.drop(['BESTELL_ID','OBS_ID','WGH1_ID','WGH3_ID','WGH4_ID','DIVISION_DESC_SORT','WGH4_DESC'],axis=1,inplace=True)
test.drop(['BESTELL_ID','OBS_ID','WGH1_ID','WGH3_ID','WGH4_ID','DIVISION_DESC_SORT','WGH4_DESC'],axis=1,inplace=True)

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
training['WGH3_DESC'].replace('WGH-Stufe Marken National',0,inplace=True)


#dummies colours
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

# AMOUNT TOTAL
training['TOTAL_AMOUNT']=training['MENGE_ECOM']+training['MENGE_CALL']


info = training.info()
description = training.describe()