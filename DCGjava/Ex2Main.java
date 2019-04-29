import java.util.LinkedList;
import java.util.Scanner;

class Ex2Main{
    public static void readInput() {
        Scanner in = new Scanner(System.in);
        Frase sr = new Frase();
        System.out.println("Intoduza uma frase, com palavras cada uma separada por um espaco e sem ponto de final: ");
        System.out.println("Exemplo: Os lobos corriam com lagrimas\n");
        System.out.println("Caso pretenda sair, escreva: exit");
        String answer = in.nextLine();

        LinkedList<String> phrase;
        while(!answer.equals("exit")){
            phrase = sr.seperarPalavrasdaFrase(answer);
            sr.phraseNomeVerbo(phrase);
            sr.anaylizePhrase();
            System.out.println("\n> ");
            answer = in.nextLine();
        }
    }
    public static void main(String [] args){
        readInput();
    }
}
