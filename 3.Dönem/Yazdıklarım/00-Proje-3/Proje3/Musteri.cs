using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Proje3
{
    class Musteri
    {
        public int ID;
        public string kiralamaSaati;
        public string kiraladigiBisikletTuru;   //Burasini kendim ekledim. Programi biraz daha derli toplu tutuyor, kolaylastiriyor gibi.
        public Musteri(int id,string kiraSaati,string bisikletTuru)
        {
            ID = id;
            kiralamaSaati = kiraSaati;
            kiraladigiBisikletTuru = bisikletTuru;
        }

        public void musteriYazdir()
        {
            Console.WriteLine("ID:: "+ ID+ "  Kiralama Saati:: "+kiralamaSaati+" Kiraladigi Bisiklet Turu:: "+kiraladigiBisikletTuru);
        }
    }
}
