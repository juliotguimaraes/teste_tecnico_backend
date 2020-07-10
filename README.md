# Teste técnico
Se você  está recebendo este teste, prabéns!! Você está mais um passo de fazer parte da equipe **Mediar**.  
Objetivo deste teste é avaliar sua capacidade de organizar, documentar, solucionar problemas e tornar seu projeto executável.  

A plataforma da Mediar possuí diversas visualizações que são alimentados a partir de uma base de dados do varejo.   
Abaixo está o exemplo de um de nossos painéis.

![](https://mediarsolutions.com/wp-content/uploads/2020/07/mediar_panel.png)

Crie um endpoint em **Django** ou **Flask** com os dados fornecidos _**(pode usar apenas os dados que considerar necessários)**_ nesse repositório que receba uma data inicial e final, uma lista de codigos de produtos e retorne o valor total vendido (dia-a-dia) correspondente ao período e aos produtos passados, com a finalidade de alimentar um gráfico temporal _**(você não precisa criar o gráfico)**_.  
A ferramenta de banco de dados fica a sua escolha, **MySQL, Postgres, Mongo, etc.**

Ao finalizar o projeto, nos envie pelo github de uma forma organizada e documentada, para que possamos executar sua API na nossa máquina local.  
Explique dentro da documentação o porque usou o banco de dados e a modelagem escolhida.

__________________________________________________________________________________________________________________________________________

Esse trabalho foi desenvolvido utilizando Django 3.0.8
Utilizei rest framework para construir a API e as requisições de POST e get.
Criando os response e renderização.

Foi criado o Models Compra com os campos que julguei necessários para cumprir a tarefa.

Além disso, foi criado um banco de dados postgreSQL, utilizando o module django psycopg2
