import pandas as pd
import plotly.express as px
import plotly.io as pio

# Seus dados
df = pd.DataFrame({
    'Gênero': ['Masculino', 'Feminino'],
    'Quantidade': [21, 4]
})

# Criando o gráfico interativo
fig = px.bar(df, x='Gênero', y='Quantidade', 
             title='Distribuição da Turma',
             color='Gênero',
             color_discrete_map={'Masculino': 'blue', 'Feminino': 'pink'})

# Gerando apenas a div do gráfico (sem o HTML completo)
grafico_html = pio.to_html(fig, full_html=False, include_plotlyjs='cdn')

# Salva em um arquivo para você copiar o código
with open("grafico_div.txt", "w", encoding="utf-8") as f:
    f.write(grafico_html)

print("Código do gráfico gerado em 'grafico_div.txt'")