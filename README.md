# ECON – AI‑Powered Medical‑Image Classifier
Early screening for **Eye, Skin, and Oral** diseases in your browser.

---

## 1 . Quick‑start (TL;DR)

```bash
# 1‑A  clone & enter project
git clone <your‑repo>.git
cd econ               # root that contains manage.py

# 1‑B  create & activate venv  (recommended)
python -m venv venv
source venv/bin/activate   # (Windows → venv\Scripts\activate)

# 1‑C  install every dependency
pip install -r requirements.txt

# 1‑D  start Django
cd econ_project               # ⚠️ important: manage.py lives one level up,
python ../manage.py migrate   # so we call it with ../
python ../manage.py runserver 0.0.0.0:8000
Open the URL shown in terminal (on CS50.dev / Codespaces it looks like
https://<workspace>-8000.app.github.dev/) and you’ll land on the Home page.

2 . Folder map (what is where?)
sql
Copy
Edit
econ/
│
├── dataset/          ← full Cataract dataset  (.jpg / .png)
├── datasetde/        ← Dry‑Eye (first letters “de”)
├── datasetst/        ← Strabismus (“st”)
├── datasetac/        ← Acne
├── datasetec/        ← Eczema
├── datasetps/        ← Psoriasis
├── datasetdc/        ← Dental‑Caries
├── datasetgi/        ← Gingivitis
│
├── econ_project/     ← Django project
│   ├── settings.py / urls.py / …
│   ├── cataract/
│   │   ├── cataract_model.h5
│   │   └── views / urls / templates
│   ├── dryeye/
│   │   ├── dryeye_model.h5
│   │   └── …
│   ├── strabismus/   (etc. for every disease)
│   ├── acne/
│   ├── eczema/
│   ├── psoriasis/
│   ├── dental_caries/
│   └── gingivitis/
│
├── main/             ← “Home” app: templates/main/index.html
├── static/           ← global css / images (main page tiles)
└── media/            ← runtime uploads (auto‑created)
3 . Training scripts (one per disease)
Every main*.py file at repo root trains exactly one model:

Script	Uses dataset	Saves model as	Django app that loads it
main.py	dataset/	cataract_model.h5	cataract/
mainde.py	datasetde/	dryeye_model.h5	dryeye/
mainst.py	datasetst/	strabismus_model.h5	strabismus/
mainac.py	datasetac/	acne_model.h5	acne/
mainec.py	datasetec/	eczema_model.h5	eczema/
mainps.py	datasetps/	psoriasis_model.h5	psoriasis/
maindc.py	datasetdc/	dental_caries_model.h5	dental_caries/
maingi.py	datasetgi/	gingivitis_model.h5	gingivitis/

Training once:

bash
Copy
Edit
python mainde.py         # example → trains Dry‑Eye model
# when finished it drops dryeye_model.h5 inside dryeye/ app automatically
All scripts share the same CNN architecture (128×128 RGB input, “yes / no” classes).
Feel free to tweak hyper‑parameters inside each script.

4 . How inference works
User uploads an image at /cataract/ (or any other app).

View saves file temporarily → calls predict.py inside that app.

predict.py loads corresponding *_model.h5, preprocesses the image, does model.predict.

Confidence % + human‑readable diagnosis go to result.html.

Uploaded file is deleted to keep media/uploads/ clean.

5 . Extending – Add a new disease in 3 steps
python manage.py startapp mydisease

Copy urls.py, views.py, templates, predict.py, and a train script from an existing app.

Register in two places:

in econ_project/settings.py → INSTALLED_APPS.append('mydisease')

in econ_project/urls.py:

python
Copy
Edit
path('mydisease/', include(('mydisease.urls', 'mydisease'), namespace='mydisease')),
Train → drop mydisease_model.h5 inside the app → done!

6 . Requirements
requirements.txt already lists everything needed:

text
Copy
Edit
Django==3.2.20
tensorflow==2.15.0
keras==2.15.0
numpy==1.24.3
scikit-learn==1.3.0
opencv-python==4.8.0.76
pillow==9.5.0
matplotlib==3.7.1
# optional but handy
django-crispy-forms==2.0
django-bootstrap4==22.2
Install with:

bash
Copy
Edit
pip install -r requirements.txt
7 . Common issues & fixes
Symptom	Fix
NoReverseMatch for cataract namespace	ensure econ_project/urls.py uses include(('cataract.urls','cataract'), namespace='cataract') and templates call {% url 'cataract:cataract_result' %}
CUDA / oneDNN warnings on Codespaces	just ignore – TensorFlow runs on CPU
FileNotFoundError for model	copy the trained *_model.h5 into its matching app folder
Images .jfif not read	convert to .jpg / .png via Pillow (see section 3‑Prepare)

8 . Licence & Contact
 Developed by TahaMansouri.
