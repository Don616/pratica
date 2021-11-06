public class Aula13 {
    public static void main(String[] args) {
        int num1[]; // Apenas Declarando
        int num2[] = new int[5]; // Declarando e determinando o tamanho
        int num3[] = {0,1,2,3,4}; // Declarando e inicializando

        for(int i = 0; i < num2.length;i++){
            System.out.println(num2[i] = i * 3);
        }
    }
} 