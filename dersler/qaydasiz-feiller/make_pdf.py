"""Qaydasız feillər — uşaqlar üçün sadə dərslik PDF-i.

İstifadə:  python3 make_pdf.py qaydasiz-feiller.pdf
"""
import sys

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (KeepTogether, PageBreak, Paragraph, SimpleDocTemplate,
                                Spacer, Table, TableStyle)

OUT = sys.argv[1] if len(sys.argv) > 1 else "qaydasiz-feiller.pdf"

FD = "/usr/share/fonts/truetype/dejavu/"
pdfmetrics.registerFont(TTFont("DV", FD + "DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("DVB", FD + "DejaVuSans-Bold.ttf"))

# ---------------------------------------------------------------- məlumat
# V1 | V2 | V3 | tələffüz (V1 – V2 – V3) | tərcümə
GROUPS = [
    {
        "title": "1-ci qrup: «Üçü də eyni» 🙂",
        "short": "Üçü də eyni",
        "tip": "Bu feillər ən asanıdır — heç dəyişmirlər! "
               "Bir dəfə öyrəndin, üç formanı da bildin. "
               "Diqqət: <b>read</b> eyni yazılır, amma keçmişdə «red» oxunur.",
        "color": "#2E9E5B", "light": "#E3F5EA",
        "rows": """
cut|cut|cut|kat – kat – kat|kəsmək
put|put|put|put – put – put|qoymaq
let|let|let|let – let – let|icazə vermək
hit|hit|hit|hit – hit – hit|vurmaq
shut|shut|shut|şat – şat – şat|bağlamaq (qapını)
cost|cost|cost|kost – kost – kost|qiyməti olmaq
hurt|hurt|hurt|hərt – hərt – hərt|ağrıtmaq, incitmək
read|read|read|rid – red – red|oxumaq (kitab)
""",
    },
    {
        "title": "2-ci qrup: «Gedib geri qayıdan»",
        "short": "1-ci = 3-cü",
        "tip": "Bunlarda 1-ci və 3-cü forma eynidir, yalnız ortadakı dəyişir: "
               "<b>come – came – come</b>. Sanki feil gedib yenə evinə qayıdır.",
        "color": "#E67E22", "light": "#FDEBD8",
        "rows": """
come|came|come|kam – keym – kam|gəlmək
become|became|become|bikam – bikeym – bikam|olmaq (çevrilmək)
run|ran|run|ran – ren – ran|qaçmaq
""",
    },
    {
        "title": "3-cü qrup: «Əkiz qardaşlar»",
        "short": "2-ci = 3-cü",
        "tip": "Bunlarda 2-ci və 3-cü forma əkiz kimi eynidir. Ən böyük qrup budur! "
               "Kiçik ailələrə böl: <b>buy, bring, think, teach, catch, fight</b> — "
               "hamısı «-ought / -aught» (oxunuşu «ot») ilə bitir.",
        "color": "#2F80ED", "light": "#E2EEFD",
        "rows": """
buy|bought|bought|bay – bot – bot|almaq (satın)
bring|brought|brought|brinq – brot – brot|gətirmək
think|thought|thought|θinq – θot – θot|düşünmək
teach|taught|taught|tiç – tot – tot|öyrətmək
catch|caught|caught|keç – kot – kot|tutmaq
fight|fought|fought|fayt – fot – fot|döyüşmək, dalaşmaq
sleep|slept|slept|slip – slept – slept|yatmaq
keep|kept|kept|kip – kept – kept|saxlamaq
feel|felt|felt|fil – felt – felt|hiss etmək
meet|met|met|mit – met – met|görüşmək, tanış olmaq
leave|left|left|liv – left – left|getmək, tərk etmək
send|sent|sent|send – sent – sent|göndərmək
spend|spent|spent|spend – spent – spent|xərcləmək (pul, vaxt)
build|built|built|bild – bilt – bilt|tikmək
have|had|had|hev – hed – hed|sahib olmaq, var olmaq
make|made|made|meyk – meyd – meyd|düzəltmək, etmək
say|said|said|sey – sed – sed|demək
pay|paid|paid|pey – peyd – peyd|ödəmək
tell|told|told|tel – tould – tould|danışmaq, söyləmək
sell|sold|sold|sel – sould – sould|satmaq
hear|heard|heard|hir – hərd – hərd|eşitmək
find|found|found|faynd – faund – faund|tapmaq
sit|sat|sat|sit – set – set|oturmaq
stand|stood|stood|stend – stud – stud|durmaq (ayaq üstə)
understand|understood|understood|andərstend – andərstud – andərstud|başa düşmək
lose|lost|lost|luz – lost – lost|itirmək
win|won|won|win – wan – wan|qalib gəlmək, udmaq
get|got|got|qet – qat – qat|almaq, əldə etmək
""",
    },
    {
        "title": "4-cü qrup: «Mahnı qrupu: i – a – u» 🎵",
        "short": "i – a – u",
        "tip": "Bu feillərdə yalnız bir hərf dəyişir: <b>i → a → u</b>. "
               "Mahnı kimi oxu: «sing – sang – sung, swim – swam – swum!»",
        "color": "#9B51E0", "light": "#F1E6FC",
        "rows": """
begin|began|begun|biqin – biqen – biqan|başlamaq
drink|drank|drunk|drink – drenk – drank|içmək
sing|sang|sung|sinq – senq – sanq|mahnı oxumaq
swim|swam|swum|swim – swem – swam|üzmək
ring|rang|rung|rinq – renq – ranq|zəng çalmaq
""",
    },
    {
        "title": "5-ci qrup: «Hamısı fərqli» — ən nadinclər",
        "short": "Hamısı fərqli",
        "tip": "Bunlarda üç forma da fərqlidir. Amma çoxunun 3-cü forması "
               "<b>-n</b> ilə bitir: eaten, taken, given, known... "
               "Bunları hər gün 3–4 dənə öyrən.",
        "color": "#EB5757", "light": "#FDE4E4",
        "rows": """
be|was / were|been|bi – waz / wər – bin|olmaq
do|did|done|du – did – dan|etmək
go|went|gone|qou – went – qon|getmək
see|saw|seen|si – so – sin|görmək
eat|ate|eaten|it – eyt – itən|yemək
take|took|taken|teyk – tuk – teykən|götürmək, almaq
give|gave|given|qiv – qeyv – qivən|vermək
write|wrote|written|rayt – rout – ritən|yazmaq
speak|spoke|spoken|spik – spouk – spoukən|danışmaq
break|broke|broken|breyk – brouk – broukən|sındırmaq
wake|woke|woken|weyk – wouk – woukən|oyanmaq
choose|chose|chosen|çuz – çouz – çouzən|seçmək
drive|drove|driven|drayv – drouv – drivən|(maşın) sürmək
ride|rode|ridden|rayd – roud – ridən|minmək (velosiped, at)
know|knew|known|nou – nu – noun|bilmək
grow|grew|grown|qrou – qru – qroun|böyümək
throw|threw|thrown|θrou – θru – θroun|atmaq
fly|flew|flown|flay – flu – floun|uçmaq
draw|drew|drawn|dro – dru – dron|(şəkil) çəkmək
wear|wore|worn|wer – wor – worn|geyinmək
fall|fell|fallen|fol – fel – folən|yıxılmaq, düşmək
forget|forgot|forgotten|fərqet – fərqat – fərqatən|unutmaq
""",
    },
]
for g in GROUPS:
    g["rows"] = [l.split("|") for l in g["rows"].strip().splitlines()]
    g["title"] = g["title"].replace(" 🙂", "").replace(" 🎵", "")  # emoji şriftdə yoxdur

# Çalışmalarda işlənən sözlər (lüğət)
VOCAB = """
yesterday|yestərdey|dünən
last week|lest wik|keçən həftə
school|skul|məktəb
friend|frend|dost
teacher|tiçər|müəllim
mother|maðər|ana
ball|bol|top
apple|epl|alma
water|wotər|su
milk|milk|süd
cake|keyk|tort
song|sonq|mahnı
picture|pikçər|şəkil
letter|letər|məktub
window|windou|pəncərə
book|buk|kitab
bird|bərd|quş
bike|bayk|velosiped
homework|houmwərk|ev tapşırığı
morning|morninq|səhər
""".strip().splitlines()
VOCAB = [l.split("|") for l in VOCAB]

# Çalışmalar
EX1 = [  # (V1, V2, V3) — None boş qalır
    ("go", None, None), (None, "saw", None), ("eat", None, None),
    (None, None, "bought"), ("swim", None, None), (None, "came", None),
    ("write", None, None), (None, None, "slept"), ("cut", None, None),
    (None, "drank", None),
]
EX1_ANS = [("go", "went", "gone"), ("see", "saw", "seen"), ("eat", "ate", "eaten"),
           ("buy", "bought", "bought"), ("swim", "swam", "swum"), ("come", "came", "come"),
           ("write", "wrote", "written"), ("sleep", "slept", "slept"), ("cut", "cut", "cut"),
           ("drink", "drank", "drunk")]

EX2 = [
    ("Yesterday I ( go / went / gone ) to school.", "went"),
    ("My mother ( make / made / maked ) a cake.", "made"),
    ("We ( see / saw / seen ) a bird in the tree yesterday.", "saw"),
    ("I have ( eat / ate / eaten ) an apple.", "eaten"),
    ("Tom ( drinked / drank / drunk ) milk in the morning.", "drank"),
    ("She has ( write / wrote / written ) a letter.", "written"),
    ("Last week we ( sing / sang / sung ) a song.", "sang"),
    ("I have ( lose / lost / losed ) my ball.", "lost"),
]

EX3 = [
    ("Yesterday I ______ (read) a book.", "read"),
    ("My friend ______ (give) me a picture.", "gave"),
    ("We ______ (swim) in the sea last week.", "swam"),
    ("The teacher ______ (teach) us a new song.", "taught"),
    ("I ______ (break) the window. Sorry!", "broke"),
    ("Ali ______ (ride) his bike yesterday.", "rode"),
    ("I ______ (find) my book under the bed.", "found"),
    ("The bird ______ (fly) away.", "flew"),
]

EX4 = [
    ("I have ______ (do) my homework.", "done"),
    ("She has ______ (go) to school.", "gone"),
    ("We have ______ (buy) a new ball.", "bought"),
    ("Have you ______ (see) my cat?", "seen"),
    ("He has ______ (draw) a picture.", "drawn"),
    ("I have ______ (forget) his name.", "forgotten"),
]

EX5 = [  # hansı qrupdandır?
    ("put", 1), ("think", 3), ("sing", 4), ("run", 2), ("take", 5),
    ("hit", 1), ("know", 5), ("feel", 3), ("ring", 4), ("become", 2),
]

# ---------------------------------------------------------------- üslublar
INK = colors.HexColor("#2B2B3A")
ACC = colors.HexColor("#5B3FD6")
S = lambda name, **kw: ParagraphStyle(name, fontName=kw.pop("font", "DV"),
                                      textColor=kw.pop("color", INK), **kw)
TITLE = S("t", font="DVB", fontSize=30, leading=36, alignment=TA_CENTER, color=ACC)
SUB = S("s", fontSize=13, leading=18, alignment=TA_CENTER, color=colors.HexColor("#555566"))
H1 = S("h1", font="DVB", fontSize=18, leading=23, spaceBefore=4, spaceAfter=6, color=ACC)
H2 = S("h2", font="DVB", fontSize=13.5, leading=18, spaceBefore=6, spaceAfter=4)
BODY = S("b", fontSize=11, leading=16, spaceAfter=4)
BIG = S("big", fontSize=13, leading=20, alignment=TA_CENTER)
CELL = S("c", fontSize=10, leading=13)
CELLB = S("cb", font="DVB", fontSize=10.5, leading=13)
CELLC = S("cc", fontSize=10, leading=13, alignment=TA_CENTER)
HEAD = S("hd", font="DVB", fontSize=10, leading=13, color=colors.white)
HEADC = S("hdc", font="DVB", fontSize=10, leading=13, color=colors.white, alignment=TA_CENTER)
EXS = S("ex", fontSize=11.5, leading=22)

P = Paragraph


def box(content, bg, border, width=180 * mm, pad=8):
    t = Table([[content]], colWidths=[width])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor(bg)),
        ("BOX", (0, 0), (-1, -1), 1.5, colors.HexColor(border)),
        ("ROUNDEDCORNERS", [8, 8, 8, 8]),
        ("LEFTPADDING", (0, 0), (-1, -1), pad), ("RIGHTPADDING", (0, 0), (-1, -1), pad),
        ("TOPPADDING", (0, 0), (-1, -1), pad), ("BOTTOMPADDING", (0, 0), (-1, -1), pad),
    ]))
    return t


