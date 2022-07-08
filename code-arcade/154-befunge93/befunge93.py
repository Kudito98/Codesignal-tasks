def solution(program):
    progLen = len(program)
    lineLen = len(program[0])
    x = 0
    valueAtPc = ''
    instructionsRun = 0
    instructionsLimit = 100000
    pc = [0, 0]
    inc = [0, 1]
    outp = ""
    sticky = [0] * (instructionsLimit * 2)
    going = True
    valueAtPc = program[pc[0]][pc[1]]
    while(going and instructionsRun < instructionsLimit):
        result = {
          '>': lambda x: ("inc",[0, 1]),
          '<': lambda x: ("inc",[0,-1]),
          'v': lambda x: ("inc",[1, 0]),
          '^': lambda x: ("inc",[-1, 0]),
          '#': lambda x: ("jump",[pc[0] + inc[0], pc[1] + inc[1]]), #pc = 
          '_': lambda x: ("inc",[0, 1 if (sticky.pop() == 0) else -1]), #inc =
          '|': lambda x: ("inc",[(1 if (sticky.pop() == 0) else -1), 0 ]), # inc =
          '+': lambda x: ("push",sticky.append(sticky.pop() + sticky.pop())),
          '-': lambda x: ("push",sticky.append((0-sticky.pop()) + sticky.pop())),
          '*': lambda x: ("push",sticky.append(sticky.pop() * sticky.pop())),
          '/': lambda x: ("divy",[sticky.pop(), sticky.pop()]),
          '%': lambda x: ("remmy",[sticky.pop(), sticky.pop()]),
          '!': lambda x: ("push",sticky.append(1 if sticky.pop() == 0 else 0)),
          '`': lambda x: ("push",sticky.append(1 if sticky.pop() < sticky.pop() else 0)),
          ':': lambda x: ("push",sticky.append(sticky[-1])),
          '\\':lambda x: ("swap",([])),
          '$': lambda x: ("none",sticky.pop()),
          '.': lambda x: ("outy",str(int(sticky.pop())) + " "),
          ',': lambda x: ("outy",str(chr(int(sticky.pop())))),
          '0': lambda x: ("push",sticky.append(0)),
          '1': lambda x: ("push",sticky.append(1)),
          '2': lambda x: ("push",sticky.append(2)),
          '3': lambda x: ("push",sticky.append(3)),
          '4': lambda x: ("push",sticky.append(4)),
          '5': lambda x: ("push",sticky.append(5)),
          '6': lambda x: ("push",sticky.append(6)),
          '7': lambda x: ("push",sticky.append(7)),
          '8': lambda x: ("push",sticky.append(8)),
          '9': lambda x: ("push",sticky.append(9)),
          '\"':lambda x: ("string",[]),
          ' ': lambda x: ("None",[]),
          '@': lambda x: ("end",[])
        }[valueAtPc](x)
        instructionsRun += 1
        if len(outp) >= 100:
            return outp[:100]
        if result[0] == "end":
            going = False
        else:
            if result[0] == "inc":
                inc = result[1]
            elif result[0] == "outy":
                newst = result[1]
                outp += newst
            elif result[0] == "jump":
                pc = [pc[0] + inc[0],pc[1] + inc[1]]
            elif result[0] == "swap":
                sticky[-1], sticky[-2] = sticky[-2], sticky[-1]
            elif result[0] == "string":
                pc = [pc[0] + inc[0],pc[1] + inc[1]]
                valueAtPc = program[pc[0]][pc[1]]
                while valueAtPc != "\"":
                    sticky.append(ord(valueAtPc))
                    pc = [pc[0] + inc[0],pc[1] + inc[1]]
                    if pc[0] == -1:
                        pc[0] = progLen -1
                    pc[0] %= progLen
                    if pc[1] == -1:
                        pc[1] = lineLen -1
                    pc[1] %= lineLen
                    valueAtPc = program[pc[0]][pc[1]]
            elif result[0] == "divy":
                sug = result[1]
                sticky.append(sug[1]/sug[0])
            elif result[0] == "remmy":
                sug = result[1]
                sticky.append(sug[1]%sug[0])
            else:
                pass
            pc = [pc[0] + inc[0],pc[1] + inc[1]]
            if pc[0] == -1:
                pc[0] = progLen -1
            pc[0] %= progLen
            if pc[1] == -1:
                pc[1] = lineLen -1
            pc[1] %= lineLen
            valueAtPc = program[pc[0]][pc[1]]
    return "".join(outp)
