/* Calculadora feita no bloco de notas para treinar. Para calcular, passe os parâmetros direto no terminal
Se não passar derá erro, então passe de out of the range.
Estou com preguiça de tratar...
Grato pela compreensão */

public class Calculadora{

	public static void main(String[] args){
	
	int a = Integer.parseInt(args[0]);
	int b = Integer.parseInt(args[1]);

	System.out.println(somar(a,b));
	System.out.println(diminuir(a,b));
	System.out.println(dividir(a,b));
	System.out.println(multiplicar(a,b));

	}

	public static int somar(int x, int y){
	return x + y;

	}

	public static int diminuir(int x,int y){
	return x - y;	

	}

	public static int dividir(int x, int y){
	return x / y;

	}
	
	public static int multiplicar(int x, int y){
	return x * y;	

	}



}
