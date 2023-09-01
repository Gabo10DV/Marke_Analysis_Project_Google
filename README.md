# <h1 align="CENTER">**`Market Analysis Project Google`**</h1>

## <h2 align="CENTER">**`Freag data consultant`**</h2>

<p align='center'>
<img src = 'src/Ilustration_V2_A_sleek_modern_logo_with_a_circular_aqua_green_3.jpg' height = 250>
<p>

---

<details>
  <summary>Tabla de Contenidos</summary>
  <ol>
    <li><a href="#indice">Introducción</a></li>
    <li><a href="#introducción">Alcance</a></li>
    <li><a href="#objetivo">Paquete Tecnológico-Analítico</a></li>
    <li><a href="#servicio-api-rest">Servicio API Rest</a></li>
    <li><a href="#machine-learning">Machine Learning</a></li>
    <li><a href="#analisis-del-mercado">Analisis del mercado</a></li>
    <li><a href="#desarrollo-del-proyecto">Desarrollo del Proyecto</a></li>
    <li><a href="#desarrolladores">Desarrolladores</a></li>
    <li><a href="#stack-tecnológico">Stack Tecnológico</a></li>
  </ol>
</details>

---

## <div align="CENTER">**`Introducción`**</div>

Somos una consultoría de análisis de datos que está desarrollando un nuevo paquete de servicios enfocado en mejorar el rendimiento de locales del sector gastronómico. Este paquete está diseñado para ayudar a los restaurantes a aumentar su popularidad, mejorar su servicio al cliente y aumentar sus ventas.

Dicho paquete está siendo evaluada para ser implementada en una cadena de restaurantes en el estado de Nevada. Y para la evaluación del produlto, estos servicios están siendo evaluados poniéndolos en ejecución en 10 restuarantes selectos de forma aletoria en el estado de Nevada y estados fronterizos: Óregon, Idaho, California, utah y Arizona.

<div align="CENTER">
  <img src="src/map.jpg" alt="Our TEAM" width="80%">
  <p>Zona Demografica a Evaluar<p>
</div>

EL criterio para la selección de restaurantes fue su popularidad o rendimiento en sitios webs de Reseñas y críticas, para así comparar lo que nuestro paquete de servicios puede lograr en dichos restaurantes de bajo rendimeinto enfréntandolos contra aquellos que si tienen buen rendimiento.

El paquete incluye los siguientas soluciones: 

- **Servicio API REST:** servicio para la obtención de competidores y usuarios: Esta API proporcionará a los restaurantes datos sobre sus competidores y sus clientes. Los datos de los competidores se utilizarán para identificar oportunidades de crecimiento y diferenciación. Los datos de los clientes se utilizarán para personalizar las campañas de marketing y mejorar el servicio al cliente.

- **Modelos de machine learning:** Se crearán dos modelos de machine learning utilizarán los datos de los competidores y los clientes para proporcionar información y recomendaciones valiosas a los restaurantes. El modelo de clasificación de usuarios identificará a los clientes potenciales que son más propensos a participar en campañas de marketing. El modelo de lenguaje natural analizará las reseñas de los clientes para proporcionar información sobre la satisfacción de los clientes y las áreas de mejora del restaurante.

- **Análisis y dashboard interactivo:** Este análisis proporcionará a los restaurantes una visión general de su rendimiento y les ayudará a identificar áreas de mejora. El dashboard interactivo será fácil de usar y proporcionará información visual atractiva.

Este paquete inicialmente se alimentará de datos obtenidsos de fuentes YELP y Google. Ambos servicios proporcionan información de localidades, y reseñas, y el análisis de sus datos nos permitirá proporcionar un análisis detallado del sector gatronómico y la evaluación preliminar de nuestros paquete de servicios.

## <h2 align="CENTER">**`Paquete Tecnológico-Analítico`**</h2>

El paquete ofrece la realización de tres soluciones tecnológicas enfocadas a tres diferentes contextos: información de competidores, determinación de potenciales clientes, y soluciones de marquetin y analítica.

