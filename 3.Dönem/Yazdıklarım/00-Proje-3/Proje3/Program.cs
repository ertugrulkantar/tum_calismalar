using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Proje3
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.BackgroundColor = ConsoleColor.White;
            Console.Clear();
            Console.ForegroundColor = ConsoleColor.Black;

            String[] duraklar = { "İnciraltı, 28, 2, 10", "Sahilevleri, 8, 1, 11", 
                                  "Doğal Yaşam Parkı, 17, 1, 6", "Bostanlı İskele, 7, 0, 5",
                                  "Alsancak, 8,3,9", "Üçkuyular, 23 , 2 ,7",
                                  "Bayraklı, 11 , 2 , 4","Bornova, 7,1,5",
                                  "Göztepe, 10 , 2 ,20" };
            
            //Adresler karismasin diye lazim olan miktarda listeler olusturuldu.
            List<Durak> duraklarListesi = durakListesiniOlustur(duraklar);
            List<Durak> hashTabledaKullanilacakDuraklarListesi = durakListesiniOlustur(duraklar);
            List<Durak> heapYapisindaKullanilacakDuraklarListesi = durakListesiniOlustur(duraklar);

            BinTree ikiliAramaAgaci = new BinTree();
            Random randomNesnesi2 = new Random();

            foreach (Durak durakNesne in duraklarListesi)
            {
                List<Musteri> dugumeEklenecekMusteriListesi = new List<Musteri>();
                int dugumeEklenecekMusteriSayisi = randomNesnesi2.Next(1, 11);
                for(int i = 0; i < dugumeEklenecekMusteriSayisi; i++)
                {
                    Musteri musteriEklenecek = randomMusteriOlustur(randomNesnesi2);
                    dugumeEklenecekMusteriListesi.Add(musteriEklenecek);
                }
                foreach(Musteri musteriNesne in dugumeEklenecekMusteriListesi)
                {
                    if(durakNesne.bostakiTandemBisikletSayisi>0 &&(musteriNesne.ID==8 || musteriNesne.ID==12))
                    {
                        musteriNesne.kiraladigiBisikletTuru = "Tandem Bisiklet";
                        durakNesne.bostakiTandemBisikletSayisi -= 1;
                        durakNesne.bosParkAlaniSayisi += 1;
                    }
                    else if (durakNesne.bostakiNormalBisikletSayisi > 0)
                    {
                        musteriNesne.kiraladigiBisikletTuru = "Normal Bisiklet";
                        durakNesne.bostakiNormalBisikletSayisi -= 1;
                        durakNesne.bosParkAlaniSayisi += 1;
                    }
                    else
                    {
                        musteriNesne.kiraladigiBisikletTuru = "Kiralayamadi!";
                    }
                }
                ikiliAramaAgaci.insert(durakNesne,dugumeEklenecekMusteriListesi);
            }

            ///////////////1-b/////////////////////
            Console.WriteLine("Agacin Derinligi::"+(ikiliAramaAgaci.getHeight(ikiliAramaAgaci.getRoot()) - 1)+"\n");    //Root 0.duzey sayildi.
            ikiliAramaAgaci.inOrder(ikiliAramaAgaci.getRoot());
            
            ///////////////1-c/////////////////////
            Console.Write("Bulunmasini istediginiz ID yi (1,20) giriniz::");
            int bulunmasiIstenenID = Int32.Parse(Console.ReadLine());
            Console.WriteLine("ID si "+bulunmasiIstenenID+" olan musterinin kiralama bilgileri(Karti okutan ama kiralama yapamayanlari yazmaz!...\n");
            musteriyiBulveYazdir(bulunmasiIstenenID,ikiliAramaAgaci.getRoot());
            
            ///////////////1-d/////////////////////
            Musteri sonradanEklenecekMusteri = randomMusteriOlustur(randomNesnesi2);
            Console.Write("Eklenecek olan musterinin ID sini giriniz::");
            int eklenecekMusteriID = Int32.Parse(Console.ReadLine());
            Console.Write("Kiralama isleminin hangi istasyondan yapilacagini giriniz::");
            string istenenIstasyon = Console.ReadLine();
            Console.WriteLine("");
            sonradanEklenecekMusteri.ID = eklenecekMusteriID;
            sonradanEklenecekMusteri.kiraladigiBisikletTuru = "Normal Bisiklet";
            bisikletKirala(istenenIstasyon, sonradanEklenecekMusteri, ikiliAramaAgaci.getRoot());
            Console.WriteLine("Kiralama gerceklestikten sonra duraklar yazdiriliyor...");
            ikiliAramaAgaci.inOrder(ikiliAramaAgaci.getRoot());

            ///////////////2-a/////////////////////
            Hashtable durakHashTable = new Hashtable();
            foreach(Durak durak in hashTabledaKullanilacakDuraklarListesi) //Dizi yerine onceden olusturdugum listeden yararlandım.
            {
                durakHashTable.Add(durak.durakAdi, durak);
            }


            for (int i = 0; i< hashTabledaKullanilacakDuraklarListesi.Count; i++)
            {
                Durak siradakiNesne = hashTabledaKullanilacakDuraklarListesi[i];
                if (siradakiNesne.bosParkAlaniSayisi > 5)
                {
                    siradakiNesne.bostakiNormalBisikletSayisi += 5;
                    siradakiNesne.bosParkAlaniSayisi -= 5;   //Burada park alanina iliskin detay verilmemis, ama ben azaltmayi tercih ettim.
                    durakHashTable[siradakiNesne.durakAdi] = siradakiNesne;
                }
            }

            Console.WriteLine("Max Heap'ten bilgi cekme asamasi icin herhangi bir tusa basin...");
            Console.ReadKey();
            MaxHeap h = new MaxHeap(heapYapisindaKullanilacakDuraklarListesi,heapYapisindaKullanilacakDuraklarListesi.Count);
            Durak d1 = h.RemoveMaximum();
            Durak d2 = h.RemoveMaximum();
            Durak d3 = h.RemoveMaximum();
            Console.WriteLine("Heap'den bilgi cekiliyor...");
            Console.WriteLine(d1.durakAdi);
            d1.durakYazdir();
            Console.WriteLine(d2.durakAdi);
            d2.durakYazdir();
            Console.WriteLine(d3.durakAdi);
            d3.durakYazdir();

            Console.WriteLine("Siralama algoritmalari asamasi icin herhangi bir tusa basin...");
            Console.ReadKey();
            int[] bubbleSiralanacakDizi = { 99,98,97,55,33,22,10,5 };
            BubbleSort bubbleSirala = new BubbleSort(bubbleSiralanacakDizi);
            int[] quickSortlaSiralanacakDizi = { 23, 33, 10, 5, 1, 99, 37, 90, 16, 27 };
            Console.WriteLine("Quicksort...");
            QuickSort quickSirala = new QuickSort(quickSortlaSiralanacakDizi);

            Console.ReadKey();
        }

                                                   ////////METOTLAR///////
        public static Musteri randomMusteriOlustur(Random randomNesnesi)    
        // # ID'si ve kiralama zamani rastgele olan bir musteri nesnesi olusturur.        
        {
            
            {
                int ID = randomNesnesi.Next(1, 21);
                int kiralamaSaati = randomNesnesi.Next(100, 124);
                int kiralamaDakikasi = randomNesnesi.Next(100, 160);
                string kiralamaSaatiStr = kiralamaSaati.ToString();
                string kiralamaDakikasiStr = kiralamaDakikasi.ToString();
                string kiralamaZamanBilgisi = kiralamaSaatiStr.Substring(1) + ":" + kiralamaDakikasiStr.Substring(1);
                Musteri musteriDondurulecek= new Musteri(ID, kiralamaZamanBilgisi, null);
                return musteriDondurulecek;
            }
        }

        public static List<Durak> durakListesiniOlustur(string[] durakDizi)
        // # String dizisini isler, durak nesnesi olusturur, listeye ekler ve listeyi dondurur.
        {
            List<Durak> duraklarListesi = new List<Durak>(9);
            foreach (string eleman in durakDizi)
            {
                string[] ayristirilmisStringler = eleman.Split(',');

                string durakAdi = ayristirilmisStringler[0];
                int bosPark = Int32.Parse(ayristirilmisStringler[1]);
                int tandemBisikletSay = Int32.Parse(ayristirilmisStringler[2]);
                int normalBisikletSay = Int32.Parse(ayristirilmisStringler[3]);
                Durak listeyeEklenecekDurak = new Durak(durakAdi, bosPark, tandemBisikletSay, normalBisikletSay);
                duraklarListesi.Add(listeyeEklenecekDurak);
            }
            return duraklarListesi;
        }

        public static void musteriyiBulveYazdir(int musteriID,TreeNode localRoot)
        // # ID si verilen musterinin kiralama bilgilerini listeler.
        {
            if (localRoot != null)
            {
                foreach(Musteri eleman in localRoot.musteriList)
                {
                    if (eleman.ID == musteriID && eleman.kiraladigiBisikletTuru!= "Kiralayamadi!")
                    {
                        Console.WriteLine("Bisiklet kiraladigi istasyon:: " + localRoot.data.durakAdi);
                        Console.WriteLine("Kiralama Zamani:: " + eleman.kiralamaSaati+"\n");
                    }
                }
                    musteriyiBulveYazdir(musteriID,localRoot.leftChild);
                    musteriyiBulveYazdir(musteriID,localRoot.rightChild);
            }

            
        }
        public static void bisikletKirala(string istenenIstasyon,Musteri musteri,TreeNode localNode)
        {
            while (true)
            {
                if (istenenIstasyon == localNode.data.durakAdi)
                {
                    localNode.data.bosParkAlaniSayisi += 1;                 //Burda bos park artacak dendigi icin arttirdim.                                                  
                    if (localNode.data.bostakiNormalBisikletSayisi > 0)     //Ancak bisiklet yoksa artmamasi daha uygun gibiydi.
                        localNode.data.bostakiNormalBisikletSayisi -= 1;
                    else
                        musteri.kiraladigiBisikletTuru = "Kiralayamadi!";   
                    localNode.musteriList.Add(musteri);
                    return;
                }
                else if (istenenIstasyon.CompareTo(localNode.data.durakAdi) > 0)
                    localNode = localNode.rightChild;
                else
                    localNode = localNode.leftChild;

            }
        }
    }
}
