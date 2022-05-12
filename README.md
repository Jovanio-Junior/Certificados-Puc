# automatização de busca de certificados no site da PUC-GOIAS

###
    Na presente dada(12/05/2022) o site de certificados da puc-goias tem 1911 certificados, a busca manual fica inviavel
    Este pequeno codigo, em py usando selenium visa facilitar a busca de certificados.

## Instalação
    Instalação do Python
    Instalação do selenium
        pip install selenium
        ou
        pip3 install selenium
    Baixar o Web driver do chrome ou outro navegador
       OBS: todos os testes foram feitos usando o chrome como base pode haver erros em outros navegadores
       Primeiramente apertar tecla do windows + r e digitar 
        na janela que abrir digitar "powershell"
        com o powershell aberto inserir o seguinte comando
        >
            $(Get-Package -Name "Google Chrome").Version
        como resposta deve ser retornado a versão do chrome
            > $(Get-Package -Name "Google Chrome").Version
                101.0.4951.64

        com a versão do chrome em mãos entrar no site 
            https://chromedriver.chromium.org/downloads
                busque o web driver para seu sistema operacional e baixe
                    coloque ele na mesma pasta de seu codigo



## modificações
    Alteração no nome que vai ser buscado.
        linha 16 do codigo
            Nome = "seu nome aqui"
    Alteração no modo de execução 
        ha dois modos:
            sem cabeça - não mostra a execução no navegador.
            ou
            com cabeça - mostra passo a passo oque esta acontecendo
        Para alterar:
            linha 12
                Remover o comentario('#')

## execução
    pyhton certificados.py


