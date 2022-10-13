# Online Test Software Engineer - Zulfa Fajrul Falah
## Deskripsi
Repositori ini merupakan hasil pekerjaan dari Test Software Engineer di  PT Aku Pintar Indonesia. Service API ini di bangung dengan framework Flask (Python) dengan database mysql.

## Dokumentasi API
https://documenter.getpostman.com/view/12744419/2s83zpK1g4

## Langkah Instalasi
- Buat virtual environment 
```
python -m venv env
```
- Aktifkan env (linux/mac)
```
source env/bin/activate
```
- install requirements.txt
```
pip install -r requirements.txt
```
- Settings configurasi mysql di .env
- Silakan Migrate database
```
flask db upgrade      
```
- Jalankan Flask-Seed
```
flask seed run 
```
- Jalan Flask Aplication
```
flask run 
```
- Selesai
