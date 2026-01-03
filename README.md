# Docs
## Summary
This model is specifically designed to handle the OCR characteristics of Indonesian ID cards (KTP) documents, which are often difficult for standard language models to read:

Font Optimization: Trained using the OCR-A Extended font dataset, which is identical to the NIK printed on the physical card.

Character Accuracy: Successfully reduced the character error rate (BCER) to 0.391%.

Typo Fixing: Minimized classic misinterpretations, such as the number 6 being read as b, or 0 being read as O.

## How to use

-  Make sure the tesseract version is 5
   ```bash
   tesseract --version
    # 5.xx
   ```
- download the trained data
  - wget
    ```bash
    wget https://raw.githubusercontent.com/DjorroDev/tesseract-trained-ktp_nik/main/ktp_nik.traineddata
    ```
  - curl
    ```bash
    curl -LO https://raw.githubusercontent.com/DjorroDev/tesseract-trained-ktp_nik/main/ktp_nik.traineddata
    ```
- place the traineddata to the tesstdata

  Ubuntu/Linux: /usr/share/tesseract-ocr/5/tessdata/

  macOS (Homebrew): /usr/local/Cellar/tesseract/<version>/share/tessdata/

  example (Linux):
  ```bash
  sudo mv ktp_nik.traineddata /usr/share/tesseract-ocr/5/tessdata/
  ```
- verification
  Make sure `ind.traineddata` and `ktp_nik.traineddata` both avaiable
  ```bash
  tesseract --list-langs
  ```
    - download ind.traineddata if not available:
      ```bash
      wget https://github.com/tesseract-ocr/tessdata_best/raw/main/ind.traineddata
      ```


## Upgrade or install tesseract 5
   ```bash
     # Hapus versi lama dan konfigurasi terkait (Opsional tapi disarankan)
     sudo apt purge tesseract-ocr -y
     sudo apt autoremove -y

     # Tambahkan Repositori Tesseract 5
     sudo add-apt-repository ppa:alex-p/tesseract-ocr5 -y
     sudo apt update

     # Install Tesseract 5
     sudo apt install tesseract-ocr
   ```

## Dev mode
  Kalau mau otak atik silahkan bisa ubah juga generate NIK nya pada python file nya. Command train nya lupa tehee~
