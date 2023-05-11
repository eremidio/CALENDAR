#Um programa simples que exibe um calendário e assinala o dia corrente

#Importando bibliotecas usadas

from datetime import datetime as dt

#Funções usadas no programa
def numero_nome_mes(n:int)->str:
 '''Função que dá nome ao mês baseado no horário e data atual'''
 nome:str='xx'
 if(n==1):
  nome='Janeiro'
 if(n==2):
  nome='Fevereiro'
 if(n==3):
  nome='Março'
 if(n==4):
  nome='Abril'
 if(n==5):
  nome='Maio'
 if(n==6):
  nome='Junho'
 if(n==7):
  nome='Julho'
 if(n==8):
  nome='Agosto'
 if(n==9):
  nome='Setembro'
 if(n==10):
  nome='Outubro'
 if(n==11):
  nome='Novembro'
 if(n==12):
  nome='Dezembro'
 return nome


def vermelho(string:str)->str:
 '''Função para marcar uma string'''
 return('\033[31m'+'\033[01m'+string+'\033[0;0m')

def azul(string:str)->str:
 '''Função para marcar uma string'''
 return('\033[34m'+'\033[01m'+string+'\033[0;0m')

def negrito(string:str)->str:
 '''Função para marcar uma string'''
 return('\033[01m'+string+'\033[0;0m')

def numero_string(n:int)->str:
 '''Função que converte número inteiro em um string com dois digitos'''
 string:str=str(n).zfill(2)
 return string

#Obtendo a data atual
hoje=dt.now()
ano_atual:int=hoje.year
mes_atual:str=numero_nome_mes(hoje.month)
dia_atual:str=str(hoje.day).zfill(2)

'''Módulo teste da data atual'''
#print(ano_atual)
#print(mes_atual)
#print(dia_atual)

#Listas úteis
dias_semanais:list=[vermelho('D '),negrito('S '),negrito('T '),negrito('Q '),negrito('Q '),negrito('S '),negrito('S ')]

#Ajustando os dias nos meses do ano para o caso em que o ano seja bissexto ou não
if((ano_atual%4)==0):
 bissexto:int=1
else:
 bissexto:int=0

primeiro_dia:int=dt(ano_atual, 1, 1).weekday()+1


