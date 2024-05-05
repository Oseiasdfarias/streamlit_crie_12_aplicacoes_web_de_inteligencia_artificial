<p align="center">
  <img height="40px" src="../utils/streamlit_logo.png">
</p>



<h3  id="techs">Tecnologias</h3>

<p align=center> <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54"> <img src="https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white""> <img src="https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white"> <img src="https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black"> <img src="https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white"> <img src="https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white"> <img src="https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=for-the-badge&logo=PyTorch&logoColor=white"> <img src="https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white">
  </ul>
  <br>
</p>


# Previsão de produção de Leite usando dados históricos

O Projeto implementa um modelo de previsão de produção de leite a partir
de dados históricos, para isso foi aplicado um modelo de previsão
de séries temporas chamado SARIMAX.

A partir dos dados históricos é possivel predizer a produção de leite,
os daos históricos foram obtidos mensalmente, então a predição é feita
para meses futuros.


### **Descrição do Modelo SARIMAX**

descricao = """O modelo SARIMAX (Seasonal AutoRegressive Integrated Moving
Average with eXogenous factors) é uma extensão do modelo SARIMA
(Seasonal AutoRegressive Integrated Moving Average) que permite
incorporar variáveis exógenas, ou seja, fatores externos que podem
influenciar a série temporal que está sendo analisada.

### Vamos quebrar isso em partes:

1. Seasonal (Sazonal): Refere-se a padrões repetitivos ou ciclos que
ocorrem em intervalos fixos de tempo, como sazonalidade anual em vendas
de Natal ou sazonalidade mensal em dados climáticos.

2. AutoRegressive (Auto-regressivo): Significa que a variável depende
linearmente de seus próprios valores passados, ou seja, a previsão é
uma função de observações passadas da série temporal.

3. Integrated (Integrado): Refere-se à diferenciação da série temporal
para torná-la estacionária, ou seja, remover tendências não
estacionárias ou padrões de comportamento.

4. Moving Average (Média Móvel): Refere-se ao uso de erros de previsão
passados na previsão atual.

5. eXogenous factors (fatores exógenos): São variáveis independentes
que não estão dentro do sistema que está sendo modelado, mas que podem
influenciar o comportamento da variável dependente. Por exemplo, se
estamos modelando vendas de sorvete e queremos incorporar a temperatura
ambiente como um fator exógeno, podemos usar SARIMAX.

Em resumo, o modelo SARIMAX é uma técnica poderosa para modelar e
prever séries temporais que levam em conta tanto padrões sazonais
quanto fatores externos que podem influenciar os dados. Ele é
amplamente utilizado em áreas como finanças, economia, meteorologia
e análise de vendas, entre outros.




