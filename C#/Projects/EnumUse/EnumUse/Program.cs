using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;



namespace EnumUse
{
    class Program

    {
        public enum weather
        {
            Sunny,
            Windy,
            Rainy,
            Snowing,
            Hurricane,

        }
        static void Monday()
        {
            foreach (string cond in Enum.GetNames(typeof(weather)))
                {
                Console.WriteLine("Monday's weather expected to be {0}", cond);
                }
            Console.Read();
        }
        static void Main(string[] args)
        {
            Monday();
        }
    }
}
