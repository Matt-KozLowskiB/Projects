using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace NullableTypesUse
{
    class Nullable
    {
        public int? x = 11;
        public char? space = 'a';
        public byte?[] BlobArray = { 111, 101 };


        static void Main(string[] args)
        {
            Nullable Demo = new Nullable();
            Console.WriteLine(Demo.x);
            Console.WriteLine(Demo.space);
            Console.WriteLine(Demo.BlobArray[1]);

            Console.Read();
            Demo.x = null;
            Demo.space = null;
            Demo.BlobArray[1] = null;
            Console.WriteLine(Demo.x);
            Console.WriteLine(Demo.space);
            Console.WriteLine(Demo.BlobArray[1]);         //nothing displayed because values are null: nothing exists to write to Console!

            Console.Read();
        }
    }
}
