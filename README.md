## Proyecto de Asistente para el Lenguaje de Señas

Este proyecto utiliza técnicas de visión computacional para reconocer y reproducir letras en lenguaje de señas, ayudando a personas en el proceso de aprendizaje de señas. Este repositorio incluye modelos preentrenados que se pueden utilizar de inmediato para identificar señas de letras específicas.

## Requisitos

- **Python 3.9.0**
- **Git** (opcional, si prefieres clonar el repositorio en lugar de descargar el zip)

### Dependencias adicionales

Este proyecto requiere ciertas librerías que puedes instalar siguiendo los pasos a continuación.

## Instrucciones de Instalación

1. **Clona el repositorio**

   Si tienes \`git\` instalado, puedes clonar el repositorio con el siguiente comando:

   ```bash
   git clone https://github.com/computervisioneng/sign-language-detector-python.git
   ```

   Alternativamente, puedes descargar el proyecto como un archivo ZIP desde GitHub y extraerlo en tu computadora.

2. **Instala las dependencias**

   Asegúrate de tener \`Python 3.9.0\` instalado. Luego, abre una terminal en el directorio del proyecto y ejecuta los siguientes comandos para instalar las dependencias requeridas:

 ```bash
  pip install opencv-python==4.7.0.68
  pip install mediapipe==0.10.0
  pip install scikit-learn==1.2.0
  pip install numpy==1.26.4
  pip install PyQt5==5.15.11
  pip install PyQt5-Qt5==5.15.2
  pip install PyQt5_sip==12.15.0
  pip install python-dateutil==2.9.0.post0
  pip install pyttsx3==2.98
  pip install pywin32==308
```
3. **Ejecuta el modelo**

   Este repositorio ya incluye los modelos entrenados necesarios para identificar señas. Para probar el modelo, abre el módulo \`Testeo_Modelo\` en un editor como Visual Studio Code y ejecuta el archivo dando clic en \\"Run\\".

4. **Haz la seña**

   Una vez que el script esté corriendo, puedes realizar una seña y el modelo intentará identificar la letra correspondiente. Por ejemplo, puedes intentar hacer las señas para las letras \`U\`, \`N\`, \`A\` y \`H\`.

## Notas adicionales

- **Precisión del modelo**: La precisión de los resultados depende de la calidad de la cámara y el entorno de iluminación. Para mejores resultados, usa el modelo en un área bien iluminada.
- **Posibles problemas**: Si encuentras problemas con la instalación o ejecución, verifica que todas las dependencias estén instaladas correctamente y que estás usando la versión de Python recomendada.
