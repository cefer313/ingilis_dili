import re
import sys
from collections import Counter

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

TRANSCRIPT, OUT = sys.argv[1], sys.argv[2]

# söz | tələffüz (Azərbaycan hərfləri ilə) | tərcümə (videodakı mənasına görə)
DATA = """
i'm|aym|mən ...am (I am)
a|ə|bir (artikl)
coconut|koukənat|kokos
warrior|woriər|döyüşçü
me|mi|mən, məni, mənə
too|tu|də, həm də
hurry|həri|tələs
come|kam|gəl, gəlmək
on|on|üstündə; "come on" — haydı, gəl
how|hau|necə
are|ar|-san, -sınız (to be)
you|yu|sən, siz; səni, sizi
almost|olmoust|az qala
there|ðer|orada
what|wat|nə
no|nou|yox
oh|ou|oh (nida)
sorry|sari|bağışla, üzr istəyirəm
po|pou|Po (ad)
we'll|wil|biz ...acağıq (we will)
bring|brinq|gətirmək
back|bek|geri
souvenir|suvənir|suvenir, xatirə hədiyyəsi
i'll|ayl|mən ...acağam (I will)
it|it|o (əşya), bu
is|iz|-dır, -dir
an|ən|bir (saitdən əvvəl artikl)
historic|histarik|tarixi
day|dey|gün
isn't|izənt|deyilmi
master|mestər|ustad, usta
oogway|uqwey|Uqvey (ad)
yes|yes|bəli
and|end|və
one|wan|bir; burada "elə bir (gün)"
i|ay|mən
feared|fird|qorxurdum
would|wud|-ardı (şərt forması)
not|nat|yox, deyil
live|liv|yaşamaq
to|tu|-a, -ə; üçün
see|si|görmək
your|yor|sənin, sizin
students|stuudənts|tələbələr, şagirdlər
ready|redi|hazır
now|nau|indi
know|nou|bilmək
this|ðis|bu
old|ould|köhnə; qoca
friend|frend|dost
whomever|humevər|kimi (seçsəm), hər kim
choose|çuz|seçmək
will|wil|-acaq, -əcək
only|ounli|yalnız
peace|pis|sülh, əmin-amanlıq
the|ðə|müəyyənlik artikli (tərcümə olunmur)
valley|veli|vadi
but|bat|amma, lakin
also|olsou|həmçinin
let|let|qoy, icazə ver
tournament|törnəmənt|turnir, yarış
begin|bigin|başlamaq
yeah|yeə|hə
wait|weyt|gözlə
coming|kaminq|gəlirəm
hey|hey|hey
open|oupən|açmaq
door|dor|qapı
in|in|içində, içəri
citizens|sitizənz|vətəndaşlar, sakinlər
of|av|-ın, -in (yiyəlik)
my|may|mənim
great|greyt|böyük, əla
honor|anər|şərəf
present|prizent|təqdim etmək
tigress|tayqris|Tayqris (ad; dişi pələng)
viper|vaypər|Vayper (ad; gürzə ilan)
crane|kreyn|Kreyn (ad; durna)
monkey|manki|Manki (ad; meymun)
mantis|mentis|Mentis (ad; peyğəmbərdevəsi)
furious|fyuriəs|qəzəbli; "Furious Five" — Qorxunc Beşlik
five|fayv|beş
warriors|woriərz|döyüşçülər
prepare|pripér|hazırlaşın
peeky|piki|anlaşılmaz nida (altyazı xətası ola bilər)
ho|hou|ho (nida)
for|for|üçün
battle|betl|döyüş
woo|wu|vuu (sevinc nidası)
thousand|θauzənd|min
tons|tanz|tonlar
fire|fayər|od, atəş
wa|wa|vay (nida)
look|luk|bax
at|et|-a, -ə (istiqamət)
that|ðet|o, həmin; ki
get|get|almaq, çatmaq; "get out" — çəkil
out|aut|bayıra, çölə
way|wey|yol
ow|au|ay! (ağrı nidası)
finally|faynəli|nəhayət
believe|biliv|inanmaq
have|hev|var; köməkçi feil
seen|sin|görmüş (see — III forma)
anything|eniθinq|heç nə, hər hansı şey
yet|yet|hələ; amma
face|feys|qarşılaşmaq, üz-üzə gəlmək
iron|ayərn|dəmir
ax|eks|balta ("Iron Ax" — Dəmir Balta)
his|hiz|onun (kişi)
blades|bleydz|tiyələr, bıçaqlar
death|deθ|ölüm
sense|sens|hiss etmək
dragon|dreqən|əjdaha
among|əmanq|arasında
us|as|biz, bizi, bizə
huh|hə|hı? (təəccüb)
doing|duinq|edirsən
does|daz|edir (köməkçi feil)
like|layk|kimi; sevmək
stop|stap|dayan
going|qouinq|gedirəm
don't|dount|etmə; -mıram
understand|andərstend|başa düşmək
had|hed|var idi; görmüşdün
noodle|nudl|əriştə
dream|drim|yuxu, arzu; yuxu görmək
lied|layd|yalan dedim
about|əbaut|haqqında
noodles|nudlz|əriştələr
dad|ded|ata
love|lav|sevmək
kung|kunq|kunq ("kung fu" ilə birlikdə)
fu|fu|fu; "kung fu" — kunq-fu (döyüş sənəti)
son|san|oğul
let's|lets|gəlin ...ək
work|wörk|iş
okay|oukey|yaxşı, oldu
uh-oh|a-ou|oy-oy (pis bir şey olanda)
what's|wats|nə (var)
where|wer|harada, haraya
uh|ı|ıı (tərəddüd)
pointing|poyntinq|barmaqla göstərmək
just|cast|sadəcə
wanted|wantid|istədim
who|hu|kim
was|waz|idi
interesting|intrestinq|maraqlı
him|him|onu, ona (kişi)
universe|yunivörs|kainat
has|hez|(köməkçi feil) -dir; var
brought|brot|gətirdi
told|tould|dedi
flabby|flebi|sallaq, piylənmiş
panda|pendə|panda
can't|kent|bacarmaz, ola bilməz
possibly|pasəbli|heç cür (inkarda); ola bilsin
be|bi|olmaq
answer|ensər|cavab
our|auər|bizim
problem|prabləm|problem
were|wör|idin, idiniz
point|poynt|göstərmək
thing|θinq|şey
fell|fel|yıxıldı, düşdü
front|frant|ön; "in front of" — qarşısında
her|hör|onun, onu (qadın)
accident|eksidənt|təsadüf; qəza
accidents|eksidənts|təsadüflər
forgive|fərgiv|bağışla
we|wi|biz
failed|feyld|uğursuz olduq; ümidini doğrultmadıq
if|if|əgər
quit|kwit|atmaq, əl çəkmək
by|bay|-a qədər
morning|morninq|səhər
then|ðen|onda, sonra
cannot|kenat|bacarmazsan, olmaz
leave|liv|tərk etmək, getmək
real|riəl|əsl, həqiqi
never|nevər|heç vaxt
quits|kwits|əl çəkir
watch|waç|bax, izlə
am|em|-am (I am)
supposed|səpouzd|gərək, guya; "how am I supposed to" — mən necə ...malıyam
beat|bit|məğlub etmək; qabaqlamaq
tai|tay|Tay ("Tai Lung" — ad)
lung|lanq|Lunq ("Tai Lung" — ad)
even|ivən|hətta
stairs|sterz|pilləkən
because|bikoz|çünki
believed|bilivd|inandın
from|fram|-dan, -dən
first|först|ilk, birinci
moment|moumənt|an
got|gat|gəldim (got here); oldu
here|hir|bura, burada
you've|yuv|sən ...misən (you have)
been|bin|olmuş (be — III forma)
trying|trayinq|çalışırsan
rid|rid|"get rid of" — yaxa qurtarmaq
ask|esk|xahiş etmək; soruşmaq
trust|trast|etibar etmək, inanmaq
as|ez|kimi
mine|mayn|mənimki
you're|yur|sən ...sən (you are)
why|way|niyə
didn't|didənt|etmədin
knew|nu|bilirdin
stayed|steyd|qaldım
every|evri|hər
time|taym|vaxt; dəfə
threw|θru|atdın
brick|brik|kərpic
head|hed|baş
or|or|və ya
said|sed|dedin
smelled|smeld|iy verirdim
hurt|hört|ağrıtdı, incitdi
could|kud|bilərdi
more|mor|daha çox
than|ðen|-dan (müqayisə)
did|did|etdi
life|layf|həyat
being|biinq|olmaq (olmaq halı)
thought|θot|düşündüm
anyone|eniwan|kimsə
change|çeync|dəyişmək
make|meyk|etmək
greatest|greytist|ən böyük
teacher|tiçər|müəllim
all|ol|bütün
china|çaynə|Çin
can|ken|bacarmaq, bilmək
turn|törn|çevirmək
into|intu|-a, -ə (çevirmək)
right|rayt|düz; "right now" — elə indi
takes|teyks|(vaxt) çəkir
hundred|handrid|yüz
years|yirz|illər
that's|ðets|bu ...dır (that is)
trained|treynd|məşq etdirdin, hazırladın
try|tray|çalışmaq
we're|wir|biz ...ıq (we are)
with|wið|ilə
happened|hepənd|baş verdi
eat|it|yemək
when|wen|nə vaxt; -anda, -əndə
upset|apset|əsəbi, kədərli
need|nid|ehtiyac
explain|ikspleyn|izah etmək
might|mayt|ola bilərdi
he|hi|o (kişi)
hides|haydz|gizlədir
almond|almənd|badam
cookies|kukiz|peçenyelər
top|tap|ən üst
shelf|şelf|rəf
tell|tel|demək, söyləmək
disgust|disgast|iyrəndirmək
mean|min|nəzərdə tutmaq
up|ap|yuxarı
guess|ges|güman etmək
getting|getinq|götürürdüm
cookie|kuki|peçenye
10|ten|on
ft|fit|fut (≈30 sm; feet)
off|of|-dan yuxarı, ayrı
ground|graund|yer
done|dan|etmiş (do — III forma)
perfect|pörfikt|mükəmməl
split|split|şpaqat
mystical|mistikəl|mistik, sirli
fu-y|fui|kunq-fu tərzli (zarafatla)
least|list|ən az; "at least" — heç olmasa
dragged|dreqd|sürüdün, gətirdin
bath|beθ|çimmək, vanna
do|du|etmək
wash|waş|yumaq
pits|pits|qoltuqlar (armpits)
pool|pul|hovuz
sacred|seykrid|müqəddəs
tears|tirz|göz yaşları
pools|pulz|hovuzlar
unraveled|anrevəld|açdı (sirri)
mysteries|mistəriz|sirlər
harmony|harməni|harmoniya, ahəng
focus|foukəs|diqqət, fokus; diqqəti cəmləmək
birthplace|börθpleys|doğulduğu yer
want|want|istəmək
learn|lörn|öyrənmək
cry|kray|ağlamaq
concentrate|kansəntreyt|diqqəti cəmləmək
stink|stink|çox pis olmaq (danışıq); iy vermək
perhaps|pərheps|bəlkə
fault|folt|günah
train|treyn|məşq etdirmək
through|θru|vasitəsilə; "get through" — başa salmaq
cuz|kaz|çünki (because — qısa)
hungry|hanqri|ac
good|gud|yaxşı
may|mey|bilərsən (icazə)
cut|kat|kəs
where's|werz|haradadır
looking|lukinq|baxırsan
think|θink|düşünmək
fool|ful|axmaq
none|nan|heç biri
heard|hörd|eşitdim
sky|skay|səma
ball|bol|kürə, top
he's|hiz|o ...dır (he is)
unlike|anlayk|bənzəməyən, fərqli
world|wörld|dünya
ever|evər|heç vaxt (indiyədək)
so|sou|deməli
name|neym|ad
worthy|wörði|layiqli
opponent|əpounənt|rəqib
legendary|lecəndəri|əfsanəvi
help|help|kömək et
go|gou|get
thinking|θinkinq|düşünürdüm
shifu|şifu|Şifu (ad)
taught|tot|öyrətdi
well|wel|yaxşı
teach|tiç|öyrətmək
everything|evriθinq|hər şey
"""

