package com.capsule.java.cafe;

public class MaquinaCafe {
	int acucarDisponivel;
	
	public void fazerCafe(int quantidadeAcucar) {
		if (acucarDisponivel < quantidadeAcucar) {
			System.out.println("Nao ha a�ucar suficiente para fazer seu cafe.");
		} else {
			acucarDisponivel -= quantidadeAcucar;
			System.out.println("Fazendo cafezinho com " + quantidadeAcucar + " gramas de a�ucar.");
		}
			
	}
	public void fazerCafe() {
		fazerCafe(10);
	}
	

}
