using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CreateSealedClass
{
    public class Alpha
    {
        public int x = 1;
        internal int y = 2;
        protected int z = 3;
        private int a = 4;
        protected internal int b = 5;
    }
    sealed class Bravo : Alpha { }       //permitted because sealed class can be derived from another class
    public class Charlie : Bravo         //forbidden because no class can be derived from a sealed class
    {



        static void Main(string[] args)
        {


        }
    }
}