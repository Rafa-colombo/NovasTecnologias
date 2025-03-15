import os
import cv2
import json
import numpy as np
import time
from datetime import datetime
from deepface import DeepFace

#modelos para reconhecimento
models = [
  "VGG-Face",
  "Facenet",
  "Facenet512",
  "OpenFace",
  "DeepFace",
  "DeepID",
  "ArcFace",
  "Dlib",
  "SFace",
  "GhostFaceNet",
]

#backends para analyse
backends = [
  'opencv',
  'ssd',
  'dlib',
  'mtcnn',
  'fastmtcnn',
  'retinaface',
  'mediapipe',
  'yolov8',
  'yunet',
  'centerface',
]

# Converte todos os valores para tipos Python nativos (int, float, str)
def convert_types(obj):
    if isinstance(obj, np.integer):
        return int(obj)
    elif isinstance(obj, np.floating):
        return float(obj)
    elif isinstance(obj, dict):
        return {k: convert_types(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [convert_types(v) for v in obj]
    else:
        return obj

#aperta p chama função extrair rosto do frame ( funcao extract )
def extrair_rosto(frame):
    faces = DeepFace.extract_faces(frame,
    detector_backend=backends[0],  # Detector usado
    enforce_detection=False,  # Garante que há um rosto
    align=True,  # Alinha o rosto
    expand_percentage=0)  # Expande a área do rosto

    #print("Coordenadas: ", faces)

    if len(faces) > 0:
        for face in faces:
            facial_area = face['facial_area']
            x, y, w, h = facial_area['x'], facial_area['y'], facial_area['w'], facial_area['h']
            face_img = frame[y:y + h, x:x + w]  # Recorta a face
            cv2.imshow("Rosto Detectado", face_img)
            analise(face_img)
    else:
        print("Nenhum rosto detectado.")


# funcao find, funcao analyze
def analise(face_img):
    # realizar comparação com banco de dados
    db_path = r"C:\Users\rafae\OneDrive\Desktop\python\DeepFace\.venv\database"
    matches = DeepFace.find(img_path=face_img, db_path=db_path, model_name=models[1], enforce_detection=True)

    with open("resultado.txt", "a", encoding="utf-8") as f:
        f.write(f"\nQnt identificado: {len(matches)}")
        data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Formato: "AAAA-MM-DD HH:MM:SS"
        f.write(f"\nRegistro realizado em: {data_hora}\n")
        rosto_reconhecido = False  # Flag para verificar se um rosto foi encontrado no banco

        # Itera sobre os DataFrames retornados por .find()
        for i in range(len(matches)):
            if not matches[i].empty:  # Verifica se há resultados no DataFrame atual
                rosto_reconhecido = True
                for index, row in matches[i].iterrows():
                    file_path = row['identity']
                    file_name = os.path.basename(file_path)
                    f.write(f"✅ Correspondência encontrada: {file_name}\n")

            if not rosto_reconhecido:
                f.write("\n❌ Rosto não identificado no banco de dados.\n")

            result = DeepFace.analyze(face_img, actions=['age', 'gender', 'emotion'], enforce_detection=True)
            result_convertido = convert_types(result)
            f.write("\nResultados da Análise Facial:\n")
            f.write(json.dumps(result_convertido, indent=4, ensure_ascii=False))

#leitura da webcam
webcam = cv2.VideoCapture(0)
pic = 0

while True:
    ret, frame = webcam.read()
    if not ret:
        print("Erro leitura webcam")
        break

    cv2.imshow("Detecção de Rosto", frame)

    if cv2.waitKey(1) & 0xFF == ord("p"):
        pic+=1
        print(f"Picture {pic}")
        extrair_rosto(frame)
        print("Processo finalizado")

    if cv2.waitKey(1) & 0xFF == ord("f"):
        print("Close")
        break

webcam.release()
cv2.destroyAllWindows()