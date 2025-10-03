import numpy as np
from sklearn.linear_model import LinearRegression
import joblib
import os

# 1. Örnek Veri Kümesi Oluşturma
# Giriş (X) ve Çıkış (y) verileri. Basit bir doğrusal ilişki: y = 2*x1 + 3*x2 + 5
X = np.array([
    [1, 2],
    [5, 4],
    [10, 8],
    [15, 12],
    [20, 16]
])
# Örneğin, ilk satır için: y = 2*1 + 3*2 + 5 = 13
y = np.array([13, 27, 49, 71, 93]) 

# 2. Modeli Eğitme
model = LinearRegression()
model.fit(X, y)

# Eğitimi kontrol et (Örnek tahmin)
# [10.0, 5.0] için tahmin: 2*10 + 3*5 + 5 = 40
print(f"Örnek tahmin ([10, 5]): {model.predict([[10.0, 5.0]])[0]:.2f}")

# 3. Modelin Kaydedileceği Dizini Oluşturma
model_dir = 'ModelService/model'
os.makedirs(model_dir, exist_ok=True)

# 4. Modeli joblib (pickle'ın optimize edilmiş versiyonu) ile kaydetme
model_path = os.path.join(model_dir, 'linear_model.pkl')
joblib.dump(model, model_path)

print(f"\nModel başarıyla '{model_path}' konumuna kaydedildi.")
print("Bu dosyayı GitHub reponuza ekleyebilirsiniz.")
