using System;
using System.Collections.Generic;
using System.Linq;

class Student
{
    // Encapsulation (Properties)
    public int StudentId { get; set; }
    public string Name { get; set; }
    public string Department { get; set; }
    public int Year { get; set; }
    public int Marks { get; set; }

    // Constructor
    public Student(int id, string name, string dept, int year, int marks)
    {
        StudentId = id;
        Name = name;
        Department = dept;
        Year = year;
        Marks = marks;
    }
}

class Program
{
    static void Main()
    {
        List<Student> students = new List<Student>();

        int n;
        Console.Write("Enter number of students: ");
        n = Convert.ToInt32(Console.ReadLine());

        // Create student objects
        for (int i = 0; i < n; i++)
        {
            Console.WriteLine("\nEnter Student Details");

            Console.Write("ID: ");
            int id = Convert.ToInt32(Console.ReadLine());

            Console.Write("Name: ");
            string name = Console.ReadLine();

            Console.Write("Department: ");
            string dept = Console.ReadLine();

            Console.Write("Year: ");
            int year = Convert.ToInt32(Console.ReadLine());

            Console.Write("Marks: ");
            int marks = Convert.ToInt32(Console.ReadLine());

            students.Add(new Student(id, name, dept, year, marks));
        }

        // Display all students
        Console.WriteLine("\nAll Student Records");
        foreach (var s in students)
        {
            Console.WriteLine($"{s.StudentId} {s.Name} {s.Department} {s.Year} {s.Marks}");
        }

        // Students with marks > 75
        Console.WriteLine("\nStudents with Marks > 75");
        var highMarks = students.Where(s => s.Marks > 75);
        foreach (var s in highMarks)
        {
            Console.WriteLine($"{s.Name} - {s.Marks}");
        }

        // Sort by marks
        Console.WriteLine("\nStudents Sorted by Marks (Descending)");
        var sorted = students.OrderByDescending(s => s.Marks);
        foreach (var s in sorted)
        {
            Console.WriteLine($"{s.Name} - {s.Marks}");
        }

        // Top 3 scorers
        Console.WriteLine("\nTop 3 Scorers");
        var top3 = students.OrderByDescending(s => s.Marks).Take(3);
        foreach (var s in top3)
        {
            Console.WriteLine($"{s.Name} - {s.Marks}");
        }
        Console.ReadLine();
    }
}
