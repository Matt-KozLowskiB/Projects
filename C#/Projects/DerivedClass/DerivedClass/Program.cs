using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DerivedClass
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
        public string displaySpecs()
        {
            return String.Format("This engine has {0} cylinders, {1} of displacement, uses a {2} fuel delivery system and has a {3} ignition system",
                numOfCylinders, displacement, fueldelivery, ignitionType);
        }

        // method overloading engDisp:
        public int engDisp(int boreDiam, int strokeLength, int numOfCylinders)
        {
            return boreDiam * strokeLength * numOfCylinders;
        }
        public double engDisp(double boreDiam, double strokeLength, int numOfCylinders)
        {
            return boreDiam * strokeLength * numOfCylinders;
        }
    }
    class V8 : Engine
    {
        public string engGeometry { get; set; }
        public V8() : base()
        {
            engGeometry = "Not Specified";
            numEngClasses++;
        }
        public V8(int displacement, int numOfCylinders, string fueldelivery, string ignitionType, string engMake, string engGeometry) : base
        (displacement, numOfCylinders, fueldelivery, ignitionType, engMake)
        {
            this.engGeometry = engGeometry;
            numEngClasses++;
        }       
    }
    class Program
    {
        static void Main(string[] args)
        {
            V8 Cad550 = new V8();
            Console.WriteLine("Cad550 Displacement(ci) is: ");
            Console.WriteLine(Cad550.engDisp(9.2, 7.474, 8));
            Console.WriteLine("Number of Engine Classes is:");
            Console.WriteLine(Engine.getnumEngClasses());
            Console.ReadKey();
        }
    }
    
    
}