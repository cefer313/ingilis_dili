# Kung Fu Panda — videodakı bütün sözlər

Mənbə video: [How Po Became the Dragon Warrior — Full Story](https://youtu.be/LtXp4RGuq_o) (17:48).

- **`kung-fu-panda-sozler.pdf`** — 328 fərqli söz, videoda ilk səsləndikləri ardıcıllıqla: ingiliscə yazılış, Azərbaycan hərfləri ilə tələffüz, tərcümə və videoda neçə dəfə işləndiyi. Cəmi 965 söz.
- **`transcript.txt`** — videonun altyazı mətni (adlardakı altyazı səhvləri düzəldilib: Oogway, Tigress, Po).
- **`make_pdf.py`** — PDF-i yaradan skript. Lüğətdə dəyişiklik etmək üçün skriptdəki `DATA` hissəsini redaktə edib yenidən işə salın:

```bash
python3 make_pdf.py transcript.txt kung-fu-panda-sozler.pdf
```

Lazımdır: Python 3, `reportlab`, DejaVu Sans şrifti.
