import java.util.Scanner;
//Aula de funções no java;

public class Aula14 {

	public static void main(String[] args){
		exec();

	}

	static void exec(){ // static void executa somente, sem retornar nada
		Scanner teclado = new Scanner(System.in);

		System.out.println("Digite um número: ");
		int x = teclado.nextInt();
		System.out.println("Digite outro número: ");
		int y = teclado.nextInt();
		int n1 = m1(x,y);
		int n2 = m2(x,y);
		int conta_fim = conta(n1,n2); 

		teclado.close();

		System.out.println("\nSua conta total foi: "+ conta_fim);
	}
	static int conta(int m1, int m2){ // static int (ou String, ou char... etc) sempre retornam
		return m2 + m1;

	}

	static int m1(int x, int y){
		return x * y;
	}
	static int m2(int x, int y){
		return (x * y) * 2;
	}
}

