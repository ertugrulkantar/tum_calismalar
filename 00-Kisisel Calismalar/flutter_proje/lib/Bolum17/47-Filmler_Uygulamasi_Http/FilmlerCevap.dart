import 'package:flutter_proje/Bolum17/47-Filmler_Uygulamasi_Http/31-Filmler.dart';

class FilmlerCevap{
  int success;
  List<Filmler> filmlerNesnesi;

  FilmlerCevap(this.success, this.filmlerNesnesi);

  factory FilmlerCevap.fromJson(Map<String,dynamic> json){
    var jsonArray=json["filmler"] as List;
    List<Filmler> filmlerlerNesnesi=jsonArray.map((jsonArrayNesnesi) => Filmler.fromJson(jsonArrayNesnesi)).toList();
    return FilmlerCevap(json["success"] as int,filmlerlerNesnesi);
  }
}