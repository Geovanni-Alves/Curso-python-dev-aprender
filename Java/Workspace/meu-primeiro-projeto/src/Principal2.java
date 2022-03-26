
public class Principal2 {

	public static void main(String[] args) {
		Proprietario dono1 = new Proprietario();
		dono1.nome = "Geovanni Alves";
		
		
		Carro meuCarro = new Carro ();
		meuCarro.modelo = "Civic";
		
		Carro seuCarro = new Carro ();
		seuCarro.modelo = "Palio";
		
		meuCarro.dono = dono1;
		seuCarro.dono = dono1;
		
		meuCarro.dono.nome = "Lorena";
		
		System.out.println(meuCarro.dono.nome);
		System.out.println(seuCarro.dono.nome);
		System.out.println(dono1.nome);
		
	}

}
