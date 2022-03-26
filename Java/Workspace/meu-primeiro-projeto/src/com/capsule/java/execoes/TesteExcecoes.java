package com.capsule.java.execoes;

public class TesteExcecoes {
	public static void main(String[] args) {
		// int numero = 5 /0;  // lan�a java.lang.arithmeticException
		//String s = "Texto";
		//s = null;
		//s.toUpperCase();  lan�a // java.lang.NullPointerException
		
		ContaCorrente cc = new ContaCorrente(1000);
		
		try {
			cc.depositar(-10);
			// varias linhas de codigo.... 
		} catch(IllegalArgumentException e) {
			System.out.println("Voce executou uma opera��o ilegal: "
					+ e.getMessage());
		}
	}
}
