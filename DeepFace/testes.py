import os
import cv2
import json
import numpy as np
import threading
import concurrent.futures
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

#aperta p chama função extrair rosto do frame ( funcao extract )
def extrair_rosto(frame):
    faces = DeepFace.extract_faces(frame,
    detector_backend=backends[0],  # Detector usado
    enforce_detection=True,  # Garante que há um rosto
    align=True,  # Alinha o rosto
    expand_percentage=0)  # Expande a área do rosto

    if not faces:
        print("Nenhum rosto detectado.")
        return

    for face in faces:
        print("Detectado.")
        facial_area = face['facial_area']
        x, y, w, h = facial_area['x'], facial_area['y'], facial_area['w'], facial_area['h']
        face_img = frame[y:y + h, x:x + w]  # Recorta a face
        #cv2.imshow("Rosto Detectado", face_img)
        threading.Thread(target=analise, args=(frame.copy(),), daemon=True).start()


# funcao find, funcao analyze
def analise(face_img):
    # realizar comparação com banco de dados
    db_path = r"C:\Users\rafae\OneDrive\Desktop\python\DeepFace\.venv\database"
    matches = DeepFace.find(img_path=face_img, db_path=db_path, model_name=models[1], enforce_detection=True)

    # Realiza a análise do rosto (independente de estar no banco de dados)
    result = DeepFace.analyze(face_img, actions=['age', 'gender', 'emotion'], enforce_detection=True)
    result_convertido = convert_types(result)
    print("Final do .find")
    if any(not df.empty for df in matches):  # Se algum rosto for encontrado
        salvar_resultado(matches, result_convertido)
        print("Processo finalizado")
    else:
        salvar_erro(result_convertido)
        print("Processo finalizado")


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

#funções salvar resultados txt
def salvar_resultado(matches, result_convertido):
    with open("resultado.txt", "a", encoding="utf-8") as f:
        data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"\n🔹 Registro realizado em: {data_hora}")
        f.write(f"\n👥 Quantidade de rostos identificados: {len(matches)}\n")

        for i in range(len(matches)):
            if not matches[i].empty:
                for index, row in matches[i].iterrows():
                    file_path = row['identity']
                    file_name = os.path.basename(file_path)
                    f.write(f"✅ Correspondência encontrada: {file_name}\n")

        f.write("\n📊 Resultados da Análise Facial:\n")
        f.write(json.dumps(result_convertido, indent=4, ensure_ascii=False))
        f.write("\n" + "="*50 + "\n")
    print("Salvo em resultado")

def salvar_erro(result_convertido):
    with open("resultado_semDB.txt", "a", encoding="utf-8") as f:
        data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"\n❌ Rosto não identificado - Registro em: {data_hora}\n")
        f.write("\n📊 Resultados da Análise Facial:\n")
        f.write(json.dumps(result_convertido, indent=4, ensure_ascii=False))
        f.write("\n" + "="*50 + "\n")
    print("Salvo em erro")


webcam = cv2.VideoCapture(0)
pic = 0

def processar_rosto(frame):  #fazer thread para evitar travamento de webcam
    extrair_rosto(frame)

# Criando um pool de threads para evitar criar threads infinitas
executor = concurrent.futures.ThreadPoolExecutor(max_workers=2)

while True:
    ret, frame = webcam.read()
    if not ret:
        print("Erro leitura webcam")
        break

    cv2.imshow("Detecção de Rosto", frame)

    if cv2.waitKey(1) & 0xFF == ord("p"):
        pic += 1
        print(f"Picture {pic}")
        executor.submit(processar_rosto, frame.copy())

    if cv2.waitKey(1) & 0xFF == ord("f"):
        webcam.release()
        cv2.destroyAllWindows()
        print("Close")
        break

