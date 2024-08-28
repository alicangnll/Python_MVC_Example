# Flask Python MVC Örneği | Flask Python MVC Example

<p>
    Merhabalar, bu repoda Python'un Flask kütüphanesiyle MVC mimarisi yapısını kurdum. Umarım bu kaynak size çok yardımcı olmuştur.
<p>

## Kurulum
<code>
    python3 -m pip install -r requirements.txt
</code>

## Dosya Yapısı
<code>
proje/
|
├── templates/
|   └── index.html
|
├── migrations/ (Geçici dosya init komutuyla oluşturulacak)
|   └── ...
|
├── instance/
|   └── data.db (DB oluşturulduktan sonra gelecek)
|
├── routes/
|   └── Route.py
|
├── models/
|   └── DBModel.py
|
├── controllers/
|   └── Controller.py
|
├── app.py
└── config.py
</code>

## Uygulama İçeriği
<code>
main/
|
├── iexampleuser (Example userları insert eder)
└── listuser (Tablodaki kullanıcıları listeler)
</code>

## Database oluşturma
<p>
    Database oluşturmak için öncelikle proje klasörünün içerisinde <b>"python3 -m flask db init"</b> komutuyla migrate klasörlerini oluşturuyoruz. Ardından <b>"python3 -m flask db migrate"</b> ile DB dosyasını oluşturuyoruz. Tüm bu işlemlerden sonra ise <b>"python3 -m flask db upgrade"</b> ile DB içerisine tablolar insert edilir.
</p>

## PyCache dosyalarını silme kodu
<code>
    python3 -Bc "import pathlib; [p.unlink() for p in pathlib.Path('.').rglob('*.py[co]')]"
    python3 -Bc "import pathlib; [p.rmdir() for p in pathlib.Path('.').rglob('__pycache__')]"
</code>