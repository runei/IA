
sentence(sent(FraseNominal,FraseVerbal)) --> frase_nom(FraseNominal),frase_verb(FraseVerbal).
sentence(sent(FraseNominal,FraseVerbal)) --> frase_nom_p(FraseNominal), plural_frase_verb(FraseVerbal).

frase_nom(frase_nom(Artigo,Nome)) --> artigo_feminino(Artigo), nome_feminino(Nome).
frase_nom(frase_nom(Nome)) --> nome_feminino(Nome).
frase_nom(frase_nom(Artigo,Nome)) --> artigo_masculino(Artigo), nome_masculino(Nome).
frase_nom(frase_nom(Nome)) --> nome_masculino(Nome).

frase_verb(frase_verb(Verbo,FraseNominal)) --> verbo(Verbo), frase_nom(FraseNominal).
frase_verb(frase_verb(Verbo,FraseNominal)) --> verbo(Verbo), frase_nom_p(FraseNominal).
frase_verb(frase_verb(Verbo,FrasePreposicional)) --> verbo(Verbo), frase_preposicional(FrasePreposicional).
frase_verb(frase_verb(Verbo,FraseNominalComContracao)) --> verbo(Verbo), frase_nom_c_contracao(FraseNominalComContracao).
frase_verb(frase_verb(Verbo)) --> verbo(Verbo).

frase_nom_p(frase_nom(Artigo,Nome)) --> plural_artigo_feminino(Artigo), plural_nome_feminino(Nome).
frase_nom_p(frase_nom(Nome)) --> plural_nome_feminino(Nome).
frase_nom_p(frase_nom(Artigo,Nome)) --> plural_artigo_masculino(Artigo), plural_nome_masculino(Nome).
frase_nom_p(frase_nom(Nome)) --> plural_nome_masculino(Nome).

frase_verb_p(frase_verb_p(Verbo,FraseNominal)) --> plural_verbo(Verbo), frase_nom(FraseNominal).
frase_verb_p(frase_verb_p(Verbo,FraseNominal)) --> plural_verbo(Verbo), frase_nom_p(FraseNominal).
frase_verb_p(frase_verb_p(Verbo,FrasePreposicional)) --> plural_verbo(Verbo), frase_preposicional(FrasePreposicional).
frase_verb_p(frase_verb_p(Verbo,FraseNominalComContracao)) --> plural_verbo(Verbo), frase_nom_c_contracao(FraseNominalComContracao).
frase_verb_p(frase_verb_p(Verbo,FraseNominalPluralComContracao)) --> plural_verbo(Verbo), frase_nom_p_c_contracao(Verbo,FraseNominalPluralComContracao).
frase_verb_p(frase_verb_p(Verbo)) --> plural_verbo(Verbo).

frase_nom_c_contracao(frase_nom_c_contracao(Contracao,Nome)) --> contracao_feminina(Contracao), nome_feminino(Nome).
frase_nom_c_contracao(frase_nom_c_contracao(Contracao,Nome)) --> contracao_masculina(Contracao), nome_masculino(Nome).
frase_nom_p_c_contracao(frase_nom_p_c_contracao(Contracao,Nome)) --> plural_contracao_feminina(Contracao),plural_nome_feminino(Nome).
frase_nom_p_c_contracao(frase_nom_p_c_contracao(Contracao,Nome)) --> plural_contracao_masculina(Contracao),
plural_nome_masculino(Nome).

frase_preposicional(frase_preposicional(Preposicao,FraseNominal)) --> prep(Preposicao), frase_nom(FraseNominal).
frase_preposicional(frase_preposicional(Preposicao,FraseNominal)) --> prep(Preposicao), frase_nom_p(FraseNominal).

prep(preposicao(para)) --> [para].
prep(preposicao(com)) --> [com].

contracao_feminina(artigo(na)) --> [na].
contracao_feminina(artigo(pela)) --> [pela].
plural_contracao_feminina(artigo(na)) --> [nas].
plural_contracao_feminina(artigo(pela)) --> [pelas].

contracao_masculina(artigo(no)) --> [no].
contracao_masculina(artigo(pelo)) --> [pelo].
plural_contracao_masculina(artigo(no)) --> [nos].
plural_contracao_masculina(artigo(pelo)) --> [pelos].


nome_feminino(nome(menina)) --> [menina].
nome_feminino(nome(floresta)) --> [floresta].
nome_feminino(nome(mae)) --> [mae].
nome_feminino(nome(vida)) --> [vida].
nome_feminino(nome(noticia)) --> [noticia].
nome_feminino(nome(cidade)) --> [cidade].
plural_nome_feminino(nome(lagrimas)) --> [lagrimas].
nome_feminino(nome(porta)) --> [porta].
plural_nome_feminino(nome(meninas)) --> [meninas].

nome_masculino(nome(tempo)) --> [tempo].
nome_masculino(nome(cacador)) --> [cacador].
plural_nome_masculino(nome(lobos)) --> [lobos].
nome_masculino(nome(rosto)) --> [rosto].
nome_masculino(nome(rio)) --> [rio].
nome_masculino(nome(mar)) --> [mar].
nome_masculino(nome(vento)) --> [vento].
nome_masculino(nome(martelo)) --> [martelo].
nome_masculino(nome(cachorro)) --> [cachorro].
nome_masculino(nome(tambor)) --> [tambor].
plural_nome_masculino(nome(tambores)) --> [tambores].
nome_masculino(nome(sino)) --> [sino].

verbo(verbo(corre)) --> [corre].
verbo(verbo(correu)) --> [correu].
plural_verbo(verbo(corriam)) --> [corriam].
verbo(verbo(bateu)) --> [bateu].
plural_verbo(verbo(bateram)) --> [bateram].
plural_verbo(verbo(correram)) --> [correram].

artigo_feminino(artigo(a)) --> [a].
artigo_feminino(artigo('A')) --> ['A'].
artigo_masculino(artigo(o)) --> [o].
artigo_masculino(artigo('O')) --> ['O'].
plural_artigo_feminino(artigo(as)) --> [as].
plural_artigo_feminino(artigo('As')) --> ['As'].
plural_artigo_masculino(artigo(os)) --> [os].
plural_artigo_masculino(artigo('Os')) --> ['Os'].