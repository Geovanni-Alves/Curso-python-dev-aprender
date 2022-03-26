
public class Carro {

	String fabricante;
	String modelo;
	String cor;
	int anoDeFabricacao;
	boolean flex = true;
	
	Proprietario dono;
	
	void alterarModelo(String modelo) {
		if (modelo != null) {
			this.modelo = modelo;
		}
	}	
	void alterarFabricante(String fabricante) {
		if (fabricante != null) {
			this.fabricante = fabricante;
		}
	}
}
