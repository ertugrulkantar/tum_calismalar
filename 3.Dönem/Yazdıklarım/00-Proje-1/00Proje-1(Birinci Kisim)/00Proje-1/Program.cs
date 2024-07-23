using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _00Proje_1
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("1) GENERATING DISTANCE MATRIX FROM POINTS IN A 2D PLANE");
            Console.WriteLine("--------------------------------------------------------\n");
            
            
            double[,] koordinatMatrisTest1 = RastgeleNoktaUret(10, 100, 100);
            double[,] koordinatMatrisTest2 = RastgeleNoktaUret(100, 100, 100);

            Console.WriteLine("###RASTGELE NOKTA TEST-1:: n=10, width=100, height=100\n");
            IkiBoyutluMatrisYazdir(koordinatMatrisTest1,"X ve Y");
            Console.WriteLine("");

            Console.WriteLine("###RASTGELE NOKTA TEST-2:: n=100, width=100, height=100\n");
            IkiBoyutluMatrisYazdir(koordinatMatrisTest2,"X ve Y");
            Console.WriteLine("");

            Console.WriteLine("###UZAKLIK MATRISI TEST:: n=10, width=100, height=100 (koordinantMatrisTest1 kullanildi)\n");
            double[,] uzaklikMatrisTest = UzaklikMatrisiOlustur(koordinatMatrisTest1);
            IkiBoyutluMatrisYazdir(uzaklikMatrisTest,"N x N");
            
            Console.WriteLine("\nBirinci programin sonu...");
            Console.ReadKey();

        }

        public static double[,] RastgeleNoktaUret(int n, double widht, double height)
        {
            Random r1 = new Random();
            double[,] koordinatMatris = new double[n, 2];
            for (int i = 0; i < n; i++)
            {
                
                double koordinatX = r1.NextDouble() * widht;
                koordinatMatris[i, 0] = koordinatX;
                //Console.WriteLine(koordinatMatris[i, 0]);
                double koordinatY = r1.NextDouble() * height;
                koordinatMatris[i, 1] = koordinatY;
                //Console.WriteLine(koordinatMatris[i, 1]);
            }
            return koordinatMatris;
        }
        public static void IkiBoyutluMatrisYazdir(double[,] matris,string matrisTuru)
        {
            /*Burada iki ayrı yazdirma metodu yerine, yazdirilacak matrise gore 2.bir 
             parametre alacak sekilde duzenledim ve bu parametreye gore basim seklini degistirdim.*/

            if (matrisTuru=="X ve Y")
            {
                Console.WriteLine("Index\t   X" + "\t\t   Y");
                Console.WriteLine("        -------\t        -------");
            }
                
            else if(matrisTuru=="N x N")
            {
                Console.Write("Index");
                for(int k=0; k < matris.GetLength(0); k++)
                {
                    Console.Write( "      "+k+"         ");
                }
                Console.WriteLine("");
                for(int a=0; a < matris.GetLength(0); a++)
                {
                    Console.Write("        ------- ");
                }
                Console.WriteLine("");
            }
                
            for (int i = 0; i < matris.GetLength(0); i++)      
            {
                Console.Write(i + "-)");
                for (int j = 0; j < matris.GetLength(1); j++)  
                {
                    
                    Console.Write("     "+matris[i, j].ToString("000.000" + "    "));
                }
                Console.WriteLine("\n");
            }
        }
        

        public static double[,] UzaklikMatrisiOlustur(double[,] matris)
        {
            int matrisSatirSayisi = matris.GetLength(0);
            double[,] uzaklikMatrisi = new double[matrisSatirSayisi, matrisSatirSayisi];

            for (int i = 0; i < matrisSatirSayisi; i++)
            {
                for (int j = 0; j < matrisSatirSayisi; j++)
                {
                    uzaklikMatrisi[i, j] = Math.Sqrt(Math.Pow(matris[i, 0] - matris[j, 0], 2) + Math.Pow(matris[i, 1] -matris[j, 1],2) );
                }
            }

            return uzaklikMatrisi;
        }

    
    
    
    }

}

