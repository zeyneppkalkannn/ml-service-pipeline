Makine Öğrenmesi Modelini API Olarak Sunma ve CI/CD Prensibini Uygulama 

Bu proje, önceden eğitilmiş bir makine öğrenmesi modelini (Python/Flask) bir C# .NET Core Web API’si üzerinden sunmayı; bu servisi Docker ile konteynerize etmeyi ve GitHub Actions ile otomatikleştirmeyi amaçlar.

Nasıl Çalıştırılır (Yerel Ortam)

Aşağıdaki adımları sırayla uygulayın:

1) Model Dosyasını Oluşturma
Python tarafında modeli eğitip disk üzerine kaydetmeniz gerekir. Bu dosya Docker build sırasında imaja dahil edilecektir.
	1.	Gerekli kütüphaneleri kurun:
  pip install scikit-learn numpy joblib

  2.	Modeli eğitip kaydeden script’i çalıştırın (ör. create_model.py):
  python create_model.py

Bu işlem sonucunda model dosyası örneğin ModelService/model/linear_model.pkl konumuna kaydedilecek.


2) Konteynerleri Başlatma
Projeyi kök dizinde çalıştırın. (Proje docker-compose.yml içeriyor varsayımıyla.)
Tüm servisleri build eder ve arka planda başlatır:
docker-compose up --build -d

Başarıyla çalıştığını doğrulamak için:
docker ps

komutuyla konteynerlerin durumunu kontrol edin.


3) API’yi Test Etme
Uygulama ayağa kalktıktan sonra tahmin isteği gönderin:
curl -X POST http://localhost:8080/api/prediction \
  -H "Content-Type: application/json" \
  -d '{"features": [[10.0, 5.0]]}'
   
Beklenen çıktı: modelin verdiği tahmin JSON formatında dönecektir (ör. {"prediction": ...}).


CI/CD Akışını Doğrulama (Sürekli Entegrasyon)

Otomasyonun çalıştığını test etmek için:
	1.	GitHub deponuzdaki herhangi bir dosyada küçük bir değişiklik yapın (ör. README.md’ye bir boş satır ekleyin).
    2.	Değişikliği commit edip GitHub’a push edin:
    git add .
    git commit -m "test: trigger CI pipeline"
    git push origin main
    3.	GitHub arayüzünde Actions sekmesine gidin.
    4.	Yeni push ile birlikte "ML API CI Pipeline" (veya repositoryde tanımlı workflow) tetiklenmiş olmalı; workflow çalışıp Docker imajını yeniden derleyecektir.
