import 'package:flutter_proje/Bolum17/47-Filmler_Uygulamasi_Http/31-Kategoriler.dart';

class KategorilerCevap{
  int success;
  List<Kategoriler> kategorilerNesnesi;

  KategorilerCevap(this.success, this.kategorilerNesnesi);

  factory KategorilerCevap.fromJson(Map<String,dynamic> json){
    var jsonArray=json["kategoriler"] as List;
    List<Kategoriler> kategorilerNesnesi=jsonArray.map((jsonArrayNesnesi) => Kategoriler.fromJson(jsonArrayNesnesi)).toList();
    return KategorilerCevap(json["success"] as int,kategorilerNesnesi);
  }
}