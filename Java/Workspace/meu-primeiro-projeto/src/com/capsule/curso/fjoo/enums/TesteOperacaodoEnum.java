package com.capsule.curso.fjoo.enums;

public class TesteOperacaodoEnum {

	public static void main(String[] args) {
		OperacaoAritimetica o1 = OperacaoAritimetica.ADICAO;
		
		int resultado1 = o1.operacao(5, 3);
		System.out.println(resultado1);
		
		for (OperacaoAritimetica oa : OperacaoAritimetica.values()) {
		System.out.println(oa + " -> " + oa.operacao(4, 2));	
		}
		
		

	}

}
