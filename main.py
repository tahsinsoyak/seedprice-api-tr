import fastapi as _fastapi
import json
from typing import Optional
from fastapi import Query


app = _fastapi.FastAPI()


with open('tohumfiyatlari.json','r') as f:
    fiyatlar = json.load(f)

@app.get("/")
def root():
    return fiyatlar


#tüm ürünler ve arama için
@app.get('/tohumsearch',status_code=200)
def search_urun(name: Optional[str] = Query(None, title="Name",description="Aranacak Ürün Giriniz.")):
    if name is None:
        return {"Aradığınız Ürün Bulunamadı"}
    else:
        people2 = [p for p in fiyatlar if name.lower() in p ['urunismi'].lower()]
        return people2

@app.get('/all',status_code=200)
def butun_urunler():
    return fiyatlar


@app.get('/marul',status_code=200)
def ankara_urunler(name: Optional[str] = Query(None, title="Name",description="Aranacak Ürün Giriniz.")):
    if name is None:
        tumankara = [p for p in fiyatlar if 'Marul'.lower() in p ['urunismi'].lower()]
        return tumankara
    else:
        tumankara = [p for p in fiyatlar if 'Marul'.lower() in p ['urunismi'].lower()]
        urun = [p for p in tumankara if name.lower() in p ['urunismi'].lower()]
        return urun

@app.get('/biber',status_code=200)
def ankara_urunler(name: Optional[str] = Query(None, title="Name",description="Aranacak Ürün Giriniz.")):
    if name is None:
        tumankara = [p for p in fiyatlar if 'biber'.lower() in p ['urunismi'].lower()]
        return tumankara
    else:
        tumankara = [p for p in fiyatlar if 'biber'.lower() in p ['urunismi'].lower()]
        urun = [p for p in tumankara if name.lower() in p ['urunismi'].lower()]
        return urun

@app.get('/domates',status_code=200)
def ankara_urunler(name: Optional[str] = Query(None, title="Name",description="Aranacak Ürün Giriniz.")):
    if name is None:
        tumankara = [p for p in fiyatlar if 'domates'.lower() in p ['urunismi'].lower()]
        return tumankara
    else:
        tumankara = [p for p in fiyatlar if 'domates'.lower() in p ['urunismi'].lower()]
        urun = [p for p in tumankara if name.lower() in p ['urunismi'].lower()]
        return urun


@app.get('/cicek',status_code=200)
def ankara_urunler(name: Optional[str] = Query(None, title="Name",description="Aranacak Ürün Giriniz.")):
    if name is None:
        tumankara = [p for p in fiyatlar if 'çiçe'.lower() in p ['urunismi'].lower()]
        return tumankara
    else:
        tumankara = [p for p in fiyatlar if 'çiçe'.lower() in p ['urunismi'].lower()]
        urun = [p for p in tumankara if name.lower() in p ['urunismi'].lower()]
        return urun

@app.get('/patlican',status_code=200)
def ankara_urunler(name: Optional[str] = Query(None, title="Name",description="Aranacak Ürün Giriniz.")):
    if name is None:
        tumankara = [p for p in fiyatlar if 'patlıcan'.lower() in p ['urunismi'].lower()]
        return tumankara
    else:
        tumankara = [p for p in fiyatlar if 'patlıcan'.lower() in p ['urunismi'].lower()]
        urun = [p for p in tumankara if name.lower() in p ['urunismi'].lower()]
        return urun

@app.get('/salatalik',status_code=200)
def ankara_urunler(name: Optional[str] = Query(None, title="Name",description="Aranacak Ürün Giriniz.")):
    if name is None:
        tumankara = [p for p in fiyatlar if 'salatalık'.lower() in p ['urunismi'].lower()]
        return tumankara
    else:
        tumankara = [p for p in fiyatlar if 'salatalık'.lower() in p ['urunismi'].lower()]
        urun = [p for p in tumankara if name.lower() in p ['urunismi'].lower()]
        return urun


@app.get('/cilek',status_code=200)
def ankara_urunler(name: Optional[str] = Query(None, title="Name",description="Aranacak Ürün Giriniz.")):
    if name is None:
        tumankara = [p for p in fiyatlar if 'çilek'.lower() in p ['urunismi'].lower()]
        return tumankara
    else:
        tumankara = [p for p in fiyatlar if 'çilek'.lower() in p ['urunismi'].lower()]
        urun = [p for p in tumankara if name.lower() in p ['urunismi'].lower()]
        return urun


@app.get('/kabak',status_code=200)
def ankara_urunler(name: Optional[str] = Query(None, title="Name",description="Aranacak Ürün Giriniz.")):
    if name is None:
        tumankara = [p for p in fiyatlar if 'kabak'.lower() in p ['urunismi'].lower()]
        return tumankara
    else:
        tumankara = [p for p in fiyatlar if 'kabak'.lower() in p ['urunismi'].lower()]
        urun = [p for p in tumankara if name.lower() in p ['urunismi'].lower()]
        return urun