def verb_table(rows, color, light, start=1):
    W = [9 * mm, 29 * mm, 29 * mm, 29 * mm, 48 * mm, 36 * mm]
    data = [[P("#", HEADC), P("1-ci forma<br/>(indi)", HEAD), P("2-ci forma<br/>(keçmiş)", HEAD),
             P("3-cü forma<br/>(have/has ilə)", HEAD), P("Tələffüz", HEAD), P("Tərcümə", HEAD)]]
    for i, (v1, v2, v3, pr, tr) in enumerate(rows, start):
        data.append([P(str(i), CELLC), P(v1, CELLB), P(v2, CELLB), P(v3, CELLB),
                     P(pr, CELL), P(tr, CELL)])
    t = Table(data, colWidths=W, repeatRows=1)
    st = [
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor(color)),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#CCCCDD")),
        ("TOPPADDING", (0, 0), (-1, -1), 4), ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ]
    for r in range(1, len(data)):
        if r % 2 == 0:
            st.append(("BACKGROUND", (0, r), (-1, r), colors.HexColor(light)))
    t.setStyle(TableStyle(st))
    return t


def on_page(c, doc):
    c.saveState()
    c.setFillColor(ACC)
    c.rect(0, A4[1] - 8 * mm, A4[0], 8 * mm, fill=1, stroke=0)
    c.setFillColor(colors.white)
    c.setFont("DVB", 9)
    c.drawString(15 * mm, A4[1] - 5.6 * mm, "Qaydasız feillər — Irregular Verbs")
    c.setFillColor(colors.HexColor("#777788"))
    c.setFont("DV", 9)
    c.drawCentredString(A4[0] / 2, 9 * mm, f"— {doc.page} —")
    c.restoreState()