Estos productos son los siguientes:

### Servico API REST

Con tla de poder obtener informacion de los competidores de nuestro cliente, se desarrollara un Servicio Api REST Ful para obtentener. Este servicio se desplejara en la web, ynuestro cliente podra acceder a el para obtener informacion reeavante de la empresa.

#### Restaurante por id

<details>
  <summary>
    <code>GET</code>
    <code><b>/api/restaurant/{id}</b></code>
  </summary>

#### Ejemplo de Uso

```txt
Próximamente
```

#### Ejemplo de Respuesta


```json
{

}
```

</details>

#### Categorias de restaurantes

<details>
  <summary>
    <code>GET</code>
    <code><b>/api/categories</b></code>
  </summary>

#### Ejemplo de Uso

```txt
Próximamente
```

#### Ejemplo de Respuesta


```json
{

}
```

</details>


#### Restaurantes por categoría

<details>
  <summary>
    <code>GET</code>
    <code><b>/api/restaurant-by-categorie</b></code>
  </summary>

#### Ejemplo de Uso

```txt
Próximamente
```

#### Ejemplo de Respuesta


```json
{

}
```

</details>

#### Lista de Competidores Cercanos

<details>
  <summary>
    <code>GET</code>
    <code><b>/api/competitors-list/{km2}</b></code>
  </summary>

#### Ejemplo de Uso

```txt
Próximamente
```

#### Ejemplo de Respuesta


```json
{

}
```

</details>

#### Competidores Cercanos

<details>
  <summary>
    <code>GET</code>
    <code><b>/api/competitors/{km2}</b></code>
  </summary>

#### Ejemplo de Uso

```txt
Próximamente
```

#### Ejemplo de Respuesta

```json
{
  
}
```

</details>

#### Reviews por sentimiento

<details>
  <summary>
    <code>GET</code>
    <code><b>/api/reviews-by-sentiment/{sentiment}</b></code>
  </summary>

#### Ejemplo de Uso

```txt
Próximamente
```

#### Ejemplo de Respuesta

```json
{
  
}
```

</details>

#### Reviews por restaurante

<details>
  <summary>
    <code>GET</code>
    <code><b>/api/review-of-restaurant/{id}</b></code>
  </summary>

#### Ejemplo de Uso

```txt
Próximamente
```

#### Ejemplo de Respuesta

```json
{
  
}
```
</details>

#### Usuario

<details>
  <summary>
    <code>GET</code>
    <code><b>/api/user/{id}</b></code>
  </summary>

#### Ejemplo de Uso

```txt
Próximamente
```

#### Ejemplo de Respuesta

```json
{
  
}
```

</details>



###  Modelos de Machine Learning
Con tla de poder obtener informacion de los competidores de nuestro cliente, se desarrollara un Servicio Api REST Ful para obtentener. Este servicio se desplejara en la web, ynuestro cliente podra acceder a el para obtener informacion reeavante de la empresa.

- **Modelo de clasificación:**  En base a las opniones y reviews de los usuarios que participan en paginas web de reviews, podemos desarrolar un modelo de clasificacion de usuarios. Este modelo clasificará que tipo de clientes son potenciales nuevos clientes para formar parte de una campaña de marketing.

- **Sistema de Scoring con Lenguaje natural:** Se usarán las opiniones de los clientes o reviews, para crear un modelo que determinará que tan positivia o negativa es la opinión de un cliente. Este modelo está pensado para hacer una inspección rapida de las reviews de los clientes filtrandolas según si son positivas o negativas.

- **KPI N°1: Aumento de la Cantidad de Reseñas de Clientes a lo Largo de un Año.**

**Definición**: Este KPI mide el incremento en la cantidad total de reseñas dejadas por los clientes en los diferentes locales de restaurantes durante el transcurso de un año.

**Fórmula:** ((Cantidad de Reseñas Actuales - Cantidad de Reseñas Inicial) / Cantidad de Reseñas Inicial) x 100

