
package deneme;


public class Queue {
    private int maxSize;
    private int front;
    private int rear;
    private int nItems;
    public Object kuyrukDizi[]; //Listeyi yazdirirken gerekiyor.get() kullanmadigim icin
                                //diziyi public olarak olusturdum.
    
    
    public Queue(int diziUzunlugu)
    {
        maxSize=diziUzunlugu;
        front=0;
        rear=-1;
        nItems=0;
        kuyrukDizi=new Object[diziUzunlugu];
    }
    
    public void insert(Object eklenecek)
    {
        if (rear==maxSize-1)
        {
            rear=-1;
            kuyrukDizi[rear+1]=eklenecek;
            rear++;
            nItems++;
        }
        else
        {
            kuyrukDizi[rear+1]=eklenecek;
            rear++;
            nItems++;
        }
    }
    
    public Object remove()
    {
        if(front==maxSize)
        {
            Object dondurulecekEleman=kuyrukDizi[front];
            kuyrukDizi[front]=kuyrukDizi[front-1];
            front=0;
            nItems--;
            return "Listeden cikarilan eleman::"+dondurulecekEleman;
        }
        else if(front==0)
        {
            Object dondurulecekEleman=kuyrukDizi[front];
            kuyrukDizi[front]=null;
            front++;
            nItems--;
            return "Listeden cikarilan eleman::"+dondurulecekEleman;
        }
        else
        {
            Object dondurulecekEleman=kuyrukDizi[front];
            kuyrukDizi[front]=kuyrukDizi[front-1];
            front++;
            nItems--;
            return "Listeden cikarilan eleman::"+dondurulecekEleman;    
        }
    }
    
    public Object peekFront()
    {
        return kuyrukDizi[front];
    }
    
    public boolean isEmpty()
    {
        return(nItems==0);
    }
            
    public boolean isFull()
    {
        return (nItems==maxSize);
    }
    
    public int size()
    {
        return nItems;
    }
    
}
