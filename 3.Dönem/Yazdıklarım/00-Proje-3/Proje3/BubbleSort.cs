using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Proje3
{
    class BubbleSort
    {
        int[] siralanacakDizi;
        public BubbleSort(int[] siralanmasiIstenenDizi)
        {
            siralanacakDizi = siralanmasiIstenenDizi;
            bubbleSortlaDiziSirala(siralanacakDizi);
        }

        public void bubbleSortlaDiziSirala(int[] dizi)
        {
            int temp;
            bool swap;
            yazdir(dizi);
            Console.WriteLine("==>Dizisi BubbleSort ile siralaniyor...\n");
            for (int j = 0; j <= dizi.Length - 2; j++)  
            {
                swap = false;
                for (int i = 0; i <= dizi.Length - 2; i++)
                {
                    if (dizi[i] > dizi[i + 1])
                    {
                        temp = dizi[i + 1];
                        dizi[i + 1] = dizi[i];
                        dizi[i] = temp;
                        swap = true;    //Swap gerceklesmezse dizi sirali demektir.
                    }
                }
                if (swap == false)      //Dolayisiyla islemi sonlandirabiliriz.
                    return;
                Console.WriteLine((j +1)+ ". Turda dizinin durumu...\n===========================");
                yazdir(dizi);
                Console.WriteLine("\n");
            }
        }
        public void yazdir(int[] yazdirilacakdizi)
        {
            foreach (int eleman in yazdirilacakdizi)
                Console.Write(eleman + "  ");
        }
            
            
    }
}
