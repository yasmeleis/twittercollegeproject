# GRAPHING THE RESULTS FROM OUR DATA PULL: 

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

raw_data = {'first_name': ['Trump', 'Cruz', 'Kasich', 'Sanders', 'Clinton'],
        'pre_score': [44, 11.7, 44.4, 37.2, 62.8],
        'mid_score': [64.3, 13.7, 22, 36.6, 63.4],
        'post_score': [64.4, 21.1, 14.5, 69.5, 30.5]}
df = pd.DataFrame(raw_data, columns = ['first_name', 'pre_score', 'mid_score', 'post_score'])
df

# Positioning the bars and adding the width of .25: 
pos = list(range(len(df['pre_score']))) 
width = 0.25 

# Plotting: 
fig, ax = plt.subplots(figsize=(10,5))

# Create a bar with pre_score data or the pre-election predictions and edit design: 
plt.bar(pos, 
        df['pre_score'], 
        width, 
        alpha=0.5, 
        color='#EE3224', 
        label=df['first_name'][0]) 

# Create a bar with mid_score data or election results and edits design: 
plt.bar([p + width for p in pos], 
        df['mid_score'],
        width, 
        alpha=0.5, 
        color='#F78F1E', 
        label=df['first_name'][1]) 

# Create a bar with post_score data or twitter popularity and edit design: 
plt.bar([p + width*2 for p in pos], 
        df['post_score'], 
        width, 
        alpha=0.5, 
        color='#FFC222', 
        label=df['first_name'][2]) 

# Label Y axis: 
ax.set_ylabel('Popularity by Percentage')

# Title the chart: 
ax.set_title('Predicted, Voter, and Twitter Popularity Results for Presidential Candidates')

# Putting the x ticks in place: 
ax.set_xticks([p + 1.5 * width for p in pos])

# Setting lables: 
ax.set_xticklabels(df['first_name'])

# x-axis and y-axis limits: 
plt.xlim(min(pos)-width, max(pos)+width*4)
plt.ylim([0, max(df['pre_score'] + df['mid_score'] + df['post_score'])] )

# Adding legend and printing: 
plt.legend(['Predicted Votes', 'Primary Results', 'Twitter Popularity'], loc='upper left')
plt.grid()
plt.show()