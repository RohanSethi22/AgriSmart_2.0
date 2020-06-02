
import pandas as pd
import numpy as np

df=pd.read_csv("district_climate.csv")

df2=pd.read_csv("crop_prediction_datasets.csv")

#districts=list(set([ district for district in df['District_Name'] ]))
clim_dict={}

for i in range(len(df['District'])):
	print(str(i),df['District'][i],df['Climate'][i])
	clim_dict[df['District'][i]]=df['Climate'][i]

clim_list=[clim_dict[district] for district in df2['District_Name'] ]

print(df2.head)

df2['Climate']=clim_list

print(df2.head)

df2.to_csv('complete_dataset.csv',index=False)

'''
url = 'http://api.openweathermap.org/data/2.5/weather?q={}&APPID=406e0137603a69be44bee1e86b44881d&units=metric'.format(districts[0])
response=requests.get(url)
data=response.json()

print(data)

if data['cod']=='404':
	print("Couldn't fetch data.")
'''

