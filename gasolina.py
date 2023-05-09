import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dados = pd.read_csv('/content/gasolina.csv')
dados.to_csv('dados.csv')

with sns.axes_style('whitegrid'):

  grafico = sns.lineplot(data=dados, x="dia", y="p/gasolina", palette="pastel")
  plt.savefig('gasolina.png')