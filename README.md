
455 / 5.000
## 1. WEB SCRAPING TEST

### Description
Python project to automate the collection of PDF attachments from the ANS (National Health Insurance Agency) portal and compress them into a single ZIP file.

### Functionalities
- Access to the ANS website to update the List of Procedures
- Automatic download of Annexes I and II in PDF format
- Compression of downloaded files into a single ZIP file

### Prerequisites
- Python 3.8+
- Libraries listed in `requirements.txt`

### Installation
```bash
pip install -r requirements.txt
```

### Use
Run the main script:
```bash
python src/main.py
```

### File Structure
```
WebScraping/
├── resources/
│   └── attachment/               # Folder to store downloaded attachments
│   └── zipped_attachments.zip    # Resulting compressed file
├── src/
│   ├── download.py               # Script to download PDFs
│   ├── compress_folder.py        # Script for compaction
│   ├── extract.py                # Script for extraction 
│   └── main.py                   # Main orchestration script
```


## 2. DATA TRANSFORMATION TEST

### Description
Python project to extract tabular data from appendix I of test 1, transform them into CSV format and compress the file

### Functionalities
- Extraction of tables from PDF (Appendix I)
- Transformation to CSV with appropriate structure
- Renaming of columns (OD → Dental Sec., AMB → Outpatient Sec.)
- Compression of the resulting CSV

### Prerequisites
- Python 3.8+
- Libraries listed in `requirements.txt`

###  Installation
```bash
pip install -r requirements.txt
```

### Use
Run the main script:
```bash
python src/main.py
```

### File Structure
```
DataTransTest/
├── resources/
│   ├── Anexo_1.pdf               # PDF source for extraction
│   ├── Teste_Sabrina.csv         # Resulting CSV
│   └── Teste_Sabrina.zip         # Final compressed file
├── src/
│   ├── extract_data.py           # PDF Data Extraction
│   ├── file_csv.py               # Transformation to CSV
│   ├── compress.py               # Result compression
│   └── main.py                   # Main orchestration script
```

## Common Configuration

Creating a virtual environment to run the project
```bash
python -m venv nome_do_ambiente
```