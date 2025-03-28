import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


# 1
df = df = pd.read_csv("medical_examination.csv")
# Calculate BMI
df['BMI'] = df['weight'] / ((df['height'] / 100) ** 2)

# Assign overweight: 1 if BMI > 25, else 0
df['overweight'] = (df['BMI'] > 25).astype(int)
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)



# 2
df['overweight'] = None

# 3


# 4
def draw_cat_plot():
    # 5
    df_cat = None


    # 6
    df_cat = None
    

    # 7



    # 8
    fig = None


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = None

    # 12
    corr = None

    # 13
    mask = None



    # 14
    fig, ax = None

    # 15



    # 16
    fig.savefig('heatmap.png')
    return fig
