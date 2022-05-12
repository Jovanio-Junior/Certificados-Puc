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