# Credit Default EDA

![alt text](https://www.simplilearn.com/ice9/free_resources_article_thumb/financial-risk-and-types-rar131-article.jpg)

En este notebook se pretende detectar indicios, en un contexto financiero, que indiquen si un solicitante tiene dificultades para pagar sus cuotas, lo que puede servir para tomar medidas como denegar el préstamo, reducir el importe del mismo, prestar (a solicitantes de riesgo) a un tipo de interés más alto, etc. De este modo, se evitará rechazar a los consumidores capaces de devolver el préstamo y se reducirá la morosidad.

Para el Analisis Exploratorio de Datos, hemos seguido los siguientes pasos:

Importación de módulos
Estudio del dataset
Limpieza de Datos
Tratamiento de los valores ausentes
Conversión de tipo
Revisión de filas y columnas: eliminación de filas/columnas innecesarias (mediante la gestión de valores perdidos y correlación)
Tratamiento de Outliers
Análisis univariante
Análisis bivariante y multivariante

## Conclusiones:

1. Hay columnas en el dataset que están altamente correlacionadas entre sí. Lo que significa que ambas tendrán un impacto similar en el valor objetivo (target value). 

2. Este conjunto de datos está muy desequilibrado 

3. Los solicitantes cuyos préstamos anteriores fueron aprobados tienen más probabilidades de pagar el préstamo actual a tiempo, que los solicitantes cuyos préstamos anteriores fueron rechazados. 
**La característica más importante es que el 7% de los solicitantes de préstamos aprobados anteriormente que pagaron el préstamo actual a tiempo y son más propensos a pagarlo puntualmente que los solicitantes de préstamos rechazados.

- El 7% de los solicitantes de préstamos previamente aprobados que no pagaron el préstamo actual
- El 90% de los solicitantes de préstamos previamente rechazados que pudieron pagar el préstamo actual

4. 'SCO', 'LIMIT' y 'HC' son los motivos más comunes de rechazo.

5. La mayoría de las personas no solicitaron un seguro durante la solicitud del préstamo.

6. En las "Tarjetas" el porcentaje de morosos es el más alto (17%). **'NAME_PORTFOLIO'** es una característica importante para analizar la variable 'TARGET'.

7. El 15% de los solicitantes de préstamos son morosos para Préstamo en efectivo (AP+). **El "CHANNEL_TYPE" es una característica importante para el análisis de la variable "TARGET".

8. El porcentaje más alto (17%) de casos de impago corresponde a "Card Street". **'PRODUCT_COMBINATION'** nos da informacón valiosa para el caso.
