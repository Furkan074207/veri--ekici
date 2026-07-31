from pathlib import Path
import json
import sys
sys.path.insert(0, str(Path(__file__).parents[1]))

from main import read_source, write_output

def test_file_source_and_csv_output(tmp_path):
    source = tmp_path / "source.json"
    source.write_text(json.dumps([{"name": "Ada", "score": 3}]), encoding="utf-8")
    config = tmp_path / "config.json"
    config.write_text(json.dumps({"file": str(source)}), encoding="utf-8")
    output = tmp_path / "out.csv"
    write_output(read_source(config), output, "csv")
    assert output.read_text(encoding="utf-8").splitlines() == ["name,score", "Ada,3"]
