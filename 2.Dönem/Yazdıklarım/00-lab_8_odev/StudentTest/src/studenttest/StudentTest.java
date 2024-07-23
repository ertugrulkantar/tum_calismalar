
package studenttest;


public class StudentTest {

  
    public static void main(String[] args) {
        
        UnderGraduateStudent s1=new UnderGraduateStudent("Ali","Kabak","32487633880","İzmir","Nuray Aydın");
        System.out.println("UnderGraduateStudent::\n"+s1);
        System.out.println("----------------------------------------");
        GraduateStudent s2=new GraduateStudent("Kaya", "Koca","84678909096", "Aydın", "Arttirilmis Gerceklik");
        System.out.println("GraduateStudent::\n"+s2);
    }
    
}
