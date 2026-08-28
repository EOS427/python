from scapy.all import rdpcap
from scapy.layers.inet import IP, TCP
pcap_address=input()
packets = rdpcap(pcap_address)
print(f"总共抓取到 {len(packets)} 个数据包。")
while True:
    pack_num=int(input())
    if pack_num>len(packets):
        print("error:length illegal")
        continue
    break
for i in range(min(pack_num, len(packets))):
    pkt = packets[i]
    print(f"\n数据包 {i + 1} 的摘要: {pkt.summary()}")

    if pkt.haslayer(IP):
        ip_layer = pkt[IP]
        print(f"  - 源IP: {ip_layer.src}")
        print(f"  - 目标IP: {ip_layer.dst}")

    if pkt.haslayer(TCP):
        tcp_layer = pkt[TCP]
        print(f"  - 源端口: {tcp_layer.sport}")
        print(f"  - 目标端口: {tcp_layer.dport}")