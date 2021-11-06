public class Recursivo{
    public static void main(String[] args){

        for(int i=0;i<20;i++){
            System.out.println(fibonacci(i));
        }

    }

    public static int fibonacci(int x){
        if(x == 0 || x == 1){
            return x;
        }else{
            return fibonacci(x-1) + fibonacci(x-2);
        }
    }
}