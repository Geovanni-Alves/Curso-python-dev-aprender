
public class TesteArrays {

	public static void main(String[] args) {
		int[] notas = new int[5];
		notas[0] = 10;
		notas[1] = 5;
		notas[2] = 8;
		notas[3] = 9;
		notas[4] = 7;
		
		System.out.println(notas.length);
		
		for (int i = 0; i < notas.length; i++) {
			System.out.println("posicao[" + i + "]= " + notas[i]);
		}
	

	}

}
