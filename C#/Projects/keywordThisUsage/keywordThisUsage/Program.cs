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
            this.displacement = 0;
            this.numOfCylinders = 0;
            this.fueldelivery = "Not Specified";
            this.ignitionType = "Not Specified";
            this.engMake = "Not Specified";

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
    }
}