# ---------------------------------------------------------------- məzmun
story = []
total = sum(len(g["rows"]) for g in GROUPS)

# --- Üz qabığı + giriş
story += [Spacer(1, 18 * mm), P("Qaydasız feillər", TITLE),
          P("Irregular Verbs", S("t2", font="DVB", fontSize=20, leading=26,
                                 alignment=TA_CENTER, color=colors.HexColor("#E67E22"))),
          Spacer(1, 4 * mm),
          P(f"Uşaqlar üçün asan əzbərləmə dərsliyi · {total} feil · 5 qrup", SUB),
          Spacer(1, 10 * mm)]

story.append(P("Feil nədir?", H1))
story.append(P("Feil — <b>hərəkət</b> bildirən sözdür: qaçmaq, yemək, oynamaq, getmək. "
               "İngilis dilində hər feilin <b>3 forması</b> var. Bunları üç pilləli nərdivan kimi düşün:", BODY))
steps = Table([[P("<b>1-ci forma</b><br/>indi, hər gün<br/><font color='#2E9E5B'><b>go</b></font><br/>I <b>go</b> to school.<br/><i>Mən məktəbə gedirəm.</i>", CELLC),
                P("<b>2-ci forma</b><br/>keçmiş, dünən<br/><font color='#E67E22'><b>went</b></font><br/>I <b>went</b> to school.<br/><i>Mən məktəbə getdim.</i>", CELLC),
                P("<b>3-cü forma</b><br/>have / has ilə<br/><font color='#EB5757'><b>gone</b></font><br/>She has <b>gone</b> to school.<br/><i>O, məktəbə gedib.</i>", CELLC)]],
              colWidths=[60 * mm] * 3)
