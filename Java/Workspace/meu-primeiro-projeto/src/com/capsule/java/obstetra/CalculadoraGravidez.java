package com.capsule.java.obstetra;


import java.util.Calendar;
import java.util.Date;
import java.util.GregorianCalendar;

public class CalculadoraGravidez {
	
	public CalculadoraGravidez(Date dataUltimoPeriodoMenstrual) {
		this.dataUltimoPeriodoMenstrual = dataUltimoPeriodoMenstrual;
	}
	private Date dataUltimoPeriodoMenstrual;
	
	private Calendar converterDateParaCalendar(Date data) {
		Calendar calendar = new GregorianCalendar();
		calendar.setTime(data);
		return calendar;
	}
	
	public Date calcularDataEstimadaConcepcao(Date concepcao) {
		Calendar c = converterDateParaCalendar(concepcao);
		c.add(Calendar.DAY_OF_WEEK, 14);
		concepcao = c.getTime();
		return concepcao;
	} 
	
	public Date calcularDataEstimadaParto(Date parto) {
		Calendar c = converterDateParaCalendar(parto);
		c.add(Calendar.DAY_OF_WEEK, 7 * 40);
		parto = c.getTime();
		return parto;
	} 
			
	
}
