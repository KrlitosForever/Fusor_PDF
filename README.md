#  <div align="center"> Fusor_PDF</div>

<div align="center">

![](logo.ico) 

</div>

El programa ofrece una solución eficiente y versátil para unir archivos PDF, permitiendo a los usuarios combinar múltiples documentos en uno solo de forma rápida y sencilla. Con la capacidad de ser ejecutado tanto a través de la terminal como mediante un ejecutable, garantiza una experiencia de usuario conveniente y adaptable a diferentes preferencias y necesidades. Ya sea para fusionar documentos de trabajo, proyectos académicos o cualquier otro propósito, mi programa proporciona una herramienta confiable y accesible para simplificar el proceso de manejo de archivos PDF.

## Dependencias a utilizar
Para asegurar el correcto funcionamiento de este programa, es necesario instalar las dependencias especificadas en el archivo requirements.txt. Puedes hacerlo ejecutando el siguiente comando:

```python
pip install -r requirements.txt
```

## Ejecutable
Fusor también puede ser utilizado como un ejecutable independiente, lo que facilita su uso en diferentes plataformas, especialmente en sistemas Windows. Para generar un archivo .exe en Windows, sigue estos pasos:

1. Abre una terminal.
2. Navega hasta el directorio donde se encuentra el archivo Fusor.py.
3. Ejecuta el siguiente comando:

```bash
pyinstaller --windowed --onefile --icon=./logo.ico Fusor.py
```

Con esto se generará un archivo Fusor.exe en la misma carpeta. Este archivo puede ser compartido y utilizado en cualquier computadora con Windows sin necesidad de tener instalado Python ni ninguna dependencia adicional.

