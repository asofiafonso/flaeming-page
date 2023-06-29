# The name of the Pygments (syntax highlighting) style to use.
from pygments.style import Style
from pygments.token import (
    Comment,
    Error,
    Generic,
    Keyword,
    Literal,
    Name,
    Number,
    Operator,
    Other,
    Punctuation,
    String,
    Text,
    Whitespace,
)


# Colors
CELFOCUS_DARKERGRAY = "#231f20"
CELFOCUS_DARKERED = "#4a0000"
CELFOCUS_RED = "#ee1c25"
CELFOCUS_BROWNRED = "#7a0101"
CELFOCUS_DARKRED = "#b11117"
CELFOCUS_DARKGRAY = "#646466"
CELFOCUS_GRAY = "#949599"
CELFOCUS_LIGHTGRAY = "#c8c9cb"

CELFOCUS_DARKBLUE = "#4b5667"
CELFOCUS_BLUE = "#006775"
CELFOCUS_LIGHTBLUE = "#2496a3"
CELFOCUS_DARKGREEN = "#6b9e83"
CELFOCUS_GREEN = "#a4b06e"
CELFOCUS_LIGHTGREEN = "#e8ebc8"
CELFOCUS_PURPLE = "#9e7eb9"
CELFOCUS_PINK = "#cb9fa5"
CELFOCUS_ORANGE = "#e4a157"
CELFOCUS_WHITE = "#ffffff"
CELFOCUS_BLACK = "#000000"


class FlaemingStyleDark(Style):
    """
    This style mimics the DTx color scheme (dark version)
    """

    background_color = CELFOCUS_DARKERED
    highlight_color = CELFOCUS_LIGHTGREEN

    styles = {
        # No corresponding class for the following:
        Text: CELFOCUS_WHITE,  # class:  ''
        Whitespace: "",  # class: 'w'
        Error: f"{CELFOCUS_WHITE} bg:{CELFOCUS_RED}",  # class: 'err'
        Other: "",  # class 'x'
        Comment: CELFOCUS_RED,  # class: 'c'
        Comment.Multiline: "",  # class: 'cm'
        Comment.Preproc: "",  # class: 'cp'
        Comment.Single: "",  # class: 'c1'
        Comment.Special: "",  # class: 'cs'
        Keyword: CELFOCUS_ORANGE,  # class: 'k'
        Keyword.Constant: "",  # class: 'kc'
        Keyword.Declaration: "",  # class: 'kd'
        Keyword.Namespace: f"bold {CELFOCUS_LIGHTGREEN}",  # class: 'kn'
        Keyword.Pseudo: "",  # class: 'kp'
        Keyword.Reserved: "",  # class: 'kr'
        Keyword.Type: "",  # class: 'kt'
        Operator: CELFOCUS_WHITE,  # class: 'o'
        Operator.Word: "",  # class: 'ow' - like keywords
        Punctuation: CELFOCUS_WHITE,  # class: 'p'
        Name: CELFOCUS_WHITE,  # class: 'n'
        Name.Attribute: CELFOCUS_LIGHTGREEN,  # class: 'na' - to be revised
        Name.Builtin: CELFOCUS_RED,  # class: 'nb'
        Name.Builtin.Pseudo: "",  # class: 'bp'
        Name.Class: f"bold {CELFOCUS_PINK}",  # class: 'nc' - to be revised
        Name.Constant: CELFOCUS_PURPLE,  # class: 'no' - to be revised
        Name.Decorator: "italic #aa2d95",  # class: 'nd' - to be revised
        Name.Entity: "",  # class: 'ni'
        Name.Exception: CELFOCUS_LIGHTGRAY,  # class: 'ne'
        Name.Function: f"bold {CELFOCUS_LIGHTBLUE}",  # class: 'nf'
        Name.Property: "",  # class: 'py'
        Name.Label: "",  # class: 'nl'
        Name.Namespace: "",  # class: 'nn' - to be revised
        Name.Other: "#a6e22e",  # class: 'nx'
        Name.Tag: "#f92672",  # class: 'nt' - like a keyword
        Name.Variable: "",  # class: 'nv' - to be revised
        Name.Variable.Class: "",  # class: 'vc' - to be revised
        Name.Variable.Global: "",  # class: 'vg' - to be revised
        Name.Variable.Instance: "",  # class: 'vi' - to be revised
        Number: CELFOCUS_PINK,  # class: 'm'
        Number.Float: "",  # class: 'mf'
        Number.Hex: "",  # class: 'mh'
        Number.Integer: "",  # class: 'mi'
        Number.Integer.Long: "",  # class: 'il'
        Number.Oct: "",  # class: 'mo'
        Literal: CELFOCUS_GRAY,  # class: 'l'
        Literal.Date: CELFOCUS_PURPLE,  # class: 'ld'
        String: CELFOCUS_LIGHTBLUE,  # class: 's'
        String.Backtick: "",  # class: 'sb'
        String.Char: "",  # class: 'sc'
        String.Doc: "",  # class: 'sd' - like a comment
        String.Double: "",  # class: 's2'
        String.Escape: "#fefdde",  # class: 'se'
        String.Heredoc: "",  # class: 'sh'
        String.Interpol: "",  # class: 'si'
        String.Other: "",  # class: 'sx'
        String.Regex: "",  # class: 'sr'
        String.Single: "",  # class: 's1'
        String.Symbol: "",  # class: 'ss'
        Generic: "",  # class: 'g'
        Generic.Deleted: "#f92672",  # class: 'gd',
        Generic.Emph: "italic",  # class: 'ge'
        Generic.Error: "",  # class: 'gr'
        Generic.Heading: "",  # class: 'gh'
        Generic.Inserted: "#a6e22e",  # class: 'gi'
        Generic.Output: "#66d9ef",  # class: 'go'
        Generic.Prompt: "bold #f92672",  # class: 'gp'
        Generic.Strong: "bold",  # class: 'gs'
        Generic.Subheading: "#75715e",  # class: 'gu'
        Generic.Traceback: "",  # class: 'gt'
    }


