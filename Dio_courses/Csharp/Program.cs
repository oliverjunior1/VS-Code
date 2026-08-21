// About the $ sign before the string
/*string nome = "Joaquim";
int idade = 25;
Console.WriteLine($"Hello, {nome}!");
Console.WriteLine($"You are {idade} years old.");
*/
// About the @ sign before the string
/*string path = @"C:\Users\Joaquim\Documents\file.txt";
Console.WriteLine(path);
*/
// Combining both $ and @ signs
/*string nome = "Joaquim";
int idade = 25;
string path = @"C:\Users\Joaquim\Documents\file.txt";
Console.WriteLine($"Hello, {nome}!");
Console.WriteLine($"You are {idade} years old.");
Console.WriteLine(path);
*/
// Switch case example
/*
while (true)
{
    Console.WriteLine("Put the number of the day to see the week day correspondently: ");
    string day = Console.ReadLine();
    int day_num = Convert.ToInt32(day);

    switch (day_num)
    {
        case 1:
            Console.WriteLine("Sunday");
            break;
        case 2:
            Console.WriteLine("Monday");
            break;
        case 3:
            Console.WriteLine("Tuesday");
            break;
        case 4:
            Console.WriteLine("Wednesday");
            break;
        case 5:
            Console.WriteLine("Thursday");
            break;
        case 6:
            Console.WriteLine("Friday");
            break;
        case 7:
            Console.WriteLine("Saturday");
            break;
        default:
            Console.WriteLine("Invalid option.");
            break;
    }

}

*/

// Lottery example
// MegaSena and Lotofacil
/*
Random random = new Random();
int[] megaSena = new int[6];
int[] lotoFacil = new int[15];
for (int i = 0; i < 6; i++)
{
    megaSena[i] = random.Next(1, 61);
}
for (int i = 0; i < 15; i++)
{
    lotoFacil[i] = random.Next(1, 26);
}

// Print the results in in crescent order and without repetitions, and if there are repetitions, generate new numbers until the array is full of unique numbers
while (megaSena.Distinct().Count() < 6)
{
    for (int i = 0; i < 6; i++)
    {
        megaSena[i] = random.Next(1, 61);
    }
}

while (lotoFacil.Distinct().Count() < 15)
{
    for (int i = 0; i < 15; i++)
    {
        lotoFacil[i] = random.Next(1, 26);
    }
}

Array.Sort(megaSena);
Array.Sort(lotoFacil);
Console.WriteLine("Mega Sena: " + string.Join(", ", megaSena.Distinct()));
Console.WriteLine("Loto Facil: " + string.Join(", ", lotoFacil.Distinct()));

*/
// class and object example
/*
Person person1 = new Person();
person1.Name = "Joaquim";
person1.Age = 25;
person1.IntroduceYourself();
Person person2 = new Person();
person2.Name = "Maria";
person2.Age = 30;
person2.IntroduceYourself();
public class Person
{
    public string Name;
    public int Age;

    public void IntroduceYourself()
    {
        Console.WriteLine($"Hello, my name is {Name} and I am {Age} years old.");
    }
}



//1. 	Solicita o nome e idade do usuário.
Console.WriteLine("Enter your name: ");
string name = Console.ReadLine();
Console.WriteLine("Enter your age: ");
int age = Convert.ToInt32(Console.ReadLine());
//2. 	Imprime uma mensagem personalizada.
Console.WriteLine($"Hello {name}, you are {age} years old.");
//3. 	Diz se o usuário é maior de idade.
if (age >= 18)
{
    Console.WriteLine("You are an adult.");
}
else
{
    Console.WriteLine("You are a minor.");
}
//4. 	Calcula e imprime o ano de nascimento do usuário.
int currentYear = DateTime.Now.Year;
int birthYear = currentYear - age;
Console.WriteLine($"You were born in {birthYear}.");

*/

//5. 	Calcula e imprime quantos anos faltam para o usuário se aposentar (considerando 65 anos para homens e 60 para mulheres).
Console.WriteLine("Enter your gender (M/F): ");
string gender = Console.ReadLine();
int retirementAge = (gender.ToUpper() == "M") ? 65 : 60;
int age = Convert.ToInt32(Console.ReadLine());
int yearsLeft = retirementAge - age;
Console.WriteLine($"You have {yearsLeft} years left until retirement.");

if (yearsLeft > 0)
{
    Console.WriteLine($"You have {yearsLeft} years left until retirement.");
}
else
{
    Console.WriteLine("You are already retired.");
}


