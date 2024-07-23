using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _3_lab3_kendi_cozumum     //Hocam bu hafta çok ödev vardı, süresi geçti ama yaptıktan sonra
{                                   //yüklemek istedim. Ne kadar doğru yaptığım bilmiyorum ancak
                                    //yükleme klasörü açık, o sebeple yüklüyorum. Saygılarımla.
    class SehirCiftleri                    
    {
        public String sehir1;
        public String sehir2;
        public int puan;
        public SehirCiftleri(String sehir1,String sehir2,int puan)
        {
            this.sehir1 = sehir1;
            this.sehir2 = sehir2;
            this.puan = puan;
        }

        public void yazdir()
        {
            Console.WriteLine("sehir1::"+sehir1+" || sehir2::"+sehir2+" || puan::"+ puan);
        }
    }


    class Program
    {
        static Random r = new Random();
        static void Main(string[] args)
        {

            String[] Sehirler = new String[8] {"Istanbul","Roma","Paris","Madrid","New York","Moskova","Londra","Pekin"};
            
            
            /*foreach (String eleman in Sehirler)
                Console.WriteLine(eleman);*/


            String[] seyahatPlaniSehirleri = new String[4];
            
            for (int i = 0; i < seyahatPlaniSehirleri.GetLength(0); i++)
            {
                int randomSayi = r.Next(8-i);
                seyahatPlaniSehirleri[i] = Sehirler[randomSayi];
                for(int j = randomSayi; j < Sehirler.GetLength(0) - (i+1); j++)
                {
                    Sehirler[j] = Sehirler[j + 1];
                }
            }

            SehirCiftleri[] sehirAdlari = new SehirCiftleri[6];  //4'un 2'li kombinasyonu. Jenerikle ugrasmadim.
            int sehirAdlariIndexSayac = 0;

            for(int a=0; a < seyahatPlaniSehirleri.GetLength(0)-1; a++)
            {
                
                for(int b = a + 1; b < seyahatPlaniSehirleri.GetLength(0); ++b)
                {
                    int puan = r.Next(101);
                    SehirCiftleri eklenecekCift = new SehirCiftleri(seyahatPlaniSehirleri[a], seyahatPlaniSehirleri[b], puan);
                    sehirAdlari[sehirAdlariIndexSayac] = eklenecekCift;
                    sehirAdlariIndexSayac+= 1;

                }
            }

            Console.WriteLine("TUM ELEMANLAR YAZDIRILIYOR\n======================================");
            foreach(SehirCiftleri el in sehirAdlari)
            {
                el.yazdir();
                Console.WriteLine("-------------------------------------");
            }

            Console.WriteLine("\n\nYALNIZCA ISTANBUL ICERENLER YAZDIRILIYOR\n============================");
            foreach (SehirCiftleri ell in sehirAdlari)
            {
                if (ell.sehir1 == "Istanbul" || ell.sehir2 == "Istanbul")
                {
                    ell.yazdir();
                    Console.WriteLine("-------------------------------------");

                }
            }

            Console.ReadLine();


        }
    }
}
