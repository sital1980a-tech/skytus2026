using System;
using System.Collections.Generic;
using System.Linq;

class Student
{
    public int student_id;
    public string name;
    public string department;
    public int marks;
}

class Program
{
    static void Main()
    {
        List<Student> students = new List<Student>();

        Console.Write("Enter number of students: ");
        int n = Convert.ToInt32(Console.ReadLine());

        for (int i = 0; i < n; i++)
        {
            Student s = new Student();

            Console.Write("Student ID: ");
            s.student_id = Convert.ToInt32(Console.ReadLine());

            Console.Write("Name: ");
            s.name = Console.ReadLine();

            Console.Write("Department: ");
            s.department = Console.ReadLine();

            Console.Write("Marks: ");
            s.marks = Convert.ToInt32(Console.ReadLine());

            students.Add(s);
        }

        Console.WriteLine("\nAll Student Records");
        foreach (var s in students)
        {
            Console.WriteLine($"{s.student_id} {s.name} {s.department} {s.marks}");
        }

        Console.WriteLine("\nName and Department");
        foreach (var s in students)
        {
            Console.WriteLine($"{s.name} - {s.department}");
        }

        Console.WriteLine("\nStudents with marks > 75");
        var high = students.Where(x => x.marks > 75);

        foreach (var s in high)
        {
            Console.WriteLine($"{s.name} {s.marks}");
        }

        Console.Write("\nEnter Department to search: ");
        string dept = Console.ReadLine();

        var dep = students.Where(x => x.department.ToLower() == dept.ToLower());

        foreach (var s in dep)
        {
            Console.WriteLine($"{s.name} {s.department}");
        }

        Console.WriteLine("\nSorted by Marks (Descending)");

        var sorted = students.OrderByDescending(x => x.marks);

        foreach (var s in sorted)
        {
            Console.WriteLine($"{s.name} {s.marks}");
        }

        var top = students.OrderByDescending(x => x.marks).FirstOrDefault();

        if (top != null)
        {
            Console.WriteLine($"\nTop Scorer: {top.name} {top.marks}");
        }
        Console.ReadLine();
    }
}
