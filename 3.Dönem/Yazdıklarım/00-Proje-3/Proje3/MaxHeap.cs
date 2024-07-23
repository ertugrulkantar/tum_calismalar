using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Proje3
{
    class MaxHeap
    {
        public MaxHeap(List<Durak> input, int length)
        {
            this.Length = length;
            this.Liste = input;
            BuildMaxHeap();
        }

        public List<Durak> Liste { get;  set; }

        public int Length { get; private set; }

        private void BuildMaxHeap()
        {
            for (int i = this.Length / 2; i > 0; i--)   //Son yaprak olmayan dugum indexini yigma metoduna veriyoruz.
            {                                           //Boylece tum parent lari ve dolayisiyla childlerini dolasmis olacagiz.
                MaxHeapify(i);
            }

            return;
        }

        public void MaxHeapify(int index)
        {
            var left = 2 * index;   //Sol cocuk ayarlandi.
            var right = 2 * index + 1;  //Sag cocuk ayarlandi.

            int max = index;
            if (left <= this.Length && this.Liste[left - 1].bostakiNormalBisikletSayisi > this.Liste[index - 1].bostakiNormalBisikletSayisi) // Sol mevcutsa ve sol cocuk buyukse en buyuk sol oluyor.
            {
                max = left;
            }

            if (right <= this.Length && this.Liste[right - 1].bostakiNormalBisikletSayisi > this.Liste[max - 1].bostakiNormalBisikletSayisi)    //Sag mevcutsa sag cocuk ile en buyugu karsilastirdik.
            {
                max = right;                                                           //Eger buyukse en buyuk sag cocuk oluyor.
            }

            if (max != index)
            {
                Durak temp = this.Liste[max - 1];         //Uygun sekilde swapliyoruz
                this.Liste[max - 1] = this.Liste[index - 1];  
                this.Liste[index - 1] = temp;   //Ve yukaridaki sart saglanana,
                MaxHeapify(max);        //index maximum olana kadar, yani maxheap duzeni olusana kadar recursive devam ediyoruz.
            }

            return;
        }

        public Durak RemoveMaximum()
        {
            Durak maximum = this.Liste[0];

            this.Liste[0] = this.Liste[this.Length - 1];    //Complete ozelligini korumak icin son leafi basa aldik.
            this.Length--;  //Length i azalttik.
            MaxHeapify(1);  //Ve simdi tekrar maxheap duzenine donebilmek icin ilk elemandan tekrar yiginlamaya basladik.
            return maximum; //Boylece duzen tekrar saglanacak.
        }

        public static void printHeap(List<Durak> Liste)
        {
            Console.WriteLine("Heap duzeninde yazdiriliyor...");

            foreach(Durak eleman in Liste)
            { 
                Console.WriteLine(eleman.durakAdi);
                eleman.durakYazdir();
            }
            Console.WriteLine();
        }

    }
}
