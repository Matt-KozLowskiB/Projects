using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConApp2
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Enter your name, please:");
            String Name = Console.ReadLine();
            Console.WriteLine("Hello," + Name);
            Console.WriteLine("Press Return to terminate....");
            Console.Read();
        }
    }
}
