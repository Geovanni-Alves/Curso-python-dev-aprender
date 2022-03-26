import java.util.Scanner;

public class ClassificaProduto {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int codProduto = 0;
        String corredor = "";

        System.out.print("Digite o codigo do produto: ");
        codProduto = entrada.nextInt();
       
        if (codProduto != 0) {
            corredor = (codProduto % 2 == 0) ? "Direito" : "Esquerda";
        } else {
           
        }

        for(int i = 8 ; i >= 1 ;i--){
            if(codProduto % i == 0){
                System.out.println("O produto de codigo: " + codProduto + " ficara no corredor da " + corredor + " e na gaveta "+ i);
                break;
            }
        }

    }

}