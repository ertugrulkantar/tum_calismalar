using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _00_Proje2
{
    class OncelikliKuyrukAzalan
    {
        public List<Musteri> oncelikKuyrukAz;
        public int nItems;

        public OncelikliKuyrukAzalan()
        {
            nItems = 0;
            oncelikKuyrukAz = new List<Musteri>();
        }
        public bool bosMu() 
        {
            return (nItems == 0);
        }
        public void ekle(Musteri musteriEklenecek)
        {
            oncelikKuyrukAz.Add(musteriEklenecek);
            nItems++;
        }
        public Musteri sil()
        {  
            int silinecekIndex = 0;
            int boyut = oncelikKuyrukAz.Count;
            Musteri temp = oncelikKuyrukAz[0];
            
            for (int i = 1; i < boyut; i++) //0. indexi tempe isaretledik. O sebeple donguyu 1'den baslatabiliriz.
            {
                if (temp.urunSayisi < oncelikKuyrukAz[i].urunSayisi)
                {
                    temp = oncelikKuyrukAz[i];
                    silinecekIndex = i;
                }
            }

            oncelikKuyrukAz.RemoveAt(silinecekIndex);
            nItems--;
            return temp;
        }   
    }
}

