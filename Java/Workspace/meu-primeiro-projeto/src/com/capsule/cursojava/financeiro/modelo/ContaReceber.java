package com.capsule.cursojava.financeiro.modelo;

public class ContaReceber extends Conta {

	public ContaReceber() {
		
	}
	public ContaReceber(Cliente cliente, String descricao, 
			double valor, String dataVencimento) {
		this.situacaoConta = situacaoConta;
		this.cliente = cliente;
		this.descricao = descricao;
		this.valor = valor;
		this.dataVencimento = dataVencimento;		
	}
	public void Cancelar() {
		double vlr = this.valor;
		if (vlr > 50000) {
			System.out.println("conta maior que 50 mil, nao pode ser cancelada!");
		} else {
			System.out.println("Conta cancelada com sucesso");
		}
			
	}
	
	public void Receber() {
		
	}
}
