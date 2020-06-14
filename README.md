# SimpleFuzzer
a python script to semi automate fuzzing a potential buffer overflow vulnerability on target machine. It will also auto create a payload to be sent to the target and lastly provide a the exact offset of an EIP value to place your shellcode.

`Usage: simplefuzzer.py --target [TARGET] --port [PORT]`

## Description:
The script will start fuzzing the target starting with 100 bytes and increments by 100 bytes as well. Once it detecet a potintioal buffer overflow it will automaticly generate a random char payload based on number of bytes it sent before crashing. Then you will need to set the payload to the target host inside a debugger to get the EIP value. Once you get the EIP value a prompt will be ready to insert the EIP value (in hex) and get the exact offset.

```
root@Kali:~/SimpleFuzzer# python simplefuzzer.py --target [Host_IP] --port [Port]
Simple Fuzzer v1.0
Starting Fuzzmap at 01:56:21
Simple Fuzzer report for 172.16.252.141
[+] Connected to host successfully
Fuzzing with 100 bytes
Fuzzing with 200 bytes
Fuzzing with 300 bytes
Fuzzing with 400 bytes
Fuzzing with 500 bytes
Fuzzing with 600 bytes
Fuzzing with 700 bytes
Fuzzing with 800 bytes

[!] Possible overflow detected at 800 bytes
[+] Payload= Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9Ag0Ag1Ag2Ag3Ag4Ag5Ag6Ag7Ag8Ag9Ah0Ah1Ah2Ah3Ah4Ah5Ah6Ah7Ah8Ah9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Aj0Aj1Aj2Aj3Aj4Aj5Aj6Aj7Aj8Aj9Ak0Ak1Ak2Ak3Ak4Ak5Ak6Ak7Ak8Ak9Al0Al1Al2Al3Al4Al5Al6Al7Al8Al9Am0Am1Am2Am3Am4Am5Am6Am7Am8Am9An0An1An2An3An4An5An6An7An8An9Ao0Ao1Ao2Ao3Ao4Ao5Ao6Ao7Ao8Ao9Ap0Ap1Ap2Ap3Ap4Ap5Ap6Ap7Ap8Ap9Aq0Aq1Aq2Aq3Aq4Aq5Aq6Aq7Aq8Aq9Ar0Ar1Ar2Ar3Ar4Ar5Ar6Ar7Ar8Ar9As0As1As2As3As4As5As6As7As8As9At0At1At2At3At4At5At6At7At8At9Au0Au1Au2Au3Au4Au5Au6Au7Au8Au9Av0Av1Av2Av3Av4Av5Av6Av7Av8Av9Aw0Aw1Aw2Aw3Aw4Aw5Aw6Aw7Aw8Aw9Ax0Ax1Ax2Ax3Ax4Ax5Ax6Ax7Ax8Ax9Ay0Ay1Ay2Ay3Ay4Ay5Ay6Ay7Ay8Ay9Az0Az1Az2Az3Az4Az5Az6Az7Az8Az9Ba0Ba1Ba2Ba3Ba4Ba5Ba


[*] Enter the value of the EIP : 35724134

[!] Exact match found at 524!

```

### Notes:
- make sure pattern_create.rb is locate in `/usr/share/metasploit-framework/tools/exploit/`
- scripts will run on <= Python 2.7

Devoleped by Muhannad
