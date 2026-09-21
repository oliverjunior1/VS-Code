// tipos
/* string nome = "Joaquim";// string
int idade = 30; // integer
double salario = 3500.50; //double
bool ativo = true; //booleano
 */

// first exibition
/* string nome = "Maria";
Console.WriteLine(nome); */

// Integer
/* int idade = 25;
Console.WriteLine(idade+1); */

//double
/* double preco = 49.90;
int quantidade = 3;

double total = preco * quantidade;

Console.WriteLine(total); */

//boolean
/* bool aprovado = true;

Console.WriteLine(aprovado); */

// Recebendo dados do usuário
/* Console.Write("Digite seu nome: ");

string nome = Console.ReadLine();

Console.WriteLine("Olá, " + nome); */

//Conversao de dados

/* Console.Write("Digite sua idade: ");

int idade = int.Parse(Console.ReadLine());

Console.WriteLine("Você tem " + idade + " anos."); */

// Cálculos
/* int a = 10;
int b = 3;

Console.WriteLine(a + b);
Console.WriteLine(a - b);
Console.WriteLine(a * b);
Console.WriteLine(a / b);
Console.WriteLine(a % b); */

//Calculadora simples
/* Console.Write("Digite o primeiro número: ");
double numero1 = double.Parse(Console.ReadLine());

Console.Write("Digite o segundo número: ");
double numero2 = double.Parse(Console.ReadLine());

double soma = numero1 + numero2;
double subtracao = numero1 - numero2;
double multiplicacao = numero1 * numero2;
double divisao = numero1 / numero2;

Console.WriteLine("Soma: " + soma);
Console.WriteLine("Subtração: " + subtracao);
Console.WriteLine("Multiplicação: " + multiplicacao);
Console.WriteLine("Divisão: " + divisao); */

// Condições
/* int idade = 20;

if (idade >=18)
{
    Console.WriteLine("Maior de idade");
} */

// if else
/* int idade = 16;

if (idade >=18)
{
    Console.WriteLine("Maior de idade.");
}
else
{
    Console.WriteLine("Menor de idade");
} */

// else if

/* int nota = 8;

if (nota >= 9)
{
    Console.WriteLine("Excelente");
}
else if(nota >= 7)
{
    Console.WriteLine("Aprovado");
}
else if(nota >= 5)
{
    Console.WriteLine("Recupecação");
}
else
{
    Console.WriteLine("Reprovado");
} */

// Operação de comparação
/* int idade = 25;

if (idade >= 18)
{
    Console.WriteLine("Pode entrar.");

} */

// And - &&

/* using System.Text.Json;

int idade = 25;
bool document = true;

if (idade >= 18 && document == true)
{
    Console.WriteLine("Entrada permitida.");
} */

// Or - ||
/* bool administrador = false;
bool gerente = true;

if (administrador || gerente)
{
    Console.WriteLine("Acesso permitido.");
} */

// Not - !
/* bool ativo = true;

if (!ativo)
{
    Console.WriteLine("Usuário inativo.");
} */

// Sistema de notas
/* Console.Write("Digite a nota:");

double nota = double.Parse(Console.ReadLine());

if (nota >= 9)
{
    Console.WriteLine("Excelente!");
}
else if (nota >= 7)
{
    Console.WriteLine("Aprovado!");
}
else if (nota >= 5)
{
    Console.WriteLine("Recuperação.");
}
else
{
    Console.WriteLine("Reprovado");
} */

// for
/* for (int i = 1; i <= 5; i++)
{
    Console.WriteLine(i);
} */

// while
int contador = 1;

while (contador <= 5)
{
    Console.WriteLine(contador);

    contador++;
}