package com.capsule.java.seguro;

public class Carro implements Seguravel {
	
	private double valorMercado;
	private int anoFabricacao;
	
	public Carro(double valorMercado, int anoFabricacao) {
		this.valorMercado = valorMercado;
		this.anoFabricacao = anoFabricacao;
	}


	public double calcularValorApolice() {
		double valorApolice = this.valorMercado * 0.04;
		if (anoFabricacao < 2000) {
			valorApolice = valorApolice * 0.90;
		}
		return valorApolice;
	}

	
	public String obterDescricao() {

		return "Carro ano " + this.anoFabricacao + " com valor de mercado "
				+ this.valorMercado;
	}

}
