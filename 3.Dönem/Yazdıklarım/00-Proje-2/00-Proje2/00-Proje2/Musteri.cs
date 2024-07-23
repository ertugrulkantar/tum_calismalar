using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _00_Proje2
{
    class Musteri
    {
        //1-a////////////////////////////////
        public string musteriAdi;
        public int urunSayisi;

        public Musteri(string musteriAdi,int urunSayisi)
        {
            this.musteriAdi = musteriAdi;
            this.urunSayisi = urunSayisi;
        }

        public void yazdir()
        {
            Console.WriteLine("Musteri Adi:: " + musteriAdi + "  || Urun Sayisi:: " + urunSayisi);
        }
    }
}
