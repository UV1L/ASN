import subprocess
import re
from prettytable import PrettyTable
import pyasn


class Tracert:
    def get_path(self, hostname):
        tracert = subprocess.Popen(['tracert', '-w', '30', hostname], stdout=subprocess.PIPE)
        re_ip = re.compile("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")
        n = 0
        result = PrettyTable()
        result.field_names = ['№ по порядку', 'IP', 'AS']

        i = 0
        for line in iter(tracert.stdout.readline, ""):
            if i < 4:
                i += 1
                continue
            line = line.decode('windows-1251')
            if "*        *        *" in line:
                print(result)
                break
            else:
                ip = re.search(re_ip, line)[0]
                asndb = pyasn.pyasn('ipasn_20140513.dat')
                tuple = asndb.lookup(ip)
                if tuple[0] is None:
                    asn = ''
                else:
                    asn = tuple[0]
                result.add_row(n, ip, asn)
                n += 1
