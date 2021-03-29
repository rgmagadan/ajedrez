import os

import Piezas as p, Variables as v

def matriz():
	matriz=[[None]*8 for i in range(8)]
	matriz[0][0]=p.ntd
	matriz[0][1]=p.ncd
	matriz[0][2]=p.nad
	matriz[0][3]=p.nd
	matriz[0][4]=p.nr
	matriz[0][5]=p.nar
	matriz[0][6]=p.ncr
	matriz[0][7]=p.ntr
	matriz[1][0]=p.npa
	matriz[1][1]=p.npb
	matriz[1][2]=p.npc
	matriz[1][3]=p.npd
	matriz[1][4]=p.npe
	matriz[1][5]=p.npf
	matriz[1][6]=p.npg
	matriz[1][7]=p.nph
	matriz[6][0]=p.bpa
	matriz[6][1]=p.bpb
	matriz[6][2]=p.bpc
	matriz[6][3]=p.bpd
	matriz[6][4]=p.bpe
	matriz[6][5]=p.bpf
	matriz[6][6]=p.bpg
	matriz[6][7]=p.bph
	matriz[7][0]=p.btd
	matriz[7][1]=p.bcd
	matriz[7][2]=p.bad
	matriz[7][3]=p.bd
	matriz[7][4]=p.br
	matriz[7][5]=p.bar
	matriz[7][6]=p.bcr
	matriz[7][7]=p.btr
	return matriz


def bucle(matriz):
	global indice
	global nmj
	while not v.detener:
		blancas(v.indice,mj(matriz))
		v.nmj+=1
		negras(mj(matriz))
		v.nmj+=1
		v.indice+=1


def blancas(indice, move):
	directorio=os.getcwd()+'\Partidas.txt'
	escritura=open(directorio,"at",encoding="utf-8")
	escritura.write(str(indice)+'. '+move+' ')
	escritura.close()


def negras(move):
	directorio=os.getcwd()+'\Partidas.txt'
	escritura=open(directorio,"at",encoding="utf-8")
	escritura.write(move+' ')
	escritura.close()


def mj(matrix):
	global matriz
	j,nm=dijugada(matrix)
	jugada=mover(matrix,j,nm)
	return jugada


def posicion():
	blancas=[]
	negras=[]
	pb=[p.br,p.bd,p.btd,p.btr,p.bad,p.bar,p.bcd,p.bcr,p.bpa,p.bpb,p.bpc,p.bpd,p.bpe,p.bpf,p.bpg,p.bph]
	pn=[p.nr,p.nd,p.ntd,p.ntr,p.nad,p.nar,p.ncd,p.ncr,p.npa,p.npb,p.npc,p.npd,p.npe,p.npf,p.npg,p.nph]
	for i in pb:
		if i.juega is True:
			blancas.append(i.mostrar())
	blancas=",".join(blancas)
	for i in pn:
		if i.juega is True:
			negras.append(i.mostrar())
	negras=",".join(negras)
	return 'Blancas: '+blancas+'\n'+'Negras: '+negras


