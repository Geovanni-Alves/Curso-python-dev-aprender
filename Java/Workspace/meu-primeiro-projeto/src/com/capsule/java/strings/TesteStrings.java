package com.capsule.java.strings;

public class TesteStrings {
	public static void main(String[] args) {
		// String, StringBuilder e StringBuffer
		
		String s = "Ola"; // Criada a String "Ola"
		s = s + " Pessoal "; // Criada a String "Ola Pessoal!"
		
		System.out.println(s);
		
		StringBuilder sb = new StringBuilder("Ola"); //existe a StringBUilder
		sb.append(" Pessoal!"); // reaproveitanto a StringBuilder
				
		String resultado = sb.toString();
		System.out.println(resultado);
		
		

	}

}
