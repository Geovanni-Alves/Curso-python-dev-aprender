package com.capsule.curso.fjoo.enums;

public enum OperacaoAritimetica {
	
	ADICAO() {
		public int operacao(int x, int y) {
			return x + y;
		}
	},
	SUBTRA��O {
		public int operacao(int x, int y) {
			return x - y;
		}
	};
	
	public abstract int operacao(int x, int y);

}
