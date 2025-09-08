# Quran MP3 Renamer

A simple Python script to rename Quran MP3 files with their corresponding Surah names.

## 📌 Features
- Works with MP3 files named as `001.mp3` → `114.mp3`.
- Renames files (or copies them into a new folder) as:

  ```
  001_الفاتحة.mp3
  002_البقرة.mp3
  ...
  114_الناس.mp3
  ```

- Keeps the original numbering (`001`, `002`, …).
- Supports all 114 Surahs with correct Arabic names.

## 🚀 Usage

1. Clone this repository:
   ```bash
   git clone https://github.com/prof-abdelrahman/quran-mp3-renamer.git
   cd quran-mp3-renamer
   ```

2. Put your MP3 files (`001.mp3` → `114.mp3`) into a folder, e.g. `input/`.

3. Edit the script `rename_quran_mp3.py` and set:
   ```python
   source_folder = "input", example: "/home/prof_abdelrahman/Quran/Abdulbasit_Abdulsamad_(MP3_Quran)"
   destination_folder = "output", example: "/home/prof_abdelrahman/Quran/Abdulbasit_Abdulsamad_(MP3_Quran)/New_Folder"
   ```

4. Run the script:
   ```bash
   python rename_quran_mp3.py
   ```

5. Your renamed MP3 files will be available in the `output/` folder.

## 🗂 Example Output
```
001_الفاتحة.mp3
002_البقرة.mp3
003_آل عمران.mp3
...
114_الناس.mp3
```

## ⚖️ License
This project is released under the **MIT License**.  
You are free to use, modify, and share it.
