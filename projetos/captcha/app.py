# pip install captcha
from captcha.image import ImageCaptcha

# configura a imagem

image = ImageCaptcha(width=280, height=90)

#Texto escolhido para o captcha
texto = "Matheus Lindo"

#Gera a imagem do captcha

data = image.generate(texto)

# Salva imagem do caminho escolhido
image.write(texto, './captcha/captcha.png')


