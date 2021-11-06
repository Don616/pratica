public class Aula7 {
    public static void main(String[] args) {
        int num = 90;

        String p = (num % 2 == 0)? "\nO numero "+num+" é Par.\n":"\nO número "+num+" é Impar.\n";
        System.out.println(p);

    }
}