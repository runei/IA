import java.util.LinkedList;

class Frase{
    LinkedList<String> fr_Nominal;
    LinkedList<String> fr_Verbal;

    /**
     *Obtencao de palavras da frase que foi introduzida pelo utilizador
     * @param s
     * @return
     */
    public LinkedList<String> seperarPalavrasdaFrase(String s) {
        String [] phrase = s.split(" ");
        LinkedList<String> finalResult = new LinkedList<String>();

        for(int i = 0; i < phrase.length; i++){
            finalResult.addLast(phrase[i]);
        }
        return finalResult;
    }

    /**
     *Divide a frase em frase nominal e frase verbal
     * @param phrase
     */
    public void phraseNomeVerbo(LinkedList<String> phrase){
        fr_Nominal = new LinkedList<>();
        fr_Verbal = new LinkedList<>();

        int foundVerb = 0;

        for(String word : phrase){
            if(singularVerb(word))
                foundVerb = 1;
            if(pluralVerb(word))
                foundVerb = 1;

            if(foundVerb == 0)
                fr_Nominal.addLast(word);
            else if(foundVerb == 1){
                fr_Verbal.addLast(word);
            }
        }
    }

    /**
     *artigos masculinos singular
     * @param palavra
     * @return
     */
    public boolean artigoMasculinoSingular(String palavra){
        String[] artigos = {"O", "o"};

        for(String a: artigos){
            if(palavra.equals(a))
                return true;
        }
        return false;
    }

    /**
     *artigos masculinos plural
     * @param palavra
     * @return
     */
    public boolean artigoMasculinoPlural(String palavra){
        String[] artigos = {"Os","os"};

        for(String a: artigos){
            if(palavra.equals(a))
                return true;
        }
        return false;
    }

    /**
     *artigos femininos singular
     * @param palavra
     * @return
     */
    public boolean artigoFemininoSingular(String palavra){
        String[] artigos = {"A","a"};

        for(String a: artigos){
            if(palavra.equals(a))
                return true;
        }
        return false;
    }

    /**
     *artigos femininos plural
     * @param palavra
     * @return
     */
    public boolean artigoFemininoPlural(String palavra){
        String[] artigos = {"As","as"};

        for(String a: artigos){
            if(palavra.equals(a))
                return true;
        }
        return false;
    }

    /**
     *substantivos masculinos singulares
     * @param palavra
     * @return
     */
    public boolean substantivoMasculinoSingular(String palavra){
        String[] substantivo = {"tempo","cacador","rosto","rio","mar","vento","martelo","cachorro","tambor","sino"};

        for(String s: substantivo){
            if(palavra.equals(s))
                return true;
        }
        return false;
    }

    /**
     *substantivos masculinos plural
     * @param palavra
     * @return
     */
    public boolean substantivoMasculinoPlural(String palavra){
        String[] substantivo = {"lobos","tambores"};

        for(String s: substantivo){
            if(palavra.equals(s))
                return true;
        }
        return false;
    }

    /**
     *substantivos femininos singular
     * @param palavra
     * @return
     */
    public boolean substantivoFemininoSingular(String palavra){
        String[] substantivo = {"menina","vida","noticia","porta","floresta","mae","cidade"};

        for(String s: substantivo){
            if(palavra.equals(s))
                return true;
        }
        return false;
    }

    /**
     *substantivos femininos plural
     * @param palavra
     * @return
     */
    public boolean substantivoFemininoPlural(String palavra){
        String[] substantivo = {"lagrimas"};

        for(String s: substantivo){
            if(palavra.equals(s))
                return true;
        }
        return false;
    }

    /**verbos singulares
     *
     * @param palavra
     * @return
     */
    public boolean singularVerb(String palavra){
        String[] verbos = {"corre","correu","bateu"};

        for(String v: verbos){
            if(palavra.equals(v))
                return true;
        }
        return false;
    }

    /**
     *verbos no plural
     * @param palavra
     * @return
     */
    public boolean pluralVerb(String palavra){
        String[] verbos = {"corriam","correram","bateram"};

        for(String v: verbos){
            if(palavra.equals(v))
                return true;
        }
        return false;
    }

    /**
     *preposicoes
     * @param palavra
     * @return
     */
    public boolean preposicao(String palavra){
        String[] prep = {"para","com","no","na","pelo","pela"};

        for(String p: prep){
            if(palavra.equals(p))
                return true;
        }
        return false;
    }

