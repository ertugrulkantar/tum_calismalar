using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Proje3
{
    class Durak
    {  
        public string durakAdi;
        public int bosParkAlaniSayisi;
        public int bostakiTandemBisikletSayisi;
        public int bostakiNormalBisikletSayisi;

        public Durak(string durakAd,int bosPark,int tandemBisikletSayisi,int normalBisikletSayisi)
        {
            durakAdi = durakAd;
            bosParkAlaniSayisi = bosPark;
            bostakiTandemBisikletSayisi = tandemBisikletSayisi;
            bostakiNormalBisikletSayisi = normalBisikletSayisi;
        }

        public void durakYazdir()
        {
            Console.WriteLine("\nBos Park Alani Sayisi:: "+ bosParkAlaniSayisi+
                "\nBostaki Normal Bisiklet Sayisi:: "+bostakiNormalBisikletSayisi
                +"\nBostaki Tandem Bisiklet Sayisi:: "+bostakiTandemBisikletSayisi+"\n");
        }
    }
}