steps.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (0, 0), colors.HexColor("#E3F5EA")),
    ("BACKGROUND", (1, 0), (1, 0), colors.HexColor("#FDEBD8")),
    ("BACKGROUND", (2, 0), (2, 0), colors.HexColor("#FDE4E4")),
    ("BOX", (0, 0), (-1, -1), 1, colors.white), ("INNERGRID", (0, 0), (-1, -1), 4, colors.white),
    ("TOPPADDING", (0, 0), (-1, -1), 8), ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
]))
story += [steps, Spacer(1, 5 * mm)]

story.append(P("Qaydalı və qaydasız feillər", H1))
story.append(box(P("😊".replace("😊", "") + "<b>Qaydalı feillər — «tərbiyəli» feillərdir.</b> "
                   "Onlar keçmişdə sadəcə sonuna <b>-ed</b> alırlar:<br/>"
                   "play → play<b>ed</b> (oynadım) &nbsp;·&nbsp; jump → jump<b>ed</b> (tullandım) "
                   "&nbsp;·&nbsp; watch → watch<b>ed</b> (baxdım)", BODY), "#E3F5EA", "#2E9E5B"))
story.append(Spacer(1, 3 * mm))
story.append(box(P("<b>Qaydasız feillər — «nadinc» feillərdir.</b> "
                   "Onlar -ed almırlar, öz istədikləri kimi dəyişirlər:<br/>"
                   "go → <b>went</b> (getdim) &nbsp;·&nbsp; eat → <b>ate</b> (yedim) "
                   "&nbsp;·&nbsp; see → <b>saw</b> (gördüm)<br/>"
                   "Buna görə də onları <b>əzbərləmək</b> lazımdır. Narahat olma — "
                   "aşağıdakı fəndlərlə çox asan olacaq!", BODY), "#FDE4E4", "#EB5757"))