    /**
     * imprime o tuplo da estrutura da frase caso esteja sintaticamente correta
     * @param p
     */
    private void printTuple(int p){
        if(p == 1){
            System.out.println("sent(frase_nom(artigo('"+fr_Nominal.get(0)+"'),substantivo('"+fr_Nominal.get(1)+"'))" +
                    ",frase_verb(verbo('"+fr_Verbal.get(0)+"')))");
        }
        else if(p == 2){
            System.out.println("sent(frase_nom(artigo('"+fr_Nominal.get(0)+"')," +
                    "substantivo('"+fr_Nominal.get(1)+"')),frase_verb(verbo('"+fr_Verbal.get(0)+"')," +
                    "preposicao('"+fr_Verbal.get(1)+"'),artigo('"+fr_Verbal.get(2)+"'),substantivo('"+fr_Verbal.get(3)+"')))");
        }
        else if(p == 3){
            System.out.println("sent(frase_nom(artigo('"+fr_Nominal.get(0)+"'),substantivo('"+fr_Nominal.get(1)+"'))," +
                    "frase_verb(verbo('"+fr_Verbal.get(0)+"'),preposicao('"+fr_Verbal.get(1)+"'),substantivo('"+fr_Verbal.get(2)+"')))");
        }
        else if(p == 4){
            System.out.println("sent(frase_nom(artigo('"+fr_Nominal.get(0)+"')," +
                    "substantivo('"+fr_Nominal.get(1)+"')),frase_verb(verbo('"+fr_Verbal.get(0)+"')," +
                    "artigo('"+fr_Verbal.get(1)+"'),substantivo('"+fr_Verbal.get(2)+"')))");
        }
        else
            System.out.println("Frase sintaticamente incorreta!");
    }

