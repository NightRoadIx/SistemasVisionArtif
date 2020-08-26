import cv2
import numpy as np

# Crear una imagen en negro
img = np.zeros((512,512,3), np.uint8)

# Dibujar una línea azul diagonal con un ancho de 5 px
img = cv2.line(img,(0,0),(511,511),(255,0,0),5)				# imagen, punto inicial, punto final, color, anchura en px

# Rectángulo
img = cv2.rectangle(img,(384,0),(510,128),(0,255,0),5)		# imagen, esquina superior izq, esquina superior der, anchura px

# Círculo
img = cv2.circle(img,(447,63), 63, (0,0,255), -1)			# imagen, centro, radio, color, anchura px (-1 cículo)

'''
Para dibujar una elipse se requiere de pasar varios argumentos. Uno es el centro de la elipse (x,y)
El siguiente argumento es la longitud de los ejes (mayor, menor). Ángulo de rotación de la elipse en dirección antihorario
Ángulo de inicio y ángulo de final denota el arco medido en dirección horaria del eje mayor.
Esto es dar valores de 0 y 360 dan la elipse completa
'''
img = cv2.ellipse(img,(256,256),(100,50),0,0,180,255,-1)

# Polígono
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
img = cv2.polylines(img,[pts],True,(0,255,255))

# Añadir texto
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv2.LINE_AA)
# imagen, texto, coords esq inf izq, fuente, multiplo escala base de la fuente, color, anchura px, tipo de línea

# Mostrar la imagen
cv2.imshow('Imagen',img)
k = cv2.waitKey(0)
cv2.destroyAllWindows()