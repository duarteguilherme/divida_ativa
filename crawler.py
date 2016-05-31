import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
import re
from binascii import a2b_base64
from PIL import Image

class Crawler:
    def __init__(self):
        self.sessao = requests.Session()
        self.pagina = self.sessao.get('https://www2.pgfn.fazenda.gov.br/ecac/contribuinte/devedores/listaDevedores.jsf',
                verify=False)
        print(self.pagina.text)
        self.le_captcha()

    def le_captcha(self):
        v = self.sessao.post('http://captcha.servicoscorporativos.serpro.gov.br/captcha/1.0.0/imagem','a2e6a479dc9a4fde9014b57856ee77c7')
        base_png = re.split('@',v.text)
        texto = a2b_base64(base_png[1])
        with open('arquivo.png','wb') as arquivo:
            arquivo.write(texto)
        img = Image.open('arquivo.png')
        img.show()
    

crawler = Crawler()
