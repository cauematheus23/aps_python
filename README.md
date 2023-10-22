# aps_python
o objetivo dessa aps é fazer um script em python que leia arquivos com diferentes quantidades de dados, ordenados e desordenados e compare a velocidade de ordenação atraves de um grafico das funçãos do python
---
# Intruções

1) Suponha que sejam coletadas imagens da floresta amazônica, as quais são registradas em um banco de dados com a data e o horário em que foram capturadas. O formato para a data é:
   
YYYY-MM-DD 
Por exemplo: "2023-08-15" 

2) Em vez de implementar um banco de dados, o grupo deverá desenvolver um programa utilizando arquivos de texto. O grupo deverá gerar arquivos de texto, nos quais cada linha corresponde a uma data. 

Serão necessários dois tipos de arquivos: o primeiro com datas ordenadas cronologicamente; o segundo, com datas em ordem aleatória. Além disso, o grupo deverá produzir arquivos distintos, com diferentes quantidades de elementos. 

Por exemplo: 

Pasta 1 – Arquivos Aleatórios 
	
Arquivo_Aleatorio_1.txt: 10 linhas 
	
Arquivo_Aleatorio_2.txt: 20 linhas 
	
Arquivo_Aleatorio_3.txt: 30 linhas 
…. 
Arquivo_1000.txt: 1000 linhas 

Pasta 2 – Arquivos Ordenados 	

Arquivo_Ordenado_1.txt: 22 linhas 
	
Arquivo_Ordenado_2.txt: 44 linhas 
…. 	
Arquivo_Ordenado_100.txt: 1024 linhas 
	
Para gerar um conjunto de dados com datas aleatórias, recomenda-se utilizar o site random.org, que oferece um serviço de geração de valores realmente aleatórios, se baseando em ruído atmosférico.  O endereço eletrônico do site é: https://www.random.org/calendar-dates/ 

3) Em seguida, o grupo deve implementar três algoritmos de ordenação distintos e compará-los quanto à sua eficiência e complexidade computacional. Os algoritmos podem ser escolhidos livremente, inclusive aqueles que não foram abordados em aula. Sugere-se que sejam utilizados algoritmos com diferentes classes de complexidade, como O(n²), O(n log n) ou O(n). 

Dica: Faça algum código de ordenação funcionar, aplique ele para ordenar as Datas Aleatórias, e com o resultado, crie os arquivos com Datas Ordenados.  

4) Os programas devem ser elaborados na linguagem Python. Deve-se enviar o arquivo .py ou o arquivo jupyter correspondente, contendo o código-fonte e os comentários explicativos. 

5) Você deve cronometrar o tempo de execução de cada algoritmo para ordenar cada arquivo. Em seguida, você deve criar um gráfico para visualizar seus resultados. O gráfico deve ter o tempo no eixo vertical, e a quantidade de linhas de cada arquivo no eixo horizontal. 

Observação 1: Recomenda-se que você não utilize o computador para realizar outras tarefas no momento da cronometragem do tempo, pois a execução é tão rápida que outros processos em segundo plano podem interferir no seu resultado. 

Observação 2: Os gráficos devem ser gerados pelo próprio Python, utilizando a biblioteca Matplotlib. 

