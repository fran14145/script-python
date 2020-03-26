import requests
from bs4 import BeautifulSoup as bs
print(20 * '\033[46m=','DIGITE A OPÇÃO DESEJADA',15 * '=')
print('\033[m')
lot = int(input('''            1 - RESULTADO MEGASENA
            2 - RESULTADO QUINA
            3 - RESULTADO LOTOFACIL
            4 - RESULTADO DIA DE SORTE?
____________________________________________________________'''


))
if lot == 2:
   print('\n')
   url = 'http://www1.caixa.gov.br/loterias/loterias/quina/quina_pesquisa_new.asp'
   p = requests.get(url)
   s = bs(p.content, 'html.parser')
   lista = s.find('ul')
   números = lista.findAll('li')
   for n in números:
	    print ('\033[31m', n.getText())
	    print(60 * '_')
  #pegar data do sorteio e concurso
  
# 43m cor de fundo amarela
else:
	print('Opção invalida')

