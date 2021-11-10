# Generated from MyGrammer by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MyGrammerParser import MyGrammerParser
else:
    from MyGrammerParser import MyGrammerParser

# This class defines a complete generic visitor for a parse tree produced by MyGrammerParser.

class MyGrammerVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MyGrammerParser#program.
    def visitProgram(self, ctx:MyGrammerParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammerParser#block.
    def visitBlock(self, ctx:MyGrammerParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammerParser#value.
    def visitValue(self, ctx:MyGrammerParser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammerParser#statement.
    def visitStatement(self, ctx:MyGrammerParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammerParser#statements.
    def visitStatements(self, ctx:MyGrammerParser.StatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammerParser#poststatements.
    def visitPoststatements(self, ctx:MyGrammerParser.PoststatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammerParser#vardef.
    def visitVardef(self, ctx:MyGrammerParser.VardefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammerParser#varset.
    def visitVarset(self, ctx:MyGrammerParser.VarsetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammerParser#callst.
    def visitCallst(self, ctx:MyGrammerParser.CallstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammerParser#printst.
    def visitPrintst(self, ctx:MyGrammerParser.PrintstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammerParser#ret.
    def visitRet(self, ctx:MyGrammerParser.RetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammerParser#ifelse.
    def visitIfelse(self, ctx:MyGrammerParser.IfelseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammerParser#postponest.
    def visitPostponest(self, ctx:MyGrammerParser.PostponestContext):
        return self.visitChildren(ctx)



del MyGrammerParser