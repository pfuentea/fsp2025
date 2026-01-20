import cv2
import os
BASE_DIR=os.path.dirname(__file__)
nombre_archivo="persona.jpg"
RUTA_ARCHIVO=os.path.join(BASE_DIR,nombre_archivo)

#Cargamos el clasificador de rostros
face_cascade=cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

#Cargamos la imagen
image =cv2.imread(RUTA_ARCHIVO)

#convirtiendo la imagen a gris
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

#detectar rostros
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.5,
    minNeighbors=5
)

#dibujar rectagulos
for (x,y,w,h) in faces:
    cv2.rectangle(
        image,
        (x,y),
        (x+w,y+h),
        (0,255,0),
        2
    )

#Mostramos la imagen
cv2.imshow("Deteccion de rostros",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
