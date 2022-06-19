import inicio
import requests
from bs4 import BeautifulSoup
while True:
	inicio.tela('CAMPEONATO BRASILEIRO')

	opcao = int(input("""1- PARA RODADA COMPLETA
2- PARA JOGOS DE HOJE
3- CLASSIFICAÇÃO
4- PARA SAIR DO PROGRAMA"""))
	if opcao == 1:
	# SITE QUE PEGA OS DADOS
		url = 'https://www.cbf.com.br/futebol-brasileiro/competicoes/campeonato-brasileiro-serie-a/2022'


		acesso = requests.get(url)

		site = BeautifulSoup(acesso.text, 'html.parser')


		rodada = site.find('div', attrs={'class': 'swiper-slide active'})

		rodada_atual = rodada.find('h3', attrs={'class':'text-center'})

		print('' )
		print('\033[32m='*70)
		print(f'{rodada_atual.text:^70}')
		print('='*70)
		print(' \033[m')

		hora1 = rodada.findAll('span', attrs={'class':'partida-desc text-1 color-lightgray p-b-15 block uppercase text-center'})
#print(hora1.text[32:-124])
		timec1 = rodada.findAll('div', attrs={'class': 'time pull-left'})

		timef1 = rodada.findAll('div', attrs={'class': 'time pull-right'})
#print(timef1.text[1:-2])
		estadio1 = rodada.findAll('span', attrs={'class': 'partida-desc text-1 color-lightgray block uppercase text-center'})

		result = rodada.findAll('span', attrs={'class': 'bg-blue color-white label-2'})

#print(estadio1.text[16:-23])
		inicio.tela('PARTIDAS ENCERADAS')
		for data1, clubec1, clubef1, local1, placar in zip (hora1, timec1, timef1, estadio1, result):
			print('\033[36m-'*70)
			print(f"""                          {data1.text[32:-50]}
           	         {clubec1.text[1:-2]:^10}{placar.text}{clubef1.text[1:-2]:^10}
                        {local1.text[16:-21]}
	\033[m""")
	
		if not result:
			msg = 'NENHUMA PARTIDA NESSA RODADA COMEÇOU!'
			print(70*'-')
			print(f'\033[36m{msg:^70}\033[m')
			print(70*'-')
		
		inicio.tela('\033[33m    RODADA COMPLETA\033[m')
		for data1, clubec1, clubef1, local1 in zip (hora1, timec1, timef1, estadio1):
			print('-'*70)
			print(f"""                          {data1.text[32:-50]}
           	           {clubec1.text[1:-2]:^10}X{clubef1.text[1:-2]:^10}
                        {local1.text[16:-21]}
	""")
	
		
	elif opcao == 2:

# SITE QUE PEGA OS DADOS
		url = 'https://www.cbf.com.br/futebol-brasileiro/jogosdehoje/campeonato-brasileiro-serie-a'

		acesso = requests.get(url)

		site = BeautifulSoup(acesso.text, 'html.parser')


		rodada = site.find('section', attrs={'class': 'm-b-0 p-t-10 row'})


		hora2  = rodada.findAll('div', attrs={'class':'text-1 m-b-10 text-center uppercase'})
#print(hora1.text[32:-124])
		timec2 = rodada.findAll('b', attrs={'class': 'text-2 pull-right p-t-15 p-r-10 hidden-lg hidden-md'})

		timef2 = rodada.findAll('b', attrs={'class': 'text-2 pull-left p-t-15 p-l-10 hidden-lg hidden-md'})
#print(timef1.text[1:-2])
		estadio2 = rodada.findAll('div', attrs={'class': 'text-1 m-t-10 text-center uppercase'})

#print(estadio1.text[16:-23])

		for data2, clubec2, clubef2, local2 in zip (hora2, timec2, timef2, estadio2):
			print('-'*70)
			print(f"""                          {data2.text[:-38]}
           	         {clubec2.text}  X  {clubef2.text}
                {local2.text[5:-23]}
	""")  
		if not hora2:
			msg = 'HOJE NÃO TEM PARTIDAS'
			print(70*'-')
			print(f'\033[36m{msg:^70}\033[m')
			print(70*'-')

	elif opcao == 3:

			inicio.tela('TIMES | PONTUAÇÀO')

# SITE QUE PEGA OS DADOS
			url = 'https://www.cbf.com.br/futebol-brasileiro/competicoes/campeonato-brasileiro-serie-a/2022'

			acesso = requests.get(url)

			site = BeautifulSoup(acesso.text, 'html.parser')


			tabelas = site.find('section', attrs={'class': 'm-b-50 p-t-10 row'})

			time = tabelas.findAll('span', attrs= {'class': 'hidden-xs'})
	
			ponto = tabelas.findAll('th', attrs= {'class': ''})
	
	
			for times, pontos, in zip(time, ponto):
				print('-'*70)
				print(f"""{times.text:^40}  {pontos.text} """)
	elif opcao == 4:
		break
		
	

	