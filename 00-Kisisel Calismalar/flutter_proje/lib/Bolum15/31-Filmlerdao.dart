import 'package:flutter_proje/Bolum15/31-Filmler.dart';
import 'package:flutter_proje/Bolum15/31-Kategoriler.dart';
import 'package:flutter_proje/Bolum15/31-VeritabaniYardimcisi.dart';
import 'package:flutter_proje/Bolum15/31-Yonetmenler.dart';

class Filmlerdao{

  Future<List<Filmler>> tumFilmlerByKategoriId(int kategori_id) async{
    var db=await VeritabaniYardimcisi.veritabaniErisim();

    List<Map<String,dynamic>> maps=await db.rawQuery("SELECT * FROM filmler,kategoriler,yonetmenler "
        "WHERE filmler.kategori_id=kategoriler.kategori_id and filmler.yonetmen_id=yonetmenler.yonetmen_id and filmler.kategori_id=$kategori_id");

    return List.generate(maps.length,(i){
      var satir=maps[i];
      var k= Kategoriler(satir["kategori_id"],satir["kategori_ad"]);
      var y=Yonetmenler(satir["yonetmen_id"],satir["yonetmen_ad"]);
      var f=Filmler(satir["film_id"], satir["film_ad"], satir["film_yil"], satir["film_resim"], k, y);
      return f;
    });
  }
}