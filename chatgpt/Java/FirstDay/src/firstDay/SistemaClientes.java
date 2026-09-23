package firstDay;

import java.util.Scanner;

public class SistemaClientes {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		
		System.out.println("Coloque o nome: ");
		String nome = scanner.next();
		
		System.out.println("Coloque a idade: ");
		int idade = scanner.nextInt();
		
		System.out.println("Coloque o salário: ");
		double salario = scanner.nextDouble();
		
		System.out.printf("===== CLIENTE =====%n Nome: %s %nIdade: %d %nSalário: %.2f", nome, idade, salario);
		
		scanner.close();
		

	}

}
