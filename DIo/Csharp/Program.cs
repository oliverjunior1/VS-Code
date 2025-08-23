// int[] array_test = new int[] { 25, 76, 15, 27 };

// for (int i = 0; i < 4; i++)
// {
//     Console.WriteLine($"The array {i} é {array_test[i]}");
// }
///////////////////////////////////////////////////////////////
// int[] arrayInteiros = new int[3];

// arrayInteiros[0] = 72;
// arrayInteiros[1] = 64;
// arrayInteiros[2] = 50;
// // arrayInteiros[3] = 1;

// // Percorrendo o Array com o For
// for (int i = 0; i < arrayInteiros.Length; i++)
// {
//     Console.WriteLine($"Posicao nº {i} - {arrayInteiros[i]}");
// }

// // Console.WriteLine("Percorrendo o array com o foreach");
// // int contadorForEach = 0;
// // foreach (int valor in arrayInteiros)
// // {
// //     Console.WriteLine($"Posicao nº{contadorForEach}-{valor}");
// //     contadorForEach++;
// // }
// Array.Resize(ref arrayInteiros, arrayInteiros.Length * 2);

// int[] arratInteirosDobrado = new int[arrayInteiros.Length * 2];
// Array.Copy(arrayInteiros, arratInteirosDobrado, arrayInteiros.Length);
/////////////////////////////Listas//////////////////////////////

List<string> listaString = new List<string>();

listaString.Add("SP");
listaString.Add("BA");
listaString.Add("MG");
listaString.Add("GO");

for (int i = 0; i < listaString.Count; i++)
{
    Console.WriteLine($"Posicao nº {i} - {listaString[i]}");
}

int contador = 0;
foreach (string item in listaString)
{
    Console.WriteLine($"Posicao nº {contador} - {listaString[contador]}");
    contador++;
}

Console.WriteLine($"Itens na minha lista: {listaString.Count} - Capacidade: {listaString.Capacity}");

listaString.Add("SC");

Console.WriteLine($"Itens na minha lista: {listaString.Count} - Capacidade: {listaString.Capacity}");

listaString.Add("MG");

Console.WriteLine($"Itens na minha lista: {listaString.Count} - Capacidade: {listaString.Capacity}");

