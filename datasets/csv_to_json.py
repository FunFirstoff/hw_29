import json
import csv

DATA_ADS = "ad.csv"
JSON_ADS = "ad.json"
DATA_CATEGORIES = "category.csv"
JSON_CATEGORIES = "category.json"


def convert_file(file_path, json_file, model_name):
    result = []
    with open(file_path, "r", encoding="utf-8") as csv_f:
        for row in csv.DictReader(csv_f):
            to_add = {"model": model_name, "pk": int(row["Id"] if "Id" in row else row["id"])}
            if "id" in row:
                del row["id"]
            else:
                del row["id"]
            if 'is_published' in row:
                if row['is_published'] == 'TRUE':
                    row['is_published'] = True
                else:
                    row['is_published'] = False
            if 'price' in row:
                row['price'] = int(row['price'])
            to_add["fields"] = row
            result.append(to_add)
    with open(json_file, "w", encoding="utf-8") as json_f:
        json_f.write(json.dumps(result, ensure_ascii=False))
    return result


convert_file(DATA_CATEGORIES, JSON_CATEGORIES, 'ads.category')
convert_file(DATA_ADS, JSON_ADS, 'ads.ad')
