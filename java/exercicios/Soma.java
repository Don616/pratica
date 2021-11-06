public class Soma{
    public static void main(String[] args){
        System.out.println(sum(5,6,5));
        System.out.println(sum(5,6));
        System.out.println(sum(5,6,1));
        System.out.println(sum(1,2,3,4,5,6,7));
    }

    public static int sum(int... n){
        int res=0;
        for(int v : n){
            res+=v;
        }
        return res;
    }
}