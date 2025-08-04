# veri-ekici

`veri-ekici`, çeşitli kaynaklardan (web siteleri, API’ler, CSV/Excel dosyaları vb.) veri toplayıp işleyerek kolayca kullanılabilir formatlarda (JSON, CSV) çıktılar oluşturan Python tabanlı bir araçtır.

## Özellikler

* 🔍 Belirlediğin hedef URL veya API’den veri çekme
* ⚙️ CSV, JSON veya SQLite formatında kaydetme
* ⏰ Zamanlanmış (cron) çalıştırma desteği
* 🚀 Kolay yapılandırma ve eklenti sistemi

## Başlarken

Aşağıdaki adımları izleyerek projeyi kendi makinenizde çalıştırabilirsiniz.

### Gereksinimler

* Python 3.7 veya üzeri
* `pip` paket yöneticisi

### Kurulum

```bash
# Depoyu kopyala
git clone https://github.com/Furkan074207/veri--ekici.git
cd veri--ekici

# Sanal ortam oluştur (isteğe bağlı)
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Gerekli paketleri yükle
pip install -r requirements.txt
```

## Kullanım

1. `config.yaml` veya `.env` dosyanızı düzenleyin:

   ```yaml
   source:
     - type: "web"
       url: "https://ornek-site.com/veri"
   output:
     format: "json"
     path: "data/output.json"
   ```
2. Ana betiği çalıştırın:

   ```bash
   python main.py --config config.yaml
   ```
3. `data/output.json` veya belirttiğiniz dosya yolunda çıktı dosyasını bulun.

## Yapılandırma (Opsiyonel)

* `--schedule`: Cron formatında zamanlama eklemek için kullanabilirsiniz.
* `--format`: `json`, `csv` veya `sqlite` seçenekleri.

```bash
python main.py --config config.yaml --schedule "0 2 * * *"
```

## Geliştirme ve Katkı

1. Fork’layın ([https://github.com/Furkan074207/veri--ekici/fork](https://github.com/Furkan074207/veri--ekici/fork))
2. Yeni bir branch oluşturun (`git checkout -b feature-yeni-ek`)
3. Değişikliklerinizi commit edin (`git commit -m 'Yeni özellik ek'`)
4. Branch’e push edin (`git push origin feature-yeni-ek`)
5. Pull request açın

## Lisans

Bu proje MIT Lisansı ile lisanslanmıştır. Detaylar için [LICENSE](LICENSE) dosyasına bakın.

---

`veri-ekici` ile veri toplama, dönüştürme ve depolama işlemlerinizin hepsini tek bir araçta birleştirebilirsiniz.