**Interpretación:** Un aumento positivo en este KPI indica que las estrategias de marketing y las interacciones con los clientes están motivando a más personas a dejar reseñas sobre su experiencia en los restaurantes.

**Detalle**: Los datos para este KPI se obtendrán a partir del numero total de reseñas que contiene cada local.

- **KPI N°2: Sentimiento de Reseñas en Comparación con Locales con Mejores Reseñas.**

**Definición**: Este KPI mide el sentimiento general de las reseñas para cada local de restaurante en comparación con los locales que tienen las mejores reseñas.

**Fórmula**: (Porcentaje de Reseñas Positivas del Local - Porcentaje de Reseñas Positivas de los Locales de Referencia) +
(Porcentaje de Reseñas Neutras del Local - Porcentaje de Reseñas Neutras de los Locales de Referencia) +
(Porcentaje de Reseñas Negativas del Local - Porcentaje de Reseñas Negativas de los Locales de Referencia)

**Interpretación**: Un resultado positivo indica que las reseñas del local tienen un sentimiento más positivo en comparación con los locales de referencia. Un resultado negativo sugiere un sentimiento más negativo. Un valor cercano a cero podría indicar que el sentimiento es similar al de los locales de referencia.

**Detalle**: Los datos para este KPI se obtendrán a partir del rating promedio que tenga cada local.

- **KPI N°3: Retención de Clientes.**

**Definición**: Esta métrica evalúa la capacidad de la empresa para mantener a sus clientes existentes durante un período de tiempo determinado.
**Fórmula**: ((Clientes al final del período - Nuevos clientes durante el período) / Clientes al inicio del período) x 100
**Interpretación**: Una alta retención de clientes indica la satisfacción y el valor continuo que los clientes encuentran en los servicios de la empresa. Una baja retención podría indicar problemas en la calidad del servicio o la necesidad de mejorar el soporte al cliente.

**Detalle**: Esta métrica en cuanto a la cantidad de clientes, se toma a partir de la cantidad de Reviews que se tienen. Y 

- **KPI N°4: Análisis de Conveniencia de Ubicación Basado en Turismo y Cantidad de Reseñas.**

**Definición:** Este KPI evalúa la conveniencia de establecer un nuevo negocio en un área geográfica en función de la cantidad de reseñas de locales existentes y la actividad turística en esos lugares.

**Fórmula**: Combina la cantidad de reseñas positivas, la cantidad total de reseñas y la actividad turística para calcular un índice de conveniencia de ubicación. Por ejemplo:

**Índice de Conveniencia = (Cantidad de Reseñas Positivas + Actividad Turística) / (Cantidad Total de Reseñas + Actividad Turística)**

**Interpretación:** Un valor más alto del índice de conveniencia sugiere que la ubicación tiene un buen equilibrio entre reseñas positivas y actividad turística. Esto podría indicar que es una ubicación atractiva para establecer un nuevo negocio.

---

# <h2 align="CENTER">**`Conclusiones del Proyecto`**</h2>

Por Redactar

---

## <h2 align="CENTER">**`Desarrollo del Proyecto`**</h2>


### Pipeline

<img src="src/pipeline.jpg" alt="Pipeline" width="720">

### Metodología Scrum

<img src="src/scrum-conogram.png" alt="Pipeline" width="720" >

### Documentacion

