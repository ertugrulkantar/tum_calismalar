using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _00_Proje2
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.BackgroundColor = ConsoleColor.White;
            Console.Clear();
            Console.ForegroundColor = ConsoleColor.Black;


            string[] musteriAdiDizi = {"Ali","Merve","Veli","Gülay","Okan","Zekiye","Kemal","Banu","İlker","Songül","Nuri","Deniz" };
            int[] urunSayisiDizi = {8,11,16,5,15,14,19,3,18,17,13,15};

            ArrayList genericListeleriTutanArrayList = new ArrayList();

            Random listRandomLength = new Random();
            int sayac = 0;

            while (sayac < musteriAdiDizi.Length)
            {
                int listLength = listRandomLength.Next(1, 6);
                List<Musteri> musteriGenericList = new List<Musteri>(listLength);

                for(int i = 0; i < listLength; i++)
                {
                    Musteri musteriEklenecek = new Musteri(musteriAdiDizi[sayac], urunSayisiDizi[sayac]);
                    musteriGenericList.Add(musteriEklenecek);
                    sayac++;

                    if (sayac == musteriAdiDizi.Length)
                        break;
                }
                genericListeleriTutanArrayList.Add(musteriGenericList);
            }

            Console.WriteLine("#genericListeleriTutanArrayList ve Icindekiler Yazdiriliyor...\n*****Parantez icindeki sayilar kacinci" +
                " listede bulunuldugunu belirtir.*****");

            for(int j = 0; j < genericListeleriTutanArrayList.Count; j++)
            {
                List<Musteri> yazdirilacakListe = (List<Musteri>)genericListeleriTutanArrayList[j];
                Console.WriteLine("(" + (j + 1) + ")");
                foreach (Musteri el in yazdirilacakListe)
                {
                    el.yazdir();
                   
                }
                Console.WriteLine();
            }
            /********* 1-b Sonu*************/

            float musteriAdlariDizisiLengthFloat = musteriAdiDizi.Length;
            float arrayListLength = genericListeleriTutanArrayList.Count;
            float ortalamaListeElemanSayisi = (musteriAdlariDizisiLengthFloat) / (arrayListLength);

            Console.WriteLine("\n#Arraylist Icindeki Eleman Sayisi ve Listelerdeki Ortalama Eleman Sayisi Yazdiriliyor...\n*****");
            Console.WriteLine("ArrayList icindeki liste sayisi:: " + arrayListLength);
            Console.WriteLine("Listelerdeki ortalama eleman sayisi:: " + ortalamaListeElemanSayisi);
            /********* 1-c Sonu*************/

            int musteriAdlariDizisiLengthInt = (int)musteriAdlariDizisiLengthFloat;

            StackM musteriStack = new StackM(musteriAdlariDizisiLengthInt);

            for(int say1 = 0; say1 < musteriAdlariDizisiLengthInt; say1++)
            {
                Musteri stackeEklenecekMusteriNesnesi = new Musteri(musteriAdiDizi[say1],urunSayisiDizi[say1]);
                musteriStack.push(stackeEklenecekMusteriNesnesi);
            }

            Console.WriteLine("\n\n#musteriStack Yazdiriliyor...\n*****");
            while(musteriStack.isEmpty()==false)
            {
                Musteri temp1 = musteriStack.pop();
                temp1.yazdir();
            }
            /********* 2-a Sonu*************/

            QueueM musteriQueue = new QueueM(musteriAdiDizi.Length);

            for(int say2 = 0; say2 < musteriAdlariDizisiLengthInt; say2++)
            {
                Musteri diziyeEklenecekMusteriNesnesi = new Musteri(musteriAdiDizi[say2], urunSayisiDizi[say2]);
                musteriQueue.insert(diziyeEklenecekMusteriNesnesi);
            }
            QueueM ortalamaSureHesaplamadaKullanilacakmusteriQueue = new QueueM(musteriQueue);

            Console.WriteLine("\n\n#musteriQueue Yazdiriliyor...\n*****");
            while(musteriQueue.isEmpty()==false)
            {
                Musteri temp = musteriQueue.remove();
                temp.yazdir();
            }
            /********* 2-b Sonu*************/

            OncelikliKuyrukAzalan oncelikliKuyruk1 = new OncelikliKuyrukAzalan();

            for(int say3 = 0; say3 < musteriAdlariDizisiLengthInt; say3++)
            {
                Musteri oncelikliKuyruk1EklenecekMusteriNesnesi = new Musteri(musteriAdiDizi[say3], urunSayisiDizi[say3]);
                oncelikliKuyruk1.ekle(oncelikliKuyruk1EklenecekMusteriNesnesi);
            }

            Console.WriteLine("\n\n#oncelikliKuyruk1 (Azalan Sirada) Yazdiriliyor...\n*****");
            while (oncelikliKuyruk1.bosMu() == false)
            {
                Musteri temp = oncelikliKuyruk1.sil();
                temp.yazdir();
            }
            Console.WriteLine("\n");
            /********* 3-a Sonu*************/

            OncelikliKuyrukArtan oncelikliKuyruk2 = new OncelikliKuyrukArtan();

            for(int say4 = 0; say4 < musteriAdlariDizisiLengthInt; say4++)
            {
                Musteri oncelikKuyruk2EklenecekMusteriNesnesi = new Musteri(musteriAdiDizi[say4], urunSayisiDizi[say4]);
                oncelikliKuyruk2.ekle(oncelikKuyruk2EklenecekMusteriNesnesi);
            }
 
            float kisilerinBekledigiSureFIFO = 0;
            float kumulatifBeklemeSuresiFIFO = 0;
            Console.WriteLine("#FIFO Yapisindaki Kuyrukta...\n*****");
            while (ortalamaSureHesaplamadaKullanilacakmusteriQueue.isEmpty() == false)
            {
                Musteri temp = ortalamaSureHesaplamadaKullanilacakmusteriQueue.remove();
                kisilerinBekledigiSureFIFO += temp.urunSayisi;
                kumulatifBeklemeSuresiFIFO += kisilerinBekledigiSureFIFO;
                Console.WriteLine("Musteri Adi:: " + temp.musteriAdi + " || Bekleyecegi Sure:: " + kisilerinBekledigiSureFIFO);
            }
            Console.WriteLine("#FIFO Kuyrukta Ortalama Bekleme Suresi:: "+kumulatifBeklemeSuresiFIFO + "/" + musteriAdlariDizisiLengthFloat + "= "+(kumulatifBeklemeSuresiFIFO) / musteriAdlariDizisiLengthFloat+"\n");

            float kisilerinBekledigiSurePQ = 0;
            float kumulatifBeklemeSuresiPQ = 0;
            Console.WriteLine("\n#PQ (Azalan Sirada) Yapisindaki Kuyrukta...\n*****");
            while (oncelikliKuyruk2.bosMu() == false)
            {
                Musteri temp = oncelikliKuyruk2.sil();
                kisilerinBekledigiSurePQ += temp.urunSayisi;
                kumulatifBeklemeSuresiPQ += kisilerinBekledigiSurePQ;
                Console.WriteLine("Musteri Adi:: " + temp.musteriAdi + " || Bekleyecegi Sure:: " + kisilerinBekledigiSurePQ);
            }
            Console.WriteLine("#PQ (Azalan Sirada) Kuyrukta Ortalama Bekleme Suresi:: "+kumulatifBeklemeSuresiPQ+"/"+musteriAdlariDizisiLengthFloat+"= " + (kumulatifBeklemeSuresiPQ) / musteriAdlariDizisiLengthFloat + "\n");
            Console.WriteLine("\n");
            /********* 4-b Sonu*************/

            Console.ReadLine();
        }
    }
}
