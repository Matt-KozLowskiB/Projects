using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace tryCatchBlock
{
    class Program
    {
        static void Main(string[] args)
        {
            try
            {
                Console.WriteLine("Enter a number");
                int number = int.Parse(Console.ReadLine());
                Console.WriteLine("You entered: " + number);
            }
            catch (FormatException ex)
            {
                Console.WriteLine("Entry must be a number");
                Console.WriteLine(ex.GetType().Name);
                Console.Read();
            }
            finally
            {
                Console.WriteLine("Please re-run the program");
                Console.Read();
            }
        }
    }
}
