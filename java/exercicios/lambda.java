
public class lambda {
@FunctionalInterface
interface Calc{
    public int calc(int x, int y);
}

    public static void main(String[] args){
        Calc soma = (x,y) -> x+y;


        System.out.println(exeOperation(soma, 10, 20));

        
    }

    public static int exeOperation(Calc calc, int x, int y) {
        return calc.calc(x, y);
    }



}