// using System;

// namespace Program2
// {
//   // Create a Car class
//   class Car
//   {
//     public string model;  // Create a field

//     // Create a class constructor for the Car class
//     public Car()
//     {
//       model = "Mustang"; // Set the initial value for model
//     }

//     static void Main(string[] args)
//     {
//       Car Ford = new Car();  // Create an object of the Car Class (this will call the constructor)
//       Console.WriteLine(Ford.model);  // Print the value of model
//     }
//   }
// }

// using System;

// namespace Program2
// {
//     class Car
//     {
//         public string model;
//         public Car()
//         {
//             model = "Mustang";
//         }
//         static void Main(string[] args)
//         {
//             Car Ford = new Car();
//             Console.WriteLine(Ford.model);
//         }
//     }
// }

// using System;

// namespace Program2
// {
//     class Car
//     {
//         public string model;
    
//         public Car(string modelName)
//         {
//             model = modelName;
//         }
//         static void Main(string[] args)
//         {
//             Car Ford = new Car("Mustang");
//             Console.WriteLine(Ford.model);
//         }
//     }

// }

// using System;

// namespace Program2
// {
//     class Car
//     {
//         public string model;
//         public string color;
//         public int year;

//         public Car(string modelNasme, string modelColor, int modelYear)
//         {
//             model = modelNasme;
//             color = modelColor;
//             year = modelYear;
//         }
//         static void Main(string[] args)
//         {
//             Car Ford = new Car("Mustang", "Red", 1969);
//             Console.WriteLine(Ford.color + " " + Ford.year + " " + Ford.model);
//         }
//     }
// }

// using System;
// using Prog2;

// namespace Program2
// {
//     class Program
//     {
//         static void Main(string[] args)
//         {
//             Car Ford = new Car();
//             Ford.model = "Mustang";
//             Ford.color = "red";
//             Ford.year = 1969;

//             Car Opel = new Car();
//             Opel.model = "Astra";
//             Opel.color = "white";
//             Opel.year = 2005;

//             Console.WriteLine(Ford.model);
//             Console.WriteLine(Opel.model);

//         }
//     }
// }

// Access Modifiers

