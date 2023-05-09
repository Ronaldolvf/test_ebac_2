dados = pd.read_csv('/content/test_ebac_2/gasolina.csv')

with sns.axes_style('whitegrid'):

  grafico = sns.lineplot(data=dados, x="dia", y="venda", palette="pastel")
  plt.savefig('gasolina.png')