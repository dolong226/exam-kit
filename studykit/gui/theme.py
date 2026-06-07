"""
Hằng số màu sắc, font và kích thước dùng chung cho toàn bộ GUI.
Thay đổi tại đây sẽ ảnh hưởng toàn bộ giao diện.
"""

# ── Màu nền ──────────────────────────────────────────────────────────────────
BG_PRIMARY = "#1a1a2e"       # Nền chính (frame ngoài)
BG_SECONDARY = "#16213e"     # Nền thứ cấp (card, panel)
BG_CARD = "#0f3460"          # Nền card câu hỏi
BG_INPUT = "#1a1a2e"         # Nền ô input

# ── Màu chữ ──────────────────────────────────────────────────────────────────
TEXT_PRIMARY = "#e0e0e0"     # Chữ chính
TEXT_SECONDARY = "#a0a0b0"   # Chữ phụ, hint
TEXT_ACCENT = "#e94560"      # Tiêu đề, accent
TEXT_SUCCESS = "#4ecca3"     # Đúng
TEXT_ERROR = "#e94560"       # Sai
TEXT_WARNING = "#f5a623"     # Cảnh báo

# ── Màu nút ──────────────────────────────────────────────────────────────────
BTN_PRIMARY = "#652a34"          # Nút chính (bắt đầu, tiếp tục)
BTN_PRIMARY_HOVER = "#c73652"
BTN_PRIMARY_TEXT = "#ffffff"

BTN_SECONDARY = "#0f3460"        # Nút phụ
BTN_SECONDARY_HOVER = "#1a4a80"
BTN_SECONDARY_TEXT = "#e0e0e0"

BTN_SUCCESS = "#4ecca3"          # Nút đáp án đúng (highlight)
BTN_SUCCESS_TEXT = "#0f3460"

BTN_CHOICE_DEFAULT = "#16213e"   # Nút phương án chưa chọn
BTN_CHOICE_DEFAULT_BORDER = "#0f3460"
BTN_CHOICE_HOVER = "#1e2d4a"
BTN_CHOICE_SELECTED = "#0f3460"
BTN_CHOICE_CORRECT = "#1a3a2a"   # Nền khi đáp án đúng
BTN_CHOICE_CORRECT_BORDER = "#4ecca3"
BTN_CHOICE_WRONG = "#3a1a2a"     # Nền khi đáp án sai
BTN_CHOICE_WRONG_BORDER = "#e94560"

BTN_NEUTRAL = "#252540"
BTN_NEUTRAL_HOVER = "#303055"
BTN_NEUTRAL_TEXT = "#e0e0e0"

# ── Màu viền ─────────────────────────────────────────────────────────────────
BORDER_DEFAULT = "#0f3460"
BORDER_ACCENT = "#e94560"
BORDER_SUCCESS = "#4ecca3"
BORDER_ERROR = "#e94560"

# ── Font ─────────────────────────────────────────────────────────────────────
FONT_FAMILY = "Segoe UI"          # Windows; fallback tự động trên macOS/Linux

FONT_TITLE = (FONT_FAMILY, 22, "bold")
FONT_SUBTITLE = (FONT_FAMILY, 13)
FONT_HEADING = (FONT_FAMILY, 16, "bold")
FONT_BODY = (FONT_FAMILY, 13)
FONT_BODY_BOLD = (FONT_FAMILY, 13, "bold")
FONT_SMALL = (FONT_FAMILY, 11)
FONT_SMALL_BOLD = (FONT_FAMILY, 11, "bold")
FONT_CHOICE = (FONT_FAMILY, 13)
FONT_MONO = ("Consolas", 12)      # Dùng cho explanation block

# ── Kích thước ───────────────────────────────────────────────────────────────
WINDOW_WIDTH = 900
WINDOW_HEIGHT = 680
WINDOW_MIN_WIDTH = 780
WINDOW_MIN_HEIGHT = 560

PADDING_OUTER = 24   # Padding ngoài cùng của frame
PADDING_INNER = 16   # Padding bên trong card
CORNER_RADIUS = 12
BTN_CORNER = 8
BTN_HEIGHT = 44
BTN_HEIGHT_SM = 34

CHOICE_BTN_HEIGHT = 52   # Chiều cao mỗi nút phương án
PROGRESS_HEIGHT = 6