#Criando a classe mês
class meses(object):
 #Instanciando os atributos da classe
 def __init__(self, numero:int, numero_dias:int, delay:int):
  '''Definindo os atributos da classe'''
  self.numero=numero
  self.numero_dias=numero_dias
  self.delay=delay #Primeiro dia do mês

 #Métodos da classe
 def mostrar_mes(self):
  '''Função que mostra o calendário'''
  array:list=[dias_semanais[0],dias_semanais[1],dias_semanais[2],dias_semanais[3],dias_semanais[4], dias_semanais[5], dias_semanais[6]] #lista com os dias da semana
  #Atribuindo os dias da semana ao mês
  #Inserindo os  delays dos calendários
  for i in range(self.delay):
   array.append('  ')
  for i in range(self.numero_dias):
   array.append(numero_string(i+1))
  for i in range(20):
   array.append('  ')
  array=array
  #printando o mês na tela
  for i in range(47):
   if(numero_nome_mes(self.numero)==mes_atual and array[i]== dia_atual):
    array[i]=azul(array[i])
  #Preenchendo o calendário
  print('\033[01m'+'\033[036m'+numero_nome_mes(self.numero)+'\033[0;0m')
  print('+------+------+------+------+------+------+------+')
  print('|      |      |      |      |      |      |      |')
  print('|  {}  |  {}  |  {}  |  {}  |  {}  |  {}  |  {}  |'.format(array[0], array[1], array[2], array[3],array[4], array[5], array[6]))
  print('|      |      |      |      |      |      |      |')
  print('+------+------+------+------+------+------+------+')
  print('|      |      |      |      |      |      |      |')
  print('|  {}  |  {}  |  {}  |  {}  |  {}  |  {}  |  {}  |'.format(array[7], array[8], array[9], array[10],array[11], array[12], array[13]))
  print('|      |      |      |      |      |      |      |')
  print('+------+------+------+------+------+------+------+')
  print('|      |      |      |      |      |      |      |')
  print('|  {}  |  {}  |  {}  |  {}  |  {}  |  {}  |  {}  |'.format(array[14], array[15], array[16], array[17],array[18], array[19], array[20]))
  print('|      |      |      |      |      |      |      |')
  print('+------+------+------+------+------+------+------+')
  print('|      |      |      |      |      |      |      |')
  print('|  {}  |  {}  |  {}  |  {}  |  {}  |  {}  |  {}  |'.format(array[21], array[22], array[23], array[24],array[25], array[26], array[27]))
  print('|      |      |      |      |      |      |      |')
  print('+------+------+------+------+------+------+------+')
  print('|      |      |      |      |      |      |      |')
  print('|  {}  |  {}  |  {}  |  {}  |  {}  |  {}  |  {}  |'.format(array[28], array[29], array[30], array[31],array[32], array[33], array[34]))
  print('|      |      |      |      |      |      |      |')
  print('+------+------+------+------+------+------+------+')
  print('|      |      |      |      |      |      |      |')
  print('|  {}  |  {}  |  {}  |  {}  |  {}  |  {}  |  {}  |'.format(array[35], array[36], array[37], array[38],array[39], array[40], array[41]))
  print('|      |      |      |      |      |      |      |')
  print('+------+------+------+------+------+------+------+')
  print('|      |      |      |      |      |      |      |')
  print('|  {}  |  {}  |  {}  |  {}  |  {}  |  {}  |  {}  |'.format(array[42], array[43], array[44], array[45],array[46], array[47], array[48]))
  print('|      |      |      |      |      |      |      |')
  print('+------+------+------+------+------+------+------+')


#Lista dos meses do ano 
ano:list=[]
#Criando os meses do ano e adicionando a lista ano
jan=meses(1, 31,(primeiro_dia)%7)
ano.append(jan)

fev=meses(2, 28+bissexto, (jan.delay+jan.numero_dias)%7)
ano.append(fev)

mar=meses(3, 31, (fev.delay+fev.numero_dias)%7)
ano.append(mar)

abr=meses(4,30, (mar.delay+mar.numero_dias)%7)
ano.append(abr)

mai=meses(5,31,(abr.delay+abr.numero_dias)%7)
ano.append(mai)

jun=meses(6,30,(mai.delay+mai.numero_dias)%7)
ano.append(jun)

jul=meses(7,31,(jun.delay+jun.numero_dias)%7)
ano.append(jul)

ago=meses(8,31,(jul.delay+jul.numero_dias)%7)
ano.append(ago)

setem=meses(9, 30, (ago.delay+ago.numero_dias)%7)
ano.append(setem)

out=meses(10,31, (setem.delay+setem.numero_dias)%7)
ano.append(out)

nov=meses(11,30, (out.delay+out.numero_dias)%7)
ano.append(nov)

dez=meses(12,31, (nov.delay+nov.numero_dias)%7)
ano.append(dez)

ano=ano #Atualizando a lista de meses do ano

#Printando o calendário na tela
print('\033[94m'+'\033[01m'+' ***   *         *      *  *  *')
print('\033[94m'+'\033[01m'+'*   *  *        * *     *  *  *')
print('\033[94m'+'\033[01m'+'*   *  *       *****    *  *  *')
print('\033[94m'+'\033[01m'+'*   *  *      *     *          ')
print('\033[94m'+'\033[01m'+' ***   ****  *       *  *  *  *\n\n'+'\033[0;0m')
print('Este é o calendário do ano de %s.\n\n'%vermelho(str(ano_atual)))

for i in range(len(ano)):
 ano[i].mostrar_mes()
