"""
Hằng số màu sắc, font và kích thước dùng chung cho toàn bộ GUI.
Thiết kế mới: tối giản, typography làm trọng tâm, contrast cao.
"""

# ── Màu nền ──────────────────────────────────────────────────────────────────
BG_PRIMARY   = "#0f0f13"      # Nền chính
BG_SECONDARY = "#16161c"      # Panel, sidebar
BG_CARD      = "#1c1c24"      # Card, list item
BG_INPUT     = "#1c1c24"      # Ô input
BG_HOVER     = "#22222e"      # Hover state
BG_SELECTED  = "#1e1e30"      # Item được chọn

# ── Màu chữ ──────────────────────────────────────────────────────────────────
TEXT_PRIMARY   = "#e8e8ec"
TEXT_SECONDARY = "#7a7a90"
TEXT_TERTIARY  = "#46465a"
TEXT_ACCENT    = "#7c6aff"    # Tím nhạt — accent chính
TEXT_SUCCESS   = "#34c98a"
TEXT_ERROR     = "#f05d72"
TEXT_WARNING   = "#f5a623"

# ── Màu nút ──────────────────────────────────────────────────────────────────
BTN_PRIMARY         = "#7c6aff"
BTN_PRIMARY_HOVER   = "#6857e0"
BTN_PRIMARY_TEXT    = "#ffffff"

BTN_SECONDARY       = "#1c1c24"
BTN_SECONDARY_HOVER = "#22222e"
BTN_SECONDARY_TEXT  = "#e8e8ec"

BTN_NEUTRAL         = "#1c1c24"
BTN_NEUTRAL_HOVER   = "#22222e"
BTN_NEUTRAL_TEXT    = "#7a7a90"

BTN_SUCCESS       = "#1a3a2a"
BTN_SUCCESS_TEXT  = "#34c98a"

BTN_DANGER        = "#3a1a22"
BTN_DANGER_HOVER  = "#4a2030"
BTN_DANGER_TEXT   = "#f05d72"

# ── Choice button states ──────────────────────────────────────────────────────
BTN_CHOICE_DEFAULT        = "#1c1c24"
BTN_CHOICE_DEFAULT_BORDER = "#2a2a38"
BTN_CHOICE_HOVER          = "#22222e"
BTN_CHOICE_CORRECT        = "#0e2a1e"
BTN_CHOICE_CORRECT_BORDER = "#34c98a"
BTN_CHOICE_WRONG          = "#2a0e18"
BTN_CHOICE_WRONG_BORDER   = "#f05d72"

# ── Màu viền ─────────────────────────────────────────────────────────────────
BORDER_DEFAULT = "#2a2a38"
BORDER_SUBTLE  = "#1e1e2c"
BORDER_ACCENT  = "#7c6aff"
BORDER_SUCCESS = "#34c98a"
BORDER_ERROR   = "#f05d72"

# ── Mode tag colors ───────────────────────────────────────────────────────────
TAG_MC_BG      = "#1a1a30"
TAG_MC_TEXT    = "#9a8fff"
TAG_ESSAY_BG   = "#2a1e10"
TAG_ESSAY_TEXT = "#f5a623"

# ── Font ─────────────────────────────────────────────────────────────────────
FONT_FAMILY      = "DM Sans"
FONT_FAMILY_MONO = "DM Mono"

FONT_TITLE      = (FONT_FAMILY, 20, "bold")
FONT_SUBTITLE   = (FONT_FAMILY, 13)
FONT_HEADING    = (FONT_FAMILY, 15, "bold")
FONT_BODY       = (FONT_FAMILY, 13)
FONT_BODY_BOLD  = (FONT_FAMILY, 13, "bold")
FONT_SMALL      = (FONT_FAMILY, 12)
FONT_SMALL_BOLD = (FONT_FAMILY, 12, "bold")
FONT_TINY       = (FONT_FAMILY, 11)
FONT_TINY_BOLD  = (FONT_FAMILY, 11, "bold")
FONT_CHOICE     = (FONT_FAMILY, 13)
FONT_MONO       = (FONT_FAMILY_MONO, 12)

# ── Kích thước cửa sổ ────────────────────────────────────────────────────────
WINDOW_WIDTH     = 960
WINDOW_HEIGHT    = 680
WINDOW_MIN_WIDTH = 800
WINDOW_MIN_HEIGHT = 560

# ── Spacing ──────────────────────────────────────────────────────────────────
PADDING_OUTER  = 20
PADDING_INNER  = 14
CORNER_RADIUS  = 10
BTN_CORNER     = 8
BTN_HEIGHT     = 40
BTN_HEIGHT_SM  = 32

CHOICE_BTN_HEIGHT = 44   # chiều cao TỐI THIỂU — sẽ expand nếu text dài
PROGRESS_HEIGHT   = 3

# ── Avatar colors cho môn học ─────────────────────────────────────────────────
AVATAR_COLORS = [
    ("#1a1a38", "#9a8fff"),   # tím
    ("#0e2a1e", "#34c98a"),   # xanh lá
    ("#2a1010", "#f05d72"),   # đỏ
    ("#1a2a10", "#7ec850"),   # xanh lá nhạt
    ("#2a1e10", "#f5a623"),   # cam
    ("#101e2a", "#4ec3f0"),   # xanh dương
    ("#1e102a", "#c97af0"),   # tím hồng
]