story.append(Spacer(1, 5 * mm))

story.append(P("Tələffüz işarələri", H2))
story.append(P("Tələffüz Azərbaycan hərfləri ilə yazılıb (Amerika ingiliscəsinə yaxın). "
               "Bizim dildə olmayan səslər üçün:", BODY))
sym = Table([[P("<b>θ</b>", CELLC), P("dilin ucu dişlər arasında, səssiz «s» kimi — think → <b>θinq</b>", CELL)],
             [P("<b>ð</b>", CELLC), P("dilin ucu dişlər arasında, səsli «z» kimi — mother → <b>maðər</b>", CELL)],
             [P("<b>w</b>", CELLC), P("dodaqlar dairəvi, qısa «u» kimi — went → <b>went</b>", CELL)]],
            colWidths=[14 * mm, 166 * mm])
sym.setStyle(TableStyle([("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#CCCCDD")),
                         ("BACKGROUND", (0, 0), (0, -1), colors.HexColor("#ECE8FB")),
                         ("VALIGN", (0, 0), (-1, -1), "MIDDLE")]))
story += [sym, PageBreak()]

# --- Necə əzbərləyək
story.append(P("Necə asan əzbərləyək? 7 sehrli fənd", H1))
tips = [
    ("Qruplarla öyrən", "Feillər 5 qrupa bölünüb. Oxşar feillər birlikdə daha tez yadda qalır. "
     "Əvvəl ən asan qrupdan — «Üçü də eyni»dən başla."),
    ("Hər gün 5 feil", "Bir gündə hamısını öyrənmək olmaz. Hər gün yalnız 5 yeni feil götür, "
     "dünənkiləri isə bir dəfə təkrar et. 2–3 həftəyə hamısını biləcəksən!"),
    ("Mahnı kimi oxu", "Feili ucadan, ritmlə, əl çalaraq oxu: «go – went – gone! "
     "see – saw – seen!». Ritm beyində ilişib qalır."),
    ("Bağla və yoxla", "Cədvəldə 2-ci və 3-cü sütunu kağızla örtüb de. Sonra kağızı qaldırıb yoxla. "
     "Səhv etdiyin feilin yanına kiçik nöqtə qoy — sabah onu yenə təkrar et."),
    ("Kartoçka düzəlt", "Kiçik kağızın bir üzünə <b>go</b>, o biri üzünə <b>went – gone</b> yaz. "
     "Kartları qarışdırıb oyna. Ailəndən kimsə ilə yarış da edə bilərsən."),
    ("Özün haqqında cümlə qur", "Hər feillə dünən etdiyin bir işi de: «Yesterday I <b>ate</b> a cake.» "
     "Öz həyatınla bağlı cümlə heç unudulmur."),
    ("Şəklini təsəvvür et", "Feili deyəndə hərəkəti gözünün önünə gətir və ya göstər: "
     "<b>swim – swam – swum</b> deyəndə əllərinlə üzmə hərəkəti et."),
]
for i, (h, t) in enumerate(tips, 1):
    num = Table([[P(f"<font color='white'><b>{i}</b></font>", S(f"n{i}", font="DVB", fontSize=16,
                                                                  leading=20, alignment=TA_CENTER)),
                  P(f"<b>{h}</b><br/>{t}", BODY)]], colWidths=[14 * mm, 166 * mm])
    col = ["#2E9E5B", "#E67E22", "#2F80ED", "#9B51E0", "#EB5757", "#2E9E5B", "#E67E22"][i - 1]
    num.setStyle(TableStyle([("BACKGROUND", (0, 0), (0, 0), colors.HexColor(col)),
                             ("BACKGROUND", (1, 0), (1, 0), colors.HexColor("#F6F5FB")),
                             ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                             ("TOPPADDING", (0, 0), (-1, -1), 6), ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
                             ("LEFTPADDING", (1, 0), (1, 0), 8)]))
    story += [num, Spacer(1, 3 * mm)]

