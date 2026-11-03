
import tkinter as tk
from tkinter import ttk

# ---------------- CONFIGURATION ----------------
BG = "#f5f6f8"
WHITE = "#ffffff"
DARK = "#202b3c"
BLUE = "#387ed1"
GREEN = "#26a69a"
RED = "#ef5350"
TEXT = "#444444"
MUTED = "#888888"

root = tk.Tk()
root.title("Kite - Trading Dashboard")
root.geometry("1450x850")
root.configure(bg=BG)
root.minsize(1100, 700)

# ---------------- HEADER ----------------
header = tk.Frame(root, bg=WHITE, height=65)
header.pack(fill="x")
header.pack_propagate(False)

tk.Label(
    header, text="kite",
    font=("Arial", 25, "bold"),
    fg=BLUE, bg=WHITE
).pack(side="left", padx=30)

nav = ["Dashboard", "Orders", "Holdings", "Positions", "Funds"]

for item in nav:
    tk.Label(
        header, text=item,
        font=("Arial", 11),
        fg=TEXT, bg=WHITE
    ).pack(side="left", padx=18)

tk.Label(
    header, text="●  Account",
    font=("Arial", 11),
    fg=BLUE, bg=WHITE
).pack(side="right", padx=30)

# ---------------- MARKET INDICES ----------------
market = tk.Frame(root, bg=WHITE, height=85)
market.pack(fill="x", pady=(2, 12))
market.pack_propagate(False)

indices = [
    ("NIFTY 50", "24,850.20", "+125.40 (0.51%)"),
    ("SENSEX", "81,450.65", "+310.25 (0.38%)"),
    ("BANK NIFTY", "56,120.80", "-85.30 (0.15%)")
]

for name, value, change in indices:
    card = tk.Frame(market, bg=WHITE)
    card.pack(side="left", padx=35, pady=12)

    tk.Label(
        card, text=name, font=("Arial", 10),
        fg=MUTED, bg=WHITE
    ).pack(anchor="w")

    tk.Label(
        card, text=value, font=("Arial", 16, "bold"),
        fg=DARK, bg=WHITE
    ).pack(anchor="w")

    color = RED if "-" in change else GREEN

    tk.Label(
        card, text=change, font=("Arial", 9),
        fg=color, bg=WHITE
    ).pack(anchor="w")

# ---------------- MAIN CONTENT ----------------
main = tk.Frame(root, bg=BG)
main.pack(fill="both", expand=True, padx=20, pady=5)

# ---------------- LEFT WATCHLIST ----------------
left = tk.Frame(main, bg=WHITE, width=280)
left.pack(side="left", fill="y", padx=(0, 15))
left.pack_propagate(False)

tk.Label(
    left, text="Market Watch",
    font=("Arial", 16, "bold"),
    bg=WHITE, fg=DARK
).pack(anchor="w", padx=18, pady=18)

stocks = [
    ("RELIANCE", "1,425.50", "+1.25%"),
    ("TCS", "3,850.20", "+0.85%"),
    ("INFY", "1,520.80", "-0.45%"),
    ("HDFCBANK", "1,680.25", "+0.62%"),
    ("ICICIBANK", "1,240.60", "+1.10%"),
    ("ITC", "420.50", "-0.25%"),
    ("TATAMOTORS", "680.90", "+2.15%"),
    ("SBIN", "815.40", "+0.95%"),
]

for stock, price, change in stocks:
    row = tk.Frame(left, bg=WHITE)
    row.pack(fill="x", padx=15, pady=9)

    color = RED if "-" in change else GREEN

    tk.Label(
        row, text=stock, font=("Arial", 10, "bold"),
        fg=TEXT, bg=WHITE
    ).pack(side="left")

    info = tk.Frame(row, bg=WHITE)
    info.pack(side="right")

    tk.Label(
        info, text=price, font=("Arial", 10),
        fg=TEXT, bg=WHITE
    ).pack(anchor="e")

    tk.Label(
        info, text=change, font=("Arial", 9),
        fg=color, bg=WHITE
    ).pack(anchor="e")

    ttk.Separator(left).pack(fill="x", padx=12)

