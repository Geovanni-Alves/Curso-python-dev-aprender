
public class Principal {

	public static void main(String[] args) {
		Carro meuCarro = new Carro();
		Carro seuCarro = new Carro();
		
		meuCarro.cor = "Branco";
		meuCarro.fabricante = "Honda";
		meuCarro.modelo = "Civic";
		meuCarro.anoDeFabricacao = 2021;
		
		seuCarro.fabricante = "Fiat";
		seuCarro.modelo = "Palio";
		seuCarro.anoDeFabricacao = 2011;
		seuCarro.cor = "Prata";
		
		System.out.println("Meu carro");
		System.out.println(meuCarro.fabricante);
		System.out.println(meuCarro.modelo);		
		System.out.println(meuCarro.cor);
		System.out.println(meuCarro.anoDeFabricacao);
		
				
		
	}

}
