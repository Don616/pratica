

import java.util.Scanner;

public class Aula5{
	public static void main(String[] args) {
		int idade = 1;
		String nome;
		Scanner input = new Scanner(System.in);
		
		do {
			nome = input.nextLine();
			System.out.println(">> "+ nome);
			idade = Integer.parseInt(input.nextLine());
			System.out.println(">> "+ idade);

		} while(idade < 18);
		System.out.println(nome + idade);
		
		input.close();
	}
}
