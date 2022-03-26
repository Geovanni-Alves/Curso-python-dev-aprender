package com.capsule.java.obstetra;


import java.text.DateFormat;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Locale;
import java.util.Scanner;

public class Principal {
	
	public static void main(String[] args) {
		new Principal();
	}
	public Principal() {
		Scanner entrada = new Scanner(System.in);
		
		try {
			System.out.println("Data do ultimo periodo menstrual (dd/mm/aaaa):");
			String ultimoPeriodoMenstrual = entrada.nextLine();
			
			 
			Date dataUltimoPeriodoMenstrual = this.converterEmData(ultimoPeriodoMenstrual);
			CalculadoraGravidez calculadora = new CalculadoraGravidez(dataUltimoPeriodoMenstrual);
			
			Date dataEstimadaConcepcao = calculadora.calcularDataEstimadaConcepcao(dataUltimoPeriodoMenstrual);
			System.out.println("Data estimada da concepcao: "
					+ this.formatarData(dataEstimadaConcepcao));
					
			Date dataEstimadaParto = calculadora.calcularDataEstimadaParto(dataUltimoPeriodoMenstrual);
			System.out.println("Data estimada para o parto:"
					+ this.formatarData(dataEstimadaParto));
		} catch (ParseException pe) {
			System.out.println("Informe uma data no padrao dd/mm/aaaa.");
		}
	}
	private String formatarData(Date data) {
		DateFormat formatador = new SimpleDateFormat("EEEE, dd 'de' MMMM 'de' yyyy",
				new Locale("pt","br"));
		return formatador.format(data);
	}
	
	private Date converterEmData(String texto) throws ParseException {
		
		/*String dataAniversario = "26/03/1984";
		DateFormat formatador2 = new SimpleDateFormat("dd/MM/yyyy");
		try {
			Date aniversario = formatador2.parse(dataAniversario);
			System.out.println(formatador2.format(aniversario));
		} catch (ParseException e) {
			System.out.println("Formatado de data invalido");*/
		
		
		DateFormat formatador = new SimpleDateFormat("dd/MM/yyyy");
		try {
			Date dataFormatada = formatador.parse(texto);
			//System.out.println(data.format(dataFormatada));
		} catch (ParseException e) {
			System.out.println("Formatado de data invalido");
		}
		return formatador.parse(texto);
	}

}
