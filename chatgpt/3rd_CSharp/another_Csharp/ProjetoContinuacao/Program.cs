/* string[] cars = {"Volvo", "BMW", "Ford", "Mazda"};
foreach (string i in cars)
{
    Console.WriteLine(i);
} */

/* for (int i = 0; i < 10; i++)
{
    if (i==4)
    {
        break;
    }
    Console.WriteLine(i);
} */

for (int i = 0; i < 10; i++)
{
    if (i == 4)
    {
        continue;
    }
    Console.WriteLine(i);
}