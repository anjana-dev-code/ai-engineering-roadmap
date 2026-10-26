import turtle as t
import math as m
import random as r
import time

# ---------- settings (change these to experiment) ----------
BG = "#050005"        # background colour
FONT = "Segoe UI"     # Windows font with wide language support
SC = 20               # scale: bigger = bigger heart
OY = 40               # shift the heart up/down on screen
WORDS = 110           # how many words around the outline
LAYERS = [1.0, 0.72]  # 1.0 = outer heart, 0.72 = smaller heart inside

PHRASES = [
    "I love you", "Seni seviyorum", "Te amo", "Je t'aime",
    "Ich liebe dich", "Ti amo", "Eu te amo", "Я тебя люблю",
    "사랑해", "愛してる", "我爱你", "मैं तुमसे प्यार करता हूँ",
    "Σ' αγαπώ", "Ik hou van jou", "Jag älskar dig", "Kocham cię",
    "ฉันรักเธอ", "Anh yêu em", "Aku cinta kamu", "Я тебе кохаю",
    "હું તને પ્રેમ કરું છું",   # Gujarati
    "मी तुझ्यावर प्रेम करते",   # Marathi
]

# Word mix: 40% English, 15% Marathi, the rest other languages
ENGLISH_CHANCE = 0.40
MARATHI = [
    "मी तुझ्यावर प्रेम करते",
    "माझं तुझ्यावर प्रेम आहे",
    "तू माझा आहेस",
]
MARATHI_CHANCE = 0.15

# Big message in the middle of the heart
CENTER_TEXT = "I love you"
NAME = ""   # put his name here, e.g. NAME = "Rohan"

# ---------- screen ----------
s = t.Screen()
s.setup(800, 800)
s.bgcolor(BG)
s.title("Love Heart")
s.tracer(0)  # draw manually, so animation stays smooth

pen = t.Turtle()
pen.hideturtle()
pen.penup()

rng = r.Random(11)  # fixed seed = same "random" heart every run

# ---------- font cache ----------
_fonts = {}
def font_for(size):
    if size not in _fonts:
        _fonts[size] = (FONT, size, "bold")
    return _fonts[size]

# ---------- the heart equation ----------
def heart(a):
    x = 16 * m.sin(a) ** 3
    y = (
        13 * m.cos(a)
        - 5 * m.cos(2 * a)
        - 2 * m.cos(3 * a)
        - m.cos(4 * a)
    )
    return x * SC, y * SC + OY

# ---------- one word with a neon glow ----------
def neon_word(text, x, y, size):
    # soft outer glow (bigger + dark red), then the bright core on top
    for colour, extra in (("#5a0010", 3), ("#ff1744", 1), ("#ff8a80", 0)):
        pen.color(colour)
        pen.goto(x, y)
        pen.write(text, align="center", font=font_for(size + extra))

# ---------- draw ----------
for k in LAYERS:
    for i in range(WORDS):
        a = i / WORDS * 2 * m.pi
        x, y = heart(a)
        x, y = x * k, (y - OY) * k + OY
        roll = rng.random()
        if roll < ENGLISH_CHANCE:
            text = "I love you"
        elif roll < ENGLISH_CHANCE + MARATHI_CHANCE:
            text = rng.choice(MARATHI)
        else:
            text = rng.choice(PHRASES)
        size = rng.randint(9, 15)
        neon_word(text, x, y, size)
        if i % 2 == 0:
            s.update()
            time.sleep(0.03)  # words appear one by one

time.sleep(0.5)
neon_word(CENTER_TEXT, 0, OY - 30, 22)
if NAME:
    neon_word(NAME, 0, OY - 75, 18)

s.update()
t.done()