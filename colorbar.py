import seaborn as sns
sns.set(font_scale=1.5)
import pandas as pd
import numpy as np


# data=pd.read_csv('./test.csv',header=0)
data=[[-0.012,0.016,0.025,0.003],[0.016,0.019,0.014,0.018],[0.025,0.014,0.007,0.001],[0.003,0.018,0.001,-0.001]]
print(data)

mask=np.ones((4,4))
for i in range(4):
    for j in range(i+1):
        mask[i,j]=0
import matplotlib.pyplot as plt
xlabelticks=['RandomCrop','Corrupt','PhotoMetricDistortion','RandomAffine']
ylabelticks=['RandomCrop','Corrupt','PhotoMetricDistortion','RandomAffine']
plt.figure(figsize=(12, 8))
ax=sns.heatmap(data,cmap='YlGnBu',annot=True,
linewidth=0.9,linecolor='white',square=True,robust=True,
cbar_kws={'orientation':'vertical','shrink':1,'extend':'max','location':'right'},
annot_kws={'color':'black','size':20,'family':None,'style':None,'weight':10},
            xticklabels=xlabelticks,yticklabels=ylabelticks)
xticklabels = ax.get_xticklabels()
yticklabels=ax.get_yticklabels()
ax.set_xticklabels(xticklabels, fontsize=15,rotation=45,ha="right")
ax.set_yticklabels(xticklabels, fontsize=15,ha="right")
plt.tight_layout()
plt.show()