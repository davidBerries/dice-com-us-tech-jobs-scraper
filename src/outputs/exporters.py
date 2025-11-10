thonimport json
import csv

class DataExporter:
    def __init__(self, output_format):
        self.output_format = output_format

    def export(self, data):
        if self.output_format == 'json':
            self.export_json(data)
        elif self.output_format == 'csv':
            self.export_csv(data)
        else:
            raise ValueError("Unsupported output format")

    def export_json(self, data):
        with open("output.json", "w") as f:
            json.dump(data, f, indent=4)

    def export_csv(self, data):
        with open("output.csv", "w", newline='') as f:
            writer = csv.DictWriter(f, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)