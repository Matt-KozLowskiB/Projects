using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace keywordThisUsage
{
    class Engine
    {
        public int displacement { get; set; }
        public int numOfCylinders { get; set; }
        public string fueldelivery { get; set; }
        public string ignitionType { get; set; }
        public string engMake { get; set; }



        public Engine()
        {
            displacement = 0;
            numOfCylinders = 0;
            fueldelivery = "Not Specified";
            ignitionType = "Not Specified";
            engMake = "Not Specified";

            numEngClasses++;

        }
        public Engine(int displacement, int numOfCylinders, string fueldelivery, string ignitionType, string engMake)
        {
            this.displacement = displacement;
            this.numOfCylinders = numOfCylinders;
            this.fueldelivery = fueldelivery;
            this.ignitionType = ignitionType;
            this.engMake = engMake;

            numEngClasses++;
        }
        public static int numEngClasses = 0;
        public static int getnumEngClasses()
        {
            return numEngClasses;
        }
    }
    class Program
    {
        static void Main(string[] args)
        {
            Engine Cad550 = new Engine();
            Console.WriteLine("Number of Engine Classes is:");
            Console.WriteLine(Engine.getnumEngClasses());
            Console.ReadKey();
        }
    }
}