    /**
     * Funcao que analisa a frase.
     * Implementado para todos os casos de comecar a frase.
     * @return
     */
    public boolean anaylizePhrase() {
        //A frase vai comecar com um artigo masculino singular
        if(artigoMasculinoSingular(fr_Nominal.get(0))){
            //se o artigo e masculino e singular, o substantivo tem de ser masculino e singular devido a concordancia.
            if(substantivoMasculinoSingular(fr_Nominal.get(1))){
                //substantivo singular, verbo singular
                if(singularVerb(fr_Verbal.get(0))){
                    if(fr_Verbal.size()==1){ //para frases que terminam no verbo
                        printTuple(1);
                        return true;
                    }

                    else{
                        //para frases que continuam depois do verbo
                        if(preposicao(fr_Verbal.get(1))){//verbos seguidos de preposicao

                            if(artigoMasculinoSingular(fr_Verbal.get(2))){ //verbos seguidos de artigo masculino singular
                                if(substantivoMasculinoSingular(fr_Verbal.get(3))){ //artigo masculino singular de seguida um substantivo masculino singular
                                    printTuple(2);
                                    return true;
                                }
                            }

                            else if(artigoMasculinoPlural(fr_Verbal.get(2))){ //verbos seguidos de artigo masculino plural
                                if(substantivoMasculinoPlural(fr_Verbal.get(3))){ //artigo masculino plural, substantivo masculino plural
                                    printTuple(2);
                                    return true;
                                }
                            }

                            else if(artigoFemininoSingular(fr_Verbal.get(2))){ //verbos seguidos de artigo feminino singular
                                if(substantivoFemininoSingular(fr_Verbal.get(3))){ //artigo feminino singular, substantivo feminino singular
                                    printTuple(2);
                                    return true;
                                }
                            }

                            else if(artigoFemininoPlural(fr_Verbal.get(2))){ //verbos seguidos de artigo feminino plural
                                if(substantivoFemininoPlural(fr_Verbal.get(3))){ //artigo feminino plural, substantivo feminino plural
                                    printTuple(2);
                                    return true;
                                }
                            }
                            //se nao tiver artigo: verbo + substantivo
                            else if(substantivoMasculinoSingular(fr_Verbal.get(2))){
                                printTuple(3);
                                return true;
                            }

                            else if(substantivoMasculinoPlural(fr_Verbal.get(2))){
                                printTuple(3);
                                return true;
                            }

                            else if(substantivoFemininoSingular(fr_Verbal.get(2))){
                                printTuple(3);
                                return true;
                            }

                            else if(substantivoFemininoPlural(fr_Verbal.get(2))){
                                printTuple(3);
                                return true;
                            }

                        }

                        //Sem preposicao
                        else if(artigoMasculinoSingular(fr_Verbal.get(1))){ //verbos seguidos de artigo masculino singular
                            if(substantivoMasculinoSingular(fr_Verbal.get(2))){ //artigo masculino singular, substantivo masculino singular
                                printTuple(4);
                                return true;
                            }
                        }

                        else if(artigoMasculinoPlural(fr_Verbal.get(1))){ //verbos seguidos de artigo masculino plural
                            if(substantivoMasculinoPlural(fr_Verbal.get(2))){ //artigo masculino plural, substantivo masculino plural
                                printTuple(4);
                                return true;
                            }
                        }

                        else if(artigoFemininoSingular(fr_Verbal.get(1))){ //verbos seguidos de artigo feminino singular
                            if(substantivoFemininoSingular(fr_Verbal.get(2))){ //artigo feminino singular, substantivo feminino singular
                                printTuple(4);
                                return true;
                            }
                        }

                        else if(artigoFemininoPlural(fr_Verbal.get(1))){ //verbos seguidos de artigo feminino plural
                            if(substantivoFemininoPlural(fr_Verbal.get(2))){ //artigo feminino plural, substantivo feminino plural
                                printTuple(4);
                                return true;
                            }
                        }
                    }
                }
            }
        }

        else if(artigoMasculinoPlural(fr_Nominal.get(0))){ //frase comeca com artigo masculino plural
            if(substantivoMasculinoPlural(fr_Nominal.get(1))){ //se o artigo e masculino e plural, o substantivo tem de ser masculino e plural
                if(pluralVerb(fr_Verbal.get(0))){ //substantivo plural, verbo plural
                    if(fr_Verbal.size()==1){ //para frases que terminam no verbo
                        printTuple(1);
                        return true;
                    }

                    else{ //para frases que continuam depois do verbo

                        if(preposicao(fr_Verbal.get(1))){//verbos seguidos de preposicao

                            if(artigoMasculinoSingular(fr_Verbal.get(2))){ //verbos seguidos de artigo masculino singular
                                if(substantivoMasculinoSingular(fr_Verbal.get(3))){ //artigo masculino singular, substantivo masculino singular
                                    printTuple(2);
                                    return true;
                                }
                            }

                            else if(artigoMasculinoPlural(fr_Verbal.get(2))){ //verbos seguidos de artigo masculino plural
                                if(substantivoMasculinoPlural(fr_Verbal.get(3))){ //artigo masculino plural, substantivo masculino plural
                                    printTuple(2);
                                    return true;
                                }
                            }

                            else if(artigoFemininoSingular(fr_Verbal.get(2))){ //verbos seguidos de artigo feminino singular
                                if(substantivoFemininoSingular(fr_Verbal.get(3))){ //artigo feminino singular, substantivo feminino singular
                                    printTuple(2);
                                    return true;
                                }
                            }

                            else if(artigoFemininoPlural(fr_Verbal.get(2))){ //verbos seguidos de artigo feminino plural
                                if(substantivoFemininoPlural(fr_Verbal.get(3))){ //artigo feminino plural, substantivo feminino plural
                                    printTuple(2);
                                    return true;
                                }
                            }

                            //nao tem artigo depois da preposicao
                            else if(substantivoMasculinoSingular(fr_Verbal.get(2))){
                                printTuple(3);
                                return true;
                            }

                            else if(substantivoMasculinoPlural(fr_Verbal.get(2))){
                                printTuple(3);
                                return true;
                            }

                            else if(substantivoFemininoSingular(fr_Verbal.get(2))){
                                printTuple(3);
                                return true;
                            }

                            else if(substantivoFemininoPlural(fr_Verbal.get(2))){
                                printTuple(3);
                                return true;
                            }

                        }

                        //frases sem preposicao depois do artigo
                        else if(artigoMasculinoSingular(fr_Verbal.get(1))){ //verbos seguidos de artigo masculino singular
                            if(substantivoMasculinoSingular(fr_Verbal.get(2))){ //artigo masculino singular, substantivo masculino singular
                                printTuple(4);
                                return true;
                            }
                        }

                        else if(artigoMasculinoPlural(fr_Verbal.get(1))){ //verbos seguidos de artigo masculino plural
                            if(substantivoMasculinoPlural(fr_Verbal.get(2))){ //artigo masculino plural, substantivo masculino plural
                                printTuple(4);
                                return true;
                            }
                        }

                        else if(artigoFemininoSingular(fr_Verbal.get(1))){ //verbos seguidos de artigo feminino singular
                            if(substantivoFemininoSingular(fr_Verbal.get(2))){ //artigo feminino singular, substantivo feminino singular
                                printTuple(4);
                                return true;
                            }
                        }

                        else if(artigoFemininoPlural(fr_Verbal.get(1))){ //verbos seguidos de artigo feminino plural
                            if(substantivoFemininoPlural(fr_Verbal.get(2))){ //artigo feminino plural, substantivo feminino plural
                                printTuple(4);
                                return true;
                            }
                        }
                    }
                }
            }
        }

        else if(artigoFemininoSingular(fr_Nominal.get(0))){ //frase comeca com artigo feminino singular
            if(substantivoFemininoSingular(fr_Nominal.get(1))){ //se o artigo e feminino e singular, o substantivo tem de ser feminino e singular
                if(singularVerb(fr_Verbal.get(0))){ //substantivo singular, verbo singular
                    if(fr_Verbal.size()==1){ //para frases que terminam no verbo
                        printTuple(1);
                        return true;
                    }

                    else{ //para frases que continuam depois do verbo

                        if(preposicao(fr_Verbal.get(1))){//verbos seguidos de preposicao

                            if(artigoMasculinoSingular(fr_Verbal.get(2))){ //verbos seguidos de artigo masculino singular
                                if(substantivoMasculinoSingular(fr_Verbal.get(3))){ //artigo masculino singular, substantivo masculino singular
                                    printTuple(2);
                                    return true;
                                }
                            }

                            else if(artigoMasculinoPlural(fr_Verbal.get(2))){ //verbos seguidos de artigo masculino plural
                                if(substantivoMasculinoPlural(fr_Verbal.get(3))){ //artigo masculino plural, substantivo masculino plural
                                    printTuple(2);
                                    return true;
                                }
                            }

                            else if(artigoFemininoSingular(fr_Verbal.get(2))){ //verbos seguidos de artigo feminino singular
                                if(substantivoFemininoSingular(fr_Verbal.get(3))){ //artigo feminino singular, substantivo feminino singular
                                    printTuple(2);
                                    return true;
                                }
                            }

                            else if(artigoFemininoPlural(fr_Verbal.get(2))){ //verbos seguidos de artigo feminino plural
                                if(substantivoFemininoPlural(fr_Verbal.get(3))){ //artigo feminino plural, substantivo feminino plural
                                    printTuple(2);
                                    return true;
                                }
                            }
                            //frases sem artigo depois da preposicao
                            else if(substantivoMasculinoSingular(fr_Verbal.get(2))){
                                printTuple(3);
                                return true;
                            }

                            else if(substantivoMasculinoPlural(fr_Verbal.get(2))){
                                printTuple(3);
                                return true;
                            }

                            else if(substantivoFemininoSingular(fr_Verbal.get(2))){
                                printTuple(3);
                                return true;
                            }

                            else if(substantivoFemininoPlural(fr_Verbal.get(2))){
                                printTuple(3);
                                return true;
                            }

                        }

                        // frases sem preposicao depois do artigo
                        else if(artigoMasculinoSingular(fr_Verbal.get(1))){ //verbos seguidos de artigo masculino singular
                            if(substantivoMasculinoSingular(fr_Verbal.get(2))){ //artigo masculino singular, substantivo masculino singular
                                printTuple(4);
                                return true;
                            }
                        }

                        else if(artigoMasculinoPlural(fr_Verbal.get(1))){ //verbos seguidos de artigo masculino plural
                            if(substantivoMasculinoPlural(fr_Verbal.get(2))){ //artigo masculino plural, substantivo masculino plural
                                printTuple(4);
                                return true;
                            }
                        }

                        else if(artigoFemininoSingular(fr_Verbal.get(1))){ //verbos seguidos de artigo feminino singular
                            if(substantivoFemininoSingular(fr_Verbal.get(2))){ //artigo feminino singular, substantivo feminino singular
                                printTuple(4);
                                return true;
                            }
                        }

                        else if(artigoFemininoPlural(fr_Verbal.get(1))){ //verbos seguidos de artigo feminino plural
                            if(substantivoFemininoPlural(fr_Verbal.get(2))){ //artigo feminino plural, substantivo feminino plural
                                printTuple(4);
                                return true;
                            }
                        }
                    }
                }
            }
        }

        else if(artigoFemininoPlural(fr_Nominal.get(0))){ //frase comeca com artigo feminino plural
            if(substantivoFemininoPlural(fr_Nominal.get(1))){//se o artigo e feminino e plural, o substantivo tem de ser feminino e plural
                if(pluralVerb(fr_Verbal.get(0))){ //substantivo plural, verbo plural
                    if(fr_Verbal.size()==1){ //para frases que terminam no verbo
                        printTuple(1);
                        return true;
                    }

                    else{ //para frases que continuam depois do verbo

                        if(preposicao(fr_Verbal.get(1))){//verbos seguidos de preposicao

                            if(artigoMasculinoSingular(fr_Verbal.get(2))){ //verbos seguidos de artigo masculino singular
                                if(substantivoMasculinoSingular(fr_Verbal.get(3))){ //artigo masculino singular, substantivo masculino singular
                                    printTuple(2);
                                    return true;
                                }
                            }

                            else if(artigoMasculinoPlural(fr_Verbal.get(2))){ //verbos seguidos de artigo masculino plural
                                if(substantivoMasculinoPlural(fr_Verbal.get(3))){ //artigo masculino plural, substantivo masculino plural
                                    printTuple(2);
                                    return true;
                                }
                            }

                            else if(artigoFemininoSingular(fr_Verbal.get(2))){ //verbos seguidos de artigo feminino singular
                                if(substantivoFemininoSingular(fr_Verbal.get(3))){ //artigo feminino singular, substantivo feminino singular
                                    printTuple(2);
                                    return true;
                                }
                            }

                            else if(artigoFemininoPlural(fr_Verbal.get(2))){ //verbos seguidos de artigo feminino plural
                                if(substantivoFemininoPlural(fr_Verbal.get(3))){ //artigo feminino plural, substantivo feminino plural
                                    printTuple(2);
                                    return true;
                                }
                            }

                            //frases que nao tem artigo depois da preposicao.
                            else if(substantivoMasculinoSingular(fr_Verbal.get(2))){
                                printTuple(3);
                                return true;
                            }

                            else if(substantivoMasculinoPlural(fr_Verbal.get(2))){
                                printTuple(3);
                                return true;
                            }

                            else if(substantivoFemininoSingular(fr_Verbal.get(2))){
                                printTuple(3);
                                return true;
                            }

                            else if(substantivoFemininoPlural(fr_Verbal.get(2))){
                                printTuple(3);
                                return true;
                            }

                        }

                        //frases sem preposicao depois do verbo
                        else if(artigoMasculinoSingular(fr_Verbal.get(1))){ //verbos seguidos de artigo masculino singular
                            if(substantivoMasculinoSingular(fr_Verbal.get(2))){ //artigo masculino singular, substantivo masculino singular
                                printTuple(4);
                                return true;
                            }
                        }

                        else if(artigoMasculinoPlural(fr_Verbal.get(1))){ //verbos seguidos de artigo masculino plural
                            if(substantivoMasculinoPlural(fr_Verbal.get(2))){ //artigo masculino plural, substantivo masculino plural
                                printTuple(4);
                                return true;
                            }
                        }

                        else if(artigoFemininoSingular(fr_Verbal.get(1))){ //verbos seguidos de artigo feminino singular
                            if(substantivoFemininoSingular(fr_Verbal.get(2))){ //artigo feminino singular, substantivo feminino singular
                                printTuple(4);
                                return true;
                            }
                        }

                        else if(artigoFemininoPlural(fr_Verbal.get(1))){ //verbos seguidos de artigo feminino plural
                            if(substantivoFemininoPlural(fr_Verbal.get(2))){ //artigo feminino plural, substantivo feminino plural
                                printTuple(4);
                                return true;
                            }
                        }
                    }
                }
            }
        }

        //caso nenhum daqueles casos nao se aplicar, entao retorna a string com a expressao invalida
        printTuple(5);
        return false;
    }
}
