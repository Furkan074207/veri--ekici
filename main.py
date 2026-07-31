"""JSON kaynaklarını JSON veya CSV olarak dışa aktaran CLI."""
from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from urllib.request import urlopen

def read_source(config_path: str | Path):
    config = json.loads(Path(config_path).read_text(encoding="utf-8"))
    if "file" in config:
        return json.loads(Path(config["file"]).read_text(encoding="utf-8"))
    if "url" in config:
        with urlopen(config["url"], timeout=15) as response:
            return json.load(response)
    raise ValueError("Konfigürasyon 'file' veya 'url' içermelidir.")

def write_output(data, output_path: str | Path, output_format: str) -> None:
    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)
    if output_format == "json":
        output.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
        return
    if not isinstance(data, list) or not all(isinstance(row, dict) for row in data):
        raise ValueError("CSV çıktısı için kaynak, nesnelerden oluşan JSON dizisi olmalıdır.")
    fields = sorted({key for row in data for key in row})
    with output.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(data)

def main() -> None:
    parser = argparse.ArgumentParser(description="Veri çek ve dışa aktar")
    parser.add_argument("--source", required=True, help="JSON konfigürasyon dosyası")
    parser.add_argument("--output", required=True)
    parser.add_argument("--format", choices=("json", "csv"))
    args = parser.parse_args()
    output_format = args.format or Path(args.output).suffix.lstrip(".") or "json"
    write_output(read_source(args.source), args.output, output_format)

if __name__ == "__main__":
    main()
