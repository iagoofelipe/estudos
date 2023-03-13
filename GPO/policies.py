import os

abs_path = os.path.abspath('') #caminho do executável

#importando 
os.system(r"secedit /configure /db c:\windows\security\local.sdb /cfg {local}\secpol.cfg /areas SECURITYPOLICY".format(local=abs_path))

#servidor de internet
os.system(r"REG ADD HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\DateTime\Servers /v 0 /t reg_sz /d a.st1.ntp.br /f")