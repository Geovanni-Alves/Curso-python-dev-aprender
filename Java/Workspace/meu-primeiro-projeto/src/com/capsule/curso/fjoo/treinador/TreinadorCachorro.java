package com.capsule.curso.fjoo.treinador;

import com.capsule.curso.fjoo.animal.Cachorro;

public class TreinadorCachorro {

	public static void main(String[] args) {
		Cachorro cachorro = new Cachorro();
		cachorro.setNome("Goku");

		DonoCachorro dono = new DonoCachorro();
		dono.ensinarCahorroSentar(cachorro);
	}

}
