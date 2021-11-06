import java.util.Random;

public class Rand{
	public static void main(String[] args){

		Random num = new Random();
		int a = num.nextInt();
		System.out.println(a);
		System.out.println(num.nextInt(522));
	}
}
