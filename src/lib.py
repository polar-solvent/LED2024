import sys    
from pathlib import Path

def parse_input_path(argv:list[str]):
    length = len(argv)

    if length == 1:
        print('no frame path')
        sys.exit(1)

    return str(Path(argv[1]).resolve())

def parse_options(argv:list[str], ops:dict[str, dict[str, str]]):
    length = len(argv)

    if length > 2+2*len(ops):
        print("too much options or miss space")
        sys.exit(1)

    opdict = [{"option" : argv[2::2][x], "value" : argv[3::2][x]} for x in range(int(length/2-1))]
    oplist_original = [dct.get("option") for dct in opdict]
    oplist = [op if len(op) == 2 else op[1:3] for op in oplist_original]

    if len(set(oplist)) != len(oplist):
        print("enter one option only once")
        sys.exit(1)

    for op in ops.values():
        try:
            opindex = oplist.index(op["command"])
        except ValueError:
            continue
        op["default"] = opdict[opindex]["value"]
        
    return [dct.get("default") for dct in ops.values()]
