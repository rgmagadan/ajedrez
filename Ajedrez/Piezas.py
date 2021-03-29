import winsound

class Torre:

	def __init__(self,color,casilla):
		self.color=color
		self.casilla=casilla
		self.valor=5
		self.juega=True
		self.nombre="T"

	def captura(self):
		self.valor=0
		self.juega=False
		self.casilla=""
		winsound.PlaySound('captura.wav',winsound.SND_FILENAME)

	def mostrar(self):
		if self.juega:
			return self.nombre+self.casilla
 

	def valor(self):
		return self.valor

	def cambiar_casilla(self,nueva_casilla):
		self.casilla=nueva_casilla


class Caballo:

	def __init__(self,color,casilla):
		self.color=color
		self.casilla=casilla
		self.valor=3
		self.juega=True
		self.nombre="C"

	def captura(self):
		self.valor=0
		self.juega=False
		self.casilla=""
		winsound.PlaySound('captura.wav',winsound.SND_FILENAME)

	def mostrar(self):
		if self.juega:
			return self.nombre+self.casilla


	def valor(self):
		return self.valor

	def cambiar_casilla(self,nueva_casilla):
		self.casilla=nueva_casilla


class Alfil:

	def __init__(self,color,casilla):
		self.color=color
		self.casilla=casilla
		self.valor=3
		self.juega=True
		self.nombre="A"

	def captura(self):
		self.valor=0
		self.juega=False
		self.casilla=""
		winsound.PlaySound('captura.wav',winsound.SND_FILENAME)

	def mostrar(self):
		if self.juega:
			return self.nombre+self.casilla


	def valor(self):
		return self.valor

	def cambiar_casilla(self,nueva_casilla):
		self.casilla=nueva_casilla


class Dama:

	def __init__(self,color,casilla):
		self.color=color
		self.casilla=casilla
		self.valor=9
		self.juega=True
		self.nombre="D"

	def captura(self):
		self.valor=0
		self.juega=False
		self.casilla=""
		winsound.PlaySound('captura.wav',winsound.SND_FILENAME)

	def mostrar(self):
		if self.juega:
			return self.nombre+self.casilla


	def valor(self):
		return self.valor

	def cambiar_casilla(self,nueva_casilla):
		self.casilla=nueva_casilla


class Rey:

	def __init__(self,color,casilla):
		self.color=color
		self.casilla=casilla
		self.valor=1000
		self.juega=True
		self.nombre="R"

	def enroque():
		winsound.PlaySound('enroque.wav',winsound.SND_FILENAME)

	def captura(self):
		pass

	def mostrar(self):
		return self.nombre+self.casilla

	def valor(self):
		return self.valor

	def cambiar_casilla(self,nueva_casilla):
		self.casilla=nueva_casilla


class Peon:

	def __init__(self,color,casilla):
		self.color=color
		self.casilla=casilla
		self.valor=1
		self.juega=True

	def captura(self):
		self.valor=0
		self.juega=False
		self.casilla=""
		winsound.PlaySound('captura.wav',winsound.SND_FILENAME)

	def mostrar(self):
		if self.juega:
			return self.casilla


	def valor(self):
		return self.valor

	def cambiar_casilla(self,nueva_casilla):
		self.casilla=nueva_casilla


ntd=Torre("n","a8")
ncd=Caballo("n","b8")
nad=Alfil("n","c8")
nd=Dama("n","d8")
nr=Rey("n","e8")
ntr=Torre("n","h8")
ncr=Caballo("n","g8")
nar=Alfil("n","f8")
npa=Peon("n","a7")
npb=Peon("n","b7")
npc=Peon("n","c7")
npd=Peon("n","d7")
npe=Peon("n","e7")
npf=Peon("n","f7")
npg=Peon("n","g7")
nph=Peon("n","h7")
btd=Torre("b","a1")
bcd=Caballo("b","b1")
bad=Alfil("b","c1")
bd=Dama("b","d1")
br=Rey("b","e1")
btr=Torre("b","h1")
bcr=Caballo("b","g1")
bar=Alfil("b","f1")
bpa=Peon("b","a2")
bpb=Peon("b","b2")
bpc=Peon("b","c2")
bpd=Peon("b","d2")
bpe=Peon("b","e2")
bpf=Peon("b","f2")
bpg=Peon("b","g2")
bph=Peon("b","h2")
