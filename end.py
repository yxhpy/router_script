# 系统关闭自动关闭
from ip import SomeFunc
sf = SomeFunc()
print(sf.get_some_info())
print(sf.set_dhcp(dns0="0.0.0.0", gateway="192.168.1.1"))
print(sf.reboot())