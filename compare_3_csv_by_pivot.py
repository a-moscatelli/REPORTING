#!/usr/bin/env python
# coding: utf-8
# In[1]:
import pandas as pd
# In[2]:
FN = {
'BL':'C:/TEMP/chrome_downloads/pvrecon/All_PV_BL_DAY2.csv',
'RC':'C:/TEMP/chrome_downloads/pvrecon/All_PV_RC_DAY2.csv',
'PD':'C:/TEMP/chrome_downloads/pvrecon/All_PV_PD_DAY2.csv'
}
# In[3]:
outcsv = 'C:/TEMP/chrome_downloads/pvrecon/All_PV_XX_DAY2.csv'
# In[4]:
fns = 'C:/NotBackedUp/TEMP/chrome_downloads/pvrecon/pfscope.csv'
DFS = pd.read_csv(fns)
# In[5]:
AGGREG={
    'file_PK' : ['PV Currency','Skylib TradeID'],
    'file_GROUPBY': ['Portfolio','PV Currency','TradeType'],
    'filter': 'Portfolio',
    'OP': 'sum',
    'OPFIELD': 'LCH_T0_FIXING'
}
# In[6]:
DF={}
for k in FN:
    # Load:
    DF[k] = pd.read_csv(FN[k])
    DF[k].set_index(AGGREG['file_PK'],verify_integrity=True) # fails on duplicates.
    # Filter rows:
    print(k,'pre :',DF[k].shape)
    DF[k] = pd.merge(DF[k], DFS, on = AGGREG['filter'], how = 'inner')
    # Filter cols:
    DF[k] = DF[k][AGGREG['file_GROUPBY']+[AGGREG['OPFIELD']]]
    print(k,'post:',DF[k].shape)
    DF[k] =  DF[k].groupby(AGGREG['file_GROUPBY'], as_index=False).agg({AGGREG['OPFIELD']:sum})
# In[7]:
for k in FN:
    DF[k]['K'] = k
DFU = pd.concat([DF['BL'], DF['RC'], DF['PD']])
print('DFU','shape',DFU.shape)
print(DFU.columns)
# In[8]:
#DFUG = DFU.groupby(AGGREG['file_GROUPBY']+['K'], as_index=False).agg({'LCH_T0_FIXING':sum})
# In[9]:
DFU.rename(columns = {AGGREG['OPFIELD']:AGGREG['OPFIELD']+'_tot'}, inplace = True)
print('DFU','shape',DFU.shape)
print(DFU.columns)
# In[10]:
PVT = DFU.pivot(index = AGGREG['file_GROUPBY'], columns ='K', values =[AGGREG['OPFIELD']+'_tot'])
# pivot() does not comput aggregation - just placement
PVT.columns
# In[11]:
display(PVT)
# In[12]:
dfpvt = PVT.reset_index()
display(dfpvt)
# In[13]:
#dfpvt = PVT.reset_index()
opf=AGGREG['OPFIELD']
dfpvt['delta_BL_PD'] = dfpvt['LCH_T0_FIXING_tot']['BL'] - dfpvt['LCH_T0_FIXING_tot']['PD']
dfpvt['delta_RC_PD'] = dfpvt['LCH_T0_FIXING_tot']['RC'] - dfpvt['LCH_T0_FIXING_tot']['PD']
# In[14]:
display(dfpvt)
# In[ ]: