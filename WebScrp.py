from bs4 import BeautifulSoup
from lxml import html
from selenium import webdriver
import requests
import pandas as pd
import random

secciones = ['\lista_literatura.csv','\lista_danza.csv','\lista_musica.csv','\lista_cine.csv','\lista_teatro.csv','\lista_arte.csv']
n_seccion = 0
s = secciones[n_seccion]
tabla = pd.read_csv(r'C:\Users\pablo\Desktop\UCLM\4º\TFG\Virtual' + s ,encoding = "utf-8" , sep = ';', names = ['periodico', 'direccion', 'titular', 'enlace', 'subtitulo', 'cuerpo', 'inicio', 'fin', 'cantidad', 'vueltas'], header = None)
tabla_salida = pd.DataFrame(columns = ['periodico', 'titular', 'enlace', 'subtitulo', 'cuerpo'])

def paginas (inicio, fin, num):
	a=list(range(inicio,fin))
	random.shuffle(a)
	b=a[:num]
	c=[]
	for i in range(0,num):
		c.insert(i,str(b[i]))
	return c
	
def texto_sub(per):
	try:
		s=''
		subt = eval(tabla.subtitulo[per])
		print('___')
		l = len(subt)
		print(f'{l}\n')
		for i in range(0,l):
			s = s + ' ' + subt[i].text
		return s
	except:
		return 'No subtitulo'

def texto_cpo(per):
	try:
		c=''
		crpo = eval(tabla.cuerpo[per])
		print('___')
		l = len(crpo)
		print(f'{l}\n')
		for i in range(0,l):
			c = c + ' ' + crpo[i].text
		return c
	except:
		return 'No cuerpo'

count = 0
i = 1

dr = webdriver.Chrome()
print(len(tabla.index))
for per in range(0,len(tabla.index)):
	for pag in paginas(tabla.inicio[per],tabla.fin[per], tabla.vueltas[per]):
		print(pag)
		if n_seccion != 3 and per == 1:
			pag = pag + '.html'
		if per == 2:
			pag = ''
		d = tabla.direccion[per] + pag
		print(d)
		dr.get(d)
		soup = BeautifulSoup(dr.page_source,"lxml")

		for count in range(tabla.cantidad[per]):
			titular = eval(tabla.titular[per])
			enlace =  eval(tabla.enlace[per])
			
			subtitulo = 'subtitulo' + str(i)
			cuerpo = 'cuerpo' + str(i)
			
			try:
				print(f"{i}-{titular}\n({enlace})\n")
			
				req_enlace = requests.get(enlace)
				soup1 = BeautifulSoup(req_enlace.text,"lxml")
				print('...\n')
				subtitulo = texto_sub(per)
				print(f"'{subtitulo}'\n")
				cuerpo = texto_cpo(per)
			except:
				print(f'\nERROR\n')
			i = 1 + i
			tabla_aux = pd.DataFrame([[tabla.periodico[per], titular, enlace, subtitulo, cuerpo]], columns = ['periodico', 'titular', 'enlace', 'subtitulo', 'cuerpo'])
			tabla_salida = pd.concat([tabla_salida,tabla_aux], ignore_index=True)
		
dr.close()

tabla_salida.to_csv( s[7:], sep=';', encoding='utf-8')

