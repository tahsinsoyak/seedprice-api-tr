
# seedprice-api-tr

Türkiye Tohum Fiyatlarının Fide Deposu sitesi üzerinden çekilmesi için bir api yazılmıştır.

- Bu api sayesinde mobil ve web platformlarında veriler sadece bir link üzerinden çekilebilmektedir.
- Verilere erişim için authentication işlemi yapılmamıştır, herkese açıktır.
- Scrapping için request ve beautifulsoup kullanılmıştır.
- Repo içerisinde scrapper python dosyası bulunmaktadır.
- Scrapper sonucu bir json dosyası oluşmaktadır. Bu json dosyası içerisinde tohum fiyatlarının key value şeklinde saklanması vardır.
- Fast api yapısını kullanarak bu fiyatların çekilmesi için sistem oluşturulmuştur.

