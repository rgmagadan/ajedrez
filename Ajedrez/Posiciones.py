import os,winsound,shutil

import Funciones as f

if not os.path.exists("Ejercicios accesibles"):
	os.mkdir("Ejercicios accesibles")
source=os.listdir()
for files in source:
	if files.endswith(".pgn"):
		h=0
		board=['a8','b8','c8','d8','e8','f8','g8','h8','a7','b7','c7','d7','e7','f7','g7','h7','a6','b6','c6','d6','e6','f6','g6','h6','a5','b5','c5','d5','e5','f5','g5','h5','a4','b4','c4','d4','e4','f4','g4','h4','a3','b3','c3','d3','e3','f3','g3','h3','a2','b2','c2','d2','e2','f2','g2','h2','a1','b1','c1','d1','e1','f1','g1','h1']
		numbers=['1','2','3','4','5','6','7','8']
		i=0
		fi=open(files)
		contenido=fi.read()
		fi.close()
		texto='[FEN'
		nufen=contenido.count(texto)

		while i >= 0 and i < len(contenido):
			i=contenido.find(texto,i+1)
			fin=contenido.find(']',i)+1
			fe=contenido[i:fin]
			fen=fe[6:-1].split()
			if '-' in fen:
				pos=''.join(fen[0].split('/'))
				j=fen[1]
			blancas=[]
			negras=[]
			n=0
			if 'w' in j:
				j='Juegan las blancas:'
			elif 'b' in j:
				j='Juegan las negras:'
			for c in pos:
				if c in numbers:
					n=n+int(c)
				elif c.islower():
					negras.append(c+board[n])
					n+=1
				else:
					blancas.append(c+board[n])
					n+=1
			blancas=sorted(blancas,key=f.orden)
			negras=sorted(negras,key=f.orden)
			posicion=contenido[h:fin]+'\n'+j+'\n'+''.join(blancas)+'/'+''.join(negras)+'\n'
			f.escribe(files,posicion)
			h=fin

		winsound.PlaySound('convertido.wav',winsound.SND_FILENAME)