import joblib
import numpy as np
from flask import Flask, request, jsonify

# Flask uygulamasını başlat
app = Flask(__name__)

# Modelin diskten yüklenmesi
# Not: Bu, her istekte yapılabilir, ancak performans için uygulamanın başlangıcında yüklemek daha iyidir.
try:
    # ModelService/model/linear_model.pkl dosyasını yükler
    model = joblib.load('model/linear_model.pkl')
    print("Makine Öğrenimi Modeli Başarıyla Yüklendi.")
except Exception as e:
    print(f"Model yüklenirken bir hata oluştu: {e}")
    model = None # Hata durumunda modelin None olarak kalmasını sağlar.

@app.route('/predict', methods=['POST'])
def predict():
    """
    Gelen JSON verisindeki özellikleri alır, model ile tahmin yapar ve sonucu döndürür.
    """
    if model is None:
        return jsonify({"error": "Model henüz yüklenemedi."}), 500

    data = request.get_json(force=True)
    
    # 'features' anahtarını kontrol et ve NumPy dizisine dönüştür
    try:
        features = data['features']
        # features listesinin içindeki listeleri numpy array'e dönüştürür
        X = np.array(features) 
    except KeyError:
        return jsonify({"error": "Gereken 'features' alanı bulunamadı."}), 400
    except Exception as e:
        return jsonify({"error": f"Giriş verisi formatı hatalı: {e}"}), 400

    # Tahmin yap
    prediction = model.predict(X)

    # Sonucu JSON formatında döndür (tahmin, bir numpy array'den listeye dönüştürülür)
    return jsonify({
        'prediction': prediction.tolist()
    })

if __name__ == '__main__':
    # Docker ortamında 5000 portunda çalışır
    app.run(host='0.0.0.0', port=5000)
