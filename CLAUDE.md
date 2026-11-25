# İngilis dili — Claude üçün təlimat

Bu repozitoriya ingilis dili üzrə dərs materiallarıdır: lüğətlər, dərsliklər, çalışmalar.
Bu fayldakı qaydalara hər söhbətdə əməl et.

## Ünsiyyət

- Həmişə **Azərbaycan dilində** cavab ver. İngiliscə yalnız öyrədilən söz və cümlələrdə işlənir.
- Sadə, aydın izah et. Texniki terminləri (branch, commit və s.) lazım olmadıqca işlətmə, işlədəndə izah et.
- Bilmədiyin və ya yoxlaya bilmədiyin şeyi açıq de (məs. səsi qulaqla yoxlaya bilməmək). Uydurma.

## Git qaydaları

- Bu repozitoriyada dəyişiklikləri **birbaşa `main` budağına** yaz və göndər (istifadəçinin icazəsi var).
- Hər yeni material əlavə olunanda kök `README.md`-dəki mündəricat cədvəlini yenilə.

## Qovluq quruluşu

- Video lüğətləri: `lugetler/<qısa-ad>/` — içində:
  - hazır PDF,
  - videonun mətni (`transcript.txt`),
  - PDF-i yaradan skript (`make_pdf.py`),
  - qısa `README.md` (mənbə video linki, nə olduğu, necə yenidən yaradılır).
- Dərsliklər: `dersler/<mövzu>/` (eyni prinsip: PDF + mənbə + README).

## Video lüğəti qaydaları (YouTube linkindən)

1. Videonun mətnini (altyazısını) götür.
2. **Bütün sözlər**, videonun əvvəlindən sonuna, **ilk səsləndikləri ardıcıllıqla** yazılır.
   Təkrarlanan söz bir dəfə yazılır; ayrıca **"Dəfə"** sütunu videoda neçə dəfə işləndiyini göstərir.
3. Hər söz üçün sütunlar: **#**, **İngiliscə**, **Tələffüz**, **Tərcümə**, **Dəfə**.
4. **Tələffüz Azərbaycan hərfləri ilə** yazılır (Amerika ingiliscəsinə yaxın). Azərbaycan dilində olmayan səslər üçün:
   - `θ` — dilin ucu dişlər arasında, səssiz "s" kimi (thing → θinq)
   - `ð` — dilin ucu dişlər arasında, səsli "z" kimi (the → ðə)
   - `w` — dodaqlar dairəvi, qısa "u" kimi (what → wat)
   Bu izah PDF-in əvvəlində verilir.
5. **Tərcümə sözün videodakı mənasına görə** verilir (məs. "stink" danışıq dilində "çox pis olmaq").
   Xüsusi adlar "(ad)" kimi qeyd olunur, I / I'm / I'll böyük hərflə yazılır.
6. Altyazıdakı açıq-aydın səhvləri (adlar və s.) düzəlt və PDF-də bunu qeyd et. Musiqi/səs işarələri ([music]) söz sayılmır.
7. Nəticə **PDF** olur: A4, səliqəli rəngli cədvəl, başlıqda video adı, ümumi və fərqli söz sayı, səhifə nömrələri.
   Azərbaycan hərflərini (ə, ı, ş, ç, ğ, ö, ü) və θ, ð işarələrini dəstəkləyən şrift işlət (DejaVu Sans).
8. Hazır PDF-i istifadəçiyə göndər.

## Dərslik qaydaları

- Dərsliklər rəngli, öz dizaynında, A4 PDF olur: qaydaların izahı, **lüğət (~20 söz)**, **çalışmalar** və sonda **cavablar** səhifəsi.
- Yalnız istifadəçinin verdiyi qaydaları yaz; öz tərəfindən yeni qayda əlavə etmə.
- Misalları istifadəçinin yazdığı şəkildə saxla.

## Yeni qaydalar

İstifadəçi yeni qayda və ya üstünlük deyəndə (məs. "bundan sonra belə et"):
1. Onu bu fayla, uyğun bölməyə əlavə et (uyğun bölmə yoxdursa, aşağıdakı siyahıya).
2. Dəyişikliyi dərhal `main`-ə göndər.
3. İstifadəçiyə qısaca hansı qaydanı yadda saxladığını de.

### Əlavə olunmuş qaydalar (tarixlə)

- 2026-11-25 — Bu fayl yaradıldı; yuxarıdakı qaydalar əvvəlki işlərdən toplandı.
