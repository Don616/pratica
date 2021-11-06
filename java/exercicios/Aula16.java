import java.util.Scanner;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.PrintStream;

public class Aula16{
    public static Scanner input = new Scanner(System.in);


    public static void main(String[] args) throws FileNotFoundException {

        System.out.println("Escolha uma das opções: ");
        System.out.print("Digite: [E] para Escrever ou [L] para ler  ");
        String opcao = input.nextLine();
 
        
        switch(opcao){
            case "E": case "e":
                System.out.print("==============================");
                write();
                break;
            case "L": case "l":
                System.out.print("==============================");
                read();
                break;
            default:
                System.out.print("Digite somente o indicado!");
                break;
        }

        input.close();
        
    }

    public static void write() throws FileNotFoundException {
        PrintStream write = new PrintStream(new FileOutputStream("texto.txt", true));
        String msg = input.nextLine();
        write.printf("%n%s",msg);
        write.close();
        input.close();
    }

    public static void read() throws FileNotFoundException {
        Scanner read = new Scanner(new FileInputStream("texto.txt"));
        while(read.hasNextLine()){
            String line = read.nextLine();
            System.out.println(line);
        }

        read.close();
    }
}