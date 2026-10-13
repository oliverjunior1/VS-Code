package firstDay;

import java.util.Scanner;

public class SistemaDeAprovacao {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		
		System.out.println("Digite a nota: ");
		double nota = scanner.nextDouble();
		
		if (nota >= 9) {
			System.out.println("Excelente!");
		}
		else if (nota >= 7) {
			System.out.println("Aprovado!");
		}
		else if (nota >= 5) {
			System.out.println("Recuperação.");
		}
		else {
			System.out.println("Reprovado.");
		}
		
		scanner.close();

	}

}
