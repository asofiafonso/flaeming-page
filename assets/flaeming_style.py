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


FLAEMING_ORANGE = "#fd971f"
FLAEMING_BLACK = "#000000"
FLAEMING_RED = "#dc143c"
FLAEMING_RED_DARK = "#b22222"
FLAEMING_WHITE = "#ffffff"
FLAEMING_GRAY = "#e0e0da"
FLAEMING_YELLOW = "#ffd700"
FLAEMING_YELLOW_LITE = "#f8ffd9"
FLAEMING_BLUE = "#0000f3"


class FlaemingStyleDark(Style):
    """
    This style mimics the DTx color scheme (dark version)
    """

    background_color = FLAEMING_BLACK
    highlight_color = FLAEMING_RED_DARK

    styles = {
        # No corresponding class for the following:
        Text: FLAEMING_WHITE,  # class:  ''
        Whitespace: "",  # class: 'w'
        Error: f"{FLAEMING_WHITE} bg:{FLAEMING_RED}",  # class: 'err'
        Other: "",  # class 'x'
        Comment: FLAEMING_GRAY,  # class: 'c'
        Comment.Multiline: "",  # class: 'cm'
        Comment.Preproc: "",  # class: 'cp'
        Comment.Single: "",  # class: 'c1'
        Comment.Special: "",  # class: 'cs'
        Keyword: FLAEMING_ORANGE,  # class: 'k'
        Keyword.Constant: "",  # class: 'kc'
        Keyword.Declaration: "",  # class: 'kd'
        Keyword.Namespace: f"bold {FLAEMING_YELLOW_LITE}",  # class: 'kn'
        Keyword.Pseudo: "",  # class: 'kp'
        Keyword.Reserved: "",  # class: 'kr'
        Keyword.Type: "",  # class: 'kt'
        Operator: FLAEMING_WHITE,  # class: 'o'
        Operator.Word: "",  # class: 'ow' - like keywords
        Punctuation: FLAEMING_WHITE,  # class: 'p'
        Name: FLAEMING_WHITE,  # class: 'n'
        Name.Attribute: FLAEMING_YELLOW_LITE,  # class: 'na' - to be revised
        Name.Builtin: FLAEMING_RED,  # class: 'nb'
        Name.Builtin.Pseudo: "",  # class: 'bp'
        Name.Class: f"bold {FLAEMING_YELLOW_LITE}",  # class: 'nc' - to be revised
        Name.Constant: FLAEMING_YELLOW_LITE,  # class: 'no' - to be revised
        Name.Decorator: "italic #aa2d95",  # class: 'nd' - to be revised
        Name.Entity: "",  # class: 'ni'
        Name.Exception: FLAEMING_YELLOW_LITE,  # class: 'ne'
        Name.Function: f"bold {FLAEMING_YELLOW}",  # class: 'nf'
        Name.Property: "",  # class: 'py'
        Name.Label: "",  # class: 'nl'
        Name.Namespace: "",  # class: 'nn' - to be revised
        Name.Other: "#a6e22e",  # class: 'nx'
        Name.Tag: "#f92672",  # class: 'nt' - like a keyword
        Name.Variable: "",  # class: 'nv' - to be revised
        Name.Variable.Class: "",  # class: 'vc' - to be revised
        Name.Variable.Global: "",  # class: 'vg' - to be revised
        Name.Variable.Instance: "",  # class: 'vi' - to be revised
        Number: FLAEMING_BLUE,  # class: 'm'
        Number.Float: "",  # class: 'mf'
        Number.Hex: "",  # class: 'mh'
        Number.Integer: "",  # class: 'mi'
        Number.Integer.Long: "",  # class: 'il'
        Number.Oct: "",  # class: 'mo'
        Literal: FLAEMING_BLUE,  # class: 'l'
        Literal.Date: FLAEMING_BLUE,  # class: 'ld'
        String: FLAEMING_YELLOW,  # class: 's'
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


# class FlaemingStyleLight(Style):
#     """
#     This style mimics the DTx color scheme (light version)
#     """

#     background_color = CELFOCUS_WHITE
#     highlight_color = CELFOCUS_RED

#     styles = {
#         # No corresponding class for the following:
#         Text: CELFOCUS_BLACK,  # class:  ''
#         Whitespace: "",  # class: 'w'
#         Error: f"{CELFOCUS_WHITE} bg:{CELFOCUS_RED}",  # class: 'err'
#         Other: "",  # class 'x'
#         Comment: CELFOCUS_GRAY,  # class: 'c'
#         Comment.Multiline: "",  # class: 'cm'
#         Comment.Preproc: "",  # class: 'cp'
#         Comment.Single: "",  # class: 'c1'
#         Comment.Special: "",  # class: 'cs'
#         Keyword: CELFOCUS_ORANGE,  # class: 'k'
#         Keyword.Constant: "",  # class: 'kc'
#         Keyword.Declaration: "",  # class: 'kd'
#         Keyword.Namespace: f"bold {CELFOCUS_RED}",  # class: 'kn'
#         Keyword.Pseudo: "",  # class: 'kp'
#         Keyword.Reserved: "",  # class: 'kr'
#         Keyword.Type: "",  # class: 'kt'
#         Operator: CELFOCUS_BLACK,  # class: 'o'
#         Operator.Word: "",  # class: 'ow' - like keywords
#         Punctuation: CELFOCUS_DARKERGRAY,  # class: 'p'
#         Name: CELFOCUS_DARKERED,  # class: 'n'
#         Name.Attribute: CELFOCUS_GREEN,  # class: 'na' - to be revised
#         Name.Builtin: CELFOCUS_PURPLE,  # class: 'nb'
#         Name.Builtin.Pseudo: "",  # class: 'bp'
#         Name.Class: f"bold {CELFOCUS_DARKBLUE}",  # class: 'nc' - to be revised
#         Name.Constant: CELFOCUS_PURPLE,  # class: 'no' - to be revised
#         Name.Decorator: "italic #aa2d95",  # class: 'nd' - to be revised
#         Name.Entity: "",  # class: 'ni'
#         Name.Exception: CELFOCUS_DARKRED,  # class: 'ne'
#         Name.Function: f"bold {CELFOCUS_DARKGREEN}",  # class: 'nf'
#         Name.Property: "",  # class: 'py'
#         Name.Label: "",  # class: 'nl'
#         Name.Namespace: "",  # class: 'nn' - to be revised
#         Name.Other: "#a6e22e",  # class: 'nx'
#         Name.Tag: "#f92672",  # class: 'nt' - like a keyword
#         Name.Variable: "",  # class: 'nv' - to be revised
#         Name.Variable.Class: "",  # class: 'vc' - to be revised
#         Name.Variable.Global: "",  # class: 'vg' - to be revised
#         Name.Variable.Instance: "",  # class: 'vi' - to be revised
#         Number: CELFOCUS_ORANGE,  # class: 'm'
#         Number.Float: "",  # class: 'mf'
#         Number.Hex: "",  # class: 'mh'
#         Number.Integer: "",  # class: 'mi'
#         Number.Integer.Long: "",  # class: 'il'
#         Number.Oct: "",  # class: 'mo'
#         Literal: CELFOCUS_PINK,  # class: 'l'
#         Literal.Date: "#e6db74",  # class: 'ld'
#         String: CELFOCUS_BLUE,  # class: 's'
#         String.Backtick: "",  # class: 'sb'
#         String.Char: "",  # class: 'sc'
#         String.Doc: "",  # class: 'sd' - like a comment
#         String.Double: "",  # class: 's2'
#         String.Escape: "#fefdde",  # class: 'se'
#         String.Heredoc: "",  # class: 'sh'
#         String.Interpol: "",  # class: 'si'
#         String.Other: "",  # class: 'sx'
#         String.Regex: "",  # class: 'sr'
#         String.Single: "",  # class: 's1'
#         String.Symbol: "",  # class: 'ss'
#         Generic: "",  # class: 'g'
#         Generic.Deleted: "#f92672",  # class: 'gd',
#         Generic.Emph: "italic",  # class: 'ge'
#         Generic.Error: "",  # class: 'gr'
#         Generic.Heading: "",  # class: 'gh'
#         Generic.Inserted: "#a6e22e",  # class: 'gi'
#         Generic.Output: "#66d9ef",  # class: 'go'
#         Generic.Prompt: "bold #f92672",  # class: 'gp'
#         Generic.Strong: "bold",  # class: 'gs'
#         Generic.Subheading: "#75715e",  # class: 'gu'
#         Generic.Traceback: "",  # class: 'gt'
#     }
