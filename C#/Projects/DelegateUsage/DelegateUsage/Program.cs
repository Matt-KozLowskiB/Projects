using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

delegate double Divide(double n1, double n2);

namespace DelegateUsage
{
    class Sound
    {
        public double freq { get; set; }
        public double vWave = 340.29;
        public Sound(double freq)
        {
            this.freq = freq;
        }
        public Divide wl = delegate (double n1, double n2)
        {
            return n1 / n2;
        };
    }
    class Program
    {     
        static void Main(string[] args)
        {
            Sound clap = new Sound(200);
            Console.WriteLine(clap.wl(clap.vWave, clap.freq));
            Console.Read();
        }
    }
}
