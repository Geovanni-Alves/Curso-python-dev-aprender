package com.capsule.java.execoes;

public class TesteExcecoesChegadas {
	public static void main(String[] args) {
		ContaCorrente cc = new ContaCorrente(100);
		
		try {
		   cc.sacar(80);
		} catch (SaldoInsuficienteException e) {
			System.out.println("Desculpe Saldo insuficiente");
		} finally {
			System.out.println("Obrigado por utilizar nosso sistema!");
		}
		
		System.out.println(cc.getSaldo());
		
		try {
			cc.sacar(30);
		} catch (SaldoInsuficienteException e) {
			System.out.println("Desculpe Saldo insuficiente");
		}
		
		System.out.println(cc.getSaldo());
		
	}
}
