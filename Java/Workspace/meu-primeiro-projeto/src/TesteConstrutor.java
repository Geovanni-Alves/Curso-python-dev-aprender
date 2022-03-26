
public class TesteConstrutor {

	public static void main(String[] args) {
		Pessoa p1 = new Pessoa("Geovanni");
		
		System.out.println("nome: \"" + p1.nome + "\" tem " + p1.idade + " anos." );
		
		Pessoa p2 = new Pessoa("Lorena", 35);
		//p1.nome = "Geovanni";
		p1.idade = 37;
				
		System.out.println("nome: \"" + p2.nome + "\" tem " + p2.idade + " anos." );
		//System.out.println(p1.nomear("malvado"));
		
	}

}
