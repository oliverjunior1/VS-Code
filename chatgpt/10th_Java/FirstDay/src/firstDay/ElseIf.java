package firstDay;

public class ElseIf {

	public static void main(String[] args) {
		double nota = 8;
		
		if (nota >= 9) {
			System.out.println("Excelente");
		}
		else if (nota >= 7) {
			System.out.println("Aprovado");
		}
		else if (nota >= 5) {
			System.out.println("Recuperação");
		}
		else {
			System.out.println("Reprovado");
		}

	}

}
