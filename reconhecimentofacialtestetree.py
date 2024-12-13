import cv2

# Carregar o classificador de rosto pré-treinado
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Caminho para a imagem (assumindo que está na mesma pasta que o código)
image_path = "Cristiano_Ronaldo_imagem.png"  # Nome da imagem na mesma pasta

# Tentar carregar a imagem
image = cv2.imread(image_path)

# Verificar se a imagem foi carregada corretamente
if image is None:
    print(f"Erro ao carregar a imagem. Verifique o caminho: {image_path}")
    exit()  # Encerra o script caso a imagem não seja carregada

# Converter a imagem para escala de cinza (necessário para o classificador)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detectar rostos na imagem
faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# Adicionar caixas nos rostos detectados
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

# Exibir o resultado
cv2.imshow("Rostos Detectados", image)

# Aguardar uma tecla ser pressionada e depois fechar a janela
cv2.waitKey(0)
cv2.destroyAllWindows()
iii

