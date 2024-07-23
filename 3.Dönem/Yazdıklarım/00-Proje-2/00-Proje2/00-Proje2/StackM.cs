using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _00_Proje2
{
    class StackM
    {
        public int maxSize; 
        public Musteri[] stackArray;
        public int top;

        public StackM(int boyut) 
        {
            maxSize = boyut; 
            stackArray = new Musteri[maxSize];
            top = -1; 
        }
        public void push(Musteri musteriNesnesi)
        {
            stackArray[++top] = musteriNesnesi; 
        }
        public Musteri pop() 
        {
            return stackArray[top--]; 
        }
        public bool isEmpty() 
        {
            return (top == -1);
        }
    }
}
