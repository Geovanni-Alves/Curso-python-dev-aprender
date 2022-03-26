package com.capsule.curso.sobrecarga;

public class TesteCadastro {
	public static void main(String[] args) {
		CadastroPessoa cadastro = new CadastroPessoa();
		
		Pessoa pessoa = new Pessoa("Jose", 32);
		
		cadastro.cadastrar(pessoa);
		// 
		
		cadastro.cadastrar("Maria", 25);
		
		cadastro.cadastrar("Geovanni");
		
	}

}
