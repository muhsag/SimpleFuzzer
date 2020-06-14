# SimpleFuzzer
a python script to semi automate fuzzing a potential buffer overflow vulnerability on target machine. It will also auto create a payload to be sent to the target and lastly provide a the exact offset of an EIP value to place your shellcode.

`Usage: simplefuzzer.py --target [TARGET] --port [PORT]`

## Description:
The script will start fuzzing the target starting with 100 bytes and increments by 100 bytes as well. Once it detecet a potintioal buffer overflow it will automaticly generate a random char payload based on number of bytes it sent before crashing. Then you will need to set the payload to the target host inside a debugger to get the EIP value. Once you get the EIP value a prompt will be ready to insert the EIP value (in hex) and get the exact offset.

### Notes:
- make sure pattern_create.rb is locate in `/usr/share/metasploit-framework/tools/exploit/`
- scripts will run on <= Python 2.7

Devoleped by Muhannad
