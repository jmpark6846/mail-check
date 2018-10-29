import re
import dns.resolver
import socket
import smtplib

def validate_email(mail):

    result = {}

    if not check_mail_syntax(mail):
        result = {
            'valid':False,
            'code':-1,
            'message': 'bad syntax'
        }
        return result

    domain_name = mail.split('@')[1]

    mx_record = get_mx_record(domain_name)

    host = socket.gethostname()

    server = smtplib.SMTP()
    server.set_debuglevel(0)

    server.connect(mx_record)
    server.helo(host)
    server.mail('hi@hi.com')


    code, message = server.rcpt(str(mail))

    result = {
        'code': code,
        'message': message,
    }

    if code == 250:
        result['valid']=True
    else:
        result['valid'] = False

    server.quit()
    return result


def check_mail_syntax(mail):
    match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', mail)
    return False if match == None else True


def get_mx_record(domain_name):
    try:
        records = dns.resolver.query(domain_name, 'MX')
    except Exception:
        print('invalid')
        raise ValueError('bad domain name')

    mx_record = records[0].exchange
    mx_record = str(mx_record)
    return mx_record

def check_mail_accounts():
    pass

