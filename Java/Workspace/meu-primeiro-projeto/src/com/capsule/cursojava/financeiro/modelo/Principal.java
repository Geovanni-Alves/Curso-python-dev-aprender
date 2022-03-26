package com.capsule.cursojava.financeiro.modelo;

import com.capsule.cursojava.financeiro.modelo.Fornecedor;
import com.capsule.cursojava.financeiro.modelo.ContaPagar;
import com.capsule.cursojava.financeiro.modelo.Cliente;
import com.capsule.cursojava.financeiro.modelo.ContaReceber;

public class Principal {

	public static void main(String[] args) {
		// instanciando fornecedores
		Fornecedor imobiliaria = new Fornecedor();
		imobiliaria.setNome("Casa & Cia Negocios Imobiliarios");
		Fornecedor mercado = new Fornecedor();
		mercado.setNome("Mercado do Joao");
		
		// instaciando clientes
		Cliente atacadista = new Cliente();
		atacadista.setNome("Triangulo Quadrado Atacadista");
		Cliente telecom = new Cliente();
		telecom.setNome("Fonenet Telecomunica��es");
		
		// instaciando contas a pagar
		ContaPagar contaPagar1 = new ContaPagar();
		
		contaPagar1.setDescricao("Aluguel da Matriz");
		contaPagar1.setValor(1230d);
		contaPagar1.setDataVencimento("10/05/2012");
		contaPagar1.setFornecedor(imobiliaria);
		
		ContaPagar contaPagar2 = new ContaPagar(mercado, "Compras do m�s", 390d, "19/05/2012");
		
		// instacioando contas a receber
		ContaReceber contaReceber1 = new ContaReceber();
		contaReceber1.setDescricao("Desenvolvimento de projeto de logistica em Java");
		contaReceber1.setValor(89500d);
		contaReceber1.setDataVencimento("23/05/2012");
		contaReceber1.setCliente(atacadista);
		
		ContaReceber contaReceber2 = new ContaReceber(telecom, "Manuten��o em sistema de conta online", 53200d, "13/05/2012");
		
		// pagamento e cancelamento de contas a pagar
		contaPagar1.Pagar();
		//System.out.println(contaPagar1.getFornecedor());
		contaPagar2.Cancelar();

		// recebimento e cancelamento de contas a receber
		contaReceber1.Receber();
		contaReceber2.Cancelar();
			
	}
}		
				
				
				
				
				