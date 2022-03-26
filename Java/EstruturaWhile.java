import java.util.Scanner;

public class EstruturaWhile {
	
	public static void main(String[] args) {
		Scanner entrada = new Scanner(System.in);
		
		System.out.print("Digite o numero inicial: ");
		int numeroInicial = entrada.nextInt();
		
		System.out.print("Digite o numero final: ");
		int numeroFinal = entrada.nextInt();
		
		int numeroAtual = numeroInicial;
		
		while (numeroAtual <= numeroFinal){
			System.out.println(numeroAtual);		
			numeroAtual++;
		}
		int valor = 0;
		int soma = 0;

		do {
			System.out.println("Digite 0 para sair ou qualquer numero para somar: ");
			valor = entrada.nextInt();

			soma += valor;
			System.out.println("Soma: " + soma);

		} while (valor != 0);

	}
	
} 