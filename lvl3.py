import sys
from antlr4 import *
from MyGrammerLexer import MyGrammerLexer
from MyGrammerParser import MyGrammerParser
from MyGrammerVisitor import MyGrammerVisitor
from pathlib import Path

def exec(filename):
    input_stream = FileStream(filename)
    lexer = MyGrammerLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MyGrammerParser(stream)
    tree = parser.program()
    visitor = CCCVisitor()
    visitor.visit(tree)
    #printer = CCCExecutor()
    #walker = ParseTreeWalker()
    #walker.walk(printer, tree)
    return visitor.output

class CCCErrorException(Exception):
    pass

class CCCReturnException(Exception):
    def __init__(self, val):
        self.val = val

def getLocalScope(ctx):
    if hasattr(ctx, 'localScope'):
        return ctx.localScope
    else:
        return getLocalScope(ctx.parentCtx)

def resolveVar(ctx, name):
    if not ctx:
        return None
    if hasattr(ctx, 'localScope') and name in ctx.localScope:
        print(ctx.localScope)
        return ctx.localScope[name]
    else:
        #print(dir(ctx))
        return resolveVar(ctx.parentCtx, name)


def output(ctx, text):
    scope = getLocalScope(ctx)
    if isinstance(text, bool):
        text = 'true' if text else 'false'
    if isinstance(text, int):
        text = str(text)
    scope['___output'] += text


class CCCVisitor(MyGrammerVisitor):
    output = ''

    def visitBlock(self, ctx):
        ctx.localScope = {}
        ctx.localScope['___output'] = ''
        try:
            self.visit(ctx.statements())
        except CCCErrorException:
            ctx.localScope['___output'] = 'ERROR'
        except CCCReturnException as e:
            pass
        self.output += f'{ctx.localScope["___output"]}\n'

    def visitStatements(self, ctx):
        for st in ctx.statement():
            print('------------', st.getText())
            ret = self.visit(st)

    def visitPrintst(self, ctx):
        output(ctx, self.visit(ctx.value()))

    def visitIfelse(self, ctx):
        cond = self.visit(ctx.cond)
        if not isinstance(cond, bool):
            raise CCCErrorException()
        if cond == True:
            return self.visit(ctx.ifpart)
        else:
            return self.visit(ctx.elsepart)

    def visitValue(self, ctx):
        print('visit value', ctx.getText())
        if ctx.STR():
            s = ctx.STR().getText()
            val = resolveVar(ctx, s)
            print('resoving', s, '=', val)
            if val == None:
                val = s
            return val
        elif ctx.BOOLEAN():
            return ctx.BOOLEAN().getText() == 'true'
        elif ctx.INT():
            return int(ctx.INT().getText())

    def visitVardef(self, ctx):
        scope = getLocalScope(ctx)
        #print(dir(ctx.name.text))
        name = ctx.name.text
        #print('line',  ctx.getText(), ctx.name, scope)
        if name in scope:
            raise CCCErrorException()
        scope[name] = self.visit(ctx.value())

    def visitVarset(self, ctx):
        scope = getLocalScope(ctx)
        name = ctx.name.text
        if name not in scope:
            raise CCCErrorException()
        scope[name] = self.visit(ctx.value())

    def visitRet(self, ctx):
        print('ret')
        raise CCCReturnException(self.visit(ctx.value()))


def run(lvl, file):
    text = Path(f'level{lvl}_{file}.in').read_text()
    out = exec(f'level{lvl}_{file}.in')
    Path(f'level{lvl}_{file}.out').write_text(out)

for fileno in range(0, 6):
    run(3, fileno)
