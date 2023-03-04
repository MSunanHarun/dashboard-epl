import pandas as pd
import numpy as np

def pilihmusim(s,dataset):
    data=dataset[dataset["Season"]==s]
    data.sort_values(by=["Poin"],inplace=True,ascending=False)
    data.index=[i for i in range(len(data["Rank"]))]
    data=data.drop(["Unnamed: 0","Season","Id"],axis=1)
    return data

def golterbanyak(dataset):
    data=dataset.copy()
    data.sort_values(by=["GoalScored"],inplace=True,ascending=False)
    data.index=[i for i in range(len(data["Rank"]))]
    return {"Klub":data.iloc[:1,:]["Klub"][0],"JumlahGol":data.iloc[:1,:]["GoalScored"][0]}

def kebobolanterbanyak(dataset):
    data=dataset.copy()
    data.sort_values(by=["GoalConceeded"],inplace=True,ascending=False)
    data.index=[i for i in range(len(data["Rank"]))]
    return {"Klub":data.iloc[:1,:]["Klub"][0],"JumlahKebobolan":data.iloc[:1,:]["GoalConceeded"][0]}

def kemenanganterbanyak(dataset):
    data=dataset.copy()
    data.sort_values(by=["Win"],inplace=True,ascending=False)
    data.index=[i for i in range(len(data["Rank"]))]
    return {"Klub":data.iloc[:1,:]["Klub"][0],"JumlahKemenangan":data.iloc[:1,:]["Win"][0]}

def kekalahanterbanyak(dataset):
    data=dataset.copy()
    data.sort_values(by=["Loss"],inplace=True,ascending=False)
    data.index=[i for i in range(len(data["Rank"]))]
    return {"Klub":data.iloc[:1,:]["Klub"][0],"JumlahKekalahan":data.iloc[:1,:]["Loss"][0]}

def pilihklub(c,dataset):
    s=dataset["Season"].unique()
    data=dataset[dataset["Klub"]==c]
    data=data.drop(["Unnamed: 0","Id"],axis=1)
    data_season=np.array(data["Season"])
    for i in s:
        if i not in data_season:
            data=data.append({
                "Season":i,"Rank":0,
                "Klub":c,"Poin":0,
                "GoalScored":0,"GoalConceeded":0,
                "Win":0,"Loss":0,"Draw":0,
                "GoalDegrees":0,"WinPercentage":0,"Keterangan":"Tidak Bermain Di EPL"
            },ignore_index=True)
    data.sort_values(by=["Season"],inplace=True)
    data.index=[i for i in range(len(data["Season"]))]
    return data

def cekfloat(dataset):
    kolom=dataset.columns
    for i in kolom:
        if type(dataset[i][0])!=str and type(dataset[i][0])!=int:
            dataset[i]=dataset[i].astype(int)
    return dataset

def golpermusim(dataset):
    data=dataset.copy()
    return data.groupby("Season").sum()



