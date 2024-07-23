using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Proje3
{
    class QuickSort
    {
        int[] siralanacakDizi;
        public QuickSort(int[] siralanacak)
        {
            siralanacakDizi = siralanacak;
            QuickSortlaSirala(siralanacakDizi, 0, siralanacakDizi.Length - 1);
            yazdir(siralanacakDizi);
        }

        public void QuickSortlaSirala(int[] dizi, int start, int end)
        {
            if (start >= end)
            {
                return;
            }
            int num = dizi[start];

            int i = start, j = end;

            while (i < j)
            {
                while (i < j && dizi[j] > num)
                {
                    j--;
                }


                dizi[i] = dizi[j];

                while (i < j && dizi[i] < num)
                {
                    i++;
                }

                dizi[j] = dizi[i];
            }
        

            dizi[i] = num;
            QuickSortlaSirala(dizi, start, i - 1);
            QuickSortlaSirala(dizi, i + 1, end);
    }
        public void yazdir(int[] yazdirilacakdizi)
        {
            foreach (int eleman in yazdirilacakdizi)
                Console.Write(eleman + "  ");
        }
    }
}
