
public class TesteEncapsulamento {

	public static void main(String[] args) {
		
		ArCondicionado ar = new ArCondicionado(); // 17 a 25
		
		ar.trocarTemperatura(21);
		
		System.out.println("Temperatura: " + ar.obterTemperatura()+"�");
		
		ar.trocarTemperatura(10);
		
		System.out.println("Temperatura: " + ar.obterTemperatura()+"�");
		 

	}

}
