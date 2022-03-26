
public class Pessoa {
	
	String nome;
	int idade;
	
	Pessoa() {
		
	}
	
	String nomear(String nome) {
		
		return nome;
	}
	
	Pessoa(String nome) {
		this.nome = nome;
	}
	Pessoa(String nome, int idade) {
		this(nome); // deve ser a primeira instrucao dentro do construtor
		this.idade = idade;
	}
	
	
}