- [Reportes de Springs](https://github.com)
- [Diccionario de datos](https://github.com)
- [ETL y EDA Preliminares](https://github.com)
- [Diccionario de Datos](https://github.com)
- [Esquema de DB](https://github.com)
- [Documentacion de la API](https://github.com)
- [Analisis del Mercado Gastronómico](https://github.com)
- [Conclusiones del Proyecto](https://github.com)
- [Notebook de los Modelos de Machine Learning](https://github.com)

# <h2 align="CENTER">**`Correr en Local`**</h2>

Get to know our project, cloning the repository on your computer

```bash
   git clone https://github.com/EmilianoEmanuelSosa/Marke_Analysis_Project_Google.git
```

---

# <h2 align="CENTER">**`Desarrolladores`**</h2>

<br />

<div align=center>
  
  | <div style="width:150px"><img src = 'src/profiles_photos/Emiliano.jpeg' height = 150>  <div align="center" ><a href="https://github.com/EmilianoEmanuelSosa">Emiliano Sosa</a></div><div align="center" >Ingeniero de Datos</div><div align="center" >Ingeniero ML</div><</div> |  <div style="width:150px; display:inline-block"><img src = 'src/profiles_photos/Franco.jpeg' height = 150> <div align="center" ><a href="https://github.com/franco18min">Franco Aguilera</a></div><div align="center" >Ingeniero de Datos</div><div align="center" >Ingeniero ML</div></div> | <div style="width:150px; display:inline-block"><img src = 'src/profiles_photos/GabrielU.jpeg' height = 150>  <div align="center" ><a href="https://github.com/Gabo10DV">Gabriel Urbina</a></div><div align="center" >Ingeniero de Datos</div><div align="center" >Analista de Datos</div></div> |
  | :---: | :---: | :---: |


</div>

  | <div style="width:150px"><img src = 'src/profiles_photos/Matias.jpeg' height = 150> <div align="center" ><a href="https://github.com/https://github.com/PrismaPsy">Matías Ponce</a></div><div align="center" >Ingeniero de Datos</div><div align="center" >Analista de Datos</div></div>  | <div style="width:150px"><img src = 'src/profiles_photos/Ricardo.jpeg' height = 150><div align="center" ><a href="https://github.com/Rickhersd">Ricardo Sánchez</a></div><div align="center" >Analista Funcional</div></div> |
  | :---: | :---: |

<br />

---

# <h2 align="CENTER">**`Stack Tecnológico`**</h2>

Para la realización, se utilizaron las siguientes herramientas. Cada una escogida para usos diferentes

<div style="display:flex; width:100%">
  <div style="display:flex;flex-direction:column; width:50%">
    <strong>Organización de Equipo</strong>
    <li>Discord</li>
    <li>Notion</li> 
    <li>Whatsapp</li>
    <li>Jira</li> 
    <li>Google Meet</li> 
    <li>Github</li> 
  </div>
  <div style="display:flex;flex-direction:column; width:50%">
  <strong>Herramientas Generales</strong>
    <li>Python</li>
    <li>Pandas</li>
    <li>VSCode</li>
    <li>Google Collab</li> 
    <li>Google Drive</li>
    <li>Git</li>
    <li>PowerPoint</li>
  </div>
</div>

<br />

<div style="display:flex; width:100%">
  <div style="display:flex;flex-direction:column; width:50%">
    <strong>Servicio API REST</strong>
    <li>Django</li>
    <li>GeoPandas</li> 
    <li>Postgress</li>
    <li>Numpy</li>
  </div>
  <div style="display:flex;flex-direction:column; width:50%">
  <strong>Machine Learning</strong>
    <li>TensorFlow</li>
    <li>Sklearn</li>
    <li>Keras</li>
  </div>
</div>

<br />

<div style="display:flex; width:100%">
  <div style="display:flex;flex-direction:column; width:50%">
    <strong>Análisis de Datos</strong>
    <li>Power BI</li>
    <li>Sreamlit</li> 
    <li>Matplotlib</li>
    <li>Vega Altair</li> 
    <li>Seaborn</li> 
    <li>Matplotlib</li>
    <li>Seaborn</li> 
  </div>
  <div style="display:flex;flex-direction:column; width:50%">
  <strong>DEVops</strong>
    <li>AWS (despliegue para la demo)</li>
    <li>NEON</li>
    <li>Vercel (despliegue continuo)</li>
  </div>
</div>

<br />

---

# <h2 align="CENTER">**`Presentación Del Proyecto`**</h2>

Proximamente

<!-- TO-DO:[Explanatory video]() -->