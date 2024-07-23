/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package pkg6.class_ve_uygulamalari;
 import java.util.Scanner;
/**
 *
 * @author ahmet
 */
public class Class_ve_uygulamalari {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        //DATE//
        Date date1 = new Date("December", 16, 1770),
                date2 = new Date(1, 27, 1756),
                date3 = new Date(1882),
                date4 = new Date();
        System.out.println("Whose birthday is " + date1 + "?");
        System.out.println("Whose birthday is " + date2 + "?");
        System.out.println("Whose birthday is " + date3 + "?");
        System.out.println("The default date is " + date4 + ".");
        //////////////////////////////////////////////////////////
        System.out.println("-------------------------------------------------");
        
        //PET//
        Pet usersPet = new Pet("Jane Doe");
        System.out.println("My records on your pet are incomplete.");
        System.out.println("Here is what they currently say:");
        System.out.println(usersPet);
        Scanner keyboard = new Scanner(System.in);
        System.out.println("Please enter the pet's name:");
        String name = keyboard.nextLine();
        System.out.println("Please enter the pet's age:");
        int age = keyboard.nextInt();
        System.out.println("Please enter the pet's weight:");
        double weight = keyboard.nextDouble();
        usersPet.set(name, age, weight);
        System.out.println("My records now say:");
        System.out.println(usersPet);
        
    }
    
}
