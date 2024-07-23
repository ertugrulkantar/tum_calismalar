using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Proje4
{
    class Dijkstra
    {
        public static int INFINITY = 1000;




        public static int[] Distance(int N, int[,] cost, int[] D, int src)
        {

            int w, v, min;

            bool[] visited = new bool[N];

            int[] previous = new int[N]; //for tracking shortest paths (güzergah)

            //initialization of D[], visited[] and previous[] arrays according to src node
            for (v = 0; v < N; v++)
            {
                if (v != src)
                {
                    visited[v] = false;
                    D[v] = cost[src, v];
                    if (D[v] != INFINITY) //there is a connection between src and v
                    {
                        previous[v] = src;
                    }
                    else //no path from source
                    {
                        previous[v] = -1;
                    }
                }
                else
                {
                    visited[v] = true;
                    D[v] = 0;
                    previous[v] = -1;
                }

            }

            // Searching for shortest paths
            for (int i = 0; i < N; ++i)
            {
                min = INFINITY;
                for (w = 0; w < N; w++)
                    if (!visited[w])
                        if (D[w] < min)
                        {
                            v = w;
                            min = D[w];
                        }

                visited[v] = true;

                for (w = 0; w < N; w++)
                    if (!visited[w])
                        if (min + cost[v, w] < D[w])
                        {
                            D[w] = min + cost[v, w];
                            previous[w] = v; //update the path info
                        }
            }

            return previous;
        }

        public static void printShortestPathStraight(int dest, int[] previous)
        {
            Stack<int> pathStack = new Stack<int>();

            int current = dest;
            pathStack.Push(current);

            while (previous[current] != -1)
            {
                current = previous[current];
                pathStack.Push(current);
            }

            if (pathStack.Count == 1)
            {
                Console.Write(" NO PATH");
                return;
            }

            while (pathStack.Count > 0)
            {
                Console.Write(" -> " + pathStack.Pop());
            }
        }

        public static void printShortestPathReverse(int dest, int[] previous)
        {
            int current = dest;
            Console.Write(dest + " <- ");

            while (previous[current] != -1)
            {
                current = previous[current];
                Console.Write(current + " <- ");
            }

        }
    }
}
