The code tells everything. Right now there is an issue regarding the ETC & BTC Chart in which for the moment i can not combine both plots in one subplot


import pandas as pd
import numpy as np
import yfinance as yf
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import seaborn as sns

yesterday = datetime.now()-timedelta(1)
fig = plt.figure()
datestring = datetime.strftime(datetime.now(), "%d/%m/%Y")
fig.suptitle("Volumes - Indices "+ datestring)
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

SP500 = yf.download('^GSPC', start='1993-02-01', end=yesterday)
Stats_Vol = SP500["Volume"]
#Stats_Vol.rolling(250).mean().plot()
# too many days, resample
# do a display format for date (which is the index)
sns.barplot(data=SP500.loc[:,"Volume"]\
            .resample("Y").mean().to_frame()\
            .assign(Date=lambda dfa: dfa.index.strftime("%Y")),
            x="Date", y="Volume", ax=ax1,color = "slategray")


#print(SP500["Volume"].rolling(250).mean().plot())
# rotate the labels
label1 = ax1.set_xticklabels(ax1.get_xticklabels(), rotation = 90,fontsize=5,alpha=0.5)
ax1.set_title("S&P500", fontsize=7)

#-----------------------------

NSDQ = yf.download("^NDX", start='1993-02-01', end=yesterday)
Stats_Vol = NSDQ["Volume"]

sns.barplot(data=NSDQ.loc[:,"Volume"]\
            .resample("Y").mean().to_frame()\
            .assign(Date=lambda dfa: dfa.index.strftime("%Y")),
            x="Date", y="Volume", ax=ax2,color ="darkmagenta")
#print(SP500["Volume"].rolling(250).mean().plot())
# rotate the labels
label2 = ax2.set_xticklabels(ax2.get_xticklabels(), rotation = 90,fontsize=5,alpha=0.5)
ax2.set_title("NASDAQ", fontsize=7)
#------------------------------
ETH = yf.download("ETH-EUR", start='2009-02-01', end=yesterday)
BTC = yf.download("BTC-EUR", start='2009-02-01', end=yesterday)

ETH2 = sns.barplot(data=ETH.loc[:,"Volume"]\
            .resample("m").mean().to_frame()\
            .assign(Date=lambda dfa: dfa.index.strftime("%m/%y")), x="Date",y="Volume",ax=ax3, color="coral")
BTC2 = sns.barplot(data=BTC.loc[:,"Volume"]\
            .resample("m").mean().to_frame()\
            .assign(Date=lambda dfa: dfa.index.strftime("%m/%y")), ax=ax3, x="Date",y="Volume", color="aqua" )

label3 = ax3.set_xticklabels(ax3.get_xticklabels(), rotation = 90,fontsize=5,alpha=0.5)
ax3.set_title("Bitcoin / ETH", fontsize=7)


#print(SP500["Volume"].rolling(250).mean().plot())
# rotate the labels

#------------------------------

TECDAX = yf.download("^TECDAX", start='1993-02-01', end=yesterday)
Stats_Vol = TECDAX["Volume"]

sns.barplot(data=TECDAX.loc[:,"Volume"]\
            .resample("Y").mean().to_frame()\
            .assign(Date=lambda dfa: dfa.index.strftime("%Y")),
            x="Date", y="Volume", ax=ax4,color="wheat")
#print(SP500["Volume"].rolling(250).mean().plot())
# rotate the labels
label4 = ax4.set_xticklabels(ax4.get_xticklabels(), rotation = 90,fontsize=5,alpha=0.5)
ax4.set_title("TECDAX", fontsize=7)

#------------------------------

plt.show()
