
from pyModbusTCP.client import ModbusClient
c = ModbusClient(host="192.168.1.30", port=502, auto_open=True)
regs = c.read_holding_registers(0,3)
if regs:
     print(regs[0], regs[1], regs[2], sep='\n')

else:
     print("ㅠㅠ")

c.close()

import sched, time
s = sched.scheduler(time.time, time.sleep)
def do_something(sc):

    print(regs[0], regs[1], regs[2])

    # do your stuff
    s.enter(1, 1, do_something, (sc,))

s.enter(1, 1, do_something, (s,))
s.run()

