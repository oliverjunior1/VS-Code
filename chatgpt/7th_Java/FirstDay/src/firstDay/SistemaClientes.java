package firstDay;

import java.util.Scanner;

public class SistemaClientes {
	
	public static String classificarSalario(double salario) {
		if (salario >= 5000) {
			return "Alto";
		}
		else if (salario >= 3000) {
			return "Médio";
		}
		else {
			return "Baixo";
		}
	}
	
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		
		System.out.println("Coloque o nome: ");
		String nome = scanner.next();
		
		System.out.println("Coloque a idade: ");
		int idade = scanner.nextInt();
		
		System.out.println("Coloque o salário: ");
		double salario = scanner.nextDouble();
		
		System.out.printf("===== CLIENTE =====%nNome: %s %nIdade: %d %nSalário: %.2f%n", nome, idade, salario);
		
		
		if (idade >= 18) {
			System.out.println("Maior de idade");
		}
		else {
			System.out.println("Menor de idade");
		}
		
		String[] nomes = {"Joaquim", "Alyne", "Mariane", "João", "Ana"};
		
		for (String nome1: nomes) {
			System.out.println(nome1);
		}
		
		
		scanner.close();
		

	}

}