## Exemplo de saida
    Certificado numero:  32
    Evento:  (3º Circuito Ciência em Casa) ECEC - Metodologias Ativas e a Aprendizagem Criativa no  Ensino de Ciências (04 de maio de 2021)
    Link do Certificado:  https://sites.pucgoias.edu.br/certificados/ver/61617bfeb9ec85b5de10e014918feb26
    Certificado numero:  33
    Evento:  (3º Circuito Ciência em Casa) ECEC - O Design Thinking Dentro Do Processo De Product   Discovery (19 de Maio de 2021)
    Link do Certificado:  https://sites.pucgoias.edu.br/certificados/ver/f87a723f05568c3fb66a49d979510058
    Certificado numero:  56
    Evento:  (3º Circuito Ciência em Casa) ECOM - Big Data: Fator Determinante Nas Tomadas de Decisão   Estratégicas e Editoriais (19 de Maio de 2021)
    Link do Certificado:  https://sites.pucgoias.edu.br/certificados/ver/4649fd04e962ba9b603b6cba46ad5e7b
    Certificado numero:  93
    Evento:  (3º Circuito Ciência em Casa) EENG - Introdução ao BIM - Building Information Modeling (19     de Maio de 2021)
    Link do Certificado:  https://sites.pucgoias.edu.br/certificados/ver/1886b6f71dc7fedbe54745508fd2c842
    Certificado numero:  202
    Evento:  (Circuito Ciência em Casa) ECEC - Gameficação na LG Lugar de Gente e Apresentação da LG e  do Programa de Estágio (03 de Novembro de 2020)
    Link do Certificado:  https://sites.pucgoias.edu.br/certificados/ver/b0812e6e2c3acb933cbb85b712fee0d9
    Certificado numero:  203
    Evento:  (Circuito Ciência em Casa) ECEC - Mineração de Dados (17 de Novembro de 2020)
    Link do Certificado:  https://sites.pucgoias.edu.br/certificados/ver/8254a3d208742be2293884c6e74f497d
    Certificado numero:  208
    Evento:  (Circuito Ciência em Casa) ECEC - XX Jornada Goiana de Engenharia de Software (26 de   Novembro de 2020)
    Link do Certificado:  https://sites.pucgoias.edu.br/certificados/ver/5aeba3b47b450608c0dc4c86d11faeb5
    Certificado numero:  507
    Evento:  Circuito Ciência em Casa - ECEC - Campus Party Digital Goiás: Re Boot Our Planet
    Link do Certificado:  https://sites.pucgoias.edu.br/certificados/ver/a5a3ae79ff5f410accd181c5cd4ed5c6
    Certificado numero:  676
    Evento:  ECEC - Apresentação de Trabalho de TCC: Automação Residencial Utilizando Arduino (08 de    Junho de 2021)
    Link do Certificado:  https://sites.pucgoias.edu.br/certificados/ver/5a74399c385c2984d3f44536d538bdc5
    Certificado numero:  688
    Evento:  ECEC - Apresentação de Trabalho de TCC: Estudo de Algoritmos Para Análise de Sentimentos em    Jogos Online Por Tópicos de Conversação (04 de Junho de 2021)
    Link do Certificado:  https://sites.pucgoias.edu.br/certificados/ver/b35a5a06d8de65048e7a304f70350972
    Certificado numero:  689
    Evento:  ECEC - Apresentação de Trabalho de TCC: Estudo de Caso: Estratégia de Lucro na Bolsa De    Valores Utilizando Algoritmos Preditivos (07 de Junho de 2021)
    Link do Certificado:  https://sites.pucgoias.edu.br/certificados/ver/2b40a21c259ae2d7877f0b3a9979b44c
    Certificado numero:  692
    Evento:  ECEC - Apresentação de Trabalho de TCC: Estudo de Caso: Ransomware: Segurança da Informação    e Prevenção (08 de Junho de 2021)
    Link do Certificado:  https://sites.pucgoias.edu.br/certificados/ver/f3a89a683d52e6b6c6072f6afe3c9444
    Certificado numero:  693
    Evento:  ECEC - Apresentação de Trabalho de TCC: Estudo de Caso: Virtualização de Servidores (04 de     Junho de 2021)
    Link do Certificado:  https://sites.pucgoias.edu.br/certificados/ver/da980800f858426151c289b3cc9a380f
    Certificado numero:  710
    Evento:  ECEC - Apresentação de Trabalho de TCC: Utilização de Robôs na Bolsa de Valores (04 de     Junho de 2021)
    Link do Certificado:  https://sites.pucgoias.edu.br/certificados/ver/1a5fe89cc7cd61ba955b5d71f3c1da3c
    Certificado numero:  714
    Evento:  ECEC - Aula Inaugural do Curso de Química e Física (09 de Setembro de 2020)
    Link do Certificado:  https://sites.pucgoias.edu.br/certificados/ver/83fefd95d6685a1d06755e01f686ef7f
    Certificado numero:  720
    Evento:  ECEC - Conf.com - Dia 21/08/2020 - 19h
    Link do Certificado:  https://sites.pucgoias.edu.br/certificados/ver/1ca2cd5412cc2a73ee9022f4932325eb
    Certificado numero:  726
    Evento:  ECEC - O Novo Profissional 5.0: A Partir de Agora, Como e Onde Surgem as Melhores  Oportunidades! (26 de Agosto de 2020)
    Link do Certificado:  https://sites.pucgoias.edu.br/certificados/ver/4e453d8eb310ef118f4925e97f502bda
    Certificado numero:  918
    Evento:  Evento: II Hackathon da PUC Goiás (12, 13 e 14 de Novembro de 2019)
    Link do Certificado:  https://sites.pucgoias.edu.br/certificados/ver/29ea49358b62b55cba232bc36e6d961e
    Certificado numero:  1032
    Evento:  III Programa de Formação continuada - Monitoria (de 02 a 30 de Maio )
    Link do Certificado:  https://sites.pucgoias.edu.br/certificados/ver/e0399c00d19cc480601365c57007bdb2
    Certificado numero:  1047
    Evento:  IV Congresso de Ciência e Tecnologia da PUC Goiás
    Link do Certificado:  https://sites.pucgoias.edu.br/certificados/ver/eb54b9242b12ae6b415af897844acfe7
    Certificado numero:  1051
    Evento:  IV JCECEC - Jornada Científica da Escola de Ciências Exatas e da Computação (11 a 14 de    novembro de 2019)
    Link do Certificado:  https://sites.pucgoias.edu.br/certificados/ver/992354486b29b7a17427a6dc8967893d
    Certificado numero:  1447
    Evento:  Oficina: Capacitação para uso do Portal de Periódicos da CAPES (11 de Abril de 2019)
    Link do Certificado:  https://sites.pucgoias.edu.br/certificados/ver/a6b5ca41e3c36b5f47aca27105d72ffe
    Certificado numero:  1752
    Evento:  V Congresso de Ciência e Tecnologia da PUC Goiás (Participantes)
    Link do Certificado:  https://sites.pucgoias.edu.br/certificados/ver/8b15d3327e10143bde6ee45fd1bc61a6
    Certificado numero:  1787
    Evento:  VI Congresso de Ciência e Tecnologia: Participantes
    Link do Certificado:  https://sites.pucgoias.edu.br/certificados/ver/68bb198010829c7271c0dd836b679eb3
    Certificado numero:  1860
    Evento:  Workshop de Iniciação Científica (24 de fevereiro de 2021) - Participantes
    Link do Certificado:  https://sites.pucgoias.edu.br/certificados/ver/b8634592e00d4217f7ec4fcc074bed65