from pathlib import Path

def exec(code):
    out = ''
    printint = False
    started = False
    for n, line in enumerate(code.split('\n')):
        line = line.strip()
        if n == 0:
            continue
        tokens = line.split(' ')
        for token in tokens:
            if token == 'start' and not started:
                started = True
                continue
            if started:
                if token == 'print':
                    printint = True
                elif printint:
                    out+= token
                    printint = False
    return out

def run(lvl, file):
    text = Path(f'level{lvl}_{file}.in').read_text()
    out = exec(text)
    Path(f'level{lvl}_{file}.out').write_text(out)

for lvl in range(1, 6):
    run(1, lvl)
