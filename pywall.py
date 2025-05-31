from scapy.all import sniff, IP, TCP, UDP
import json
from logger import log_packet
from utils import match_rule

def load_rules():
    with open('rules.json') as f:
        return json.load(f)

rules = load_rules()

def packet_callback(packet):
    if IP in packet:
        proto = 'TCP' if TCP in packet else 'UDP' if UDP in packet else None
        if proto:
            src_ip = packet[IP].src
            dst_port = packet[proto].dport
            for rule in rules:
                if match_rule(rule, src_ip, dst_port, proto):
                    if rule['action'] == 'block':
                        log_packet(packet, reason="Rule Matched")
                        return
    packet.show()

sniff(filter="ip", prn=packet_callback, store=0)
