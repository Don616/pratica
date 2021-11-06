public class Aula11 {
    public static void main(String[] args) {
        char l1=100,l2=(char)(l1+11),l3=(char)(l2-1);
        String[] nome;

        System.out.printf("%c%c%c\n",l1,l2,l3);
        System.out.println(Character.SIZE + l1 + l2 + l3);
    }
}