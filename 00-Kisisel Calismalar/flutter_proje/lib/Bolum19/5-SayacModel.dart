import 'package:flutter/material.dart';

class SayacModel extends ChangeNotifier{
  int sayac=0;

  int sayaciOku(){
    return sayac;
  }

  void sayaciArttir(){
    sayac++;
    notifyListeners();
  }

  void sayaciAzalt(int miktar){
    sayac-=miktar;
    notifyListeners();
  }

}