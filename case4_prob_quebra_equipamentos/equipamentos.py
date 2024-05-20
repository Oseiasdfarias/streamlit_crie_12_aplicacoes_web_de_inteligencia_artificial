import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson
import matplotlib.colors as mcolors
import matplotlib.cm as cm
import seaborn as sns


custom_params = {"axes.spines.right": False, "axes.spines.top": False}
sns.set_theme(style="ticks", rc=custom_params)


st.set_page_config(page_title="Probabilidade de falhas em equipamentos",
                   page_icon="chart_with_upwards_trend")
st.title("Probabilidade de Falhas em Equipamentos")


with st.sidebar:
    st.header("Configurações")
    tipo = st.radio("Selecione o Cálculo",
                    options=[
                        "Prob. Exata",
                        "Menos que",
                        "Mais que"
                    ])
    ocorrencia = st.number_input("Média anual de ocorrência de falhas: ",
                                 min_value=1, max_value=99,
                                 value=2, step=1)
    intervalo = st.number_input("Digite o intervalo para calcular a prob.: ",
                                min_value=1, max_value=15,
                                value=5, step=1)
    processar = st.button("Processar")

if processar:
    lamb = ocorrencia
    if lamb < int(intervalo/2):
        inic = 0
        fim = int(intervalo) - 1
    else:
        inic = lamb - int(intervalo/2)
        fim = lamb + int(intervalo/2)
    x_vals = np.arange(inic, fim + 1)
    if tipo == "Prob. Exata":
        probs = poisson.pmf(x_vals, lamb)
        tit = "Probabilidade de ocorrência"
    elif tipo == "Menos que":
        probs = poisson.cdf(x_vals, lamb)
        tit = "Probabilidade de ocorrência igual ou menor que:"
    elif tipo == "Mais que":
        probs = poisson.sf(x_vals, lamb)
        tit = "Probabilidade de ocorrência igual ou maior que:"

    z_vals = np.round(probs*100.0, 2)

    labels = [f"{i} falha" if i<=1 else f"{i} falhas" for i in x_vals]  # noqa: E501 E225

    # Step 2: Normalize the values to range [0, 1]
    norm = mcolors.Normalize(vmin=min(probs), vmax=max(probs))

    # Step 3: Create a colormap
    colormap = cm.Greys

    # Step 4: Map normalized values to colors
    colors = colormap(norm(probs))

    fig, axes = plt.subplots(figsize=(7, 4))
    barras = axes.bar(x_vals, z_vals, tick_label=labels,
                      color=colors)

    # Adicionando rótulos personalizados às barras
    for barra, p in zip(barras, probs):
        height = barra.get_height()
        axes.text(barra.get_x() + barra.get_width() / 2., height,
                  f"{np.round(p*100, 2)}%",
                  ha='center', va='bottom', fontsize=9)

    axes.set_title(tit)
    axes.set_xlabel("Possíveis ocorrências para o próximo ano")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    st.pyplot(fig)


st.markdown("---")

st.markdown("### **Descrição**")

descricao_pn = """
    Uma indústria enfrenta problemas com falhas em seus equipamentos.
    A empresa possui dados sobre a média anual de falhas desses
    equipamentos e deseja realizar um estudo para prever a probabilidade
    de falhas no próximo ano, utilizando como base a média de
    falhas do ano anterior.
"""


st.markdown(descricao_pn)

st.markdown("### **Solução Proposta**")

solucao = """
    Para inferir a probabilidade de falhas para o próximo ano pode ser usado
    a distribuição de Poisson.
"""

st.markdown(solucao)

st.markdown("---")

st.title("Distribuição de Poisson")

st.write("""
A `distribuição de Poisson` é um modelo estatístico utilizado para descrever
a probabilidade de um dado número de eventos ocorrer dentro de um intervalo
fixo de tempo ou espaço, sob a suposição de que esses eventos acontecem de
forma independente uns dos outros e com uma taxa constante. Essa distribuição
é particularmente útil em situações onde os eventos são raros ou ocorrem
com baixa frequência.

### Características Principais:

1. **Taxa Média `(λ)`:** A distribuição de Poisson é caracterizada por um
parâmetro `λ` (lambda), que representa a taxa média de ocorrência dos eventos
por unidade de tempo ou espaço. Por exemplo, `λ` poderia ser o número médio
de falhas de equipamentos no último ano.

2. **Eventos Independentes:** Os eventos são considerados independentes
o que significa que a ocorrência de um evento não afeta a probabilidade
de outro evento ocorrer.

3. **Intervalo de Tempo ou Espaço Fixo:** A análise é feita em um intervalo
fixo, seja ele de tempo (por exemplo, por minuto, hora, dia, ano) ou espaço
(por exemplo, por metro quadrado).

### Função de Probabilidade:
""")

st.latex(r'''
P(X = k) = \frac{e^{-\lambda} \lambda^k}{k!}
''')

st.write("""
onde:
- `( P(X = k) )` é a probabilidade de ocorrerem exatamente `k` eventos.
- `( e )` é a base do logaritmo natural (aproximadamente igual a `2,71828`).
- `( k )` é o número de eventos.
- `( k! )` é o fatorial de `k`.

### Propriedades:

- **Média e Variância:** Para uma distribuição de Poisson, a média `(μ)`
e a variância `(σ²)` são ambas iguais a `λ`. Isso significa que, se em média
ocorrem `λ` eventos por unidade de tempo, a variabilidade esperada ao redor
dessa média também é `λ`.
- **Não Negativa:** Como trata da contagem de eventos, o valor de `k`
(número de eventos) deve ser um número inteiro não negativo.

### Aplicações:

A distribuição de Poisson é amplamente utilizada em diversas áreas,
incluindo:
- **`Engenharia`:** Para modelar falhas de sistemas ou equipamentos.
- **`Telecomunicações`:** Para prever o número de chamadas em uma central
telefônica.
- **`Biologia`:** Para contar mutações genéticas em uma sequência de DNA.
- **`Finanças`:** Para modelar a ocorrência de eventos de crédito ou sinistros.

A flexibilidade e a simplicidade da distribuição de Poisson fazem dela
uma ferramenta poderosa para análises probabilísticas e inferências
estatísticas em contextos onde eventos ocorrem de forma aleatória e
independente dentro de um intervalo de tempo ou espaço especificado.
""")
