# Generated from MyGrammer by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\20")
        buf.write("`\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16\t")
        buf.write("\16\3\2\3\2\7\2\37\n\2\f\2\16\2\"\13\2\3\3\3\3\3\3\3\3")
        buf.write("\3\4\3\4\3\4\3\4\5\4,\n\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\5\5\65\n\5\3\6\7\68\n\6\f\6\16\6;\13\6\3\7\7\7>\n\7\f")
        buf.write("\7\16\7A\13\7\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\n\3\n")
        buf.write("\3\n\3\13\3\13\3\13\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3")
        buf.write("\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\2\2\17\2\4\6\b\n\f")
        buf.write("\16\20\22\24\26\30\32\2\2\2^\2\34\3\2\2\2\4#\3\2\2\2\6")
        buf.write("+\3\2\2\2\b\64\3\2\2\2\n9\3\2\2\2\f?\3\2\2\2\16B\3\2\2")
        buf.write("\2\20F\3\2\2\2\22J\3\2\2\2\24M\3\2\2\2\26P\3\2\2\2\30")
        buf.write("S\3\2\2\2\32[\3\2\2\2\34 \7\17\2\2\35\37\5\4\3\2\36\35")
        buf.write("\3\2\2\2\37\"\3\2\2\2 \36\3\2\2\2 !\3\2\2\2!\3\3\2\2\2")
        buf.write("\" \3\2\2\2#$\7\3\2\2$%\5\n\6\2%&\7\4\2\2&\5\3\2\2\2\'")
        buf.write(",\7\r\2\2(,\7\17\2\2),\7\16\2\2*,\5\22\n\2+\'\3\2\2\2")
        buf.write("+(\3\2\2\2+)\3\2\2\2+*\3\2\2\2,\7\3\2\2\2-\65\5\24\13")
        buf.write("\2.\65\5\26\f\2/\65\5\30\r\2\60\65\5\16\b\2\61\65\5\20")
        buf.write("\t\2\62\65\5\32\16\2\63\65\5\22\n\2\64-\3\2\2\2\64.\3")
        buf.write("\2\2\2\64/\3\2\2\2\64\60\3\2\2\2\64\61\3\2\2\2\64\62\3")
        buf.write("\2\2\2\64\63\3\2\2\2\65\t\3\2\2\2\668\5\b\5\2\67\66\3")
        buf.write("\2\2\28;\3\2\2\29\67\3\2\2\29:\3\2\2\2:\13\3\2\2\2;9\3")
        buf.write("\2\2\2<>\5\b\5\2=<\3\2\2\2>A\3\2\2\2?=\3\2\2\2?@\3\2\2")
        buf.write("\2@\r\3\2\2\2A?\3\2\2\2BC\7\5\2\2CD\7\16\2\2DE\5\6\4\2")
        buf.write("E\17\3\2\2\2FG\7\6\2\2GH\7\16\2\2HI\5\6\4\2I\21\3\2\2")
        buf.write("\2JK\7\7\2\2KL\5\6\4\2L\23\3\2\2\2MN\7\b\2\2NO\5\6\4\2")
        buf.write("O\25\3\2\2\2PQ\7\t\2\2QR\5\6\4\2R\27\3\2\2\2ST\7\n\2\2")
        buf.write("TU\5\6\4\2UV\5\n\6\2VW\7\4\2\2WX\7\13\2\2XY\5\n\6\2YZ")
        buf.write("\7\4\2\2Z\31\3\2\2\2[\\\7\f\2\2\\]\5\f\7\2]^\7\4\2\2^")
        buf.write("\33\3\2\2\2\7 +\649?")
        return buf.getvalue()


