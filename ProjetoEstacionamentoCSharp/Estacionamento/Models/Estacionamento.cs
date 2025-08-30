using System;
using System.Collections.Generic;

public class Estacionamento
{
    private List<Veiculo> veiculos = new List<Veiculo>();
    private const decimal PrecoPorHora = 5.00m;

    public void AdicionarVeiculo(string placa)
    {
        veiculos.Add(new Veiculo(placa));
        Console.WriteLine($"Veículo {placa} adicionado com sucesso.");
    }

    public void RemoverVeiculo(string placa)
    {
        var veiculo = veiculos.Find(v => v.Placa == placa);
        if (veiculo != null)
        {
            var tempoEstacionado = DateTime.Now - veiculo.HoraEntrada;
            var horas = Math.Ceiling(tempoEstacionado.TotalHours);
            var valor = (decimal)horas * PrecoPorHora;

            veiculos.Remove(veiculo);
            Console.WriteLine($"Veículo {placa} removido. Tempo: {horas}h. Valor cobrado: R${valor:F2}");
        }
        else
        {
            Console.WriteLine("Veículo não encontrado.");
        }
    }

    public void ListarVeiculos()
    {
        if (veiculos.Count == 0)
        {
            Console.WriteLine("Nenhum veículo estacionado.");
            return;
        }

        Console.WriteLine("Veículos estacionados:");
        foreach (var v in veiculos)
        {
            Console.WriteLine($"- {v.Placa} (Entrada: {v.HoraEntrada})");
        }
    }
}