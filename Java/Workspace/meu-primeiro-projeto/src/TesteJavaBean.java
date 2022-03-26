
public class TesteJavaBean {

	public static void main(String[] args) {
		PessoaBean pessoa = new PessoaBean();
		pessoa.setNome("Geovanni Alves");
		pessoa.setIdade(37);
		
		System.out.println(pessoa.getNome() + " tem " + pessoa.getIdade());

	}

}
