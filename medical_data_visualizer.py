import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1. Load dataset
df = pd.read_csv("medical_examination.csv")

# 2. Calculate BMI and overweight status
df['BMI'] = df['weight'] / ((df['height'] / 100) ** 2)
df['overweight'] = (df['BMI'] > 25).astype(int)

# 3. Normalize cholesterol and glucose values
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

# 4. Function to draw categorical plot
def draw_cat_plot():
    # Melt the dataframe for categorical features
    df_cat = pd.melt(df, id_vars=['cardio'], 
                      value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    # Rename column for compatibility with seaborn
    df_cat = df_cat.rename(columns={'variable': 'feature', 'value': 'outcome'})

    # Create the catplot
    g = sns.catplot(x="feature", hue="outcome", col="cardio", 
                    data=df_cat, kind="count", height=5, aspect=1.2)

    # Fix axis labels
    g.set_axis_labels("feature", "count")

    fig = g.fig  # Convert FacetGrid to Figure

    # Save the figure
    fig.savefig('catplot.png')
    return fig
    
# 5. Function to draw heat map
def draw_heat_map():
    # Clean the data (fix: keep only required columns)
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) & 
                 (df['height'] >= df['height'].quantile(0.025)) & 
                 (df['height'] <= df['height'].quantile(0.975)) & 
                 (df['weight'] >= df['weight'].quantile(0.025)) & 
                 (df['weight'] <= df['weight'].quantile(0.975))].copy()

    # Fix: Remove 'BMI' column before correlation
    df_heat = df_heat.drop(columns=['BMI'])

    # Compute the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # Set up the matplotlib figure (fix: ensure ax is correct)
    fig, ax = plt.subplots(figsize=(10, 8))

    # Draw the heatmap
    sns.heatmap(corr, mask=mask, annot=True, fmt=".1f", linewidths=0.5, cmap="coolwarm", ax=ax)

    # Save the figure
    fig.savefig('heatmap.png')
    return fig

# Run and display the plots
draw_cat_plot()
draw_heat_map()