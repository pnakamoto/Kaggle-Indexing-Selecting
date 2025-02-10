import pandas as pd

reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)
pd.set_option("display.max_rows", 5)

from learntools.core import binder; binder.bind(globals())
from learntools.pandas.indexing_selecting_and_assigning import *
print("Setup complete.")

reviews.head()

country	description	designation	points	price	province	region_1	region_2	taster_name	taster_twitter_handle	title	variety	winery
0	Italy	Aromas include tropical fruit, broom, brimston...	Vulkà Bianco	87	NaN	Sicily & Sardinia	Etna	NaN	Kerin O’Keefe	@kerinokeefe	Nicosia 2013 Vulkà Bianco (Etna)	White Blend	Nicosia
1	Portugal	This is ripe and fruity, a wine that is smooth...	Avidagos	87	15.0	Douro	NaN	NaN	Roger Voss	@vossroger	Quinta dos Avidagos 2011 Avidagos Red (Douro)	Portuguese Red	Quinta dos Avidagos
2	US	Tart and snappy, the flavors of lime flesh and...	NaN	87	14.0	Oregon	Willamette Valley	Willamette Valley	Paul Gregutt	@paulgwine	Rainstorm 2013 Pinot Gris (Willamette Valley)	Pinot Gris	Rainstorm
3	US	Pineapple rind, lemon pith and orange blossom ...	Reserve Late Harvest	87	13.0	Michigan	Lake Michigan Shore	NaN	Alexander Peartree	NaN	St. Julian 2013 Reserve Late Harvest Riesling ...	Riesling	St. Julian
4	US	Much like the regular bottling from 2012, this...	Vintner's Reserve Wild Child Block	87	65.0	Oregon	Willamette Valley	Willamette Valley	Paul Gregutt	@paulgwine	Sweet Cheeks 2012 Vintner's Reserve Wild Child...	Pinot Noir	Sweet Cheek

# Your code here
desc = reviews.description

# Check your answer
q1.check()

first_description = reviews.description.iloc[0]

# Check your answer
q2.check()
first_description

first_row = reviews.iloc[0]

# Check your answer
q3.check()
first_row

country                                                    Italy
description    Aromas include tropical fruit, broom, brimston...
                                     ...                        
variety                                              White Blend
winery                                                   Nicosia
Name: 0, Length: 13, dtype: object

first_descriptions = reviews.description.iloc[:10]

# Check your answer
q4.check()
first_descriptions

0    Aromas include tropical fruit, broom, brimston...
1    This is ripe and fruity, a wine that is smooth...
                           ...                        
8    Savory dried thyme notes accent sunnier flavor...
9    This has great depth of flavor with its fresh ...
Name: description, Length: 10, dtype: object

indices = [1, 2, 3, 5, 8]
sample_reviews = reviews.loc[indices]

# Check your answer
q5.check()
sample_reviews

	country	description	designation	points	price	province	region_1	region_2	taster_name	taster_twitter_handle	title	variety	winery
1	Portugal	This is ripe and fruity, a wine that is smooth...	Avidagos	87	15.0	Douro	NaN	NaN	Roger Voss	@vossroger	Quinta dos Avidagos 2011 Avidagos Red (Douro)	Portuguese Red	Quinta dos Avidagos
2	US	Tart and snappy, the flavors of lime flesh and...	NaN	87	14.0	Oregon	Willamette Valley	Willamette Valley	Paul Gregutt	@paulgwine	Rainstorm 2013 Pinot Gris (Willamette Valley)	Pinot Gris	Rainstorm
3	US	Pineapple rind, lemon pith and orange blossom ...	Reserve Late Harvest	87	13.0	Michigan	Lake Michigan Shore	NaN	Alexander Peartree	NaN	St. Julian 2013 Reserve Late Harvest Riesling ...	Riesling	St. Julian
5	Spain	Blackberry and raspberry aromas show a typical...	Ars In Vitro	87	15.0	Northern Spain	Navarra	NaN	Michael Schachner	@wineschach	Tandem 2011 Ars In Vitro Tempranillo-Merlot (N...	Tempranillo-Merlot	Tandem
8	Germany	Savory dried thyme notes accent sunnier flavor...	Shine	87	12.0	Rheinhessen	NaN	NaN	Anna Lee C. Iijima	NaN	Heinz Eifel 2013 Shine Gewürztraminer (Rheinhe...	Gewürztraminer	Heinz Eifel

cols = ['country', 'province', 'region_1', 'region_2']
lines = [0, 1, 10, 100]
df = reviews.loc[lines, cols]
# Check your answer
q6.check()
df

  	country	province	region_1	region_2
0	Italy	Sicily & Sardinia	Etna	NaN
1	Portugal	Douro	NaN	NaN
10	US	California	Napa Valley	Napa
100	US	New York	Finger Lakes	Finger Lakes

cols = ['country', 'variety']

df = reviews.loc[0:99, cols]

# cols_idx = [0, 11]
# df = reviews.iloc[:100, cols_idx]

# Check your answer
q7.check()
df

	country	variety
0	Italy	White Blend
1	Portugal	Portuguese Red
...	...	...
98	Italy	Sangiovese
99	US	Bordeaux-style Red Blend
100 rows × 2 columns

italian_wines = reviews[reviews.country == 'Italy']

# Check your answer
q8.check()
                                                                                                                                                                                         
top_oceania_wines = reviews.loc[
    (reviews.country.isin(['Australia', 'New Zealand']))
    & (reviews.points >= 95)
]

# Check your answer
q9.check()
top_oceania_wines

	country	description	designation	points	price	province	region_1	region_2	taster_name	taster_twitter_handle	title	variety	winery
345	Australia	This wine contains some material over 100 year...	Rare	100	350.0	Victoria	Rutherglen	NaN	Joe Czerwinski	@JoeCz	Chambers Rosewood Vineyards NV Rare Muscat (Ru...	Muscat	Chambers Rosewood Vineyards
346	Australia	This deep brown wine smells like a damp, mossy...	Rare	98	350.0	Victoria	Rutherglen	NaN	Joe Czerwinski	@JoeCz	Chambers Rosewood Vineyards NV Rare Muscadelle...	Muscadelle	Chambers Rosewood Vineyards
...	...	...	...	...	...	...	...	...	...	...	...	...	...
122507	New Zealand	This blend of Cabernet Sauvignon (62.5%), Merl...	SQM Gimblett Gravels Cabernets/Merlot	95	79.0	Hawke's Bay	NaN	NaN	Joe Czerwinski	@JoeCz	Squawking Magpie 2014 SQM Gimblett Gravels Cab...	Bordeaux-style Red Blend	Squawking Magpie
122939	Australia	Full-bodied and plush yet vibrant and imbued w...	The Factor	98	125.0	South Australia	Barossa Valley	NaN	Joe Czerwinski	@JoeCz	Torbreck 2013 The Factor Shiraz (Barossa Valley)	Shiraz	Torbreck

                                                                                                                                                                                         
