import java.util.Scanner;

public class Megasena {

	public static void main(String[] args) {
		Scanner entrada = new Scanner(System.in);
		System.out.print("Digite quantos jogos devem ser gerados.");
		int jogos = entrada.nextInt();
		int[] dezenas = new int[7];
		for (int j = 1; j <= jogos; j++ ) {
			for (int num = 0; num <  6; num++) {
				double dez = Math.random() * 60;
				//dez = (int) dez;
				dezenas[num] = (int) dez;
				
			}
			System.out.println(dezenas[0]+ " " + dezenas[1]
					+ " " + dezenas[2]+ " " + dezenas[3]+ " " +dezenas[4]+ " "
					+dezenas[5]+ " " +dezenas[6]);
		}
	}
}
