import 'dart:convert';
import 'package:flutter_proje/Bolum21/4-Dio/entity/Kisiler.dart';
import 'package:flutter_proje/Bolum21/4-Dio/entity/KisilerCevap.dart';
import 'package:dio/dio.dart';

class KisilerDaoRepository{

  List<Kisiler> parseKisilerCevap(String cevap){
    return KisilerCevap.fromJson(json.decode(cevap)).kisiler;
  }

  Future<void> kisiKayit(String kisi_ad,String kisi_tel) async{
    var url="http://kasimadalan.pe.hu/kisiler/insert_kisiler.php";
    var veri={"kisi_ad":kisi_ad,"kisi_tel":kisi_tel};
    var cevap=await Dio().post(url,data: FormData.fromMap(veri));
    print("Kisi ekle: ${cevap.data.toString()}");  }

  Future<void> kisiGuncelle(int kisi_id,String kisi_ad,String kisi_tel) async{
    var url="http://kasimadalan.pe.hu/kisiler/update_kisiler.php";
    var veri={"kisi_id":kisi_id,"kisi_ad":kisi_ad,"kisi_tel":kisi_tel};
    var cevap=await Dio().post(url,data: FormData.fromMap(veri));
    print("Kisi guncelle: ${cevap.data.toString()}");
  }

  Future<List<Kisiler>> tumKisileriAl() async{
    var url="http://kasimadalan.pe.hu/kisiler/tum_kisiler.php";
    var cevap=await Dio().get(url);
    return parseKisilerCevap(cevap.data.toString());
  }

  Future<List<Kisiler>> kisiAra(String aramaKelimesi) async{
    var url="http://kasimadalan.pe.hu/kisiler/tum_kisiler_arama.php";
    var veri={"kisi_ad":aramaKelimesi};
    var cevap=await Dio().post(url,data: FormData.fromMap(veri));
    return parseKisilerCevap(cevap.data.toString());
  }

  Future<void> kisiSil(int kisi_id) async{
    var url="http://kasimadalan.pe.hu/kisiler/delete_kisiler.php";
    var veri={"kisi_id":kisi_id};
    var cevap=await Dio().post(url,data: FormData.fromMap(veri));
    print("Kisi sil: ${cevap.data.toString()}");
  }
}