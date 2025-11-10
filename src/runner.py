thonimport json
import os
from extractors.dice_parser import DiceParser
from outputs.exporters import DataExporter
from config.settings import load_settings

def run_scraper():
    settings = load_settings('config/settings.example.json')
    parser = DiceParser(settings)
    job_data = parser.scrape_jobs()
    
    exporter = DataExporter(settings['output_format'])
    exporter.export(job_data)

if __name__ == '__main__':
    run_scraper()