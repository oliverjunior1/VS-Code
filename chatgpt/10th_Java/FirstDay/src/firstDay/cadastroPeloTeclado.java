package firstDay;

import java.util.Scanner;

public class cadastroPeloTeclado {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		
		System.out.println("Nome: ");
		String nome = scanner.nextLine();
		
		System.out.println("Idade: ");
		int idade = scanner.nextInt();
		
		System.out.println("Salário: ");
		double salario = scanner.nextDouble();
		
		System.out.println();
		System.out.println("===== CADASTRO =====");
		System.out.println("Nome: " + nome);
		System.out.println("Idade: " + idade);
		System.out.printf("Salário: %.2f", salario);
		
		scanner.close();

	}

}
