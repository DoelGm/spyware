import cv2
import time
import os
import requests

def capture_and_upload():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error al capturar la imagen")
            break

        timestamp = int(time.time())
        filename = f'captura_{timestamp}.jpg'
        cv2.imwrite(filename, frame)

        print(f'Imagen capturada: {filename}')

        upload_image(filename)
        
        # Espera 5 segundos antes de capturar la siguiente imagen
        time.sleep(5)

    cap.release()

def upload_image(filename):
    url = 'http://localhost:5000/upload'  # Reemplaza con tu URL del servidor
    files = {'file': open(filename, 'rb')}
    response = requests.post(url, files=files)

    if response.status_code == 200:
        print(f'Imagen {filename} subida exitosamente')
        os.remove(filename)
    else:
        print(f'Error al subir la imagen {filename}')

if __name__ == '__main__':
    capture_and_upload()
