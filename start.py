# 系统启动自动开启
from ip import SomeFunc
sf = SomeFunc()
print(sf.get_some_info())
print(sf.set_dhcp(dns0="192.168.1.50", gateway="192.168.1.50"))
print(sf.reboot())
