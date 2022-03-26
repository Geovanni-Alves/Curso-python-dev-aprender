public class OperadorAritimetico1 {
	
	public static void main(String[] args) {
		int notaAluno1 = 99;
		int notaAluno2 = 80;
		int notaAluno3 = 53;
		int totalGeral = notaAluno1 + notaAluno2 + notaAluno3;

		int soma = 2 + 10;
		int subtracao = 6 - 10;
		int multiplicacao = 8 * 3;
		int divisao = 8 / 2;
		int resto = 7 % 2;
		
		System.out.println(soma);
		System.out.println(subtracao);
		System.out.println(multiplicacao);
		System.out.println(divisao);
		System.out.println(resto);
		System.out.println("Total Geral: " + totalGeral);
		
		int mediaGeral = (notaAluno1 + notaAluno2 + notaAluno3) / 3;
		System.out.println("Media Geral: " + mediaGeral);
	
		
	}	
}	