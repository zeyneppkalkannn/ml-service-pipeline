MAKİNE ÖĞRENMESİ MODELİNİ API OLARAK SUNMA VE CI/CD PRENSİBİNİ UYGULAMA
Bu proje, önceden eğitilmiş bir makine öğrenimi modelini (Python/Flask) bir C# .NET Core Web API'si üzerinden sunmayı ve bu süreci Docker ile konteynerize edip GitHub Actions ile otomatikleştirmeyi amaçlamaktadır.

Nasıl Çalıştırılır (Yerel Ortam)
Projeyi yerel olarak test etmek için aşağıdaki adımları sırayla uygulayın:

1. Model Dosyasını Oluşturma

Python modelini eğitip disk üzerine kaydetmeniz gerekir. Bu dosya, Docker build sırasında Python imajına dahil edilecektir.

# Gerekli kütüphaneleri kur
pip install scikit-learn numpy joblib

# Modeli eğitir ve ModelService/model/linear_model.pkl olarak kaydeder
python create_model.py



2. Konteynerleri Başlatma

Projenin kök dizinindeyken Docker Compose'u çalıştırın.

# Tüm servisleri build eder ve arka planda başlatır (-d: detached mode)
docker-compose up --build -d



3. API'yi Test Etme

Uygulama başarıyla başladıktan sonra (kontrol için docker ps), tahmin isteğini gönderin.

curl -X POST http://localhost:8080/api/prediction -H "Content-Type: application/json" -d '{"features": [[10.0, 5.0]]}'



CI/CD Akışını Doğrulama (Sürekli Entegrasyon)
Projenin otomasyon özelliğini test etmek için:

GitHub deponuzda herhangi bir dosyada küçük bir değişiklik yapın (örneğin, bu README.md dosyasına bir boşluk ekleyin).

Değişikliği Git'e ekleyin ve tekrar GitHub'a push edin.

GitHub arayüzünde Actions sekmesine gidin.

Yeni push işleminizin, "ML API CI Pipeline" adlı bir workflow'u otomatik olarak tetiklediğini ve imajları yeniden derlediğini gözlemleyin. Bu, CI prensibinin çalıştığını doğrular.
