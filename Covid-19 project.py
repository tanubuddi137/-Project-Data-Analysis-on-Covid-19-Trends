from bs4 import BeautifulSoup as soup
from datetime import date,datetime
from urllib.request import  Request,urlopen
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import plotly as pl
import plotly.graph_objects as pg
import plotly.express as px
import plotly.offline as po
import warnings
import gc
warnings.filterwarnings("ignore")
from pandas_profiling import ProfileReport


##Webscraping the data

url = "https://www.worldometers.info/coronavirus/#countries"

req =  Request(url , headers={'User-Agent':"Google Chrome/Version 90.0.4430.85"})

webpage = urlopen(req)
page= soup(webpage,"html.parser")

today= datetime.now()

yesterday= "%s %d ,%d" %(date.today().strftime("%b"),today.day-1,today.year)

table= page.findAll("table",{"id":"main_table_countries_yesterday"})


totallist = table[0].findAll("tr",{"style":""})
title = totallist[0]
del totallist[0]

alldata=[]
clean = True


for country in totallist:
    countrydata=[]
    countrylist= country.findAll("td")

    if countrylist[1].text== "China":
        continue
    for i in range(1,len(countrylist)):
        final=countrylist[i].text
        if clean :
            if i!= 1 and i!=len(countrylist)-1:
                final=final.replace(",","")

                if final.find('+')!= -1:
                    final= final.replace("+","")
                    final=float(final)
                elif final.find("-")!=-1:
                    final=final.replace("-","")
                    final = float(final)*-1
        if final=='N/A':
            final=0
        elif final == ""or final==" ":
            final = -1

        countrydata.append(final)

    alldata.append(countrydata)



df=pd.DataFrame(alldata)

df.drop([15,16,17,18,19,20],inplace=True,axis=1)


coulmn_label=["Country","Total Cases","New Cases","Total Deaths"," New Deaths","Total Recovered","New Recovered",
             "Active Cases","Serious/Critical Cases","TotalCases/1M","Total Deaths/1M","Total Cases/1M","Total Tests","Population","Continent"]

df.columns=coulmn_label
for coulmn_label in df.columns:
    if coulmn_label!='Country' and coulmn_label!='Continent':
        df[coulmn_label]=pd.to_numeric(df[coulmn_label])


df["%Inc Cases"]=df["New Cases"]/df["Total Cases"]*100

df["%Inc Deaths"]=df[" New Deaths"]/df["Total Deaths"]*100

df["%Inc Recovered"]=df["New Recovered"]/df["Total Recovered"]*100

 ###EDA

cases=df[["Total Recovered","Active Cases","Total Deaths"]].loc[0]
cases_df=pd.DataFrame(cases).reset_index()
cases_df.columns=["Type","Total"]
cases_df["Percentage"]=np.round(100*cases_df["Total"]/np.sum(cases_df["Total"]),2)
cases_df["Virus"]=["covid 19" for i in range(len(cases_df))]

chart=px.bar(cases_df,x="Virus",y="Percentage",color="Type",hover_data=["Total"])

#chart.show()

bar=np.round(df[["%Inc Cases","%Inc Deaths","%Inc Recovered"]].loc[0],2)
bar_df=pd.DataFrame(bar)
bar_df.columns=["Percentage"]

fig=pg.Figure()
fig.add_trace(pg.Bar(x=bar_df.index,y=bar_df["Percentage"],marker_color=["Yellow","Red","blue"]))
fig.show()



##Continent wise

continent_df=df.groupby("Continent").sum().drop("All")
#print(continent_df)

continent_df=continent_df.reset_index()

def visualize(v_list):
    for label in v_list:
        con_df=continent_df[["Continent",label]]
        con_df["Percentage"]=np.round(100*con_df[label]/np.sum(con_df[label]),2)
        con_df["Virus"]=["Covid-19" for i in range(len(con_df))]

        fig=px.bar(con_df,x="Virus",y="Percentage",color="Continent",hover_data=[label])
        fig.update_layout(title={"text":f"{label}"})
        fig.show()


case_list=["Total Cases","Active Cases","New Cases","Serious/Critical Cases"]
deaths_list=["Total Deaths","New Deaths"]
Recovered_list=["Total Recovered","New Recovered","Total Tests"]

#visualize(case_list)

##Countries

df=df.drop([len(df)-1])
country_df=df.drop([0])
country=country_df.columns[1:14]

top_df=11
country=country_df.columns[1:14]

fig= pg.Figure()
a=0
for i in country_df.index:
    if a < top_df:
        fig.add_trace(pg.Bar(name=country_df['Country'][i],x=country,y=country_df.loc[i][1:14]))
    else:
        break

    a+=1


fig.update_layout(title={"text":f'top{top_df}countries affected'},yaxis_type="log")
fig.show()


df=df.drop([len(df)-1])
v=df.drop([0])

v_df=v.iloc[::-1]
print(v_df.reset_index())



last_df=11
country=v_df.columns[1:14]

fig= pg.Figure()
l=0
for i in v_df.index:
    if l < last_df:
        fig.add_trace(pg.Bar(name=country_df['Country'][i],x=country,y=v_df.loc[i][1:14]))
    else:
        break

    l+=1


fig.update_layout(title={"text":f'last{last_df}countries affected'},yaxis_type="log")
fig.show()





