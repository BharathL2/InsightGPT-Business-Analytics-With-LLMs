import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

def perform_eda(filepath):
    df = pd.read_csv(filepath)
    summary = df.describe(include='all').to_html()

    plots = []
    numeric_cols = df.select_dtypes(include='number').columns

    for col in numeric_cols:
        plt.figure()
        sns.histplot(df[col], kde=True)
        plot_file = f"static/{col}_plot.png"
        plt.savefig(plot_file)
        plt.close()
        plots.append(plot_file)

    return summary, plots
