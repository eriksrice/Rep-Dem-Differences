import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
import numpy as np
sns.set()
from statsmodels.stats.proportion import proportions_ztest

#importing dataset, which I've already fleshed out in excel
df = pd.read_csv('/Users/erikrice/Downloads/Partisan Spending Time w_ Family - Sheet1 (5).csv')
print(df.head())

#creating some variables
font_color = '#525252'
hfont = {'fontname':'Calibri'}
facecolor = '#eaeaf2'
color_red = '#fd625e'
color_blue = '#01b8aa'
index = df['Survey question']
column0 = df['Dem great deal/quite a bit %']
column1 = df['Rep great deal/quite a bit %']
title0 = '% Democrats Who Enjoy Activity "A Great Deal or Quite a Bit"'
title1 = '% Republicans Who Enjoy Activity "A Great Deal or Quite a Bit"'

#visualizing the data
fig, axes = plt.subplots(figsize=(10,5), facecolor = facecolor, ncols=2, sharey=True)
fig.tight_layout()
axes[0].barh(index, column0, align='center', color=color_red, zorder=10)
axes[0].set_title(title0, fontsize=8, pad=15, color=color_red, **hfont) 
axes[1].barh(index, column1, align='center', color=color_blue, zorder=10)
axes[1].set_title(title1, fontsize=8, pad=15, color=color_blue, **hfont) 
axes[0].invert_xaxis()
plt.gca().invert_yaxis()
axes[0].set(yticks=index, yticklabels=index)
axes[0].yaxis.tick_left()
axes[0].tick_params(axis='y', colors='white')
axes[0].set_xticks([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
axes[1].set_xticks([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
for label in (axes[0].get_xticklabels() + axes[0].get_yticklabels()):
    label.set(fontsize=13, color=font_color, **hfont)
for label in (axes[1].get_xticklabels() + axes[1].get_yticklabels()):
    label.set(fontsize=13, color=font_color, **hfont)
plt.subplots_adjust(wspace=0, top=0.85, bottom=0.1, left=0.18, right=0.95)
plt.show()

#are these differences statistically significant? let's do some two-sample proportion tests
#already have the percentages for each response, so no need to normalize or group results                   
#finding the z-score for the first survey response - 'Your religious faith'
p_hat_d1 = .39
p_hat_r1 = .56
n_d1 = 3961
n_r1 = 5687
p_hat1 = (n_d1 * p_hat_d1 + n_r1 * p_hat_r1) / (n_d1 + n_r1)
std_error1 = np.sqrt(p_hat1 * (1-p_hat1) / n_d1 + p_hat1 * (1-p_hat1) / n_r1)
z_score1 = (p_hat_d1 - p_hat_r1) / std_error1
print(z_score1)

#calculating the p-value
n_affirmative1 = np.array([3961, 5687])
n_total1 = np.array([10156, 10156])
z_score1, p_value1 = proportions_ztest(count=n_affirmative1, nobs=n_total1, alternative='two-sided')
print(z_score1, p_value1)

#performing two-sample proportion test on 'Meditating' survey response now
p_hat_d2 = .32
p_hat_r2 = .27
n_d2 = 3250
n_r2 = 2742
p_hat2 = (n_d2 * p_hat_d2 + n_r2 * p_hat_r2) / (n_d2 + n_r2)
std_error2 = np.sqrt(p_hat2 * (1-p_hat2) / n_d2 + p_hat2 * (1-p_hat2) / n_r2)
z_score2 = (p_hat_d2 - p_hat_r2) / std_error2
print(z_score2)
n_affirmative2 = np.array([3250, 2742])
n_total2 = np.array([10156, 10156])
z_score2, p_value2 = proportions_ztest(count=n_affirmative2, nobs=n_total2, alternative='two-sided')
print(z_score2, p_value2)

#performing test on 'Volunteer work' response now
p_hat_d3 = .35
p_hat_r3 = .31
n_d3 = 3555
n_r3 = 3148
p_hat3 = (n_d3 * p_hat_d3 + n_r3 * p_hat_r3) / (n_d3 + n_r3)
std_error3 = np.sqrt(p_hat3 * (1-p_hat3) / n_d3 + p_hat3 * (1-p_hat3) / n_r3)
z_score3 = (p_hat_d3 - p_hat_r3) / std_error3
print(z_score3)
n_affirmative3 = np.array([3555, 3148])
n_total3 = np.array([10156, 10156])
z_score3, p_value3 = proportions_ztest(count=n_affirmative3, nobs=n_total3, alternative='two-sided')
print(z_score3, p_value3)

#performing test on 'Being outdoors and experiencing nature' response
p_hat_d4 = .7
p_hat_r4 = .72
n_d4 = 7109
n_r4 = 7312
p_hat4 = (n_d4 * p_hat_d4 + n_r4 * p_hat_r4) / (n_d4 + n_r4)
std_error4 = np.sqrt(p_hat4 * (1-p_hat4) / n_d4 + p_hat4 * (1-p_hat4) / n_r4)
z_score4 = (p_hat_d4 - p_hat_r4) / std_error4
print(z_score4)
n_affirmative4 = np.array([7109, 7312])
n_total4 = np.array([10156, 10156])
z_score4, p_value4 = proportions_ztest(count=n_affirmative4, nobs=n_total4, alternative='two-sided')
print(z_score4, p_value4)

#performing test on 'Spending time with family' response
p_hat_d5 = .82
p_hat_r5 = .85
n_d5 = 8328
n_r5 = 8633
p_hat5 = (n_d5 * p_hat_d5 + n_r5 * p_hat_r5) / (n_d5 + n_r5)
std_error5 = np.sqrt(p_hat5 * (1-p_hat5) / n_d5 + p_hat5 * (1-p_hat5) / n_r5)
z_score5 = (p_hat_d5 - p_hat_r5) / std_error5
print(z_score5)
n_affirmative5 = np.array([8328, 8633])
n_total5 = np.array([10156, 10156])
z_score5, p_value5 = proportions_ztest(count=n_affirmative5, nobs=n_total5, alternative='two-sided')
print(z_score5, p_value5)

#finally, performing test on 'Spending time with friends' response
p_hat_d6 = .68
p_hat_r6 = .64
n_d6 = 6906
n_r6 = 6500
p_hat6 = (n_d6 * p_hat_d6 + n_r6 * p_hat_r6) / (n_d6 + n_r6)
std_error6 = np.sqrt(p_hat6 * (1-p_hat6) / n_d6 + p_hat6 * (1-p_hat6) / n_r6)
z_score6 = (p_hat_d6 - p_hat_r6) / std_error6
print(z_score6)
n_affirmative6 = np.array([6906, 6500])
n_total6 = np.array([10156, 10156])
z_score6, p_value6 = proportions_ztest(count=n_affirmative6, nobs=n_total6, alternative='two-sided')
print(z_score6, p_value6)