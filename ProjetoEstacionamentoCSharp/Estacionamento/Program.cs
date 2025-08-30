using System;

class Program
{
    static void Main()
    {
        var estacionamento = new Estacionamento();
        string opcao;

        do
        {
            Console.WriteLine("\n=== Sistema de Estacionamento ===");
            Console.WriteLine("1 - Adicionar veículo");
            Console.WriteLine("2 - Remover veículo");
            Console.WriteLine("3 - Listar veículos");
            Console.WriteLine("0 - Sair");
            Console.Write("Escolha uma opção: ");
            opcao = Console.ReadLine();

            switch (opcao)
            {
                case "1":
                    Console.Write("Digite a placa do veículo: ");
                    var placaAdd = Console.ReadLine();
                    estacionamento.AdicionarVeiculo(placaAdd);
                    break;

                case "2":
                    Console.Write("Digite a placa do veículo: ");
                    var placaRemover = Console.ReadLine();
                    estacionamento.RemoverVeiculo(placaRemover);
                    break;

                case "3":
                    estacionamento.ListarVeiculos();
                    break;

                case "0":
                    Console.WriteLine("Encerrando o sistema...");
                    break;

                default:
                    Console.WriteLine("Opção inválida.");
                    break;
            }

        } while (opcao != "0");
    }
}