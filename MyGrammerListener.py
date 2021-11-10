# Generated from MyGrammer by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MyGrammerParser import MyGrammerParser
else:
    from MyGrammerParser import MyGrammerParser

# This class defines a complete listener for a parse tree produced by MyGrammerParser.
class MyGrammerListener(ParseTreeListener):

    # Enter a parse tree produced by MyGrammerParser#program.
    def enterProgram(self, ctx:MyGrammerParser.ProgramContext):
        pass

    # Exit a parse tree produced by MyGrammerParser#program.
    def exitProgram(self, ctx:MyGrammerParser.ProgramContext):
        pass


    # Enter a parse tree produced by MyGrammerParser#block.
    def enterBlock(self, ctx:MyGrammerParser.BlockContext):
        pass

    # Exit a parse tree produced by MyGrammerParser#block.
    def exitBlock(self, ctx:MyGrammerParser.BlockContext):
        pass


    # Enter a parse tree produced by MyGrammerParser#value.
    def enterValue(self, ctx:MyGrammerParser.ValueContext):
        pass

    # Exit a parse tree produced by MyGrammerParser#value.
    def exitValue(self, ctx:MyGrammerParser.ValueContext):
        pass


    # Enter a parse tree produced by MyGrammerParser#statement.
    def enterStatement(self, ctx:MyGrammerParser.StatementContext):
        pass

    # Exit a parse tree produced by MyGrammerParser#statement.
    def exitStatement(self, ctx:MyGrammerParser.StatementContext):
        pass


    # Enter a parse tree produced by MyGrammerParser#statements.
    def enterStatements(self, ctx:MyGrammerParser.StatementsContext):
        pass

    # Exit a parse tree produced by MyGrammerParser#statements.
    def exitStatements(self, ctx:MyGrammerParser.StatementsContext):
        pass


    # Enter a parse tree produced by MyGrammerParser#poststatements.
    def enterPoststatements(self, ctx:MyGrammerParser.PoststatementsContext):
        pass

    # Exit a parse tree produced by MyGrammerParser#poststatements.
    def exitPoststatements(self, ctx:MyGrammerParser.PoststatementsContext):
        pass


    # Enter a parse tree produced by MyGrammerParser#vardef.
    def enterVardef(self, ctx:MyGrammerParser.VardefContext):
        pass

    # Exit a parse tree produced by MyGrammerParser#vardef.
    def exitVardef(self, ctx:MyGrammerParser.VardefContext):
        pass


    # Enter a parse tree produced by MyGrammerParser#varset.
    def enterVarset(self, ctx:MyGrammerParser.VarsetContext):
        pass

    # Exit a parse tree produced by MyGrammerParser#varset.
    def exitVarset(self, ctx:MyGrammerParser.VarsetContext):
        pass


    # Enter a parse tree produced by MyGrammerParser#callst.
    def enterCallst(self, ctx:MyGrammerParser.CallstContext):
        pass

    # Exit a parse tree produced by MyGrammerParser#callst.
    def exitCallst(self, ctx:MyGrammerParser.CallstContext):
        pass


    # Enter a parse tree produced by MyGrammerParser#printst.
    def enterPrintst(self, ctx:MyGrammerParser.PrintstContext):
        pass

    # Exit a parse tree produced by MyGrammerParser#printst.
    def exitPrintst(self, ctx:MyGrammerParser.PrintstContext):
        pass


    # Enter a parse tree produced by MyGrammerParser#ret.
    def enterRet(self, ctx:MyGrammerParser.RetContext):
        pass

    # Exit a parse tree produced by MyGrammerParser#ret.
    def exitRet(self, ctx:MyGrammerParser.RetContext):
        pass


    # Enter a parse tree produced by MyGrammerParser#ifelse.
    def enterIfelse(self, ctx:MyGrammerParser.IfelseContext):
        pass

    # Exit a parse tree produced by MyGrammerParser#ifelse.
    def exitIfelse(self, ctx:MyGrammerParser.IfelseContext):
        pass


    # Enter a parse tree produced by MyGrammerParser#postponest.
    def enterPostponest(self, ctx:MyGrammerParser.PostponestContext):
        pass

    # Exit a parse tree produced by MyGrammerParser#postponest.
    def exitPostponest(self, ctx:MyGrammerParser.PostponestContext):
        pass



del MyGrammerParser