import os

abs_path = os.path.abspath('')
os.system(r'secedit /configure /db c:\windows\security\local.sdb /cfg {local}\secpol.cfg /areas SECURITYPOLICY'.format(local=abs_path))