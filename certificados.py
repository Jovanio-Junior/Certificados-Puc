from pandas import options
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

options = Options()
options.add_argument('--disable-infobars')
options.add_argument('start-maximized')
options.add_argument('--disable-extensions')
options.add_argument('--disable-notifications')
#options.add_argument('--headless')

drive = webdriver.Chrome(chrome_options=options)
drive2 = webdriver.Chrome(chrome_options=options)
Nome = "JOVANIO JOSE GALVAO JUNIOR"

drive.get("https://sites.pucgoias.edu.br/certificados/")


lista = drive.find_elements_by_class_name('listaCertificados')
tamCertificadoList = len(lista)

time.sleep(5)
class Certificado:
    Evento = ""
    Link = ""
    def __init__(self, Evento, Link):
        self.Evento = name
        self.Link = age

listaDeCertificados = []

for i in range(tamCertificadoList):
    cssA = lista[i].find_element(by=By.CSS_SELECTOR,value='a')
    link = cssA.get_attribute('href')
    drive2.get(link)
    flag = drive2.find_elements(by=By.LINK_TEXT,value=Nome)
    if(flag):
        link2 = flag[0].get_attribute('href')
        listaDeCertificados.append(i)
        listaDeCertificados.append(lista[i].text)
        listaDeCertificados.append(link2)
        #print(listaDeCertificados)
        #flag[0].click()
        #break
        
    
for i in range(0, len(listaDeCertificados),3):
    print("Certificado numero: ", listaDeCertificados[i])
    print("Evento: ", listaDeCertificados[i+1])
    print("Link do Certificado: ", listaDeCertificados[i+2])
    