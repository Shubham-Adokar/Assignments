import re


def url_matching(input_url):
    matcher = re.fullmatch('^(http[:][/][/]|https[:][/][/]|ftp[:][/][/])[a-zA-Z0-9._-]+[.]emtecinc[.]com([/]v[0-9][.][0-9][/]api[/][a-zA-Z0-9._-]+|[:]{1}[0-9]{4}[/]v[0-9][.][0-9][/]api[/][a-zA-Z0-9._-]+)', input_url)
    if matcher is not None:
        return "Given URL is Valid"
    else:
        return "Given URL is Invalid"


def test_url_matching():
    assert url_matching('http://slack.emtecinc.com:9090/v0.2/api/messages') == "Given URL is Valid"


print(url_matching('http://slack.emtecinc.com:9090/v0.2/api/messages'))
print(url_matching('ftp://sap.emtecinc.com:8080/v0.2/api/groups'))
print(url_matching('https://empower.emtecinc.com/v0.2/api/robos'))
print(url_matching('https://empower.emtecinc.com:/v0.2/api/robos'))
