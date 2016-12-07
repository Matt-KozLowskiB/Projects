using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace accessModifiyers
{
    public class Alpha
    {
        public int x = 1;
        internal int y = 2;
        protected int z = 3;
        private int a = 4;
        protected internal int b = 5;
    }
    public class Bravo : Alpha
    { 

   


    

        static void Main(string[] args)
        {
            Alpha A = new Alpha();
            A.x = 10;                      //accessible: public
            A.y = 10;                      //y is accessible to A (internal=true) 
            A.z = 10;                      //z inaccessible to A (class A not a derivative of Class A) 
            A.a = 10;                      //a inaccessible outside of containing Class (Class A) 
            A.b = 10;                      //b accessible because A is part of current assembly
            Bravo B = new Bravo();
            B.x = 20;
            B.y = 20;
            B.z = 20;                      //z is accessible to B because B is derived from class Alpha 
            B.a = 20;                      //a is inaccessible to B because a is private and only accessible within class Alpha 
            B.b = 20;                      //b is accessible to B because it's part of current assembly 
           
        


    }
}
}
