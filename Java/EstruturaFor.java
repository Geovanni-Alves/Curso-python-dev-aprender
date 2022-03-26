import java.util.Scanner;

public class EstruturaFor {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        
        System.out.print("Ultimo numero: ");
        int numeroFinal = entrada.nextInt();

        // for (iniciação ; condição; incremento)
        for (int i = 1; i <= numeroFinal; i++){
            if (i > 50) {
                break;
            }
            System.out.println(i);
        }
        System.out.println("foi usado o break");

    }

}