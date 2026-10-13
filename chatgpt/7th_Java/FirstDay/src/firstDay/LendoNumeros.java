package firstDay;

import java.util.Scanner;

public class LendoNumeros {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		
		System.out.println("Put your age: ");
		int idade = scanner.nextInt();
		
		System.out.println("Put your salary: ");
		double salario = scanner.nextDouble();
		
		System.out.printf("Your age is %d years old, and your salary is: %.2f%n.", idade, salario);
		
		scanner.close();
	}

}