story.append(Spacer(1, 3 * mm))
plan = [[P("<b>Qrup</b>", HEAD), P("<b>Nə xüsusiyyəti var?</b>", HEAD), P("<b>Nümunə</b>", HEAD),
         P("<b>Feil sayı</b>", HEADC)]]
for n, g in enumerate(GROUPS, 1):
    v1, v2, v3 = g["rows"][0][:3]
    plan.append([P(f"<font color='{g['color']}'><b>{n}</b></font>", CELLC), P(g["short"], CELL),
                 P(f"{v1} – {v2} – {v3}", CELLB), P(str(len(g["rows"])), CELLC)])
pt = Table(plan, colWidths=[18 * mm, 62 * mm, 70 * mm, 30 * mm])
pt.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, 0), ACC),
                        ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#CCCCDD")),
                        ("VALIGN", (0, 0), (-1, -1), "MIDDLE")] +
                       [("BACKGROUND", (0, r), (-1, r), colors.HexColor(GROUPS[r - 1]["light"]))
                        for r in range(1, 6)]))
story += [P("Qruplar bir baxışda", H2), pt, PageBreak()]

# --- Qruplar
n = 1
for g in GROUPS:
    story.append(KeepTogether([
        P(f"<font color='{g['color']}'>{g['title']}</font>", H1),
        box(P(g["tip"], BODY), g["light"], g["color"]),
        Spacer(1, 3 * mm),
    ]))
    story.append(verb_table(g["rows"], g["color"], g["light"], n))
    story.append(Spacer(1, 7 * mm))
    n += len(g["rows"])
story.append(PageBreak())

# --- Hamısı bir yerdə (əlifba sırası) — iki sütun
allv = sorted((r for g in GROUPS for r in g["rows"]), key=lambda r: r[0])
story.append(P("Hamısı bir yerdə — əlifba sırası ilə (təkrar üçün)", H1))
story.append(P("Bu səhifəni çap edib divara və ya dəftərinə yapışdıra bilərsən.", BODY))
half = (len(allv) + 1) // 2
SM = S("sm", fontSize=9, leading=11)
SMB = S("smb", font="DVB", fontSize=9, leading=11)
rows = [[P("1-ci", HEAD), P("2-ci", HEAD), P("3-cü", HEAD), "",
         P("1-ci", HEAD), P("2-ci", HEAD), P("3-cü", HEAD)]]
