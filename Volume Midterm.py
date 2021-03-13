import pandas as pd
import numpy as np
import yfinance as yf
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import seaborn as sns

yesterday = datetime.now()-timedelta(1)
fig = plt.figure()
datestring = datetime.strftime(datetime.now(), "%d/%m/%Y")
fig.suptitle("Volumes Midterm- Indices "+ datestring)
ax1 = fig.add_subplot(2,2,1)
ax2= fig.add_subplot(2,2,2)
ax3= fig.add_subplot(2,2,3)
ax4=fig.add_subplot(2,2,4)
ax1.set_ylabel('Volume', fontsize = 7)
ax1.set_xlabel('GDate', fontsize = 7)
ax2.set_ylabel('Volume', fontsize = 7)
ax2.set_xlabel('GDate', fontsize = 7)
ax3.set_ylabel('Volume', fontsize = 7)
ax3.set_xlabel('GDate', fontsize = 7)
ax4.set_ylabel('Volume', fontsize = 7)
ax4.set_xlabel('GDate', fontsize = 7)

#----------------------------------Chart 1
SP500 = yf.download('^GSPC', start='2020-12-01', end=yesterday)

sns.barplot(data=SP500.loc[:,"Volume"]\
            .resample("B").mean().to_frame()\
            .assign(Date=lambda dfa: dfa.index.strftime("%d/%m")),
            x="Date", y="Volume", ax=ax1,color = "slategray")

# rotate the labels
label1 = ax1.set_xticklabels(ax1.get_xticklabels(), rotation = 90,fontsize=5,alpha=0.5)
ax1.set_title("S&P500", fontsize=7)

#-----------------------------Chart 2

NSDQ = yf.download("^NDX", start='2020-12-01', end=yesterday)
Stats_Vol = NSDQ["Volume"]

sns.barplot(data=NSDQ.loc[:,"Volume"]\
            .resample("B").mean().to_frame()\
            .assign(Date=lambda dfa: dfa.index.strftime("%d/%m")),
            x="Date", y="Volume", ax=ax2,color ="darkmagenta")
#print(SP500["Volume"].rolling(250).mean().plot())
# rotate the labels
label2 = ax2.set_xticklabels(ax2.get_xticklabels(), rotation = 90,fontsize=5,alpha=0.5)
ax2.set_title("NASDAQ", fontsize=7)
#------------------------------Chart 3
ETH = pd.DataFrame(data=yf.download("ETH-EUR", start='2020-12-01', end=yesterday))

BTC = pd.DataFrame(data=yf.download("BTC-EUR", start='2020-12-01', end=yesterday))


ETH2=pd.DataFrame(ETH.loc[:,"Volume"].resample("B").mean().to_frame().assign(Date=lambda dfa: dfa.index.strftime("%d/%m")))
Date = ETH2["Date"]
ETH2.drop(labels=["Date"],axis=1,inplace=True)
ETH2.insert(0,"Date",Date)
ETH2.rename(columns={"Volume":"Volume ETH"}, inplace=True)

BTC2= pd.DataFrame(BTC.loc[:,"Volume"].resample("B").mean().to_frame().assign(Date=lambda dfa: dfa.index.strftime("%d/%m")))
BTC2.drop(labels=["Date"],axis=1,inplace=True)
BTC2.rename(columns={"Volume":"Volume BTC"}, inplace=True)

ETH_BTC = pd.concat([ETH2, BTC2],axis=1)
ETH_BTC = pd.melt(ETH_BTC,id_vars="Date", var_name="Coin", value_name="Volume")
sns.barplot(x="Date",y="Volume", hue="Coin", data=ETH_BTC,ax=ax3, palette=sns.color_palette(["aqua", "lavender"]))

label3 = ax3.set_xticklabels(ax3.get_xticklabels(), rotation = 90,fontsize=5,alpha=0.5)
ax3.set_title("Bitcoin / ETH", fontsize=7)

#------------------------------Chart 4

Nikkei225 = yf.download("^N225", start='2020-12-01', end=yesterday)
Stats_Vol = Nikkei225["Volume"]

sns.barplot(data=Nikkei225.loc[:,"Volume"]\
            .resample("B").mean().to_frame()\
            .assign(Date=lambda dfa: dfa.index.strftime("%d/%m")),
            x="Date", y="Volume", ax=ax4,color="wheat")
#print(SP500["Volume"].rolling(250).mean().plot())
# rotate the labels
label4 = ax4.set_xticklabels(ax4.get_xticklabels(), rotation = 90,fontsize=5,alpha=0.5)
ax4.set_title("Nikkei 225", fontsize=7)

#------------------------------

plt.show()
