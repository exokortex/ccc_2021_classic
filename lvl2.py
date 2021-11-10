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

class ReturnValue:
    val: str

class CCCVisitor(MyGrammerVisitor):
    output = ''
    #def visitProgram(self, ctx):
    #    print(ctx)

    def visitBlock(self, ctx):
        print('block')
        try:
            self.visit(ctx.statements())
        except ReturnException:
            print('returned...')
            return False

    def visitStatements(self, ctx):
        print('statements')
        for st in ctx.statement():
            ret = self.visit(st)
            if isinstance(ret, ReturnValue):
                print('line', ret)
                return ret

    def visitPrintst(self, ctx):
        self.output += ctx.value().getText()

    def visitIfelse(self, ctx):
        cond = ctx.BOOLEAN().getText()
        #print(dir(ctx))
        if cond == 'true':
            return self.visit(ctx.ifpart)
        else:
            return self.visit(ctx.elsepart)

    def visitRet(self, ctx):
        print('ret')
        return ReturnValue()

class MyGrammerListener(ParseTreeListener):
    def enterBlock(self, ctx):
        pass
    def exitBlock(self, ctx):
        pass
    def enterPrintst(self, ctx):
        pass
    def exitPrintst(self, ctx):
        pass
    def enterIfelse(self, ctx):
        pass
    def exitIfelse(self, ctx):
        pass

class CCCExecutor(MyGrammerListener):
    output = ''
    def exitBlock(self, ctx):
        print("Oh, a block!")

    def enterPrintst(self, ctx):
        self.output += ctx.value().getText()
        pass

    def enterIfelse(self, ctx):
        cond = ctx.BOOLEAN().getText()
        print(cond)
        ifpart = ctx.statement(0)
        elsepart = ctx.statement(1)
        global x
        x = self
        print(dir(self))
        print(dir(ctx))
        if cond == 'true':
            self.visit(ifpart)
        else:
            self.visit(elsepart)
        return False

#def exec(code):
#    out = ''
#    printint = False
#    started = False
#    for n, line in enumerate(code.split('\n')):
#        line = line.strip()
#        if n == 0:
#            continue
#        tokens = line.split(' ')
#        for token in tokens:
#            if token == 'start' and not started:
#                started = True
#                continue
#            if started:
#                if token == 'print':
#                    printint = True
#                elif printint:
#                    out+= token
#                    printint = False
#    return out

def run(lvl, file):
    text = Path(f'level{lvl}_{file}.in').read_text()
    out = exec(f'level{lvl}_{file}.in')
    Path(f'level{lvl}_{file}.out').write_text(out)

for fileno in range(0, 6):
    run(2, fileno)
