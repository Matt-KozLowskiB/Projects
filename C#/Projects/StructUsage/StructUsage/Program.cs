using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace StructUsage

{
    struct SportsTeam
    {
        private string sportType;
        private string TeamName;
        private string HomeField;
        private int numEmployees;
        private int numPlayers;

        public void newTeam(string st, string tn, string hf, int ne, int np)
        {
            sportType = st;
            TeamName = tn;
            HomeField = hf;
            numEmployees = ne;
            numPlayers = np;
        }
        public void displayTeam()
        {
            Console.WriteLine("Sports Type:  {0}  ", sportType);
            Console.WriteLine("Team Name:  {0}  ", TeamName);
            Console.WriteLine("Home Field:  {0}  ", HomeField);
            Console.WriteLine("Total Employees:  {0}  ", numEmployees);
            Console.WriteLine("Players on Roster:  {0}  ", numPlayers);
        }





    }
    class Program
    {
        static void Main(string[] args)
        {
            SportsTeam Cougars = new SportsTeam();
            Cougars.newTeam("College Football", "Cougars", "Martin Stadium", 122, 71);
            Cougars.displayTeam();
            Console.Read();
        }
    }
}
