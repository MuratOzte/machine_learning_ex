import re
file = './toppages/access_log.txt'


format_pat = re.compile(
    r"(?P<host>[\d\.]+)\s"
    r"(?P<identity>\S*)\s"
    r"(?P<user>\S*)\s"
    r"\[(?P<time>.*?)\]\s"
    r'"(?P<request>.*?)"\s'
    r"(?P<status>\d+)\s"
    r"(?P<bytes>\S*)\s"
    r'"(?P<referer>.*?)"\s'
    r'"(?P<user_agent>.*?)"\s*'
)

URL_COUNTS = {}

with open(file, mode='r') as f:
    for line in (l.lstrip() for l in f):
        match = format_pat.match(line)
        if (match):
            access = match.groupdict()
            request = access['request']
            fields = request.split()
            if len(fields) == 3:
                (action, url, protocol) = fields
                if (action == 'GET'):
                    if url in URL_COUNTS:
                        URL_COUNTS[url] += 1
                    else:
                        URL_COUNTS[url] = 1

URL_RESULT = sorted(URL_COUNTS, key=lambda i: int(URL_COUNTS[i]), reverse=True)

USER_AGENTS = {}
with open(file, mode='r') as f:
    for line in (l.lstrip() for l in f):
        match = format_pat.match(line)
        if (match):
            access = match.groupdict()
            agent = access['user_agent']
            if (not ('bot' in agent or 'spider' in agent or '-' in agent or 'Bot' in agent or 'Spider' in agent or 'W3 Total Cache' in agent)):
                if agent in USER_AGENTS:
                    USER_AGENTS[agent] += 1
                else:
                    USER_AGENTS[agent] = 1

AGENT_RESULT = sorted(USER_AGENTS, key=lambda i: int(
    USER_AGENTS[i]), reverse=True)


# for result in results[:20]:
#     print(result + ': ' + str(URL_COUNTS[result]))

for result in AGENT_RESULT:
    print(result + ": " + str(USER_AGENTS[result]))
