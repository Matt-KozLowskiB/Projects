using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
/*
namespace C_sharp__basics_tutorial_2__exceptions_etc
{
    class Program
    {
        static void Main(string[] args)
        {

            // Exception Handling:

            try
            {
                Console.WriteLine("Divide 10 by");
                int num = int.Parse(Console.ReadLine());   //converting string to integer, you use Parse(). Console.Readline() returns strings..
                Console.WriteLine("10 / {0} = {1}", num, (10 / num));
            }
            catch (DivideByZeroException ex)
            {
                Console.WriteLine("Cannot Dive by Zero, Foo'!");
                Console.WriteLine(ex.GetType().Name);
                Console.WriteLine(ex.Message);
                throw new InvalidOperationException("Operation Negatory", ex);

            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.GetType().Name);
            }
        }
    }
*/

// Classes & Objects - classes are the blueprint to define attributes of object trying to model
namespace C_sharp__basics_tutorial_2__exceptions_etc
{
    class Program

    {



        class Animal            //public - access not limited 
                                // protected - limited to class and subclass methods
                                // private - limited specifically to instant class only
        {
            public double height { get; set; }      // use getters and setters - get limits access; set allows only certain values to be set
            public double weight { get; set; }
            public string sound { get; set; }      // I believe these are called 'declaring attributes' or something similar.
            public string name;
            public string Name
            {
                get { return name; }
                set { name = value; }   //set can be used to limit input; can run a check to see if the name contains numbers, and return an error if you like-
            }
            // Now that basic values identified, now must 'initialize' class through use of CONSTRUCTOR:
            // In C#, a 'default' constructor is initialized unless otherwise defined by user-

            public Animal()      // Default Constructor is started by calling the Class method like so <==
            {
                this.height = 0;  // use 'this.' when specific class object isn't known - 'this.' refers to the instant class object u r valuating
                this.weight = 0;
                this.sound = "No sound";    //These are setting the values for the previously identified attributes
                this.Name = "No name";      // Video Joe said 'that's how you set the attributes - with the 'dot (.) operator'
                numOfAnimals++;
            }
            public Animal(double height, double weight, string sound, string Name)  // Video Joe says this <== is the constructor that 'sets attributes' for animal
            {
                this.height = height;
                this.weight = weight;    // Although these currently show generic values, in actuality they would be specific values-
                this.sound = sound;      // Ex.:   instead of 'this.weight = weight', we would say 'this.weight = 135' etc.
                this.Name = name;
                numOfAnimals++;

            }  // Static field = assigning an attribute to an object that 'makes no sense' for the object itself, but does for progmer.
               // for instance in this case, a static field to track the total number of 'Animal' objects created-
            static int numOfAnimals = 0;  // 'Static Field' created to define what is being tracked or done
            public static int getnumOfAnimals()  // here you are defining 'static class method' for function = track tot # of animal objects created;
                                                 // NOTE:  static class methods can't access non-static method attributes.
            {
                return numOfAnimals;  // after setting this method, we added "numOfAnim++;" to the attributes so autoincremented upon instantiation of each Animal Object
            }
            public string toString()
            {
                return String.Format("{0} is {1} inches tall, weighs {2} pounds and like to 'say' {3}", Name, height, weight, sound);
            }


            static void Main(string[] args)
            {
                KeyValue<string, string> superman = new KeyValue<string, string>("", "");
                superman.key = "Superman";
                superman.value = "Clark Kent";
                KeyValue<int, string> samsungTV = new KeyValue<int, string>(0, "");

                samsungTV.key = 12345;
                samsungTV.value = "a 50 in Samsung TV";

                superman.showData();
                samsungTV;


                Animal spot = new Animal(15, 10, "Spot", "Woof, Ruff!");  // Here we have created new 'Animal' object Spot and defined his attributes!!  YAY!!
                Console.WriteLine("{0} says {1}", spot.Name, spot.sound);
                Console.WriteLine("Number of Animals " + Animal.getnumOfAnimals());
                Console.WriteLine(spot.toString());
            }


// Method Overloading:  for a given methd(), you can use the same method for two different data sizes (ex:  int  vs double)

    public int getSum(int num1 = 1, int num2 = 1)
    {
    return num1 + num2;
    }
    public double getSum(double num1 = 1, double num2 = 1)
{
    return num1 + num2;    // so with method overloading, you can pass in both (1,2) or (3.7, 6.8) and they will both work due to above .

}

            // Object intializer:
            Animal grover = new Animal
            {
                name = "Grover",
                height = 16,
                weight = 18,
                sound = "Grrrr!"
            };
            Dog spike = new Dog();

            Console.WriteLine(spike.toString());

            spike = new Dog(20, 15, "Spike","Grrr!","Chicken");

            class Dog : Animal
            {
                public string favFood { get; set; }
                public Dog() : base()
                {
                    this.favFood = "No Favorite Food"
;                }
                public Dog(double height, double weight, string name, string sound, string favFood) : base
                    (height, weight, name, sound)
                {
                    this.favFood = favFood;
                }
                // OVERRIDING class attributes:
                new public string toString()
                {
                    return String.Format("{0} is {1} inches tall, weighs {2} pounds and like to 'say' {3} and eats {4}", Name, height, weight, sound, favFood);
                }





            }
            // Abstract class: inherit one abstract class allowed per class; however with an interface you can inherit multiple interfaces. Can't create/instantiate
            //object from an abstract class

            abstract class Shape
            {
                public abstract double area();

                public void sayHi()
                {
                    Console.WriteLine("Hello");
                }

                public interface ShapeItem
                {
                    double area();
                }

                class Rectangle : Shape
                {
                    private double length;
                    private double width;

                    public Rectangle(double num1, double num2)
                    {
                        length = num1;
                        width = num2;

                    }

                    public override double area()
                    {
                        return length * width;
                    }

                    class Triangle : Shape
                    {
                        private double theBase;
                        private double heigth;

                        public Rectangle(double num1, double num2)
                        {
                            theBase = num1;
                            heigth = num2;

                        }

                        public override double area()
                        {
                            return length * width;
                        }
                    }

                    public static Rectangle operator +(Rectangle rect1, Rectangle rect2)
                    {
                        double rectLength = rect1.length + rect2.length;
                        double rectWidth = rect1.width + rect2.width;
                        return new Rectangle(rectLength, rectWidth);
                    }



                    // Polymorphism - subclasses of a superclass can have very different behaviors or characteristics:

                    Shape rect = new Rectangle(5, 5);
                    Shape tri = new Triangle(5, 5);  // obviously, a triangle and rectangle are very different, but both are polymorphs of class 'Shape'.


                    // Generic Classes: special in that you don't have to specify the DATATYPE in a class or a method when employed.

                    class KeyValue<TKey, TValue>
                    {
                        public TKey key{ get; set; }
                        public TValue value{get; set;}

                        public KeyValue(TKey k, TValue v)
                    {
                            key = k;
                            value = v; 
                    }
                        public void showData()
                        {
                            Console.WriteLine("{0} is {1}",  this.key, this.value);
                        }




                        // enumerated lists (enums):

                        public enum Temperature
                        {
                            Freeze,
                            Low,
                            Warm,
                            Boil
                        }


                        Temperature micTemp = Temperature.Low  //this guy is the SHITTIEST instructor EVER!!!

                        struct Customers
                        {
                            private string name;
                            private double balance;
                            private int Kuntcunt;

                            public void createCust(string n, double b, int i)
                            {
                                name = n;
                                balance = b;
                                Kuntcunt = i;


                            }
                            public void showCust()
                            {
                                Console.WriteLine("Name "+ name);
                                Console.WriteLine("Balance"+ balance);
                                Console.WriteLine("ID "+ Kuntcunt);
                            }
                        
                        Customers bob = new Customers();
                        bob.createCust("Bob", 15.50, 12345);
                        bob.ShowCust();                          ///FUCKING BULLSHIT CRAPPY ASS SHITTY RETARDED INSTRUCTOR!!!!


    //DELEGATES

    delegate double GetSum(double num1, double num2);



                            GetSum sum = delegate (double num1, double num2) 
                            {
                                return num1 + num2;

                            }


  //LAMBDA FUCKING DABAH DOO BULLSHIT!!!



                            Func<int, int, int> getSum = (x, y) => x + y;
                            Console.Writeline("5+3="+ getSum.Invoke(5,3));


                                List<int> numList = new List<int> { 5, 10, 15, 20, 25 };

                                List<int> oddNums = numList.Where(n=>n%2==1)ToListnew 



  worthless piece of shit says:   file io

 using (StreamWriter sw - new STreamWriter("custs.txt");
    while custName

