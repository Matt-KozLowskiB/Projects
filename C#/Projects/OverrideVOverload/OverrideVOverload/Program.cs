using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace OverrideVOverload
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

        static int numEngClasses = 0;
        public static int getnumEngClasses()
        {
            return numEngClasses;
        }
        public string displaySpecs()
        {
            return String.Format("This engine has {0} cylinders, {1} of displacement, uses a {2} fuel delivery system and has a {3} ignition system",
                numOfCylinders, displacement, fueldelivery, ignitionType);
        }

        // method overloading engDisp() method:
        public int engDisp(int boreDiam, int strokeLength, int numOfCylinders)
        {
            return boreDiam * strokeLength* numOfCylinders;
        }
        public double engDisp(double boreDiam, double strokeLength, int numOfCylinders)
        {
            return boreDiam * strokeLength* numOfCylinders;
        }
        
        class Turbo : Engine
        {
            public string kompressorMake { get; set; }
            public double maxIntakeBoost { get; set; }
            public Turbo() : base()
            {
                kompressorMake = "Not Specified";
                maxIntakeBoost = 0;
            }
            public Turbo(int displacement, int numOfCylinders, string fueldelivery, string ignitionType, string engMake, string kompressorMake, double maxIntakeBoost) : base(displacement, numOfCylinders, fueldelivery, ignitionType, engMake)
            {
                this.kompressorMake = kompressorMake;
                this.maxIntakeBoost = maxIntakeBoost;
            }

            //Method Overriding in Turbo.displaySpecs() method
            new public string displaySpecs()
            {
                return String.Format("This engine is manufactured by {4}, has {0} cylinders, {1} of displacement, uses a {2} fuel delivery system, has an {3} ignition system, and has a {5} turbocharger capable of {6} barr of boost",
                    displacement, numOfCylinders, fueldelivery, ignitionType, engMake, kompressorMake, maxIntakeBoost);
            }


            static void Main(string[] args)
            {
                Engine p400 = new Engine();
                p400 = new Engine(400, 8, "carbuereted", "points", "Pontiac");
                Console.WriteLine(p400.displaySpecs());
                Console.Read();
                Turbo Audi5000 = new Turbo(5, 220, "fuel injected", "electronic", "BMW", "Audi", 1.5 );

                //Note: Method overriding allows for a different output for displaySpecs() method in the Turbo class, derived from Engine Class.
                Console.WriteLine(Audi5000.displaySpecs());
                Console.ReadKey();

                // Note: method overload allows both integers and floats to be used in the engDisp method:
                Console.WriteLine(p400.engDisp(6, 8, 8));
                Console.WriteLine(p400.engDisp(6.0, 8.334, p400.numOfCylinders));
                Console.ReadKey();
            }
        }
    }
}