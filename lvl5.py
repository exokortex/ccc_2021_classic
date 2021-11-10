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
        return ctx.localScope[name]
    else:
        #print(dir(ctx))
        return resolveVar(ctx.parentCtx, name)

def setVar(ctx, name, val):
    if not ctx:
        raise CCCErrorException()
    if hasattr(ctx, 'localScope') and name in ctx.localScope:
        ctx.localScope[name] = val
    else:
        return setVar(ctx.parentCtx, name, val)


def output(ctx, text):
    scope = getLocalScope(ctx)
    if isinstance(text, bool):
        text = 'true' if text else 'false'
    if isinstance(text, int):
        text = str(text)
    setVar(ctx, '___output', resolveVar(ctx, '___output') + text)


class CCCVisitor(MyGrammerVisitor):
    output = ''
    program = None

    def visitProgram(self, ctx):
        self.program = ctx
        for func in ctx.block():
            output, retval = self.visit(func)
            self.output += f'{output}\n'

    def visitBlock(self, ctx):
        ctx.localScope = {}
        ctx.localScope['___output'] = ''
        ret = True
        try:
            self.visit(ctx.statements())
        except CCCErrorException:
            print('ERROR overrides', ctx.localScope['___output'])
            ctx.localScope['___output'] = 'ERROR'
        except CCCReturnException as e:
            ret = e.val
        return (ctx.localScope["___output"], ret)

    def visitStatements(self, ctx):
        ctx.execution_queu = []
        for st in ctx.statement():
            print('------------', st.getText())
            ret = self.visit(st)
        while True:
            st = None
            print('qstate', [x.getText() for x in ctx.execution_queu])
            try:
                st = ctx.execution_queu.pop(0)
            except IndexError:
                break
            self.visit(st)

    def visitCallst(self, ctx):
        val = self.visit(ctx.value())
        print('visitCall val=', val)
        if not isinstance(val, int):
            print('isint', repr(val))
            raise CCCErrorException()
        try:
            func = self.program.block()[val-1]
            print('eeeeeee', func.getText())
            out, retval = self.visit(func)
            output(ctx, out)
            return retval
        except Exception as e:
            print(e)
            print('AAAAAAAAAAAAAa')
            raise CCCErrorException()

    def visitPrintst(self, ctx):
        output(ctx, self.visit(ctx.value()))

    def visitPostponest(self, ctx):
        exec_context = ctx
        while not hasattr(exec_context, 'execution_queu'):
            exec_context = exec_context.parentCtx
        exec_context.execution_queu.append(ctx.poststatements())

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
        #scope = getLocalScope(ctx)
        name = ctx.name.text
        #if name not in scope:
        #    raise CCCErrorException()
        return setVar(ctx, name, self.visit(ctx.value()))

    def visitRet(self, ctx):
        print('ret')
        raise CCCReturnException(self.visit(ctx.value()))


def run(lvl, file):
    text = Path(f'level{lvl}_{file}.in').read_text()
    out = exec(f'level{lvl}_{file}.in')
    Path(f'level{lvl}_{file}.out').write_text(out)

#for fileno in range(0, 6):
#    run(5, fileno)
#for fileno in range(0, 10):
#    run(4, fileno)
#for fileno in range(0, 6):
#    run(3, fileno)
for fileno in range(0, 1):
    run(5, fileno)

#for fileno in [0, 6, 7]:
#    run(4, fileno)