# ---------------- RIGHT DASHBOARD ----------------
right = tk.Frame(main, bg=BG)
right.pack(side="left", fill="both", expand=True)

tk.Label(
    right, text="Dashboard Overview",
    font=("Arial", 21, "bold"),
    fg=DARK, bg=BG
).pack(anchor="w", pady=(0, 15))

# Portfolio cards
cards = tk.Frame(right, bg=BG)
cards.pack(fill="x", pady=5)

portfolio = [
    ("Available Balance", "₹1,50,000", BLUE),
    ("Invested Value", "₹85,000", DARK),
    ("Current Value", "₹92,450", GREEN),
    ("Total P&L", "+₹7,450", GREEN)
]

for title, value, color in portfolio:
    box = tk.Frame(cards, bg=WHITE, padx=15, pady=17)
    box.pack(side="left", fill="both", expand=True, padx=5)

    tk.Label(
        box, text=title,
        font=("Arial", 10), bg=WHITE, fg=MUTED
    ).pack(anchor="w")

    tk.Label(
        box, text=value,
        font=("Arial", 17, "bold"),
        bg=WHITE, fg=color
    ).pack(anchor="w", pady=8)

# ---------------- CHART ----------------
chart_box = tk.Frame(right, bg=WHITE)
chart_box.pack(fill="both", expand=True, pady=15)

tk.Label(
    chart_box, text="NIFTY 50 - Market Performance",
    font=("Arial", 14, "bold"),
    bg=WHITE, fg=DARK
).pack(anchor="w", padx=20, pady=15)

chart = tk.Canvas(
    chart_box, bg=WHITE,
    highlightthickness=0, height=230
)
chart.pack(fill="both", expand=True, padx=15, pady=10)

def draw_chart(event=None):
    chart.delete("all")

    w = chart.winfo_width()
    h = chart.winfo_height()

    if w < 50 or h < 50:
        return

    # Grid lines
    for i in range(1, 5):
        y = i * h / 5
        chart.create_line(
            35, y, w - 15, y,
            fill="#eeeeee", dash=(3, 4)
        )

    prices = [
        90, 105, 98, 120, 115, 130, 125,
        145, 138, 155, 148, 165, 158, 175,
        168, 190, 180, 200, 195, 215, 205
    ]

    points = []

    for i, value in enumerate(prices):
        x = 35 + i * (w - 60) / (len(prices) - 1)
        y = h - 20 - (value - 80) * (h - 45) / 150
        points.extend([x, y])

    chart.create_line(
        *points, fill=GREEN,
        width=3, smooth=True
    )

    chart.create_text(
        45, 15, text="Market trend (illustrative)",
        fill=MUTED, anchor="w",
        font=("Arial", 9)
    )

chart.bind("<Configure>", draw_chart)

# ---------------- HOLDINGS ----------------
holdings = tk.Frame(right, bg=WHITE)
holdings.pack(fill="x", pady=5)

tk.Label(
    holdings, text="My Holdings",
    font=("Arial", 14, "bold"),
    bg=WHITE, fg=DARK
).pack(anchor="w", padx=18, pady=12)

columns = ("Stock", "Quantity", "Avg. Price", "LTP", "P&L")

table = ttk.Treeview(
    holdings, columns=columns,
    show="headings", height=4
)

for col in columns:
    table.heading(col, text=col)
    table.column(col, anchor="center", width=120)

table.pack(fill="x", padx=10, pady=10)

holding_data = [
    ("RELIANCE", 10, "₹1,350", "₹1,425", "+₹750"),
    ("TCS", 5, "₹3,700", "₹3,850", "+₹750"),
    ("INFY", 15, "₹1,550", "₹1,520", "-₹450"),
    ("SBIN", 20, "₹780", "₹815", "+₹700")
]

for item in holding_data:
    table.insert("", "end", values=item)

# ---------------- FOOTER ----------------
footer = tk.Frame(root, bg=DARK, height=35)
footer.pack(side="bottom", fill="x")

tk.Label(
    footer,
    text="Kite Trading Dashboard | Demo Interface | Market data is simulated",
    font=("Arial", 9),
    fg=WHITE, bg=DARK
).pack(pady=8)

root.mainloop()
