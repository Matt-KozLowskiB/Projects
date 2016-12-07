using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
delegate void MCdelegate(string name);

namespace MultiCastDelegateUse




{
    class Program
    {
        static void Greet(string name)
        {
            Console.WriteLine("Greetings, {0}!", name);
        }
        static void Farewell(string name)
        {
            Console.WriteLine("Sayonara, {0}.", name);
        }
        static void DejaVu(string name)
        {
            Console.WriteLine("We meet again, {0}!", name);
        }
        static void Main(string[] args)
        {
            MCdelegate one, two, three;
            one = Greet;
            two = Farewell;
            three = DejaVu;
            Console.WriteLine("MultiCast Delagate in action:");
            one("Matt");
            two("Jim");
            three("Ralph");
            Console.Read();

        }
    }
}

