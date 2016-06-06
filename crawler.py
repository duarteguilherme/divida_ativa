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
        self.texto_pag = BeautifulSoup(self.pagina.text)
        self.le_captcha()
#        for i in range(0,26):
#            print(i)
        i = 0
        self.creating_data_letter(i)
        self.pagina_post = self.sessao.post()
    def le_captcha(self):
        v = self.sessao.post('http://captcha.servicoscorporativos.serpro.gov.br/captcha/1.0.0/imagem','ce681cad54d64970aa17f4e3ace4eadb')
        base_png = re.split('@',v.text)
        texto = a2b_base64(base_png[1])
        with open('arquivo.png','wb') as arquivo:
            arquivo.write(texto)
        img = Image.open('arquivo.png')
        img.show()
        self.captcha = input('Qual e o captcha, malandro:')
        l = self.sessao.post('https://www2.pgfn.fazenda.gov.br/captchaserpro/captcha/1.0.0/imagem','ce681cad54d64970aa17f4e3ace4eadb', verify=False)
        self.token = re.split('@',l.text)[0]

    def creating_data_letter(self, number):
        self.dados = {}
        self.dados['listaDevedoresForm'] = 'listaDevedoresForm',
        self.dados['listaDevedoresForm:captcha'] = self.captcha
        self.dados['txtToken_captcha_serpro_gov_br'] = self.token
        self.dados['listaDevedoresForm:tipoConsultaRadio'] = 'LETRA'
        self.dados['listaDevedoresForm:identificacaoInput:'] = ''
        self.dados['listaDevedoresForm:faixasInput:'] = ''
        self.dados['listaDevedoresForm:nomeInput:'] = ''
        self.dados['javax.faces.ViewState'] = self.texto_pag.find(id='javax.faces.ViewState')['value']
        print(self.dados)
        self.dados['listaDevedoresForm:j_id71:0:j_id72']  = 'listaDevedoresForm:j_id71:' + self.number + ':j_id72'

    def creating_data_page(self, number):
        self.dados = {}
        self.dados['AJAXREQUEST'] = '_viewRoot',
        self.dados['listaDevedoresForm'] = 'listaDevedoresForm',
        self.dados['listaDevedoresForm:captcha'] = self.captcha
        self.dados['txtToken_captcha_serpro_gov_br'] = self.token
        self.dados['listaDevedoresForm:tipoConsultaRadio'] = 'LETRA'
        self.dados['listaDevedoresForm:identificacaoInput:'] = ''
        self.dados['listaDevedoresForm:faixasInput:'] = ''
        self.dados['listaDevedoresForm:nomeInput:'] = ''
        self.dados['javax.faces.ViewState'] = self.texto_pag.find(id='javax.faces.ViewState')['value']
        print(self.dados)
        self.dados['ajaxSingle']:listaDevedoresForm:devedoresTableScroller
        self.dados['listaDevedoresForm:devedoresTableScroller'] = 2
        self.dados['AJAX:EVENTS_COUNT'] = 1
        crawler = Crawler()