entries = {}
for line in DATA.strip().splitlines():
    w, p, t = line.split('|')
    entries[w] = (p, t)

text = open(TRANSCRIPT).read()
toks = [w.lower() for w in re.findall(r"[A-Za-z]+(?:['’-][A-Za-z]+)*|\d+", text)]
counts = Counter(toks)
order = list(dict.fromkeys(toks))
missing = [w for w in order if w not in entries]
extra = [w for w in entries if w not in counts]
assert not missing and not extra, (missing, extra)

# ─── PDF ─────────────────────────────────────────────────────
pdfmetrics.registerFont(TTFont('DV', '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'))
pdfmetrics.registerFont(TTFont('DVB', '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'))
INK, MUTED, ACCENT, SOFT = colors.HexColor('#1B2333'), colors.HexColor('#5D6779'), colors.HexColor('#2563C9'), colors.HexColor('#EEF3FB')

def st(**k):
    base = dict(fontName='DV', fontSize=9.5, leading=12.5, textColor=INK)
    base.update(k)
    return ParagraphStyle('s', **base)
title = st(fontName='DVB', fontSize=20, leading=25)
sub = st(fontSize=10.5, leading=15, textColor=MUTED)
h2 = st(fontName='DVB', fontSize=12, leading=16, spaceBefore=6, spaceAfter=4)
cell = st()
cellb = st(fontName='DVB')
cellp = st(textColor=ACCENT)
head = st(fontName='DVB', fontSize=8.5, textColor=colors.white)
num = st(fontSize=8.5, textColor=MUTED, alignment=TA_CENTER)

