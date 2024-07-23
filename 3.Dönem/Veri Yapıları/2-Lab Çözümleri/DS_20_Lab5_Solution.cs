using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DS_Lab_5
{
    class Urun
    {
        public string urunAdı { get; set; }
        public int fiyat { get; set; }

        public Urun(string urunAdı, int fiyat)
        {
            this.urunAdı = urunAdı;
            this.fiyat = fiyat;
        }

        public override string ToString()
        {
            return "(" + urunAdı + ", " + fiyat + ")";
        }
    }

    class Kuyruk
    {
        public List<Urun> liste;

        public Kuyruk()
        {
            liste = new List<Urun>();
        }

        public void ekle(Urun urun)
        {
            liste.Add(urun);
        }

        public Urun sil()
        {
            Urun temp = liste[0];
            liste.RemoveAt(0);
            return temp;
        }

        public bool bosMu()
        {

            return (liste.Count == 0);
        }

        public int elemanSayısı()
        {
            return liste.Count;
        }

        public override string ToString()
        {
            string text = "";

            foreach (Urun eleman in liste)
                text += eleman.ToString() + ", ";

            return text;
        }

    }

    class Program
    {
        static void Main(string[] args)
        {
            Kuyruk q1 = new Kuyruk();
            Queue<Urun> q2 = new Queue<Urun>();

            q1.ekle(new Urun("masa", 100));
            q1.ekle(new Urun("TV", 1250));
            q1.ekle(new Urun("dolap", 210));
            q1.ekle(new Urun("kagıt", 35));

            Console.Write("q1 (Kuyruk) :\t");
            Console.WriteLine(q1);
            Console.WriteLine("eleman sayısı: {0}", q1.elemanSayısı());

            elemanTaşı(q1, q2);

            Console.WriteLine();
            Console.WriteLine("After q1 -> q2 transfer:");
            Console.Write("q2 (System.Collections.Queue):\t");

            foreach (Urun item in q2)
            {
                Console.Write(item.ToString() + ", ");
            }
            Console.WriteLine();
            Console.WriteLine("eleman sayısı: {0}", q2.Count);

            Console.ReadKey();
        }
        static void elemanTaşı(Kuyruk k, Queue<Urun> q2)
        {
            while (!k.bosMu())
            {
                q2.Enqueue(k.sil());
            }
        }
    }
}
