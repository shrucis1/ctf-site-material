from mail import get_list, create_list
from mailgun_config import list_name

print("[=] Creating mailing list...")
if get_list(list_name):
    print("[+] List already exists.")
else:
    if create_list(list_name):
        print("[+] List created!")
    else:
        print("[-] List creation failed")
