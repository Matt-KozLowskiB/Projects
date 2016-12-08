using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace InterfaceUse
{
    public interface Wave
    {
        double wavelength();
    }

    public class Sound : Wave
    {
        public double soundSpeed = 340.29;
        private double frequency;

        public Sound(double freq)
        {
            frequency = freq;
        }

        public double wavelength()
        {
            return soundSpeed / frequency;
        }
    

        static void Main(string[] args)
        {
            Sound  train = new Sound(1500);
            Console.WriteLine("wavelength is: " + train.wavelength());
            Console.ReadKey();

        }
    }
}
