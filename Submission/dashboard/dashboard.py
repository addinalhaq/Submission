import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime

sns.set_theme(style='dark')

st.header("Air Quality Index Analysis")
st.subheader("Changping Station")
df = pd.read_csv("PRSA_Data_Changping_20130301-20170228.csv")
df['datetime'] = pd.to_datetime(df[['year', 'month', 'day', 'hour']],dayfirst=True)
df.set_index('datetime')
df = df.drop(['No','year','month','day','hour'], axis = 1)
df.drop(columns=['wd'],inplace=True)
df.drop(columns=['station'],inplace=True)
col = ['PM2.5', 'PM10', 'SO2', 'NO2',
       'CO', 'O3', 'TEMP', 'PRES', 'DEWP', 'RAIN', 'WSPM']
for i in col:
    df[i] = df[i].fillna(df[i].mean())
Q1 = df[col].quantile(0.25)
Q3 = df[col].quantile(0.75)

IQR = Q3-Q1

mask = (df[col] < (Q1 - 1.5 * IQR)) | (df[col] > (Q3 + 1.5 * IQR))
for i in mask.columns:
    df[i].astype('float')
    temp = df[i].median()
    df.loc[mask[i], i] = temp

st.subheader("Air Quality Index Trends")
st.write("Visualisasi trends 2013-2017 (mean):")
df['datetime']=pd.to_datetime(df['datetime'])
df = df.set_index('datetime')
time = df.groupby(df.index.time).mean()
hourly_ticks = 4 * 60 * 60 * np.arange(6)
time.plot(xticks=hourly_ticks, title = 'Daily Air Quality Trends')
st.line_chart(time, use_container_width=True) 


st.subheader("Korelasi antar parameter udara")
st.write("Visualisasi korelasi metode Pearson:")
sns.set_style("whitegrid")
fig, ax = plt.subplots(figsize=(10, 5))
sns.heatmap(df.corr(),cmap='GnBu',annot=True)
ax.set_title('Pearson Correlation', fontsize=16)
st.pyplot(fig)


st.caption('cc: m312d4ky2007@bangkit.academy')