for i in range(half):
    a = allv[i]
    b = allv[i + half] if i + half < len(allv) else None
    rows.append([P(a[0], SMB), P(a[1], SM), P(a[2], SM), "",
                 P(b[0], SMB) if b else "", P(b[1], SM) if b else "", P(b[2], SM) if b else ""])
at = Table(rows, colWidths=[26 * mm, 29 * mm, 28 * mm, 14 * mm, 26 * mm, 29 * mm, 28 * mm], repeatRows=1)
ast = [("BACKGROUND", (0, 0), (2, 0), ACC), ("BACKGROUND", (4, 0), (6, 0), ACC),
       ("GRID", (0, 0), (2, -1), 0.3, colors.HexColor("#CCCCDD")),
       ("GRID", (4, 0), (6, -1), 0.3, colors.HexColor("#CCCCDD")),
       ("TOPPADDING", (0, 0), (-1, -1), 2), ("BOTTOMPADDING", (0, 0), (-1, -1), 2)]
for r in range(2, len(rows), 2):
    ast += [("BACKGROUND", (0, r), (2, r), colors.HexColor("#F1EEFC")),
            ("BACKGROUND", (4, r), (6, r), colors.HexColor("#F1EEFC"))]
at.setStyle(TableStyle(ast))
story += [at, PageBreak()]

# --- Lüğət
story.append(P("Lüğət — çalışmalardakı sözlər", H1))
story.append(P("Çalışmalara başlamazdan əvvəl bu 20 sözü oxu.", BODY))
lv = [[P("#", HEADC), P("İngiliscə", HEAD), P("Tələffüz", HEAD), P("Tərcümə", HEAD)]]
for i, (w, pr, tr) in enumerate(VOCAB, 1):
    lv.append([P(str(i), CELLC), P(w, CELLB), P(pr, CELL), P(tr, CELL)])
lt = Table(lv, colWidths=[12 * mm, 55 * mm, 55 * mm, 58 * mm])
lst = [("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#E67E22")),
       ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#CCCCDD")),
       ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
       ("TOPPADDING", (0, 0), (-1, -1), 5), ("BOTTOMPADDING", (0, 0), (-1, -1), 5)]
lst += [("BACKGROUND", (0, r), (-1, r), colors.HexColor("#FDEBD8")) for r in range(2, len(lv), 2)]
lt.setStyle(TableStyle(lst))
story += [lt, PageBreak()]

# --- Çalışmalar
story.append(P("Çalışmalar", H1))


def ex_head(num, text, col):
    t = Table([[P(f"<font color='white'><b>{num}</b></font>",
                  S(f"e{num}", font="DVB", fontSize=13, leading=16, alignment=TA_CENTER)),
                P(f"<b>{text}</b>", S(f"et{num}", font="DVB", fontSize=12, leading=16))]],
              colWidths=[10 * mm, 170 * mm])
    t.setStyle(TableStyle([("BACKGROUND", (0, 0), (0, 0), colors.HexColor(col)),
                           ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                           ("LEFTPADDING", (1, 0), (1, 0), 6)]))
    return t


BL = "____________"
e1 = [[P("1-ci forma", HEAD), P("2-ci forma", HEAD), P("3-cü forma", HEAD)]]
for v in EX1:
    e1.append([P(x if x else BL, S("e1c", font="DVB" if x else "DV", fontSize=11, leading=15,
                                   alignment=TA_CENTER, color=INK if x else colors.HexColor("#AAAAAA")))
               for x in v])
t1 = Table(e1, colWidths=[50 * mm] * 3)
t1.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#2E9E5B")),
                        ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#CCCCDD")),
                        ("TOPPADDING", (0, 0), (-1, -1), 5), ("BOTTOMPADDING", (0, 0), (-1, -1), 5)]))
story += [ex_head(1, "Cədvəli doldur: boş xanalara feilin başqa formalarını yaz.", "#2E9E5B"),
          Spacer(1, 3 * mm), t1, Spacer(1, 7 * mm)]

