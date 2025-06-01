def match_rule(rule, ip, port, protocol):
    return (rule['ip'] == ip and 
            rule['port'] == port and 
            rule['protocol'].upper() == protocol.upper())
