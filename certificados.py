from ast import Try
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


opcoes = [1,1,1,1,0]
Nome = None
listaDeCertificados = []

codigo = -1
while codigo != 0:
    if Nome == None:
        Nome = input("Digite seu nome: ")
    print("Nome Atual: ", Nome)
    print("1 - Definir novo Nome: ")
    print("2 - inicar busca: ")
    print("3 - imprimir resultados encontrados")
    print("4 - Configurações")
    codigo = int(input("Selecione a opção que deseja: (0: para sair) "))
    if codigo >= 0:
        if codigo == 1:
            Nome = input("Digite seu nome: ")
        else:
            if codigo == 2:
                try:
                    drive = webdriver.Chrome(chrome_options=options)
                    drive2 = webdriver.Chrome(chrome_options=options)
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
                except:
                    codigo = -1
            else:
                if codigo == 3:
                    print("certificados encontrados: ", len(listaDeCertificados))
                    for i in range(0, len(listaDeCertificados),3):
                        print("Certificado numero: ", listaDeCertificados[i])
                        print("Evento: ", listaDeCertificados[i+1])
                        print("Link do Certificado: ", listaDeCertificados[i+2])
                else:
                    if codigo == 4:
                        config = -1
                        while config != 0:
                            print("Argumentos atuais: ", options.arguments)
                            print("Vet", opcoes)
                            print(opcoes[0] == 0 and "1 - para Ativar infobars" or "1 - para Desativar infobars")
                            print(opcoes[1] == 0 and "2 - para start-maximized" or "2 - para Desativar start-maximized")
                            print(opcoes[2] == 0 and "3 - para disable-extensions" or "3 - para disable-extensions")
                            print(opcoes[3] == 0 and "4 - para disable-notifications" or "4 - para disable-notifications")
                            print(opcoes[4] == 0 and "5 - para ativar headless" or "5 - para Desativar headless")
                            config = int(input("Selecione a opção: (0: para sair)" ))
                            if config == 1:
                                if opcoes[0] == 1:
                                    options.arguments.remove('--disable-infobars')
                                    opcoes[0] = 0
                                else:
                                    options.add_argument('--disable-infobars')
                                    opcoes[0] = 1
                            else:
                                if config == 2:
                                    if opcoes[1] == 1:
                                        options.arguments.remove('start-maximized')
                                        opcoes[1] = 0
                                    else:
                                        options.add_argument('start-maximized')
                                        opcoes[1] = 1
                                else:
                                    if config == 3:
                                        if opcoes[2] == 1:
                                            options.arguments.remove('--disable-extensions')
                                            opcoes[2] = 0
                                        else:
                                            options.add_argument('--disable-extensions')
                                            opcoes[2] = 1
                                    else:
                                        if config == 4:
                                            if opcoes[3] == 1:
                                                options.arguments.remove('--disable-notifications')
                                                opcoes[3] = 0
                                            else:
                                                options.add_argument('--disable-notifications')
                                                opcoes[3] = 1
                                        else:
                                            if config == 5:
                                                if opcoes[4] == 1:
                                                    options.arguments.remove('--headless')
                                                    opcoes[4] = 0
                                                else:
                                                    options.add_argument('--headless')
                                                    opcoes[4] = 1
                            