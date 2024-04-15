from selenium import webdriver
from selenium.webdriver.common.by import By

import time

navegador = webdriver.Chrome()

navegador.get("https://painel.tomticket.com/login.html")
time.sleep(0.5)

empress = 'antoniovictor'
user = "avps2@aluno.ifal.edu.br"
passU = "vi93462001" 

# empresa_tic = navegador.find_element(By.XPATH, '/html/body/div/form/input[1]').click()
empresa_tic = navegador.find_element(By.XPATH, '/html/body/div/form/input[1]').send_keys(empress)

empresa_user = navegador.find_element(By.XPATH, '/html/body/div/form/input[2]').send_keys(user)

empresa_pass = navegador.find_element(By.XPATH, '/html/body/div/form/input[3]').send_keys(passU)

time.sleep(0.5)
navegador.find_element(By.XPATH, '/html/body/div/form/button').click()
# Apos Login

# Responder Chamados

# Opção Chamados
time.sleep(0.7)
navegador.find_element(By.XPATH, '//*[@id="menu"]/ul/li[4]/a/span[2]').click()
# Opção Todos
time.sleep(1)
navegador.find_element(By.XPATH, '//*[@id="menu"]/ul/li[4]/ul/li[1]/a').click()
time.sleep(2.5)

# Verificar se esta Aguardando respostas
paragrafo = navegador.find_element(By.XPATH, '//*[@id="conteudo"]/div[4]/ng-view/div/div[2]/div[4]/div[1]/table/tbody/tr[1]/td[5]/a/span').text
textt = navegador.find_element(By.XPATH, '//*[@id="conteudo"]/div[4]/ng-view/div/div[2]/div[4]/div[1]/table/tbody/tr[1]/td[5]/a/span')

# Define o número máximo de elementos que você deseja iterar

numero_maximo = 4
descricao_chamado = """
Prezado(a),
Retorno em Breve 

Att, Equipe de Suporte
"""
print("Descrição: " , descricao_chamado)
# Loop para gerar e iterar sobre os XPath dos elementos
for num in range(1, numero_maximo + 1):
    time.sleep(0.2)
    xpath_elemento = f'//*[@id="conteudo"]/div[4]/ng-view/div/div[2]/div[4]/div[1]/table/tbody/tr[{num}]/td[5]/a/span'
    elemento = navegador.find_element(By.XPATH, xpath_elemento).text
    if elemento == "Aguardando":
        print("O parágrafo tem o texto correto.")
        # ckick no element que seja true
        navegador.find_element(By.XPATH, xpath_elemento).click()
        time.sleep(1)
        navegador.find_element(By.XPATH, '//*[@id="conteudo"]/div[4]/ng-view/div/div/div[5]/div[1]/article/section/div/div[2]/div[4]/form/button/span[2]').click()
        # agora escrevar
        time.sleep(1)
        navegador.find_element(By.XPATH, '//*[@id="conteudo"]/div[4]/ng-view/div/div/div[5]/div[1]/article/section/div/div[2]/div[4]/form/div[2]/div[1]/iframe').click()
        time.sleep(0.2)
        navegador.find_element(By.XPATH, '//*[@id="conteudo"]/div[4]/ng-view/div/div/div[5]/div[1]/article/section/div/div[2]/div[4]/form/div[2]/div[1]/iframe').send_keys(descricao_chamado)
        # envia descrição
        time.sleep(1)
        navegador.find_element(By.XPATH, '//*[@id="conteudo"]/div[4]/ng-view/div/div/div[5]/div[1]/article/section/div/div[2]/div[4]/form/div[4]/div[1]/div[1]/div/button/span').click()
        # Retorna Pagina
        time.sleep(1)
        navegador.back()
        time.sleep(3)
    else:
        print("O parágrafo não tem o texto correto.")
        
    # Faça alguma coisa com o elemento, por exemplo, imprimir o texto
    print(elemento)


# Verifica o texto do parágrafo
time.sleep(0.5)
print("paragrafo: ",paragrafo)
print("textt: " , textt)
# Para aplicação não fechar
input("Pressione Enter para encerrar o script...")

