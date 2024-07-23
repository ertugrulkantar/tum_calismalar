import 'package:flutter_bloc/flutter_bloc.dart';
import 'package:flutter_proje/Bolum21/4-Dio/entity/Kisiler.dart';
import 'package:flutter_proje/Bolum21/4-Dio/repo/Kisilerdao_repository.dart';

class AnasayfaCubit extends Cubit<List<Kisiler>>{
  AnasayfaCubit() : super(<Kisiler>[]);

  var krepo=KisilerDaoRepository();

  Future<void> kisileriYukle() async{
    var liste=await krepo.tumKisileriAl();
    emit(liste);
  }

  Future<void> ara(String aramaKelimesi) async{
    var liste=await krepo.kisiAra(aramaKelimesi);
    emit(liste);
  }

  Future<void> sil(int kisi_id) async{
    await krepo.kisiSil(kisi_id);
    await kisileriYukle();
  }
}