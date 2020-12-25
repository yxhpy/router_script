import requests
import execjs
import config


class SomeFunc:
    def __init__(self):
        with open("a.js", 'r', encoding="utf-8") as f:
            self.js = execjs.compile(f.read())
        self.id = None

    def content(self):
        response = requests.get("http://192.168.1.1/common/Content.htm")
        return response.text.split("\r\n")

    def encode(self, input1, input2, input3):
        return self.js.call("securityEncode", input1, input2, input3)

    def login(self, passwd):
        content = self.content()
        new_passwd = self.encode(passwd, config.STR_DE, config.DIC)
        inp1 = content[3]
        inp3 = content[4]
        self.id = self.encode(inp1, new_passwd, inp3)
        params = {
            "code": 7,
            "asyn": 0,
            "id": self.id,
        }
        response = requests.post("http://192.168.1.1/", params=params)
        return response.text

    def get_some_info(self):
        params = {
            "code": 2,
            "asyn": 0,
            "id": self.id,
        }
        body = "1#0"
        response = requests.post("http://192.168.1.1/", params=params, data=body)
        return response.text

    def set_dhcp(self,
                 id="8",
                 enable="1",
                 poolStart="192.168.1.100",
                 poolEnd="192.168.1.199",
                 leaseTime="120",
                 dns0="0.0.0.0",
                 dns1="0.0.0.0",
                 gateway="192.168.1.1"):
        info = {
            "id": id,
            "enable": enable,
            "poolStart": poolStart,
            "poolEnd": poolEnd,
            "leaseTime": leaseTime,
            "dns 0": dns0,
            "dns 1": dns1,
            "gateway": gateway,
            "hostName": "",
        }
        data = ""
        for i in info.items():
            data += " ".join(i) + "\n"
        params = {
            "code": 1,
            "asyn": 0,
            "id": self.id,
        }
        response = requests.post("http://192.168.1.1/", params=params, data=data)
        return response.text.strip()

    def reboot(self):
        params = {
            "code": 6,
            "asyn": 0,
            "id": self.id,
        }
        response = requests.post("http://192.168.1.1/", params=params)
        return response.text.strip()


if __name__ == '__main__':
    sf = SomeFunc()
    print(sf.login("520612lgh"))
    print(sf.get_some_info())
    print(sf.set_dhcp(dns0="192.168.1.50", gateway="192.168.1.50"))
    # print(sf.set_dhcp(dns0="0.0.0.0", gateway="192.168.1.1"))
    print(sf.reboot())
