import base64

# Caminho da imagem original (mude se necessário)
input_image_path = "foto.jpg"

# Caminho do arquivo de saída
output_text_file = "foto.txt"

try:
    with open(input_image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
        
    with open(output_text_file, "w") as text_file:
        text_file.write(encoded_string)

    print(f"Base64 da imagem salva com sucesso em '{output_text_file}'")

except Exception as e:
    print(f"Erro ao processar imagem: {e}")
