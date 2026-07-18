// See https://aka.ms/new-console-template for more information
// Console.WriteLine("Hello, World!");

// int myNum = 5;
// double myDouble = 5.5;
// char myLetter = 'D';
// bool myBool = true;
// string myText = "Hello";

// Console.WriteLine(myNum);
// Console.WriteLine(myDouble);
// Console.WriteLine(myLetter);
// Console.WriteLine(myBool);
// Console.WriteLine(myText);

// int myInt = 9;
// double myDouble = myInt;
// Console.WriteLine(myInt);
// Console.WriteLine(myDouble);

// double myDouble = 9.78;
// int myInt = (int) myDouble;
// Console.WriteLine(myDouble);
// Console.WriteLine(myInt);

// int myInt = 10;
// double myDouble = 5.25;
// bool myBool = true;
// Console.WriteLine(Convert.ToString(myInt));
// Console.WriteLine(Convert.ToDouble(myInt));
// Console.WriteLine(Convert.ToInt32(myDouble));
// Console.WriteLine(Convert.ToString(myBool));

// // Type your username and press enter
// Console.WriteLine("Enter username:");
// // Create a string variable and get user input from the keyboard and store it in the variable
// string userName = Console.ReadLine();
// // Print the value of the variable (userName), which will display the input value
// Console.WriteLine("Username is: " + userName);

// Console.WriteLine("Enter your age:");
// int age = Convert.ToInt32(Console.ReadLine());
// Console.WriteLine("Your age is: " + age);

// Class Members

// using System;

// namespace MyApplication
// {
//   class Car 
//   {
//     string color = "red";
//     int maxSpeed = 200;

//     static void Main(string[] args)
//     {
//       Car myObj = new Car();
//       Console.WriteLine(myObj.color);
//       Console.WriteLine(myObj.maxSpeed);
//     }
//   }
// }

// using System;
// using System.Runtime.CompilerServices;

// namespace MyApplication
// {
//     class Program
//     {
//        static void Main(string[] args)
//         {
//             Car Ford = new Car();
//             Ford.model = "Mustang";
//             Ford.color = "red";
//             Ford.year = 1969;

//             Car Opel = new Car();
//             Opel.model = "Astra";
//             Opel.color = "White";
//             Opel.year = 2005;

//             Console.WriteLine(Ford.model);
//             Console.WriteLine(Opel.model);
//         } 
//     }
// }

using System;

namespace MyApplication
{
    class Car
    {
        string model;
        string color;
        int year;

        static void Main(string[] args)
        {
            Car Ford = new Car()
            Ford.model = "Mustang";
            Ford.color = "red";
            Ford.year = 1969;

            Car Opel = new Car();
            Opel.model = "Astra";
            Opel.color = "white";
            Opel.year = 2005;

            Console.WriteLine(Ford.model);
            Console.WriteLine(Opel.model);

        }
    }
}