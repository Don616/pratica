import java.util.Scanner;


public class Aula4 {
	public static void main(String[] args) {
		
		int idade;
		String nome;

		Scanner teclado = new Scanner (System.in);

		System.out.println("Digite seu nome: ");
		nome = teclado.nextLine();

		System.out.println("Digite sua idade: ");
		idade = teclado.nextInt();

		System.out.println("Seu nome é "+nome+" e sua idade é "+idade);

		teclado.close();
		
			
	}

}
