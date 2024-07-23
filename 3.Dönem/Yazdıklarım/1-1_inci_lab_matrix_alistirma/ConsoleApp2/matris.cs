using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp2
{
    class Matris
    {
        static void Main(string[] args)
        {
            int[,] matris = { { 5, 4, 3, 2, 1 }, { 1, 3, 4, 6, 5 }, { 6, 3, 2, 1, 0 }, { 2, 5, 7, 11, 20 }, { 13, 17, 19, 23, 25 } };

            int[] toplam = karoTopla(matris);
            for(int i = 0; i < toplam.GetLength(0); i++)
            {
                Console.Write(toplam[i]+" ");
            }

            Console.ReadKey();
        }

        static int[] karoTopla(int[,] m)
        {
            int matrisSatirSay = m.GetLength(0);
            int matrisSutunSay = m.GetLength(1);
            int[] matrisToplamDizi = new int[matrisSatirSay];
            int baslanacakSutun = (int)(m.GetLength(0) / 2);
            int durulacakSutun = baslanacakSutun;
            for (int i = 0; i < matrisSatirSay; i++)
            {
                for (int j = baslanacakSutun; j <= durulacakSutun;j++)
                {
                    matrisToplamDizi[i] += m[j,i];  //Burada j,i degistirilerek
                                                    //satir degil sutun topladin.
                }                                   //Yani bi nevi transpoze ettin.
                if (i <Math.Floor((double)m.GetLength(0)/2))
                {
                    baslanacakSutun -= 1;
                    durulacakSutun += 1;
                }
                else if (i >=((int)m.GetLength(0) / 2))
                {
                    baslanacakSutun += 1;
                    durulacakSutun -= 1;
                }
               
            }
            return matrisToplamDizi;
        }
    }
}
