using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _00_Proje2
{
    class OncelikliKuyrukArtan
    {
        public List<Musteri> oncelikKuyrukArt;
        public int nItems;

        public OncelikliKuyrukArtan()
        {
            nItems = 0;
            oncelikKuyrukArt = new List<Musteri>();
        }
        public bool bosMu()
        {
            return (nItems == 0);
        }
        public void ekle(Musteri musteriEklenecek)
        {
            oncelikKuyrukArt.Add(musteriEklenecek);
            nItems++;
        }
        public Musteri sil()
        {
            int silinecekIndex = 0;
            int boyut = oncelikKuyrukArt.Count;
            Musteri temp = oncelikKuyrukArt[0];

            for (int i = 1; i < boyut; i++) //0. indexi tempe isaretledik. O sebeple donguyu 1'den baslatabiliriz.
            {
                if (temp.urunSayisi > oncelikKuyrukArt[i].urunSayisi)
                {
                    temp = oncelikKuyrukArt[i];
                    silinecekIndex = i;
                }
            }

            oncelikKuyrukArt.RemoveAt(silinecekIndex);
            nItems--;
            return temp;
        }
    }
}