def dijugada(m):
	r=2
	while r >= 2:
		r=2
		j,nm=dj()
		if j == 'tablero':
			print(posicion())
			r=3
		elif j == 'salir':
			v.detener=True
			exit()
		elif j[0]+j[1] == j[2]+j[3] or m[nm[1]][nm[0]] is None or m[nm[3]][nm[2]].__class__ is p.Rey:
			print('Error')
			r=4
		elif m[nm[3]][nm[2]] != None and m[nm[1]][nm[0]].color == m[nm[3]][nm[2]].color:
			print(v.e4)
			r=8
		elif v.nmj == 0 and m[nm[1]][nm[0]].color == 'n':
			print(v.e5)
			r=5
		elif v.nmj != 0 and v.nmj % 2 == 0 and m[nm[1]][nm[0]].color == 'n':
			print(v.e5)
			r=6
		elif v.nmj != 0 and v.nmj % 2 != 0 and m[nm[1]][nm[0]].color == 'b':
			print(v.e6)
			r=7
		elif m[nm[1]][nm[0]].__class__ is p.Rey and j[2]+j[3] == 'c8':
			if m[0][1] != None or m[0][2] != None or m[0][3] != None:
				print(v.e7)
				r=8
		elif m[nm[1]][nm[0]].__class__ is p.Rey and j[2]+j[3] == 'g8':
			if m[0][5] != None or m[0][6] != None:
				print(v.e8)
				r=9
		elif m[nm[1]][nm[0]].__class__ is p.Rey and j[2]+j[3] == 'c1':
			if m[7][1] != None or m[7][2] != None or m[7][3] != None:
				print(v.e9)
				r=10
		elif m[nm[1]][nm[0]].__class__ is p.Rey and j[2]+j[3] == 'g1':
			if m[7][5] != None or m[7][6] != None:
				print(v.e10)
				r=11
		r-=1
	return j,nm


def mover(a,b,c):
	cap=''
	if a[c[3]][c[2]] != None:
		a[c[3]][c[2]].captura()
		cap='x'
		if a[c[1]][c[0]].__class__ is p.Peon:
			cap=b[0]+'x'
	a[c[3]][c[2]]=a[c[1]][c[0]]
	a[c[1]][c[0]]=None
	a[c[3]][c[2]].cambiar_casilla(b[2]+b[3])
	if a[c[3]][c[2]].__class__ is not p.Peon:
		jugada=a[c[3]][c[2]].nombre+cap+b[2]+b[3]
	else:
		jugada=cap+b[2]+b[3]
	if a[c[3]][c[2]].__class__ is p.Rey and b[2]+b[3] == 'c8':
		a[0][3]=a[0][0]
		a[0][0]=None
		a[0][3].cambiar_casilla('d8')
		p.Rey.enroque()
		jugada='0-0-0'
	elif a[c[3]][c[2]].__class__ is p.Rey and b[2]+b[3] == 'g8':
		a[0][5]=a[0][7]
		a[0][7]=None
		a[0][5].cambiar_casilla('f8')
		p.Rey.enroque()
		jugada='0-0'
	elif a[c[3]][c[2]].__class__ is p.Rey and b[2]+b[3] == 'c1':
		a[7][3]=a[7][0]
		a[7][0]=None
		a[7][3].cambiar_casilla('d1')
		p.Rey.enroque()
		jugada='0-0-0'
	elif a[c[3]][c[2]].__class__ is p.Rey and b[2]+b[3] == 'g1':
		a[7][5]=a[7][7]
		a[7][7]=None
		a[7][5].cambiar_casilla('f1')
		p.Rey.enroque()
		jugada='0-0'
	return jugada


def dj():
	nm=[]
	l=['a','b','c','d','e','f','g','h']
	n=['8' ,'7','6','5','4','3','2','1']
	j=input("Jugada: ")
	if j != 'tablero' and j != 'salir':
		if j[0] not in l or j[1] not in n or j[2] not in l or j[3] not in n:
			j='f2f2'
		nm.append(l.index(j[0]))
		nm.append(n.index(j[1]))
		nm.append(l.index(j[2]))
		nm.append(n.index(j[3]))
	return j,nm


def escribe(f,p):
	directorio=os.getcwd()+'\Ejercicios accesibles'+'\Copia de '+f
	escritura=open(directorio,"at",encoding="utf-8")
	escritura.write(p)
	escritura.close()


def orden(letras):
	if letras[0] == 'k' or letras[0] == 'K':
		v=0
	elif letras[0] == 'q' or letras[0] == 'Q':
		v=1
	elif letras[0] == 'r' or letras[0] == 'R':
		v=2
	elif letras[0] == 'b' or letras[0] == 'B':
		v=3
	elif letras[0] == 'n' or letras[0] == 'N':
		v=4
	elif letras[0] == 'p' or letras[0] == 'P':
		v=5
	return v


