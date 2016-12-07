using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace BuzzFizzCodeChallenge
/*The 'BuzzFizz' Code Challenge is from a mock tech interview on Utube.  The instructions were to 'create me a method that
 * for numbers between zero and 100, 'Buzz' is printed to console for numbers divisible by 3, and 'Fizz' 
 * for any number divisible by 5.  I went a couple steps further and added extraneous text for troubleshooting, and
 * added a Streamwriter method to log the output to the 'Div3Log.txt' & 'Div5Log.txt', according to whether the
 * counter int i is divisible by 3 or 5, respectively.
*/
{
    class Program
    {
        static void pause()                                 //Got tired of writing 'Console.ReadKey()'
        {
            Console.ReadKey();
        }
        static void D_splay(string s, int i)                //ditto for 'Console.Writeline()'
        {
            Console.WriteLine(s, i);
        }
        static void eWriter(string s, int i, string Path)   //Since Streamwriter invoked more than once, method created
        {
            using (StreamWriter sw = File.AppendText(Path))
            {
                sw.Write(s, i);
            }
        }
        static void BuzzFizz()  
        {
            for (int i = 0; i <= 100; i++)
            {
                if (i != 0)
                {
                    if (i % 3 == 0)
                    {
                        string Path = "Div3log.txt";
                        string s = "Number {0} divisible by 3 = ~Buzz~ \n";
                        D_splay(s, i);
                        eWriter(s, i, Path);
                        pause();   
                    }
                    else if (i % 5 == 0)
                    {
                        string Path = "Div5log.txt";
                        string s = "Number {0} divisible by 5 = !Fizz!\n";
                        D_splay(s, i);
                        eWriter(s, i, Path);
                        pause();                      
                    }
                    else
                    {
                        continue;
                    }
                }                
            }
        }
        static void Main(string[] args)
        {
            BuzzFizz();
        }
    }
}
