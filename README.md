# TRT Telaffuz Sözlük API Server
http://trttelaffuz.com/ adresinde bulunan sözlüğün api versiyonu.

Veriler adreste bulunan arama motoruna gönderilen POST datalardan gelen sayfaların "[Beautifulsoup](https://www.crummy.com/software/BeautifulSoup/)" ile çözümlenmesi sonucunda elde edilmiştir.

Projenin deploy edilmiş şekline https://trtsozluk.herokuapp.com/ adresinden ulaşabilirsiniz.

İki şekilde arama yapılabiliyor:

 1 - Adres sonuna "q" argumanı eklenerek : https://trtsozluk.herokuapp.com/?q=selam
 
 2 - https://trtsozluk.herokuapp.com adresine POST methodu ile "q" argumanına değer göndererek.
 
 ```bash
 curl -X POST -d 'q=selam' https://trtsozluk.herokuapp.com
```