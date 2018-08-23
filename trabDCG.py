def artigoSingularMasculino(string):
	return string in ["O", "o"]

def artigoPluralMasculino(string):
	return string in ["Os", "os"]

def artigoSingularFeminino(string):
	return string in ["A", "a"]

def artigoPluralFeminino(string):
	return string in ["As", "as"]

def substantivoSingularMasculino(string):
	return string in ["tempo","cacador","rosto","rio","mar","vento","martelo","cachorro","tambor","sino"]

def substantivoPliuralMasculino(string):
	return string in ["lobos","tambores"]

def substantivoSingularFeminino(string):
	return string in ["menina","vida","noticia","porta","floresta","mae","cidade"]

def substantivoPluralFeminino(string):
	return string in ["lagrimas"]

def preposicao(string):
	return string in ["para","com","no","na","pelo","pela"]

def printResult(n, nominal_phrase, verbal_phrase):
	if n == 1:
		pritn("sent(frase_nom(artigo('"+ nominal_phrase[0] + "'),substantivo('" + nominal_phrase[1] + "'))" + ",frase_verb(verbo('"+ verbal_phrase[0] + "')))")
	elif n == 2:
		pritn("sent(frase_nom(artigo('"+fr_Nominal.get(0)+"')," + "substantivo('"+fr_Nominal.get(1)+"')),frase_verb(verbo('"+fr_Verbal.get(0)+"')," + "preposicao('"+fr_Verbal.get(1)+"'),artigo('"+fr_Verbal.get(2)+"'),substantivo('"+fr_Verbal.get(3)+"')))")
	elif n == 3:
		pritn("sent(frase_nom(artigo('"+fr_Nominal.get(0)+"'),substantivo('"+fr_Nominal.get(1)+"'))," + "frase_verb(verbo('"+fr_Verbal.get(0)+"'),preposicao('"+fr_Verbal.get(1)+"'),substantivo('"+fr_Verbal.get(2)+"')))")
	elif n == 4:
		pritn("sent(frase_nom(artigo('"+fr_Nominal.get(0)+"')," + "substantivo('"+fr_Nominal.get(1)+"')),frase_verb(verbo('"+fr_Verbal.get(0)+"')," + "preposicao('"+fr_Verbal.get(1)+"'),artigo('"+fr_Verbal.get(2)+"'),substantivo('"+fr_Verbal.get(3)+"')))")
	else:
		print("Frase incorreta")


singular_verbs = ["corre", "correu", "bateu"]
plural_verbs = ["corriam", "correram", "bateram"]
nominal_phrase = []
verbal_phrase = []
phrase = input("Escreva a frase:")
words = phrase.split(" ")
has_verb = False
for word in words:
	if word in plural_verbs or word in singular_verbs:
		has_verb = True
	if has_verb:
		verbal_phrase.append(word)
	else:
		nominal_phrase.append(word)
