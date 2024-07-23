/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package citymain;

/**
 *
 * @author ahmet
 */
public class City implements Comparable{
    
    private String cityName;
    private double temperature;
    
    public City()
    {
        temperature=0.0;
        cityName=null;
    }
    
    
    public City(String sehirAdi,double sicaklik)
    {
        temperature=sicaklik;
        cityName=sehirAdi;
    }

    public String getCityName() {
        return cityName;
    }

    public void setCityName(String cityName) {
        this.cityName = cityName;
    }

    public double getTemperature() {
        return temperature;
    }

    public void setTemperature(double temperature) {
        this.temperature = temperature;
    }
    
    public String toString()
    {
        return ("Sehir Adi::"+getCityName()+"   Sicaklik::"+getTemperature());
    }
 
    public int compareTo(Object other)
    {
        City otherCity=(City) other;
        
        if (temperature==otherCity.temperature)
        {
            return 0;
        }
        if (temperature<otherCity.temperature)
        {
            return -1;
        }
        return 1;
    }
}
