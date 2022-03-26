package com.capsule.java.cafe;

public class MaquinaCafe {
	int acucarDisponivel;
	
	public void fazerCafe(int quantidadeAcucar) {
		if (acucarDisponivel < quantidadeAcucar) {
			System.out.println("Nao ha açucar suficiente para fazer seu cafe.");
		} else {
			acucarDisponivel -= quantidadeAcucar;
			System.out.println("Fazendo cafezinho com " + quantidadeAcucar + " gramas de açucar.");
		}
			
	}
	public void fazerCafe() {
		fazerCafe(10);
	}
	

}
