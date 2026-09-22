import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
    //System.out.println("Thank you my God!");

    
    //variáveis
    /* String nome = "Joaquim";
    int idade = 30;
    double salario = 4500.50;
    boolean ativo = true;

    System.out.println(nome);
    System.out.println(idade);
    System.out.println(salario);
    System.out.println(ativo); */

    
    //String
    /* String nome = "Joaquim";
    System.out.println(nome); */

    
    //Concatenar
    /* String nome = "Joaquim";
    int idade = 30;

    System.out.println("Nome: " + nome);
    System.out.println("Idade: " + idade); */

    
    // int com operações
    /* int idade = 28;
    System.out.println(idade + 1); */

    
    //double
    /* double preco = 50;
    int quantidade = 3;

    double total = preco * quantidade;

    System.out.println(total); */

    
    //Exemplo prático 1
    /* String nome = "Joaquim";
    int idade = 35;
    double salario = 5000;
    boolean ativo = true;

    System.out.println("Nome: " + nome);
    System.out.println("Idade: " + idade);
    System.out.println("Salário: " + salario);
    System.out.println("Ativo: " + ativo); */

    
    //Operadores matemáticos
    /* int a = 10;
    int b = 3;

    System.out.println(a + b);
    System.out.println(a - b);
    System.out.println(a * b);
    System.out.println(a / b);
    System.out.println(a % b); */
    

    //receber dados
    Scanner scanner = new Scanner(System.in);
    System.out.println("Digite seu nome: ");

    String nome = scanner.nextLine();

    System.out.println("Olá, " + nome);

    }
}