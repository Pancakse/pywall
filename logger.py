from datetime import datetime

def log_packet(packet, reason=""):
    with open("blocked_packets.log", "a") as f:
        f.write(f"{datetime.now()} - BLOCKED - {packet[IP].src} -> {packet[IP].dst} ({reason})\n")
