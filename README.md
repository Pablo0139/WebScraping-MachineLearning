# WebScraping-MachineLearning
DISEÑO DE UN PROTOTIPO DE ANÁLISIS DE INFORMACIÓN ONLINE BASADO EN DEEP LEARNING MEDIANTE TENSORFLOW. Código realizado para el Trabajo Fin de Grado de Ingeniería Electrónica Industrial y Automática.

En este repositorio se encuentran recogidos los dos scripts utilizados en el prototipo.

"WebScrp.py" consiste en un script capaz de obtener automáticamente los datos más relevantes de las noticias (titular, cuerpo de la noticia, clasificación, ...) 
que aparecen en diferentes periódicos online españoles. El objetivo consiste en recopilar la máxima información clasificada posible que sirva como ejemplo para
el entrenamiento de una red neuronal de clasificación automática.

"Modelo.py" se trata de un script donde una vez que se preparan los datos obtenidos anteriormente se entrena una red neuronal tipo perceptrón multicapa que sea capaz
de clasificar los diferentes cuerpos de noticias, proporcionados como entrada, en su respectiva categoría.
