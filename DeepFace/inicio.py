from deepface import DeepFace


DeepFace.stream(
    db_path=r"C:\Users\rafae\OneDrive\Desktop\python\DeepFace\.venv\database",  # Caminho do banco de dados de imagens
    model_name="Facenet",  # Modelo de reconhecimento (pode ser "VGG-Face", "Facenet", "OpenFace", etc.)
    detector_backend="opencv",  # Detector de rostos (pode ser "opencv", "ssd", "mtcnn", etc.)
    distance_metric="cosine",  # Métrica de comparação (pode ser "euclidean", "euclidean_l2", "cosine")
    enable_face_analysis=True,  # Ativa a análise de emoção, idade e gênero
    source=1,  # ID da câmera (0 para webcam principal, 1 para externa, etc.)
    time_threshold=3,  # Tempo mínimo (segundos) para considerar um rosto reconhecido novamente
    frame_threshold=15  # Quantidade de frames consecutivos necessários para reconhecer um rosto
)