class MyGrammerParser ( Parser ):

    grammarFileName = "MyGrammer"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'start'", "'end'", "'var'", "'set'", 
                     "'call'", "'print'", "'return'", "'if'", "'else'", 
                     "'postpone'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "BOOLEAN", 
                      "STR", "INT", "WHITESPACE" ]

    RULE_program = 0
    RULE_block = 1
    RULE_value = 2
    RULE_statement = 3
    RULE_statements = 4
    RULE_poststatements = 5
    RULE_vardef = 6
    RULE_varset = 7
    RULE_callst = 8
    RULE_printst = 9
    RULE_ret = 10
    RULE_ifelse = 11
    RULE_postponest = 12

    ruleNames =  [ "program", "block", "value", "statement", "statements", 
                   "poststatements", "vardef", "varset", "callst", "printst", 
                   "ret", "ifelse", "postponest" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    BOOLEAN=11
    STR=12
    INT=13
    WHITESPACE=14

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(MyGrammerParser.INT, 0)

        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyGrammerParser.BlockContext)
            else:
                return self.getTypedRuleContext(MyGrammerParser.BlockContext,i)


        def getRuleIndex(self):
            return MyGrammerParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MyGrammerParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.match(MyGrammerParser.INT)
            self.state = 30
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MyGrammerParser.T__0:
                self.state = 27
                self.block()
                self.state = 32
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statements(self):
            return self.getTypedRuleContext(MyGrammerParser.StatementsContext,0)


        def getRuleIndex(self):
            return MyGrammerParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = MyGrammerParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self.match(MyGrammerParser.T__0)
            self.state = 34
            self.statements()
            self.state = 35
            self.match(MyGrammerParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOLEAN(self):
            return self.getToken(MyGrammerParser.BOOLEAN, 0)

        def INT(self):
            return self.getToken(MyGrammerParser.INT, 0)

        def STR(self):
            return self.getToken(MyGrammerParser.STR, 0)

        def callst(self):
            return self.getTypedRuleContext(MyGrammerParser.CallstContext,0)


        def getRuleIndex(self):
            return MyGrammerParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue" ):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)




    def value(self):

        localctx = MyGrammerParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_value)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MyGrammerParser.BOOLEAN]:
                self.state = 37
                self.match(MyGrammerParser.BOOLEAN)
                pass
            elif token in [MyGrammerParser.INT]:
                self.state = 38
                self.match(MyGrammerParser.INT)
                pass
            elif token in [MyGrammerParser.STR]:
                self.state = 39
                self.match(MyGrammerParser.STR)
                pass
            elif token in [MyGrammerParser.T__4]:
                self.state = 40
                self.callst()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def printst(self):
            return self.getTypedRuleContext(MyGrammerParser.PrintstContext,0)


        def ret(self):
            return self.getTypedRuleContext(MyGrammerParser.RetContext,0)


        def ifelse(self):
            return self.getTypedRuleContext(MyGrammerParser.IfelseContext,0)


        def vardef(self):
            return self.getTypedRuleContext(MyGrammerParser.VardefContext,0)


        def varset(self):
            return self.getTypedRuleContext(MyGrammerParser.VarsetContext,0)


        def postponest(self):
            return self.getTypedRuleContext(MyGrammerParser.PostponestContext,0)


        def callst(self):
            return self.getTypedRuleContext(MyGrammerParser.CallstContext,0)


        def getRuleIndex(self):
            return MyGrammerParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = MyGrammerParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_statement)
        try:
            self.state = 50
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MyGrammerParser.T__5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 43
                self.printst()
                pass
            elif token in [MyGrammerParser.T__6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 44
                self.ret()
                pass
            elif token in [MyGrammerParser.T__7]:
                self.enterOuterAlt(localctx, 3)
                self.state = 45
                self.ifelse()
                pass
            elif token in [MyGrammerParser.T__2]:
                self.enterOuterAlt(localctx, 4)
                self.state = 46
                self.vardef()
                pass
            elif token in [MyGrammerParser.T__3]:
                self.enterOuterAlt(localctx, 5)
                self.state = 47
                self.varset()
                pass
            elif token in [MyGrammerParser.T__9]:
                self.enterOuterAlt(localctx, 6)
                self.state = 48
                self.postponest()
                pass
            elif token in [MyGrammerParser.T__4]:
                self.enterOuterAlt(localctx, 7)
                self.state = 49
                self.callst()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyGrammerParser.StatementContext)
            else:
                return self.getTypedRuleContext(MyGrammerParser.StatementContext,i)


        def getRuleIndex(self):
            return MyGrammerParser.RULE_statements

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatements" ):
                listener.enterStatements(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatements" ):
                listener.exitStatements(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatements" ):
                return visitor.visitStatements(self)
            else:
                return visitor.visitChildren(self)




    def statements(self):

        localctx = MyGrammerParser.StatementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_statements)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MyGrammerParser.T__2) | (1 << MyGrammerParser.T__3) | (1 << MyGrammerParser.T__4) | (1 << MyGrammerParser.T__5) | (1 << MyGrammerParser.T__6) | (1 << MyGrammerParser.T__7) | (1 << MyGrammerParser.T__9))) != 0):
                self.state = 52
                self.statement()
                self.state = 57
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PoststatementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyGrammerParser.StatementContext)
            else:
                return self.getTypedRuleContext(MyGrammerParser.StatementContext,i)


        def getRuleIndex(self):
            return MyGrammerParser.RULE_poststatements

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPoststatements" ):
                listener.enterPoststatements(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPoststatements" ):
                listener.exitPoststatements(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPoststatements" ):
                return visitor.visitPoststatements(self)
            else:
                return visitor.visitChildren(self)




    def poststatements(self):

        localctx = MyGrammerParser.PoststatementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_poststatements)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MyGrammerParser.T__2) | (1 << MyGrammerParser.T__3) | (1 << MyGrammerParser.T__4) | (1 << MyGrammerParser.T__5) | (1 << MyGrammerParser.T__6) | (1 << MyGrammerParser.T__7) | (1 << MyGrammerParser.T__9))) != 0):
                self.state = 58
                self.statement()
                self.state = 63
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Token

        def value(self):
            return self.getTypedRuleContext(MyGrammerParser.ValueContext,0)


        def STR(self):
            return self.getToken(MyGrammerParser.STR, 0)

        def getRuleIndex(self):
            return MyGrammerParser.RULE_vardef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVardef" ):
                listener.enterVardef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVardef" ):
                listener.exitVardef(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardef" ):
                return visitor.visitVardef(self)
            else:
                return visitor.visitChildren(self)




    def vardef(self):

        localctx = MyGrammerParser.VardefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_vardef)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(MyGrammerParser.T__2)
            self.state = 65
            localctx.name = self.match(MyGrammerParser.STR)
            self.state = 66
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarsetContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Token

        def value(self):
            return self.getTypedRuleContext(MyGrammerParser.ValueContext,0)


        def STR(self):
            return self.getToken(MyGrammerParser.STR, 0)

        def getRuleIndex(self):
            return MyGrammerParser.RULE_varset

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarset" ):
                listener.enterVarset(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarset" ):
                listener.exitVarset(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarset" ):
                return visitor.visitVarset(self)
            else:
                return visitor.visitChildren(self)




    def varset(self):

        localctx = MyGrammerParser.VarsetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_varset)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.match(MyGrammerParser.T__3)
            self.state = 69
            localctx.name = self.match(MyGrammerParser.STR)
            self.state = 70
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value(self):
            return self.getTypedRuleContext(MyGrammerParser.ValueContext,0)


        def getRuleIndex(self):
            return MyGrammerParser.RULE_callst

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCallst" ):
                listener.enterCallst(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCallst" ):
                listener.exitCallst(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCallst" ):
                return visitor.visitCallst(self)
            else:
                return visitor.visitChildren(self)




    def callst(self):

        localctx = MyGrammerParser.CallstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_callst)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.match(MyGrammerParser.T__4)
            self.state = 73
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value(self):
            return self.getTypedRuleContext(MyGrammerParser.ValueContext,0)


        def getRuleIndex(self):
            return MyGrammerParser.RULE_printst

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintst" ):
                listener.enterPrintst(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintst" ):
                listener.exitPrintst(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintst" ):
                return visitor.visitPrintst(self)
            else:
                return visitor.visitChildren(self)




    def printst(self):

        localctx = MyGrammerParser.PrintstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_printst)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.match(MyGrammerParser.T__5)
            self.state = 76
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RetContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value(self):
            return self.getTypedRuleContext(MyGrammerParser.ValueContext,0)


        def getRuleIndex(self):
            return MyGrammerParser.RULE_ret

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRet" ):
                listener.enterRet(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRet" ):
                listener.exitRet(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRet" ):
                return visitor.visitRet(self)
            else:
                return visitor.visitChildren(self)




    def ret(self):

        localctx = MyGrammerParser.RetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_ret)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.match(MyGrammerParser.T__6)
            self.state = 79
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfelseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.cond = None # ValueContext
            self.ifpart = None # StatementsContext
            self.elsepart = None # StatementsContext

        def value(self):
            return self.getTypedRuleContext(MyGrammerParser.ValueContext,0)


        def statements(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyGrammerParser.StatementsContext)
            else:
                return self.getTypedRuleContext(MyGrammerParser.StatementsContext,i)


        def getRuleIndex(self):
            return MyGrammerParser.RULE_ifelse

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfelse" ):
                listener.enterIfelse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfelse" ):
                listener.exitIfelse(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfelse" ):
                return visitor.visitIfelse(self)
            else:
                return visitor.visitChildren(self)




    def ifelse(self):

        localctx = MyGrammerParser.IfelseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_ifelse)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.match(MyGrammerParser.T__7)
            self.state = 82
            localctx.cond = self.value()
            self.state = 83
            localctx.ifpart = self.statements()
            self.state = 84
            self.match(MyGrammerParser.T__1)
            self.state = 85
            self.match(MyGrammerParser.T__8)
            self.state = 86
            localctx.elsepart = self.statements()
            self.state = 87
            self.match(MyGrammerParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PostponestContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def poststatements(self):
            return self.getTypedRuleContext(MyGrammerParser.PoststatementsContext,0)


        def getRuleIndex(self):
            return MyGrammerParser.RULE_postponest

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPostponest" ):
                listener.enterPostponest(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPostponest" ):
                listener.exitPostponest(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPostponest" ):
                return visitor.visitPostponest(self)
            else:
                return visitor.visitChildren(self)




    def postponest(self):

        localctx = MyGrammerParser.PostponestContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_postponest)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.match(MyGrammerParser.T__9)
            self.state = 90
            self.poststatements()
            self.state = 91
            self.match(MyGrammerParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





