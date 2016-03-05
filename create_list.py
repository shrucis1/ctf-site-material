from mail import get_list, create_list

print("[=] Creating mailing list...")
if get_list("ctfmembers"):
    print("[+] List already exists.")
else:
    if create_list("ctfmembers"):
        print("[+] List created!")
    else:
        print("[-] List creation failed")
