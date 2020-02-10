# Multi-threading is easy!
# It is just a matter of launching a few worker threads.

import threading
import dis

counter = 0


def worker():
    'My job is to increment the counter and print the current count'
    global counter

    counter += 1
    print('The count is %d' % counter)
    print('---------------')


print('Starting up')
for i in range(10):
    threading.Thread(target=worker).start()
print('Finishing up')


# Even here we could not get the result we were expecting, as we have race conditions in two points
# counter +=1 and the print statement that follow

# Why this is happening

bytecode = dis.Bytecode(worker)
for instr in bytecode:
    print(instr)

# Instruction(opname='LOAD_GLOBAL', opcode=116, arg=0, argval='counter', argrepr='counter', offset=0, starts_line=14, is_jump_target=False)
# Instruction(opname='LOAD_CONST', opcode=100, arg=1, argval=1, argrepr='1', offset=2, starts_line=None, is_jump_target=False)
# Instruction(opname='INPLACE_ADD', opcode=55, arg=None, argval=None, argrepr='', offset=4, starts_line=None, is_jump_target=False)
# Instruction(opname='STORE_GLOBAL', opcode=97, arg=0, argval='counter', argrepr='counter', offset=6, starts_line=None, is_jump_target=False)
# Instruction(opname='LOAD_GLOBAL', opcode=116, arg=1, argval='print', argrepr='print', offset=8, starts_line=15, is_jump_target=False)
# Instruction(opname='LOAD_CONST', opcode=100, arg=2, argval='The count is %d', argrepr="'The count is %d'", offset=10, starts_line=None, is_jump_target=False)
# Instruction(opname='LOAD_GLOBAL', opcode=116, arg=0, argval='counter', argrepr='counter', offset=12, starts_line=None, is_jump_target=False)
# Instruction(opname='BINARY_MODULO', opcode=22, arg=None, argval=None, argrepr='', offset=14, starts_line=None, is_jump_target=False)
# Instruction(opname='CALL_FUNCTION', opcode=131, arg=1, argval=1, argrepr='', offset=16, starts_line=None, is_jump_target=False)
# Instruction(opname='POP_TOP', opcode=1, arg=None, argval=None, argrepr='', offset=18, starts_line=None, is_jump_target=False)
# Instruction(opname='LOAD_GLOBAL', opcode=116, arg=1, argval='print', argrepr='print', offset=20, starts_line=16, is_jump_target=False)
# Instruction(opname='LOAD_CONST', opcode=100, arg=3, argval='---------------', argrepr="'---------------'", offset=22, starts_line=None, is_jump_target=False)
# Instruction(opname='CALL_FUNCTION', opcode=131, arg=1, argval=1, argrepr='', offset=24, starts_line=None, is_jump_target=False)
# Instruction(opname='POP_TOP', opcode=1, arg=None, argval=None, argrepr='', offset=26, starts_line=None, is_jump_target=False)
# Instruction(opname='LOAD_CONST', opcode=100, arg=4, argval=None, argrepr='None', offset=28, starts_line=None, is_jump_target=False)
# Instruction(opname='RETURN_VALUE', opcode=83, arg=None, argval=None, argrepr='', offset=30, starts_line=None, is_jump_target=False)
