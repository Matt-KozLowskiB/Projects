using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApplication1
{
    class Program
    {
        static void Main(string[] args)
        {
            // single line comment
            /* multiline comment*/
            Console.WriteLine("fucking bullshit!");
            string dickweed = Console.ReadLine();
            Console.WriteLine("Hello, Fuckin' " + dickweed);
            bool canVote = true;
            char grade = 'A';
            // int maxint = int.MaxValue = 2.1Billion size limit;
            // long maxLong = long.MaxValue = 9.2 Quintillion limit;
            // decimal maxDec= decimal.MaxValue = 79.2 nonillion(9illion);
            // BigInteger = huge decimal number.
            // float maxFloat = float.MaxValue = 32 bit number w/ 3.4 * 10^38 & 7 decimals of precision
            // double maxDouble = double.MaxValue =32 bit numberw/  1.7 * 10^308 & 15 decimals of precision
            Console.WriteLine("Max Int:" + int.MaxValue + "Max Float" + double.MaxValue);

            var anotherName = "Tom";
            anotherName = 2; //will create error because changing datatype of string variable
            Console.WriteLine("anotherName is a {0}", anotherName.GetTypeCode());
            double pi = 3.14;
            int intPi = (int)pi;
            // built- in math functions: Acos, Asin, Atan, Atan2, Cos, Cosh, Exp, Long, Sin, Sinh, Tan, Tanh
            // Math.Abs, Math.Ceiling (round up), Math.Floor(round down), Math.Max, Math.Min, Math.Pow(to the power of), Math.Round, Math.Sqrt
            Random rand = new Random()
                Console.WriteLine("Random number between 1 and 10" + (rand.Next(1, 11)));
            // Conditionals &&, ||^!
            if ((age > 7) && (age < 13))
                Console.WriteLine("fuck yourself!");
            else if ((Age > 70) && (Age < 100))
                Console.WriteLine("You Old Piece of Shit!!");
            bool canDrive = age >= 16 ? true : false;  //this says if question comes back true, assign 'true' value to 'canDrive' var
            switch (age) {
                case 0:
                    Console.WriteLine("Bitch");
                    break;
                case 1:
                    Console.WriteLine("tiny bitch"); }
            int i = 0;
            while (i < 10)
            {
                if (i == 7)
                {
                    i++;
                    continue;
                }
                if ((i % 2) > 0)  // This checks for odd number by way of testing for a remainder.  If yes, it's an odd number.
                {
                    Console.WriteLine(i);
                }
            }
            string guess;
            do
            {
                Console.WriteLine("Guess #");
                guess = Console.ReadLine();
            } while (!guess.Equals("15"));  // this states 'while guess is NOT equal to 15, continue execution' NOTE: string.equals checks string value
            // for loop:
            for (int i = 0; i < 10; i++) // in C# you initialize counter, set constraints, and increment at the beginning
            {
                if ((i % 2) > 0)
                {
                    Console.WriteLine(i);
                }

            }
            string randStr = "Here are some random characters";
            foreach (char c in randStr)
                Console.WriteLine(c);

            /*    \ = 'escape delimiter'  \' allows you to insert a single quote in a string
                                          \" allows you to insert a single double-quote in a string
                                          \\ allows you to insert a single backslash in a string
                                          \b allows you to put a backspace inside a string
                                          \n allows you to insert a new line in the middle of a string
                                          \t allows you to insert a <tab> in the middle of a string
            */

            string sampString = "bunch of random words";
            string sampString2 = "More Fucking Bullshit!!";
            Console.WriteLine("Is empty? " + String.IsNullOrEmpty(sampString));
            Console.WriteLine("Is empty: " + String.IsNullOrWhiteSpace(sampString));
            Console.WriteLine("String Length is: " + sampString.Length);

            Console.WriteLine("Index of 'bunch' is: " + sampString.IndexOf("bunch"));


            Console.WriteLine("2nd word is: " + sampString.Substring(4));

            Console.WriteLine("Index of 'bunch' is: " + sampString.IndexOf("is"));
            Console.WriteLine("Index of 'bunch' is: " + sampString.Substring(3));

            Console.WriteLine("Strings equal: " + sampString.Equals(sampString2));

            Console.WriteLine("starts with \"a bunch\": " + sampString.StartsWith("bunch of"));

            Console.WriteLine("Ends with \"Bullshit!!\": " + sampString2.EndsWith("Bullshit!!"));

            Console.WriteLine("Ends with words: " + sampString.EndsWith("words"));

            Console.WriteLine(sampString2.Trim());
            Console.WriteLine(sampString.TrimEnd());
            sampString5 = sampString2.TrimStart();
            Console.WriteLine(sampString3);
            Console.WriteLine(sampString4);
            Console.WriteLine(sampString5);
            sampString = sampString.Replace("bunch", "Cocksuckers");
            Console.WriteLine(sampString);
            sampString = sampString.Remove(0, 4);
            string[] names = new string[3] { "Matt", "Dick", "Head" };
            Console.WriteLine("Name List " + String.Join("-", names));
            string fmtStr = String.Format("{0:c}{1:00.00}{2:#.00}", 1.56, 15.5678, .56);
            Console.WriteLine(fmtStr);

            StringBuilder sb = new StringBuilder();
            sb.Append("This is my second sentence");
            sb.AppendFormat("My Name is {0} and I live in {1}", "Freeney", "Dickheadlandia");
            sb.Replace("a", "e");
            sb.Remove(4, 9);
            Console.WriteLine(sb.ToString());


            // arrays

            int[] randNumArray;  // declaring an array
            int[] randArray = new int[6];
            int[] randArray2 = { 1, 2, 3, 4, 5, 8 };
            Console.WriteLine("Array Length: " + randArray2.Length);
            Console.WriteLine("Item 0 " + randArray2[0]);
            for (i = 0; i < randArray2.Length; i++)
            {
                Console.WriteLine("{0}:{1}", i, randArray2[i]);
            }
            foreach (int num in randArray2)
                Console.WriteLine(num + "= Number of Cunts in Trumpvintory..");

            Console.WriteLine("Where is 1?   =[{0}]", Array.IndexOf(randArray2, 1)); //Array object: used to manipulate array itself (objects appear blue)

            string[] names1 = { "Tom", "Dick", "Harry" };
            string nameStr = string.Join("&", names1);
            string[] nameArray = nameStr.Split('&');
            string namesar = string.Join("", nameArray);
            Console.WriteLine(nameStr.ToString());
            Console.WriteLine(namesar.ToString());


            int[,] multArray = new int[5, 3];
            int[,] multArray2 = { { 0, 1 }, { 2, 5 }, { 6, 11 } };
            foreach (int bitchslap in multArray2)
                Console.WriteLine(bitchslap);
            for (int x = 0; x < multArray2.GetLength(0); x++)
            {
                for (int y = 0; y < multArray2.GetLength(1); y++)
                {
                    Console.WriteLine("{0}|{1}:{2} ", x, y, multArray2[x, y]);
                }
            }


            //Lists

            List<int> numList = new List<int>();
            numList.Add(5);
            numList.Add(15);
            numList.Add(25);
            numList.Add(35);
            int[] randArray0 = { 2, 4, 6, 8, 9 };
            numList.AddRange(randArray);
            List<int> numList2 = new List<int>(randArray);
            List<int> numList3 = new List<int>(new int[] {3, 4, 5, 6, 7 });
            Console.WriteLine(numList);
            for (int i = 0; i < numList.Count; i++)
                Console.WriteLine(numList[i]);













        }
    }
}
