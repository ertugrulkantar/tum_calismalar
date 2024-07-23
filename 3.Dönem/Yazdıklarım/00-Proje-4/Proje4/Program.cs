using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Proje4
{
    class Program
    {
        public static int INFINITY = 1000;
        static void Main(string[] args)
        {
            Console.BackgroundColor = ConsoleColor.White;
            Console.Clear();
            Console.ForegroundColor = ConsoleColor.Black;

            AVL tree = new AVL();
            tree.Add(10);
            tree.Add(3);
            tree.Add(15);
            tree.Add(2);
            tree.Add(7);
            tree.Add(12);
            tree.Add(1);
            tree.Add(5);
            tree.Add(6);
            tree.Add(9);
            Console.WriteLine("\n(Q-2)AVL tree ekrana yazdiriliyor...");
            BTreePrinter.Print(tree.root);
            ///////////////////////
            
            int N = 5;
            int SRC = 0;

            int[,] cost = {
        { INFINITY,    5,    3, INFINITY,    2},
        { INFINITY, INFINITY,    2,    6, INFINITY},
        { INFINITY,    1, INFINITY,    2, INFINITY},
        { INFINITY, INFINITY, INFINITY, INFINITY, INFINITY},
        { INFINITY,    6,   10,    4,    INFINITY}  };
            Console.WriteLine("\n(Q-4.1) Dijkstra's Algorithm");
            ikiBoyutluMatrisYazdir(cost, "Dijkstra");
            int[] distances = new int[N];
            int[] previous = Dijkstra.Distance(N, cost, distances, SRC);

            Console.WriteLine("\n0'dan diger dugumlere olan en kisa uzakliklar...\n");
            Console.WriteLine("0->0   0->1    0->2    0->3    0->4");
            Console.WriteLine("----   ----    ----    ----    ----");
            for (int i = 0; i < distances.Length; ++i)
                if (distances[i] != INFINITY)
                    Console.Write(" "+distances[i]+"      ");
                else Console.Write("INFINITY  ");
            Console.WriteLine("\n\n***Dijkstra's algoritma uygulamasinin sonu***");
            ///////////////////////

            int[,] graph = new int[,] { { 0, 2, 0, 6, 0 },
                                      { 2, 0, 3, 8, 5 },
                                      { 0, 3, 0, 0, 7 },
                                      { 6, 8, 0, 0, 9 },
                                      { 0, 5, 7, 9, 0 } };
            Console.WriteLine("\n(Q-4.2) Prim's Algorithm");
            ikiBoyutluMatrisYazdir(graph, "Prim");

            Prim_MST.primMST(graph);
            Console.WriteLine("\n***Prim's algoritma uygulamasinin sonu***");
            ///////////////////////
            Console.WriteLine("\n(Q-4.3) Depth First Traversal");
            GraphDFS graphDFS = new GraphDFS(9);

            graphDFS.AddEdge(0, 1);
            graphDFS.AddEdge(0, 4);
            graphDFS.AddEdge(0, 8);
            graphDFS.AddEdge(1, 2);
            graphDFS.AddEdge(1, 4);
            graphDFS.AddEdge(2, 3);
            graphDFS.AddEdge(4, 5);
            graphDFS.AddEdge(5, 6);
            graphDFS.AddEdge(6, 7);

            Console.WriteLine("\nDepth first search calistiriliyor.GRAPHS-II slaytı 10.sayfadaki ornek uygulandi. Cikmasi gereken sira 0,1,2...,8.\n");
                
            graphDFS.DFS(0);
            Console.WriteLine("\nProgram sonu...");
            Console.ReadKey();
        }
                                  ////////////////  METOTLAR  ////////////////
        public static void ikiBoyutluMatrisYazdir(int[,] matris,String mod)
        {
            int boyut = matris.GetLength(0);
            if (mod == "Dijkstra") 
            {
                Console.WriteLine("\nDijkstra'yla islenecek matris(X::Yol Yok!)...\n");
                Console.WriteLine("   0  1  2  3  4");
                Console.WriteLine("  -- -- -- -- --");
            }
            else if (mod == "Prim")
            {
                Console.WriteLine("\nPrim's MST ile islenecek matris...\n");
                Console.WriteLine("   0  1  2  3  4");
                Console.WriteLine("   -- -- -- -- --");
            }
            
            for(int i = 0; i < boyut; i++)
            {
                Console.Write(i + "| ");
                for(int j=0;j<boyut; j++)
                {
                    if (matris[i, j] == 1000)
                        Console.Write("X  ");
                    else
                        Console.Write(matris[i, j]+"  ");
                }
                Console.WriteLine();
            }
        }
    }
}
