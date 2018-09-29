# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 11:29:49 2017

@author: charlesmartens
"""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('white')


df = pd.DataFrame({'naps':[1,2,1,2,0,0,1,3,4,3,6,0,1,2,1,2,0,0,1,3,5,3,6,0,7,5,2,0,0,1,3,5,3,6,0,7,5,4,1,0], 
'heart rate':[81,65,70,61,59,85,67,49,69,54,58,72,81,65,70,64,58,89,69,47,58,69,54,74,79,70,58,89,69,48,55,69,58,65,73,48,51,60,75,80]})

sns.lmplot('naps', 'heart rate', data=df, scatter_kws={'s':80, 'alpha':.5, 'color':'green'}, fit_reg=False)
plt.xlabel('naps per week', fontsize=20)
plt.ylabel('heart rate', fontsize=20)
plt.grid(alpha=.01)
plt.xlim(-.5,7.5)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)

sns.lmplot('naps', 'heart rate', data=df, scatter_kws={'s':80, 'alpha':.5, 'color':'green'}, line_kws={'color': 'black', 'alpha':.5}, lowess=True)
plt.xlabel('naps per week', fontsize=20)
plt.ylabel('heart rate', fontsize=20)
plt.grid(alpha=.01)
plt.xlim(-.5,7.5)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
'
sns.lmplot('naps', 'heart rate', data=df, scatter_kws={'s':80, 'alpha':.5, 'color':'green'}, line_kws={'color': 'black', 'alpha':.5})
plt.xlabel('naps per week', fontsize=20)
plt.ylabel('heart rate', fontsize=20)
plt.grid(alpha=.01)
plt.xlim(-.5,7.5)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)


df['hr_dichot'] = 0
df.loc[df['heart rate']>65, 'hr_dichot'] = 1
df['hr_dichot'].value_counts()

sns.lmplot('naps', 'hr_dichot', data=df, scatter_kws={'s':80, 'alpha':.5, 'color':'green'}, line_kws={'color': 'black', 'alpha':.5}, logistic=True)
plt.xlabel('naps per week', fontsize=20)
plt.ylabel('heart rate \n(0 = lower than 65 bpm; \n1 = higher than 65 bpm)', fontsize=20)
plt.grid(alpha=.01)
plt.xlim(-.5,7.5)
plt.ylim(-.15, 1.15)
plt.xticks(fontsize=15)
plt.yticks([0,1], fontsize=15)


df['naps_dichot'] = 0
df.loc[df['naps']>2, 'naps_dichot'] = 1
df['naps_dichot'].value_counts()

sns.barplot(x='naps_dichot', y='heart rate', data=df, color='green', alpha=.5)
plt.yticks(fontsize=15)
plt.xticks([0,1], ['few', 'many'], fontsize=20)
plt.xlabel('naps', fontsize=20)
plt.ylabel('heart rate', fontsize=20)
sns.despine()

df['hr'] = df['heart rate']

plt.hist(df['hr'][df['naps_dichot']==0], color='red', alpha=.3, label='few naps')
plt.xlim(45,90)
plt.ylim(0,5)
plt.title('Few Naps', fontsize=20)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.xlabel('heart rate', fontsize=20)
plt.ylabel('count', fontsize=20)
sns.despine()

plt.hist(df['hr'][df['naps_dichot']==1], color='green', alpha=.3, label='many naps')
plt.xlim(45,90)
plt.ylim(0,5)
plt.title('Many Naps', fontsize=20)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.xlabel('heart rate', fontsize=20)
plt.ylabel('count', fontsize=20)
sns.despine()

plt.hist(df['hr'][df['naps_dichot']==0], color='red', alpha=.3, histtype='step', linewidth=5, label='few naps')
plt.hist(df['hr'][df['naps_dichot']==1], color='green', alpha=.3, histtype='step', linewidth=5, label='many naps')
plt.ylim(0,5)



sns.barplot(x='naps_dichot', y='hr_dichot', data=df, color='green', alpha=.5)
plt.yticks([0,1], fontsize=15)
plt.xticks([0,1], ['few', 'many'], fontsize=20)
plt.xlabel('naps', fontsize=20)
plt.ylabel('heart rate \n(0 = lower than 65 bpm; \n1 = higher than 65 bpm)', fontsize=20)
sns.despine()



import statsmodels.formula.api as smf #with this 'formula' api, don't need to create the design #matrices (does it automatically).
from statsmodels.formula.api import *

results = smf.logit(formula = 'hr_dichot ~ naps_dichot', data=df).fit()
print(results.summary()) 



len(df)
df['poor_sleeper'] = [0,1,1,1,0,0,0,1,1,0,0,0,0,0,0,1,1,1,0,0,0,1,1,1,0,0,0,1,1,0,0,0,0,0,0,1,1,1,0,0]

sns.lmplot(x='naps', y='heart rate', data=df, hue='poor_sleeper', scatter_kws={'s':70, 'alpha':.4}, line_kws={'alpha':.5}, legend=False, ci=.1)
plt.xlabel('naps per week', fontsize=20)
plt.ylabel('heart rate', fontsize=20)
plt.grid(alpha=.01)
plt.xlim(-.5,7.5)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.legend(['good sleeper', 'poor sleeper'], loc='top right', fontsize=15)


sns.barplot(x='naps_dichot', y='heart rate', data=df, hue='poor_sleeper', alpha=.65)
plt.yticks(fontsize=15)
plt.xticks([0,1], ['few', 'many'], fontsize=20)
plt.xlabel('naps', fontsize=20)
plt.ylabel('heart rate', fontsize=20)
sns.despine()













