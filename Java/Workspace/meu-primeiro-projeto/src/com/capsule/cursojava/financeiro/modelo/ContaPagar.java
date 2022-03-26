package com.capsule.cursojava.financeiro.modelo;

public class ContaPagar extends Conta {
	
	public ContaPagar() {
		
	}
	public ContaPagar(Fornecedor fornecedor, String descricao, 
			double valor, String dataVencimento) {
		this.situacaoConta = situacaoConta;
		this.fornecedor = fornecedor;
		this.descricao = descricao;
		this.valor = valor;
		this.dataVencimento = dataVencimento;		
	}
	void Pagar() {
		situacaoConta = getSituacaoConta();
		
		//System.out.println(situacaoConta);
		if (situacaoConta == situacaoConta.CANCELADA || situacaoConta == situacaoConta.PAGA) {
			System.out.println("Esta conta nao pode ser paga pois esta: "
					+ situacaoConta );
		} else {
			System.out.println("Conta Paga com sucesso!");
		
			
			situacaoConta = situacaoConta.PAGA;
			
			
		}
			
		
	}
	

}
