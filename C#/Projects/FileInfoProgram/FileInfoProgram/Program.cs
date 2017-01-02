using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;

namespace FileInfoProgram
{
    class Program
    {

        static void Main(string[] args)
        {
            Console.WriteLine("Enter Source Folder/Directory: ");
            string sourcepath = @Console.ReadLine();
            Console.WriteLine("Enter Destination Folder/Directory: ");
            string destinypath = @Console.ReadLine();
            bool filescopied = false;
            ProcessFolder(sourcepath, destinypath, filescopied);
            
        }
        public static void ProcessFolder(string sourcepath, string destinypath,bool filescopied)
        {
            
            try
            {
                foreach (string file in Directory.GetFiles(sourcepath))
                {
                    FileInfo fi = new FileInfo(file);
                    StreamWriter sw = File.AppendText("Moron.txt");
                    sw.WriteLine("{0}, {1}", fi.Name, fi.FullName);
                    sw.Close();
                   
                    if (DateTime.Now.AddHours(-24) <= fi.LastWriteTime)
                    {

                        MoveModedFiles(fi, destinypath, filescopied);
                        filescopied = true;
                    }
                    
                }
                
            }
            catch (Exception ex)
            {
                recordErr(ex);

            }
            finally
            {
                if (filescopied == false)
                {
                    Console.WriteLine("No files modified since {0} found... ", DateTime.Now.AddHours(-24));
                    Console.ReadKey();
                }
                
            }
                
            
        }
        public static void MoveModedFiles(FileInfo fi, string destinypath, bool filescopied )
        {
            filescopied = true;
            StreamWriter sw = File.AppendText("Moron.txt");
            try
            {
                File.Move(fi.FullName, (Path.Combine(destinypath, fi.Name)));
                Console.WriteLine("-------------------------------------\n");
                Console.WriteLine(filescopied);
                Console.WriteLine("The file {0} has been copied to {1}", fi.Name, destinypath);
                sw.WriteLine("-------------------------------------\n");
                sw.WriteLine("The file {0} has been copied to {1} on {2}", fi.Name, destinypath, DateTime.Now);
                sw.Close();
                Console.ReadKey();


            }
            catch (Exception ex)
            {
                recordErr(ex);
            }
            
            
        }
        public static void recordErr(Exception ex)
        {
            Console.WriteLine("-------------------------------------\n");
            Console.WriteLine("Process failed. Press Any Key to Terminate...");
            StreamWriter sw = File.AppendText("Moron.txt");           
            sw.WriteLine("-------------------------------------\n");
            sw.WriteLine("Process failed with following exception at: {0}\n", DateTime.Now);
            sw.WriteLine(ex);
            sw.Close();
        }
    }
}
   
                
              
                