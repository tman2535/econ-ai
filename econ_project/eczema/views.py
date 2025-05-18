import os
from django.shortcuts import render
from django.conf import settings
from .predict import predict_disease  # تابعی که قبلاً ساختیم
from django.core.files.storage import FileSystemStorage

def upload_image(request):
    """
    صفحه‌ای که کاربر می‌تونه عکس چشم خودش رو آپلود کنه.
    """
    return render(request, 'eczema/upload.html')

def cataract_result(request):
    """
    این ویو فایل آپلود شده رو دریافت می‌کنه، مدل AI رو صدا می‌زنه،
    و نتیجه تشخیص + درصد رو به قالب نمایش می‌ده.
    """
    if request.method == 'POST' and request.FILES.get('eye_image'):
        # ذخیره کردن عکس
        image_file = request.FILES['eye_image']
        fs = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'uploads'))
        filename = fs.save(image_file.name, image_file)
        file_url = fs.url(filename)
        full_path = os.path.join(settings.MEDIA_ROOT, 'uploads', filename)

        # پیش‌بینی با مدل AI
        diagnosis, confidence = predict_disease(full_path)

        # حذف فایل برای جلوگیری از شلوغ شدن
        os.remove(full_path)

        return render(request, 'eczema/result.html', {
            'diagnosis': diagnosis,
            'confidence': confidence,

        })

    # اگر کسی مستقیم به این صفحه بیاد بدون POST
    return render(request, 'eczema/result.html', {
        'diagnosis': "هیچ عکسی ارسال نشده است.",
        'confidence': 0
    })