def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont('DV', 8)
    canvas.setFillColor(MUTED)
    canvas.drawString(18 * mm, 10 * mm, 'Kung Fu Panda — videodakı bütün sözlər')
    canvas.drawRightString(A4[0] - 18 * mm, 10 * mm, f'Səhifə {doc.page}')
    canvas.restoreState()

doc = SimpleDocTemplate(OUT, pagesize=A4, leftMargin=18 * mm, rightMargin=18 * mm, topMargin=16 * mm, bottomMargin=18 * mm,
                        title='Kung Fu Panda — sözlər, tələffüz və tərcümə', author='')
story = [
    Paragraph('Kung Fu Panda — videodakı bütün sözlər', title),
    Spacer(1, 4),
    Paragraph('“How Po Became the Dragon Warrior — Full Story” (17:48). Sözlər videoda ilk dəfə səsləndikləri ardıcıllıqla verilib. '
              f'Videoda cəmi {len(toks)} söz işlənir, onlardan {len(order)}-i fərqli sözdür. Təkrarlanan söz yalnız ilk dəfə yazılıb; '
              '“Dəfə” sütunu sözün videoda neçə dəfə işləndiyini göstərir. Tərcümələr sözün videodakı mənasına uyğundur.', sub),
    Spacer(1, 8),
    Paragraph('Tələffüz işarələri', h2),
]
legend = [
    ['θ', 'dilin ucu dişlər arasında, səssiz “s” kimi: thing → θinq, thousand → θauzənd'],
    ['ð', 'dilin ucu dişlər arasında, səsli “z” kimi: the → ðə, this → ðis'],
    ['w', 'dodaqlar dairəvi, qısa “u” kimi: what → wat, warrior → woriər'],
    ['r', 'dil damağa toxunmadan, yumşaq: master → mestər'],
    ['e', 'ingiliscə “a” çox vaxt geniş “e” kimidir: panda → pendə, back → bek'],
]
lt = Table([[Paragraph(a, cellb), Paragraph(b, cell)] for a, b in legend], colWidths=[12 * mm, 162 * mm])
lt.setStyle(TableStyle([('VALIGN', (0, 0), (-1, -1), 'TOP'), ('BOTTOMPADDING', (0, 0), (-1, -1), 3), ('TOPPADDING', (0, 0), (-1, -1), 2)]))
story += [lt, Spacer(1, 6),
          Paragraph('Qeyd: YouTube altyazısındakı bir neçə səhv düzəldilib (Urguay/Ugay → Oogway, Tigris → Tigress, Paul → Po, mourning → morning). '
                    'Musiqi və səs işarələri ([music], [screaming]) söz sayılmayıb.', sub),
          Spacer(1, 10), Paragraph('Sözlər', h2)]

rows = [[Paragraph('#', head), Paragraph('İngiliscə', head), Paragraph('Tələffüz', head), Paragraph('Tərcümə', head), Paragraph('Dəfə', head)]]
for i, w in enumerate(order, 1):
    p, t = entries[w]
    shown = w.capitalize() if t.endswith(')') and '(ad' in t else w
    if w == 'i' or w.startswith("i'"):
        shown = 'I' + w[1:]
    if w in ('china', 'tai', 'lung'):
        shown = w.capitalize()
    rows.append([Paragraph(str(i), num), Paragraph(shown, cellb), Paragraph(p, cellp), Paragraph(t, cell), Paragraph(str(counts[w]), num)])

tbl = Table(rows, colWidths=[10 * mm, 30 * mm, 30 * mm, 89 * mm, 15 * mm], repeatRows=1)
tbl.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), INK),
    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, SOFT]),
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ('TOPPADDING', (0, 0), (-1, -1), 3.5),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 3.5),
    ('LINEBELOW', (0, 0), (-1, -1), 0.25, colors.HexColor('#DDE3EC')),
]))
story.append(tbl)
doc.build(story, onFirstPage=footer, onLaterPages=footer)
print('OK', len(order), 'words,', len(toks), 'tokens')
