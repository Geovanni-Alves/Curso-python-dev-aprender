
public class ExemploThis {
	public static void main(String[] args) {
		Carro carro = new Carro();
		carro.modelo = "Ford Ka";
		carro.fabricante = "Ford";
		
		System.out.println(carro.modelo);
		System.out.println(carro.fabricante);
		
		carro.alterarModelo("BMW");
		
		System.out.println(carro.modelo);
		
		carro.alterarFabricante("GM");
		
		System.out.println(carro.fabricante);
	}

}
