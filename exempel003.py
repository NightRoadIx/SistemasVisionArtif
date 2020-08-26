import cv2
import numpy as np

drawing = False # true si el ratón está presionado
mode = True # si es True, dibujar un rectángulo. Presionar 'm' para cambiar a una curva
ix,iy = -1,-1

# Función que llama al ratón
def draw_circle(event,x,y,flags,param):
    global ix,iy,drawing,mode

	# Evento de presionar el botón izquierdo
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y

	# Evento de movimiento del ratón
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
            else:
                cv2.circle(img,(x,y),5,(0,0,255),-1)

	# Cuando se levanta el botón izquierdo (se deja de presionar)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
        else:
            cv2.circle(img,(x,y),5,(0,0,255),-1)
			
img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

# Ciclo infinito de acción 
while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('m'):
        mode = not mode
    elif k == 27:
        break

cv2.destroyAllWindows()