@app.get('/cim',status_code=200)
def ankara_urunler(name: Optional[str] = Query(None, title="Name",description="Aranacak Ürün Giriniz.")):
    if name is None:
        tumankara = [p for p in fiyatlar if 'çim'.lower() in p ['urunismi'].lower()]
        return tumankara
    else:
        tumankara = [p for p in fiyatlar if 'çim'.lower() in p ['urunismi'].lower()]
        urun = [p for p in tumankara if name.lower() in p ['urunismi'].lower()]
        return urun


@app.get('/fasulye',status_code=200)
def ankara_urunler(name: Optional[str] = Query(None, title="Name",description="Aranacak Ürün Giriniz.")):
    if name is None:
        tumankara = [p for p in fiyatlar if 'fasulye'.lower() in p ['urunismi'].lower()]
        return tumankara
    else:
        tumankara = [p for p in fiyatlar if 'fasulye'.lower() in p ['urunismi'].lower()]
        urun = [p for p in tumankara if name.lower() in p ['urunismi'].lower()]
        return urun


@app.get('/yonca',status_code=200)
def ankara_urunler(name: Optional[str] = Query(None, title="Name",description="Aranacak Ürün Giriniz.")):
    if name is None:
        tumankara = [p for p in fiyatlar if 'yonca'.lower() in p ['urunismi'].lower()]
        return tumankara
    else:
        tumankara = [p for p in fiyatlar if 'yonca'.lower() in p ['urunismi'].lower()]
        urun = [p for p in tumankara if name.lower() in p ['urunismi'].lower()]
        return urun
    

@app.get('/sogan',status_code=200)
def ankara_urunler(name: Optional[str] = Query(None, title="Name",description="Aranacak Ürün Giriniz.")):
    if name is None:
        tumankara = [p for p in fiyatlar if 'sogan'.lower() in p ['urunismi'].lower()]
        return tumankara
    else:
        tumankara = [p for p in fiyatlar if 'sogan'.lower() in p ['urunismi'].lower()]
        urun = [p for p in tumankara if name.lower() in p ['urunismi'].lower()]
        return urun
    

@app.get('/roka',status_code=200)
def ankara_urunler(name: Optional[str] = Query(None, title="Name",description="Aranacak Ürün Giriniz.")):
    if name is None:
        tumankara = [p for p in fiyatlar if 'roka'.lower() in p ['urunismi'].lower()]
        return tumankara
    else:
        tumankara = [p for p in fiyatlar if 'roka'.lower() in p ['urunismi'].lower()]
        urun = [p for p in tumankara if name.lower() in p ['urunismi'].lower()]
        return urun
    


@app.get('/barbunya',status_code=200)
def ankara_urunler(name: Optional[str] = Query(None, title="Name",description="Aranacak Ürün Giriniz.")):
    if name is None:
        tumankara = [p for p in fiyatlar if 'barbunya'.lower() in p ['urunismi'].lower()]
        return tumankara
    else:
        tumankara = [p for p in fiyatlar if 'barbunya'.lower() in p ['urunismi'].lower()]
        urun = [p for p in tumankara if name.lower() in p ['urunismi'].lower()]
        return urun
    

@app.get('/misir',status_code=200)
def ankara_urunler(name: Optional[str] = Query(None, title="Name",description="Aranacak Ürün Giriniz.")):
    if name is None:
        tumankara = [p for p in fiyatlar if 'mısır'.lower() in p ['urunismi'].lower()]
        return tumankara
    else:
        tumankara = [p for p in fiyatlar if 'mısır'.lower() in p ['urunismi'].lower()]
        urun = [p for p in tumankara if name.lower() in p ['urunismi'].lower()]
        return urun
    

@app.get('/ispanak',status_code=200)
def ankara_urunler(name: Optional[str] = Query(None, title="Name",description="Aranacak Ürün Giriniz.")):
    if name is None:
        tumankara = [p for p in fiyatlar if 'ıspanak'.lower() in p ['urunismi'].lower()]
        return tumankara
    else:
        tumankara = [p for p in fiyatlar if 'ıspanak'.lower() in p ['urunismi'].lower()]
        urun = [p for p in tumankara if name.lower() in p ['urunismi'].lower()]
        return urun
    

@app.get('/bezelye',status_code=200)
def ankara_urunler(name: Optional[str] = Query(None, title="Name",description="Aranacak Ürün Giriniz.")):
    if name is None:
        tumankara = [p for p in fiyatlar if 'bezelye'.lower() in p ['urunismi'].lower()]
        return tumankara
    else:
        tumankara = [p for p in fiyatlar if 'bezelye'.lower() in p ['urunismi'].lower()]
        urun = [p for p in tumankara if name.lower() in p ['urunismi'].lower()]
        return urun