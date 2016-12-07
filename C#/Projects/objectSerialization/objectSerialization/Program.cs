using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Runtime.Serialization;
using System.Runtime.Serialization.Formatters.Binary;
using System.Text;
using System.Threading.Tasks;

namespace objectSerialization
{   [Serializable] 
    class SerializeMe
    {
        protected int[] numArray = { 1, 6, 7, 11, 15, 18, 21 };
        public int x = 241;
        private string babble = "Hello Dolly";
        public enum stooges {Tom, Dick, Harry};
        string favTeam { get; set;  }
    
        public SerializeMe()
        {
            favTeam = "Blazers";
        }
        public SerializeMe(string favTeam)
        {
            this.favTeam =favTeam;
        }



        static void Main(string[] args)
        {
            SerializeMe sm = new SerializeMe();
            SerializeMe xm = new SerializeMe("Broncos");

            IFormatter formatBin2 = new BinaryFormatter();
            Stream st2 = new FileStream("MySerial.bin",
                FileMode.Open, FileAccess.Read, FileShare.Read);
            SerializeMe xm = (SerializeMe)formatBin2.Deserialize(st2);
            st2.Close();
            Console.WriteLine(xm.favTeam);
            Console.Read();
            Console.WriteLine(xm.favTeam);
            Console.Read();
           




        }
    }
}
