from requests import get, post
import mailgun
import json

def validate_email(email_address):
    auth_data = ("api", mailgun.pub_key)
    payload = {"address": email_address}
    r = get("https://api.mailgun.net/v3/address/validate", auth=auth_data, params=payload) 
    data = json.loads(r.text)
    return data['is_valid']

def send_confirmation_email(name, email_address):
    auth_data = ('api', mailgun.mailgun_key)
    email_from = 'TJCTF 2016 <noreply@%s>' % mailgun.site_url
    email_to = [email_address]
    subject = "Thanks For Signing Up for TJCTF Emails!"
    body = "Hi %s,\n\nThank you for signing up for TJCTF Emails. We will send out more information about TJCTF 2016 as it becomes available.\n\nThanks,\nTJCTF 2016" % name
    send_data = {"from": email_from,
            "to": email_to,
            "subject": subject,
            "text": body}
    r = post(mailgun.mailgun_url + '/messages', auth=auth_data, data=send_data)
    if r.status_code == 200:
        return True
    else:
        return False

def get_list(name):
    auth_data = ('api', mailgun.mailgun_key)
    r = get('https://api.mailgun.net/v3/lists', auth=auth_data)
    data = json.loads(r.text)
    num_lists = int(data["total_count"])
    lists = []
    for i in range(num_lists):
        lists.append(str(data['items'][i]['name']))
    if name in lists:
        return True
    else:
        return False

def create_list(name):
    auth_data = ('api', mailgun.mailgun_key)
    send_data = {'address': '%s@%s' % (name, mailgun.site_url), 'name': name}
    r = post("https://api.mailgun.net/v3/lists", auth=auth_data, data=send_data)
    data = json.loads(r.text)
    if data["message"] == 'Mailing list has been created':
        return True
    else:
        return False

def add_user_to_list(name, email, list_name):
    auth_data = ('api', mailgun.mailgun_key)
    send_data = {'subscribed': True,
                 'address': email,
                 'name': name}
    r = post("https://api.mailgun.net/v3/lists/%s@%s/members" % (list_name, mailgun.site_url), auth=auth_data, data=send_data)
    data = json.loads(r.text)
    if data["message"] == 'Mailing list member has been created' or "Address already exists" in data["message"]:
        return True
    else:
        return data["message"]

