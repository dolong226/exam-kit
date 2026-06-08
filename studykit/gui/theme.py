"""
Hằng số màu sắc, font và kích thước dùng chung cho toàn bộ GUI.
Thay đổi tại đây sẽ ảnh hưởng toàn bộ giao diện.
"""

# ── Màu nền ──────────────────────────────────────────────────────────────────
BG_PRIMARY = "#111118"       # Nền chính
BG_SECONDARY = "#16161e"     # Nền thứ cấp (card, panel)
BG_CARD = "#1c1c28"          # Nền card câu hỏi
BG_INPUT = "#111118"         # Nền ô input

# ── Màu chữ ──────────────────────────────────────────────────────────────────
TEXT_PRIMARY = "#e0e0e0"
TEXT_SECONDARY = "#909090"
TEXT_ACCENT = "#e94560"
TEXT_SUCCESS = "#4ecca3"
TEXT_ERROR = "#e94560"
TEXT_WARNING = "#f5a623"

# ── Màu nút ──────────────────────────────────────────────────────────────────
BTN_PRIMARY = "#e94560"
BTN_PRIMARY_HOVER = "#c73652"
BTN_PRIMARY_TEXT = "#ffffff"

BTN_SECONDARY = "#1c1c28"
BTN_SECONDARY_HOVER = "#252535"
BTN_SECONDARY_TEXT = "#e0e0e0"

BTN_SUCCESS = "#4ecca3"
BTN_SUCCESS_TEXT = "#0f3460"

BTN_CHOICE_DEFAULT = "#1c1c28"
BTN_CHOICE_DEFAULT_BORDER = "#2a2a3a"
BTN_CHOICE_HOVER = "#252535"
BTN_CHOICE_SELECTED = "#2a2050"
BTN_CHOICE_CORRECT = "#1a3a2a"
BTN_CHOICE_CORRECT_BORDER = "#4ecca3"
BTN_CHOICE_WRONG = "#3a1a2a"
BTN_CHOICE_WRONG_BORDER = "#e94560"

BTN_NEUTRAL = "#1e1e2e"
BTN_NEUTRAL_HOVER = "#252535"
BTN_NEUTRAL_TEXT = "#e0e0e0"

# ── Màu viền ─────────────────────────────────────────────────────────────────
BORDER_DEFAULT = "#2a2a3a"
BORDER_ACCENT = "#e94560"
BORDER_SUCCESS = "#4ecca3"
BORDER_ERROR = "#e94560"

# ── Font ─────────────────────────────────────────────────────────────────────
FONT_FAMILY = "Segoe UI"

FONT_TITLE = (FONT_FAMILY, 20, "bold")
FONT_SUBTITLE = (FONT_FAMILY, 13)
FONT_HEADING = (FONT_FAMILY, 16, "bold")
FONT_BODY = (FONT_FAMILY, 14)
FONT_BODY_BOLD = (FONT_FAMILY, 14, "bold")
FONT_SMALL = (FONT_FAMILY, 12)
FONT_SMALL_BOLD = (FONT_FAMILY, 12, "bold")
FONT_CHOICE = (FONT_FAMILY, 14)
FONT_MONO = ("Consolas", 13)

# ── Kích thước ───────────────────────────────────────────────────────────────
WINDOW_WIDTH = 900
WINDOW_HEIGHT = 680
WINDOW_MIN_WIDTH = 780
WINDOW_MIN_HEIGHT = 560

PADDING_OUTER = 24
PADDING_INNER = 16
CORNER_RADIUS = 12
BTN_CORNER = 8
BTN_HEIGHT = 44
BTN_HEIGHT_SM = 34

CHOICE_BTN_HEIGHT = 52
PROGRESS_HEIGHT = 6