using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace valueVreferenceTypes
{
    class Program
    {
        class Alpha
        {
            int x = 3;
        }
        public enum Cats                                                      //enum is a value type
        {
            Minx, Alsatian, Calico
        }
        delegate double pairsOfShoes(double dressShoes, double casualShoes);  //delegates are reference types

        static void Main(string[] args)
        {
            //examples of value types
            int y = 22;
            bool dumb = true;

            //examples of reference types
            Alpha A = new Alpha();
            int[] phoneyArray = { 5, 10, 15, 20, 25 };
            string student = "Alfredo";
            
            

            

      

                    
        }
    }
}
