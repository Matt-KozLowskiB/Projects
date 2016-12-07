using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CatchErrAndLogIt
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
            catch (Exception ex)
            {
                Console.WriteLine("Entry must be a number");
                Console.WriteLine(ex.GetType().Name);
                using (StreamWriter sw = new StreamWriter("ExceptionsLog.txt"))
                {
                    sw.WriteLine(ex);
                }
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


