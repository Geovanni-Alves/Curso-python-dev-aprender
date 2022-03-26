import java.util.Scanner;

public class Estoque {

	public static void main(String[] args) {
		Scanner nomeProduto = new Scanner(System.in);
		Scanner quantProduto = new Scanner(System.in);
		
		System.out.print("Digite o nome do produto: ");
		String nomeProd = nomeProduto.nextLine();
		
		System.out.print("Quantidade do produto: ");
		int quantProd = quantProduto.nextInt();
	}

}
