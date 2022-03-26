import java.util.Scanner;

public class DescobreBissexto {

	public static void main(String[] args) {
		Scanner testeAno = new Scanner(System.in);
		
		System.out.print("Digite o ano: ");
		int ano = testeAno.nextInt();
		
		if (ano % 400 == 0) {
			System.out.println("Este ano: " + ano + ", e Bissexto");
		} else if (ano % 4 == 0) {	
			if (ano % 100 != 0) {
			    System.out.println("Este ano: " + ano + ", e Bissexto");
			} else {	
			    System.out.println("Este ano: " + ano + ", nao e Bissexto");
			}
		} else {
			System.out.println("Este ano: " + ano + ", nao e Bissexto");
		}
	
	}
}