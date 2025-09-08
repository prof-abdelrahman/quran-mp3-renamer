import os
import shutil

# --- settings ---
source_folder = "path/to/your/folder"       # folder where your mp3 files exist
destination_folder = "path/to/new/folder"   # folder where you want renamed copies

# list of surah names in order (001 to 114)
surah_names = [
    "الفاتحة","البقرة","آل عمران","النساء","المائدة","الأنعام","الأعراف","الأنفال","التوبة","يونس",
    "هود","يوسف","الرعد","إبراهيم","الحجر","النحل","الإسراء","الكهف","مريم","طه",
    "الأنبياء","الحج","المؤمنون","النور","الفرقان","الشعراء","النمل","القصص","العنكبوت","الروم",
    "لقمان","السجدة","الأحزاب","سبإ","فاطر","يس","الصافات","ص","الزمر","غافر",
    "فصلت","الشورى","الزخرف","الدخان","الجاثية","الأحقاف","محمد","الفتح","الحجرات","ق",
    "الذاريات","الطور","النجم","القمر","الرحمن","الواقعة","الحديد","المجادلة","الحشر","الممتحنة",
    "الصف","الجمعة","المنافقون","التغابن","الطلاق","التحريم","الملك","القلم","الحاقة","المعارج",
    "نوح","الجن","المزمل","المدثر","القيامة","الإنسان","المرسلات","النبإ","النازعات","عبس",
    "التكوير","الإنفطار","المطففين","الإنشقاق","البروج","الطارق","الأعلى","الغاشية","الفجر","البلد",
    "الشمس","الليل","الضحى","الشرح","التين","العلق","القدر","البينة","الزلزلة","العاديات",
    "القارعة","التكاثر","العصر","الهمزة","الفيل","قريش","الماعون","الكوثر","الكافرون","النصر",
    "المسد","الإخلاص","الفلق","الناس"
]

# make destination folder if not exists
os.makedirs(destination_folder, exist_ok=True)

# loop through 001.mp3 → 114.mp3
for i, surah in enumerate(surah_names, start=1):
    filename = f"{i:03}.mp3"  # 001.mp3, 002.mp3, ...
    src_path = os.path.join(source_folder, filename)
    if os.path.exists(src_path):
        new_filename = f"{i:03}_{surah}.mp3"
        dest_path = os.path.join(destination_folder, new_filename)
        shutil.copy2(src_path, dest_path)  # copy with metadata
        print(f"Copied: {filename} -> {new_filename}")
    else:
        print(f"Missing: {filename}")
