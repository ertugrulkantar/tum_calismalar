
package pkgfinal;



class Node 
{ 
    Vehicle info;       //Node için gerekli 
    Node prev, next;    //değişkenler tanımlandı.
} 
  
class DLL   //DoublyLinkedList
{ 
  
    static Node head, tail;     //DLL için gerekli değişkenler tanımlandı.
  
      
    static void siraliEkle(Vehicle key) //Sıralı eklemek için gerekli fonksiyon.
    { 
        Node p = new Node();    //Eklenecek düğüm oluşturuluyor.
        p.info = key; 
        p.next = null; 
  
         
        if (head == null) //Eğer head boştaysa direkt head'e ekleniyor
        {                   //ve ekleme işlemi sonlanıyor.
            head = p; 
            tail = p; 
            head.prev = null; 
            return; 
        } 
  
         
        if (head.info.compareTo(p.info)>0)  //Eğer head'den önce geliyorsa
        {                                   //oluşturulan düğüm
            p.prev = null;                  //yeni head olarak ayarlanıyor.
            head.prev = p; 
            p.next = head; 
            head = p; 
            return; 
        } 
              
         
        if (p.info.compareTo(tail.info)>=1)  //Eğer tail'den sonra geliyorsa
        {                                   //oluşturulan düğüm
            p.prev = tail;                  //yeni tail olarak ayarlanıyor.
            tail.next = p; 
            tail = p; 
            return; 
        } 
  
         
        Node temp = head.next;                  //Bu kısımda aralara ekleme için gerekli olan
        while (p.info.compareTo(temp.info)>=1)   //önce gelen düğüm bulunuyor.
                temp = temp.next; 
                  
                                  
        (temp.prev).next = p;   //Eklenecek yerden önceki node bulunduktan sonra  
        p.prev = temp.prev;     //bağlar uygun şekilde ayarlanıyor.
        temp.prev = p; 
        p.next = temp; 
    } 
  
    //DLL'yi düz yazdırma. Plakalara göre küçükten büyüğe yazdırır. 
    static void ondenYazdir() 
    { 
        Node temp=head;
        while (temp != null) 
        { 
                System.out.print(temp.info + "\n"); 
                temp = temp.next;
                System.out.println("-----------------------------");
        } 
    }
    
    //DLL'yi tersten yazdırma. Plakalara göre büyükten küçüğe yazdırır.
    static void sondanYazdir()
    {
        Node temp=tail;
            while (temp != null) 
        { 
                System.out.print(temp.info + "\n"); 
                temp = temp.prev;
                System.out.println("-----------------------------");
        } 
    }
    
    public static void plakaylaSil(String plaka)
    {
        Node current=head;  //Listeyi dolaşmak için bir düğüm oluşturuluyor.
        
        while(current!=null &&current.info.getPlaka().compareTo(plaka)!=0){
        //Burada silinecek nodu'u belirliyoruz.
            current=current.next;
        }
        deleteNode(current);    //Daha sonra silme işlemini ayarlayacak metodumuza gönderiyoruz.
    }
    
    
    private static void deleteNode(Node node) {
    if (node != null) {
        
        if (node.prev != null)          //Düğümden önceki düğüm null değilse
            node.prev.next = node.next; //düğümden önceki düğümün next'ini düğümün next'i yapıyoruz.
        else                            //Böylece silmek istediğimiz düğüm aradan çekiliyor.
            head = node.next;           //Ama öncesi yoksa o zaman sildiğimiz head'dir. Dolayısıyla
                                        //sonraki düğümü head olarak atayarak silmenin ilk adımını tamamlıyoruz.
        
        if (node.next != null)          //Düğümden sonraki düğüm null değilse
            node.next.prev = node.prev; //düğümdem sonraki düğümün prev'ini düğümün prev'i yapıyoruz.
        else                            //Böylece silmek istediğimiz düğüm aradan yine çekiliyor.
            tail = node.prev;           //Ama sonrası yoksa o zaman sildiğimiz tail'dir. Dolayısıyla
    }                                   //önceki düğümü tail olarak atayarak silmeyinin ikinci adımını 
                                        //gerçekleştiriyoruz.
}
}
