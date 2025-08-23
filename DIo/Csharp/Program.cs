// int[] array_test = new int[] { 25, 76, 15, 27 };

// for (int i = 0; i < 4; i++)
// {
//     Console.WriteLine($"The array {i} é {array_test[i]}");
// }
///////////////////////////////////////////////////////////////
int[] arrayInteiros = new int[3];

arrayInteiros[0] = 72;
arrayInteiros[1] = 64;
arrayInteiros[2] = 50;
// arrayInteiros[3] = 1;

// Percorrendo o Array com o For
for (int i = 0; i < arrayInteiros.Length; i++)
{
    Console.WriteLine($"Posicao nº {i} - {arrayInteiros[i]}");
}

// Console.WriteLine("Percorrendo o array com o foreach");
// int contadorForEach = 0;
// foreach (int valor in arrayInteiros)
// {
//     Console.WriteLine($"Posicao nº{contadorForEach}-{valor}");
//     contadorForEach++;
// }
Array.Resize(ref arrayInteiros, arrayInteiros.Length * 2);