import os
import shutil
from PIL import Image
from datetime import datetime

# Define como será a criação da estrutura de pastas para organização das imagens baseadas na data de criação da foto
def caminho_da_pasta_com_data_de_criacao_da_foto(arquivo):
    date = data_de_criacao_da_foto(arquivo)
    return date.strftime('%Y') + '/' + date.strftime('%Y-%m-%d')

# Consegue a data de criação da foto, acessando as propriedades do arquivo utilizando exif do Piloow
def data_de_criacao_da_foto(arquivo):
    foto = Image.open(arquivo)
    informacao = foto.getexif()
    if 36867 in informacao:
        data = informacao[36867]
        data = datetime.strptime(data, '%Y:%m:%d %H:%M:%S')
    else:
        data = datetime.fromtimestamp(os.path.getatime(arquivo))

    return(data)

# função que move as fotos para a pasta criada

def move_fotos(arquivo):
    nova_pasta = caminho_da_pasta_com_data_de_criacao_da_foto(arquivo)
    if not os.path.exists(nova_pasta):
        os.makedirs(nova_pasta)
    shutil.move(arquivo, nova_pasta + '/' + arquivo)

#  Testes de resultado

print('Data de criação:')
print(data_de_criacao_da_foto('ny.jpg'))
print('Estrutura de como será a criação da pasta baseada no ano de criacao da foto:')
print(caminho_da_pasta_com_data_de_criacao_da_foto('ny.jpg'))
# print('Agora vai começar a criação da pasta e mover o arquivo para a nova pasta')
# print(move_fotos('ny.jpg'))
# print(move_fotos('a.jpg'))
# print(move_fotos('b.jpg'))
# print(move_fotos('c.jpg'))
# print(move_fotos('d.jpg'))
# print(move_fotos('e.jpg'))