class FlaemingStyleLight(Style):
    """
    This style mimics the DTx color scheme (light version)
    """

    background_color = CELFOCUS_WHITE
    highlight_color = CELFOCUS_RED

    styles = {
        # No corresponding class for the following:
        Text: CELFOCUS_BLACK,  # class:  ''
        Whitespace: "",  # class: 'w'
        Error: f"{CELFOCUS_WHITE} bg:{CELFOCUS_RED}",  # class: 'err'
        Other: "",  # class 'x'
        Comment: CELFOCUS_GRAY,  # class: 'c'
        Comment.Multiline: "",  # class: 'cm'
        Comment.Preproc: "",  # class: 'cp'
        Comment.Single: "",  # class: 'c1'
        Comment.Special: "",  # class: 'cs'
        Keyword: CELFOCUS_ORANGE,  # class: 'k'
        Keyword.Constant: "",  # class: 'kc'
        Keyword.Declaration: "",  # class: 'kd'
        Keyword.Namespace: f"bold {CELFOCUS_RED}",  # class: 'kn'
        Keyword.Pseudo: "",  # class: 'kp'
        Keyword.Reserved: "",  # class: 'kr'
        Keyword.Type: "",  # class: 'kt'
        Operator: CELFOCUS_BLACK,  # class: 'o'
        Operator.Word: "",  # class: 'ow' - like keywords
        Punctuation: CELFOCUS_DARKERGRAY,  # class: 'p'
        Name: CELFOCUS_DARKERED,  # class: 'n'
        Name.Attribute: CELFOCUS_GREEN,  # class: 'na' - to be revised
        Name.Builtin: CELFOCUS_PURPLE,  # class: 'nb'
        Name.Builtin.Pseudo: "",  # class: 'bp'
        Name.Class: f"bold {CELFOCUS_DARKBLUE}",  # class: 'nc' - to be revised
        Name.Constant: CELFOCUS_PURPLE,  # class: 'no' - to be revised
        Name.Decorator: "italic #aa2d95",  # class: 'nd' - to be revised
        Name.Entity: "",  # class: 'ni'
        Name.Exception: CELFOCUS_DARKRED,  # class: 'ne'
        Name.Function: f"bold {CELFOCUS_DARKGREEN}",  # class: 'nf'
        Name.Property: "",  # class: 'py'
        Name.Label: "",  # class: 'nl'
        Name.Namespace: "",  # class: 'nn' - to be revised
        Name.Other: "#a6e22e",  # class: 'nx'
        Name.Tag: "#f92672",  # class: 'nt' - like a keyword
        Name.Variable: "",  # class: 'nv' - to be revised
        Name.Variable.Class: "",  # class: 'vc' - to be revised
        Name.Variable.Global: "",  # class: 'vg' - to be revised
        Name.Variable.Instance: "",  # class: 'vi' - to be revised
        Number: CELFOCUS_ORANGE,  # class: 'm'
        Number.Float: "",  # class: 'mf'
        Number.Hex: "",  # class: 'mh'
        Number.Integer: "",  # class: 'mi'
        Number.Integer.Long: "",  # class: 'il'
        Number.Oct: "",  # class: 'mo'
        Literal: CELFOCUS_PINK,  # class: 'l'
        Literal.Date: "#e6db74",  # class: 'ld'
        String: CELFOCUS_BLUE,  # class: 's'
        String.Backtick: "",  # class: 'sb'
        String.Char: "",  # class: 'sc'
        String.Doc: "",  # class: 'sd' - like a comment
        String.Double: "",  # class: 's2'
        String.Escape: "#fefdde",  # class: 'se'
        String.Heredoc: "",  # class: 'sh'
        String.Interpol: "",  # class: 'si'
        String.Other: "",  # class: 'sx'
        String.Regex: "",  # class: 'sr'
        String.Single: "",  # class: 's1'
        String.Symbol: "",  # class: 'ss'
        Generic: "",  # class: 'g'
        Generic.Deleted: "#f92672",  # class: 'gd',
        Generic.Emph: "italic",  # class: 'ge'
        Generic.Error: "",  # class: 'gr'
        Generic.Heading: "",  # class: 'gh'
        Generic.Inserted: "#a6e22e",  # class: 'gi'
        Generic.Output: "#66d9ef",  # class: 'go'
        Generic.Prompt: "bold #f92672",  # class: 'gp'
        Generic.Strong: "bold",  # class: 'gs'
        Generic.Subheading: "#75715e",  # class: 'gu'
        Generic.Traceback: "",  # class: 'gt'
    }
