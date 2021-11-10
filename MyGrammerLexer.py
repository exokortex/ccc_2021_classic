# Generated from MyGrammer by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\20")
        buf.write("o\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3")
        buf.write("\3\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3")
        buf.write("\f\5\f^\n\f\3\r\3\r\7\rb\n\r\f\r\16\re\13\r\3\16\6\16")
        buf.write("h\n\16\r\16\16\16i\3\17\3\17\3\17\3\17\2\2\20\3\3\5\4")
        buf.write("\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17")
        buf.write("\35\20\3\2\6\4\2C\\c|\5\2\62;C\\c|\3\2\62;\5\2\13\f\17")
        buf.write("\17\"\"\2q\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2")
        buf.write("\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2")
        buf.write("\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2")
        buf.write("\2\33\3\2\2\2\2\35\3\2\2\2\3\37\3\2\2\2\5%\3\2\2\2\7)")
        buf.write("\3\2\2\2\t-\3\2\2\2\13\61\3\2\2\2\r\66\3\2\2\2\17<\3\2")
        buf.write("\2\2\21C\3\2\2\2\23F\3\2\2\2\25K\3\2\2\2\27]\3\2\2\2\31")
        buf.write("_\3\2\2\2\33g\3\2\2\2\35k\3\2\2\2\37 \7u\2\2 !\7v\2\2")
        buf.write("!\"\7c\2\2\"#\7t\2\2#$\7v\2\2$\4\3\2\2\2%&\7g\2\2&\'\7")
        buf.write("p\2\2\'(\7f\2\2(\6\3\2\2\2)*\7x\2\2*+\7c\2\2+,\7t\2\2")
        buf.write(",\b\3\2\2\2-.\7u\2\2./\7g\2\2/\60\7v\2\2\60\n\3\2\2\2")
        buf.write("\61\62\7e\2\2\62\63\7c\2\2\63\64\7n\2\2\64\65\7n\2\2\65")
        buf.write("\f\3\2\2\2\66\67\7r\2\2\678\7t\2\289\7k\2\29:\7p\2\2:")
        buf.write(";\7v\2\2;\16\3\2\2\2<=\7t\2\2=>\7g\2\2>?\7v\2\2?@\7w\2")
        buf.write("\2@A\7t\2\2AB\7p\2\2B\20\3\2\2\2CD\7k\2\2DE\7h\2\2E\22")
        buf.write("\3\2\2\2FG\7g\2\2GH\7n\2\2HI\7u\2\2IJ\7g\2\2J\24\3\2\2")
        buf.write("\2KL\7r\2\2LM\7q\2\2MN\7u\2\2NO\7v\2\2OP\7r\2\2PQ\7q\2")
        buf.write("\2QR\7p\2\2RS\7g\2\2S\26\3\2\2\2TU\7v\2\2UV\7t\2\2VW\7")
        buf.write("w\2\2W^\7g\2\2XY\7h\2\2YZ\7c\2\2Z[\7n\2\2[\\\7u\2\2\\")
        buf.write("^\7g\2\2]T\3\2\2\2]X\3\2\2\2^\30\3\2\2\2_c\t\2\2\2`b\t")
        buf.write("\3\2\2a`\3\2\2\2be\3\2\2\2ca\3\2\2\2cd\3\2\2\2d\32\3\2")
        buf.write("\2\2ec\3\2\2\2fh\t\4\2\2gf\3\2\2\2hi\3\2\2\2ig\3\2\2\2")
        buf.write("ij\3\2\2\2j\34\3\2\2\2kl\t\5\2\2lm\3\2\2\2mn\b\17\2\2")
        buf.write("n\36\3\2\2\2\6\2]ci\3\b\2\2")
        return buf.getvalue()


class MyGrammerLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    BOOLEAN = 11
    STR = 12
    INT = 13
    WHITESPACE = 14

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'start'", "'end'", "'var'", "'set'", "'call'", "'print'", "'return'", 
            "'if'", "'else'", "'postpone'" ]

    symbolicNames = [ "<INVALID>",
            "BOOLEAN", "STR", "INT", "WHITESPACE" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "BOOLEAN", "STR", "INT", "WHITESPACE" ]

    grammarFileName = "MyGrammer"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