story += [ex_head(2, "Düzgün formanın altından xətt çək.", "#E67E22"), Spacer(1, 2 * mm)]
for i, (s, _) in enumerate(EX2, 1):
    story.append(P(f"{i}. {s}", EXS))
story += [Spacer(1, 4 * mm), PageBreak()]

story += [ex_head(3, "Mötərizədəki feili 2-ci formada (keçmiş) yaz.", "#2F80ED"), Spacer(1, 2 * mm)]
for i, (s, _) in enumerate(EX3, 1):
    story.append(P(f"{i}. {s}", EXS))
story.append(Spacer(1, 6 * mm))

story += [ex_head(4, "Mötərizədəki feili 3-cü formada yaz (have / has-dan sonra).", "#9B51E0"),
          Spacer(1, 2 * mm)]
for i, (s, _) in enumerate(EX4, 1):
    story.append(P(f"{i}. {s}", EXS))
story.append(Spacer(1, 6 * mm))

story += [ex_head(5, "Bu feil hansı qrupdandır? Qrupun nömrəsini (1–5) yaz.", "#EB5757"),
          Spacer(1, 3 * mm)]
e5 = [[P(f"<b>{v}</b> → ____", S("e5", fontSize=11.5, leading=16, alignment=TA_CENTER))
       for v, _ in EX5[k:k + 5]] for k in (0, 5)]
t5 = Table(e5, colWidths=[36 * mm] * 5)
t5.setStyle(TableStyle([("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#CCCCDD")),
                        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#FDE4E4")),
                        ("TOPPADDING", (0, 0), (-1, -1), 7), ("BOTTOMPADDING", (0, 0), (-1, -1), 7)]))
story += [t5, Spacer(1, 8 * mm),
          box(P("<b>Bonus:</b> 5 qaydasız feil seç və hər biri ilə dünən etdiyin bir iş haqqında cümlə yaz. "
                "Məsələn: <i>Yesterday I <b>drank</b> milk.</i>", BODY), "#ECE8FB", "#5B3FD6"),
          PageBreak()]

# --- Cavablar
story.append(P("Cavablar", H1))
A = S("a", fontSize=10.5, leading=15)
story.append(P("<b>1.</b> " + " &nbsp;·&nbsp; ".join(f"{a} – {b} – {c}" for a, b, c in EX1_ANS), A))
story.append(Spacer(1, 3 * mm))
story.append(P("<b>2.</b> " + " &nbsp;·&nbsp; ".join(f"{i}) {a}" for i, (_, a) in enumerate(EX2, 1)), A))
story.append(Spacer(1, 3 * mm))
story.append(P("<b>3.</b> " + " &nbsp;·&nbsp; ".join(f"{i}) {a}" for i, (_, a) in enumerate(EX3, 1)), A))
story.append(P("(1-ci cümlədə <b>read</b> yazılır, amma «red» oxunur.)", A))
story.append(Spacer(1, 3 * mm))
story.append(P("<b>4.</b> " + " &nbsp;·&nbsp; ".join(f"{i}) {a}" for i, (_, a) in enumerate(EX4, 1)), A))
story.append(Spacer(1, 3 * mm))
story.append(P("<b>5.</b> " + " &nbsp;·&nbsp; ".join(f"{v} → {g}" for v, g in EX5), A))
story.append(Spacer(1, 10 * mm))
story.append(box(P("<b>Afərin!</b> Hamısını düz yazdınsa — sən artıq qaydasız feillərin ustasısan! "
                   "Səhv etdiyin feilləri kartoçkaya yaz və sabah yenə təkrar et.", BIG),
                 "#E3F5EA", "#2E9E5B"))

doc = SimpleDocTemplate(OUT, pagesize=A4, leftMargin=15 * mm, rightMargin=15 * mm,
                        topMargin=16 * mm, bottomMargin=16 * mm,
                        title="Qaydasız feillər — Irregular Verbs", author="ingilis_dili")
doc.build(story, onFirstPage=on_page, onLaterPages=on_page)
print("OK:", OUT, "feil sayı:", total)
