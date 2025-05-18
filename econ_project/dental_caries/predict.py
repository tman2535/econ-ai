import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
import os

# مدل را فقط یک‌بار لود می‌کنیم (بهینه برای performance)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # همین پوشه‌ی cataract
MODEL_PATH = os.path.join(BASE_DIR, 'Dental Caries_model.h5')
model = tf.keras.models.load_model(MODEL_PATH)  # 🔹 این خط اضافه شده

# لیبل‌هایی که مدل آموزش دیده
labels = ["Cataract", "Mild", "Normal"]

def predict_disease(img_path):
    """
    پردازش تصویر، پیش‌بینی بیماری و برگرداندن متن تشخیص و درصد اطمینان
    """
    try:
        # بارگذاری و پیش‌پردازش تصویر
        # هر عکسی با هر ابعادی بیاد، به سایز ورودی مدل تبدیلش می‌کنیم
        img = image.load_img(img_path, target_size=(128, 128))  # 👈 مهم‌ترین تغییر
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0) / 255.0  # تبدیل به (1, 128, 128, 3)
        # پیش‌بینی
        prediction = model.predict(img_array)
        predicted_index = np.argmax(prediction)
        confidence = float(np.max(prediction)) * 100

        # تعیین پیام تشخیص
        if predicted_index in [0, 1]:  # Cataract یا Mild
            diagnosis = "شما به بیماری پوسیدگی مبتلا هستید"
        else:  # Normal
            diagnosis = "دندان شما سالم است"


        return diagnosis, round(confidence, 2)

    except Exception as e:
        # در صورت بروز خطا در پردازش
        return f"خطا در تحلیل تصویر: {e}", 0
