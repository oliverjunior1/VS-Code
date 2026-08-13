// using System;

// namespace Program
// {
//     class Casting
//     {
//         static void Main(string[] args)
//         {   // casting
//             // Conversión Explícita
//             double miDouble = 12.37;
//             int miInt;
//             miInt = (int)miDouble;
//             Console.WriteLine(miInt);
//             // Conversión implícita
//             int num = 123456;
//             long numg = num;
//             Console.WriteLine(numg);
//             string miString = miDouble.ToString();
//             Console.WriteLine(miString);
//         }
//     }
// }

// using System;

// namespace Program
// {
//     class StringMethods
//     {
//         static void Main(string[] args)
//         {
//             string nombre = "Federico";
//             string apellido = "Garay";
//             string nombreCompleto = string.Concat("", nombre,apellido,"");
//             Console.WriteLine(nombre.Substring(2));
//             Console.WriteLine(nombre.ToLower());
//             Console.WriteLine(nombre.ToUpper());
//             Console.WriteLine(nombre.IndexOf('e'));
//             Console.WriteLine(nombreCompleto.Trim());
//             Console.WriteLine(string.IsNullOrWhiteSpace(nombre));

//         }
//     }
// }

// using System;

// namespace Program
// {
//     class StringFormat
//     {
//         static void Main(string[] args)
//         {
//             var nombre = "Federico";
            
//             Console.WriteLine(String.Format("Mi nombre es {0}", nombre));
//         }
//     }
// }


using System;

namespace Program
{
    class String
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Put your name to receive the bless:  ");
            string nombre = Console.ReadLine();
            Console.WriteLine("God bless you, in the name of Jesus: " + nombre.ToUpper());
            Console.WriteLine("God bless you, in the name of Jesus: " + nombre.ToLower());
            Console.WriteLine("God bless you, in the name of Jesus: " + nombre.Trim());
            Console.WriteLine("God bless you, in the name of Jesus: " + nombre.Substring(0,5));
        }
    }
}