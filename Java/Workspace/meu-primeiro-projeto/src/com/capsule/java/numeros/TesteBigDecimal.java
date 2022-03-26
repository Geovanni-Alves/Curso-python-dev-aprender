package com.capsule.java.numeros;

import java.math.BigDecimal;
import java.text.DecimalFormat;
import java.util.Scanner;

public class TesteBigDecimal {
	public static void main(String[] args) {
		DecimalFormat formatador = new DecimalFormat("R$ #,##0.00");
		Scanner entrada = new Scanner(System.in);
		System.out.println("Digite um numero para o calculo:");
		double numeroCalculo = entrada.nextDouble();
		//System.out.println(numeroCalculo);
		
		BigDecimal valorBig = new BigDecimal(numeroCalculo);
		BigDecimal resultado = valorBig.multiply(BigDecimal.TEN).divide(new BigDecimal(100));
		System.out.println("10% do valor e: " + formatador.format(resultado));
		
	}

}
