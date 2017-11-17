import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def histograms(df, variables, n_rows, n_cols):
    fig = plt.figure(figsize = (16, 12 ))
    for i, var_name in enumerate(variables):
        ax=fig.add_subplot(n_rows, n_cols, i + 1)
        df[var_name].hist(bins=10, ax=ax)
        ax.set_title('Skew: ' + str(round(float(df[var_name].skew()), ))) 
        ax.set_xticklabels([], visible=False)
        ax.set_yticklabels([], visible=False)
    
    fig.tight_layout()  # Improves appearance a bit.
    plt.show()

def distribution(df, var, target, **kwargs):
    row = kwargs.get('row', None)
    col = kwargs.get('col', None)
    facet = sns.FacetGrid(df, hue=target, aspect=4, row = row, col = col)
    facet.map(sns.kdeplot, var, shade = True)
    facet.set(xlim=(0 , df[var].max()))
    facet.add_legend()

def categories(df, cat, target, **kwargs):
    row = kwargs.get('row', None)
    col = kwargs.get('col', None)
    facet = sns.FacetGrid(df, row = row, col = col)
    facet.map(sns.barplot, cat, target)
    facet.add_legend()
