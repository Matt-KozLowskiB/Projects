using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Runtime.Serialization;
using System.Runtime.Serialization.Formatters.Binary;
using System.Text;
using System.Threading.Tasks;

namespace BLOB_Serialization
{
    class Program
    {
       
        static void Main(string[] args)
        {
            //Original 'BLOB' to serialize:
            string Path = @"halloween.jpg";
            FileStream fs = new FileStream(Path, FileMode.Open, FileAccess.Read);
            BinaryReader br = new BinaryReader(fs);

            //BLOB file read & written into 'BLOB Array'           
            byte[] BlobValue = br.ReadBytes((int)fs.Length);
            fs.Close();
            br.Close();

            //BLOB is serialized to 'MySerial.txt' file
            System.Runtime.Serialization.IFormatter formatBin = new BinaryFormatter();
            Stream st = new FileStream("MySerial.txt",
                FileMode.Create, FileAccess.Write, FileShare.None);
            formatBin.Serialize(st, BlobValue);
            st.Close();
            Console.Read();

            //BLOB is now deserialized from 'MySerial.txt' file into new BLOB Array BlobValue2
            IFormatter formatBin2 = new BinaryFormatter();
            Stream st2 = new FileStream("MySerial.txt",
                FileMode.Open, FileAccess.Read, FileShare.Read);
            byte[] BlobValue2 = (byte[])formatBin2.Deserialize(st2);

            //Test to make sure BLOB deserialized:
            foreach (int num in BlobValue2)
            {
                Console.WriteLine(num);
            }

            //New Blob Array BlobValue2 now written to 'BeamMeUpScotty.JPg'
            Stream st3 = new FileStream("BeamMeUpScotty.jpg",
                FileMode.Create, FileAccess.Write, FileShare.None);
            BinaryWriter bw = new BinaryWriter(st3);
            bw.Write(BlobValue2);
            st3.Close();
            bw.Close();

        }
    }
}
