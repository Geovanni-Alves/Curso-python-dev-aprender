package com.capsule.cursojava.financeiro.modelo;

public class Conta {
	protected String descricao;
	protected double valor;
	protected String dataVencimento;
	protected Fornecedor fornecedor;
	protected Cliente cliente;
	
	public Cliente getCliente() {
		return cliente;
	}
	public void setCliente(Cliente cliente) {
		this.cliente = cliente;
	}

	protected SituacaoConta situacaoConta;
	
	public Conta(Fornecedor fornecedor, String descricao, 
			double valor, String dataVencimento) {
		this.situacaoConta = situacaoConta;
		this.fornecedor = fornecedor;
		this.descricao = descricao;
		this.valor = valor;
		this.dataVencimento = dataVencimento;		
	}
	public Conta() {
		situacaoConta = SituacaoConta.PENDENTE;
	}
	void Cancelar() {
		situacaoConta = getSituacaoConta();
		//System.out.println(situacaoConta);
		if (situacaoConta != situacaoConta.CANCELADA) {
			System.out.println("Conta CANCELADA com sucesso");
			situacaoConta = situacaoConta.CANCELADA;		
		}
	}
	public String getDescricao() {
		return descricao;
	}

	public void setDescricao(String descricao) {
		this.descricao = descricao;
	}

	public double getValor() {
		return valor;
	}

	public void setValor(double valor) {
		this.valor = valor;
	}

	public String getDataVencimento() {
		return dataVencimento;
	}

	public void setDataVencimento(String dataVencimento) {
		this.dataVencimento = dataVencimento;
	}

	public Fornecedor getFornecedor() {
		return fornecedor;
	}

	public void setFornecedor(Fornecedor fornecedor) {
		this.fornecedor = fornecedor;
	}

	public SituacaoConta getSituacaoConta() {
		return situacaoConta;
	}
}
