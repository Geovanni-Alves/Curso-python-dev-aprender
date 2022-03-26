package com.capsule.java.numeros;

import java.math.BigDecimal;
import java.text.DecimalFormat;
import java.text.ParseException;

public class TesteNumeros {
	
	public static void main(String[] args) {
		DecimalFormat formatador = new DecimalFormat("R$ #,###,##0.00");
		double valorProduto = 314500.59;
		double outroProduto = 10.60;
		double maisUmProduto = 5.35;
				
		System.out.println(valorProduto);
		System.out.println(formatador.format(valorProduto));
		System.out.println(formatador.format(outroProduto));
		System.out.println(formatador.format(maisUmProduto));
		
		String entrada = "R$ 50,34";
		try {
			double numero = formatador.parse(entrada).doubleValue();
			System.out.println("Numero: " + numero);
		} catch (ParseException e) {
			// TODO Auto-generated catch block
			System.out.println("Entrada Invalida.");
		}
		
		BigDecimal bg = new BigDecimal(5000);
		
		System.out.println(bg);
		
		
	}

}
