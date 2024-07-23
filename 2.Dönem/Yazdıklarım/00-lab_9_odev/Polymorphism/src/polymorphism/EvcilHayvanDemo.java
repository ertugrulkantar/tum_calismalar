
package polymorphism;


public class EvcilHayvanDemo {
    
    public static void main(String[] args) {
        EvcilHayvan EvcilHayvanDizi[]=new EvcilHayvan[4];
        
        Dog dog1= new Dog("Cavcav",9,10,"Kurt");
        Dog dog2= new Dog("Diego",7,6,"Rotweiller");
        Cat cat1= new Cat("Kara",5,3,"Sari");
        Cat cat2= new Cat("Minnak",8,4,"Beyaz");
        
        EvcilHayvanDizi[0]=dog1;
        EvcilHayvanDizi[1]=dog2;
        EvcilHayvanDizi[2]=cat1;
        EvcilHayvanDizi[3]=cat2;
        
        for (EvcilHayvan hayvan : EvcilHayvanDizi){
            System.out.println(hayvan);
            hayvan.ilac01Dozaj();
            hayvan.ilac02Dozaj();
            System.out.println("\n");
        }
    }
    
}
