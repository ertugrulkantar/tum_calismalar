using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _00_Proje2
{
    class QueueM
    {
        public int maxSize;
        public Musteri[] queArray;
        public int front;
        public int rear;
        public int nItems;

        public QueueM(int s)
        {
            maxSize = s;
            queArray = new Musteri[maxSize];
            front = 0;
            rear = -1;
            nItems = 0;
        }

        public void insert(Musteri musteriNesnesi) // put item at rear of queue
        {
            if (rear == maxSize - 1) 
                rear = -1;
            queArray[++rear] = musteriNesnesi; 
            nItems++; 
        }
        public Musteri remove() // take item from front of queue
        {
            Musteri temp = queArray[front++];
            if (front == maxSize)
                front = 0;
            nItems--; 
            return temp;
        }
        public bool isEmpty() 
        {
            return (nItems == 0);
        }
        
        public QueueM(QueueM x) //Copy Constructor.
        {
            this.maxSize = x.maxSize;
            this.queArray =(Musteri[])x.queArray.Clone();
            this.front = x.front;
            this.rear = x.rear;
            this.nItems = x.nItems;
        }    
    }
}
