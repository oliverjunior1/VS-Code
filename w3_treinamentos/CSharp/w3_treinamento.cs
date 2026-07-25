// using System;

// namespace w3_treinamento
// {
//     class Treino
//     {
//         public static void Main(string[] args)
//         {
//             Console.Write("Enter your username: ");
//             string userName = Console.ReadLine();

//             Console.WriteLine($"Welcome {userName}");
//         }
//     }
// }

using System;

namespace w3_treinamentos
{
    class treinamento
    {
        public static void Main(string[] args)
        {
            Console.WriteLine("Put your age: ");
            int age = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("Your age is: " + age);
        }
    }
}