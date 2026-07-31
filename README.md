# veri-ekici

HTTP API'lerinden veya yerel JSON dosyalarından veri çekip JSON ya da CSV olarak yazan küçük bir Python CLI aracı.

## Çalıştırma

```bash
python main.py --source config.example.json --output data/output.json
python main.py --source config.example.json --output data/output.csv --format csv
```

Konfigürasyon dosyası yalnızca bir `url` veya `file` alanı içerir. Araç JSON dizi verisini CSV'ye dönüştürebilir.

## Geliştirme

```bash
python -m pip install -r requirements-dev.txt
python -m pytest
```
