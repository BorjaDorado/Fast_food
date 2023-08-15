# Fast food
Este proyecto tiene como objetivo principal realizar la visualización de datos obtenidos a través de un proceso de ETL (Extracción, Transformación y Carga).

## Datos utilizados
Los datos utilizados para este proyecto fueron obtenidos de un archivo CSV descargado de la fuente Kaggle. El archivo contiene información sobre los valores nutricionales de menús de comida rápida en diferentes restaurantes.

## Proceso de ETL
En el primer paso de la ETL, se llevó a cabo una limpieza de los datos contenidos en el archivo CSV. Esto incluyó cambiar el tipo de dato de las columnas numéricas a float y ajustar las unidades de las columnas de colesterol y sodio al sistema internacional.

## Análisis y visualización de datos
Después de completar el proceso de ETL, se procedió a realizar un análisis exhaustivo de los datos y su posterior visualización utilizando diferentes gráficos.

## Diagrama de calor
[![calor.png](https://i.postimg.cc/SRh2qthY/calor.png)](https://postimg.cc/jwMd4cCR)
En el diagrama de calor se observa que los restaurantes KFC y Wendy's presentan un menor porcentaje de grasas y azúcares, y un mayor porcentaje de proteínas en comparación con los demás. Por otro lado, el resto de los restaurantes analizados muestran un alto contenido de carbohidratos, azúcares y grasas.

## Gráfico de puntos
[![scaterplot.png](https://i.postimg.cc/mkCYyHbC/scaterplot.png)](https://postimg.cc/9wXwWzwQ)
El gráfico de puntos revela una correlación entre las calorías y el contenido de grasas en los alimentos, con excepciones notables como McDonald's, donde la distribución es más dispersa.

## Gráfico de barras
[![Az-cares.png](https://i.postimg.cc/Zqsxbm7B/Az-cares.png)](https://postimg.cc/f3X9CGhD)
El gráfico de barras representa la cantidad de azúcar por artículo y por restaurante. Se destaca que productos como los refrescos y postres tienen una mayor concentración de azúcares, siendo los de Burger King, McDonald's y Taco Bell los menos saludables en este aspecto.

## Conclusiones
En conclusión, después del análisis realizado, se considera que KFC y Wendy's son las opciones más saludables dentro de las cadenas de comida rápida analizadas. El proyecto ha permitido explorar y visualizar de manera efectiva los datos obtenidos de la ETL, proporcionando una comprensión más clara de las diferencias nutricionales entre los restaurantes.

