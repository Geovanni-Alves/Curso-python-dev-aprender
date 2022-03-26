package com.capsule.java.cafe;

public class TesteMaquinaCafe {

	public static void main(String[] args) {
		MaquinaCafe maquina = new MaquinaCafe();
		maquina.acucarDisponivel = 30;	
		
		maquina.fazerCafe(40);
		maquina.fazerCafe();
		
		maquina.fazerCafe();
	}
}
