

while (true)

{
    Console.WriteLine("Put your age: ");
    string ageString = Console.ReadLine();
    int age = Convert.ToInt32(ageString);
    if (age >= 18 && age<=70)
    {
        Console.WriteLine("You can drive, pass away!");
    }
    else if(age < 18 && age > 70)
    {
        Console.WriteLine("You can't drive. Call someone.");
    }

}
