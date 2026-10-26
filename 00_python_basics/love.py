import turtle as t
import math as m
import random as r
import time

# ================= settings (change these!) =================
FONT = "Arial"          # Mac/Windows safe. Try "Nirmala UI" on Windows for Indian scripts
SIZE = 13               # word size on the heart outline
SC = 22                 # heart scale
OY = 40                 # move heart up/down
NAME = ""               # put his name here, e.g. NAME = "Rohan"
ENGLISH_CHANCE = 0.40   # 40% of outline words are "I love you"
MARATHI_CHANCE = 0.20   # 20% are Marathi
SEED = 11               # change for a different (still clean) arrangement

# short phrases only, so nothing overlaps
OTHER = [
    "Seni seviyorum", "Te amo", "Je t'aime", "Ich liebe dich", "Ti amo",
    "Eu te amo", "Я тебя люблю", "사랑해", "愛してる", "我爱你",
    "मुझे तुमसे प्यार है", "Σ' αγαπώ", "Ik hou van jou", "Jag älskar dig",
    "Kocham cię", "ฉันรักเธอ", "Anh yêu em", "Aku cinta kamu",
    "Я тебе кохаю", "હું તને પ્રેમ કરું છું",
]
MARATHI = ["तू माझा आहेस", "माझं प्रेम", "मी तुझी आहे"]

# messages shown in the middle, one after another
MESSAGES = [
    "You're my life",
    "You're my everything",
    "I choose you, always",
    "Forever yours",
    "I love you",          # this one stays on screen
]
SHOW_SECONDS = 2.2   # time per message
FINAL_SECONDS = 8     # last message beats this long

# ================= screen =================
s = t.Screen()
s.setup(900, 900)
s.bgcolor("#050005")
s.title("Love Heart")
s.tracer(0)

pen = t.Turtle()
pen.hideturtle()
pen.penup()

msg = t.Turtle()   # separate pen so the centre text can be erased
msg.hideturtle()
msg.penup()

rng = r.Random(SEED)

# ================= heart maths =================
def heart(a):
    x = 16 * m.sin(a) ** 3
    y = 13 * m.cos(a) - 5 * m.cos(2 * a) - 2 * m.cos(3 * a) - m.cos(4 * a)
    return x * SC, y * SC + OY

def even_outline(n=300):
    """Points spaced EVENLY along the heart (equal distance apart),
    instead of equal angle (which bunches words up at the tip)."""
    pts = [heart(i / 4000 * 2 * m.pi) for i in range(4001)]
    dist = [0.0]
    for i in range(1, len(pts)):
        dx = pts[i][0] - pts[i - 1][0]
        dy = pts[i][1] - pts[i - 1][1]
        dist.append(dist[-1] + m.hypot(dx, dy))
    out, j = [], 0
    for k in range(n):
        target = dist[-1] * k / n
        while dist[j] < target:
            j += 1
        out.append(pts[j])
    return out

# ================= drawing helpers =================
def write(turtle_obj, text, x, y, size, colour="#ff4d6d", glow="#5a0010"):
    turtle_obj.color(glow)
    turtle_obj.goto(x + 1.5, y - 1.5)
    turtle_obj.write(text, align="center", font=(FONT, size, "bold"))
    turtle_obj.color(colour)
    turtle_obj.goto(x, y)
    turtle_obj.write(text, align="center", font=(FONT, size, "bold"))

def draw_heart(p, x, y, size, colour="#ff1744"):
    """A filled red heart (our own 'emoji'), centred on x, y."""
    k = size / 16
    p.color(colour)
    p.penup()
    first = True
    for i in range(61):
        a = i / 60 * 2 * m.pi
        hx = 16 * m.sin(a) ** 3
        hy = 13 * m.cos(a) - 5 * m.cos(2 * a) - 2 * m.cos(3 * a) - m.cos(4 * a)
        px, py = x + hx * k, y + (hy + 2.5) * k
        p.goto(px, py)
        if first:
            p.pendown()
            p.begin_fill()
            first = False
    p.end_fill()
    p.penup()

def box(text, x, y, size):
    """Rough rectangle a word will occupy (for overlap checking)."""
    w = len(text) * size * 0.72 + 8
    h = size * 1.9
    return (x - w / 2, y - 4, x + w / 2, y - 4 + h)

def overlaps(b, placed):
    for p in placed:
        if not (b[2] < p[0] or b[0] > p[2] or b[3] < p[1] or b[1] > p[3]):
            return True
    return False

def pick():
    roll = rng.random()
    if roll < ENGLISH_CHANCE:
        return "I love you"
    if roll < ENGLISH_CHANCE + MARATHI_CHANCE:
        return rng.choice(MARATHI)
    return rng.choice(OTHER)

# ================= 1) heart outline, no overlaps =================
placed = []
count = 0
for (x, y) in even_outline():
    text = pick()
    b = box(text, x, y, SIZE)
    if overlaps(b, placed):
        continue            # skip this spot, try the next one
    placed.append(b)
    write(pen, text, x, y, SIZE)
    count += 1
    s.update()
    time.sleep(0.04)        # words appear one by one

time.sleep(0.6)

# ================= 2) messages in the middle =================
cx, cy = 0, OY - 40
for i, text in enumerate(MESSAGES):
    last = (i == len(MESSAGES) - 1)
    frames = int((FINAL_SECONDS if last else SHOW_SECONDS) / 0.1)
    for f in range(frames):
        beat = 22 + 7 * max(0, m.sin(f * 0.9))   # the heart "beats"
        msg.clear()
        draw_heart(msg, cx, cy + 90, beat)
        write(msg, text, cx, cy, 30, colour="#ffd1dc", glow="#8a0020")
        if NAME:
            write(msg, NAME, cx, cy - 55, 18, colour="#ffd1dc", glow="#5a0010")
        s.update()
        time.sleep(0.1)

t.done()