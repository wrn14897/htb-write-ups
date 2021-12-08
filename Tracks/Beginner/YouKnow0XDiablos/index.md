1. Use `file` to get binary file info

2. Use gdb-peda (https://github.com/longld/peda) to figure out the buffer size 
  - `pattern create 200`
  - `pattern offset AwAA`
3. Use Cutter (https://github.com/rizinorg/cutter) to trace `flag()` and find the overflow values
```
/* jsdec pseudo code output */
/* /Users/warren/Codes/HTB/Tracks/Beginner/YouKnow0XDiablos/vuln @ 0x80491e2 */
#include <stdint.h>
 
uint32_t flag (unsigned long arg_8h, unsigned long arg_ch) {
    char * format;
    FILE * stream;
    int32_t var_4h;
    _x86_get_pc_thunk_bx (ebx);
    ebx += 0x2e12;
    eax = fopen (ebx - 0x1ff6, ebx - 0x1ff8);
    stream = eax;
    if (stream == 0) {
        puts (ebx - 0x1fec);
        exit (0);
    }
    fgets (format, 0x40, stream);
    if (arg_8h == 0xdeadbeef) {
        if (arg_ch == 0xc0ded00d) {
            printf (format);
        } else {
        } else {
        }
    }
    ebx = var_4h;
    return eax;
}
```
4. Write python script using `pwd` (https://github.com/Gallopsled/pwntools) module to exploit target TCP server
