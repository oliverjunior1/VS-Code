using System;

class DescontoInteligente
{
    static void Main()
    {

        // Lê o valor original do produto
        double valorOriginal = Convert.ToDouble(Console.ReadLine());

        // Lê a porcentagem de desconto
        double porcentagemDesconto = Convert.ToDouble(Console.ReadLine());

        // TODO: Verifique se o desconto está dentro de um intervalo válido

        // TODO: Calcule o valor final do produto
        if (porcentagemDesconto > 100)
        {
            Console.WriteLine("Desconto invalido");
        }
        else
        {
            double valorFinal = valorOriginal * ((-porcentagemDesconto + 100) / 100);
            // Exibe o valor com duas casas decimais
            Console.WriteLine($"{valorFinal:F2}");
        }





    }
}