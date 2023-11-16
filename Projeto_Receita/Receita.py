import cv2
import pytesseract

# Carregar a imagem da receita
image_path = 'receita/Receita.JPG'
image = cv2.imread(image_path)

# Verificar se a imagem foi carregada com sucesso
if image is None:
    print("Erro ao carregar a imagem.")
else:
    # Pré-processamento da imagem (redimensionamento, filtro de ruído, etc.)
    # Redimensionar a imagem para um tamanho adequado para o OCR
    image = cv2.resize(image, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

    # Converter a imagem para escala de cinza para melhorar a precisão do OCR
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Aplicar limiarização para melhorar o contraste do texto
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

    # Redução de ruído usando operações morfológicas
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    cleaned_image = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

    # Reconhecimento de texto usando Tesseract
    extracted_text = pytesseract.image_to_string(cleaned_image)

    # Análise do texto para extrair informações-chave
    patient_name = None
    prescribed_medications = []
    dosages = []

    # Exemplo de busca por nome do paciente e medicamentos prescritos
    if "Nome do Paciente:" in extracted_text:
        patient_name = extracted_text.split("Nome do Paciente:")[1].split("\n")[0].strip()

    if "Medicamentos Prescritos:" in extracted_text:
        medications_text = extracted_text.split("Medicamentos Prescritos:")[1]
        for line in medications_text.split("\n"):
            if line:
                medication, dosage = line.split("-")
                prescribed_medications.append(medication.strip())
                dosages.append(dosage.strip())

    # Geração do resumo
    summary = {
        "Nome do Paciente": patient_name,
        "Medicamentos Prescritos": prescribed_medications,
        "Dosagens": dosages
    }

    # Saída do resumo
    for key, value in summary.items():
        print(f"{key}: {value}")
