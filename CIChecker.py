import ipaddress
import os
import argparse

def expand_ranges(input_file, output_file):
    """Extract all IPv4 addresses from ranges and store them in a file."""
    all_ips = set()

    # Load existing IPs if the output file exists
    if os.path.exists(output_file):
        with open(output_file, "r") as f:
            all_ips.update(f.read().splitlines())

    try:
        with open(input_file, "r") as f:
            for line in f:
                line = line.strip()
                if not line or ":" in line:  # Ignore empty lines and IPv6
                    continue
                try:
                    if "-" in line:  # IP Range
                        start_ip, end_ip = map(ipaddress.IPv4Address, line.split("-"))
                        for ip in range(int(start_ip), int(end_ip) + 1):
                            all_ips.add(str(ipaddress.IPv4Address(ip)))
                    elif "/" in line:  # CIDR
                        network = ipaddress.IPv4Network(line, strict=False)
                        all_ips.update(str(ip) for ip in network.hosts())
                    else:  # Single IP
                        all_ips.add(line)
                except ValueError:
                    print(f"[!] Error processing: {line}")  # Show error but continue

        # Save only new unique IPs
        with open(output_file, "w") as f:
            f.write("\n".join(sorted(all_ips)) + "\n")

        print(f"[+] Extracted {len(all_ips)} unique IPs and saved to {output_file}")

    except FileNotFoundError:
        print(f"[!] File not found: {input_file}")
        exit(1)

def check_ip(ip, output_file):
    """Check if a single IP exists in the CDN list."""
    if not os.path.exists(output_file):
        print("[!] CDN IP list does not exist. Run the script with a range file first.")
        exit(1)

    with open(output_file, "r") as f:
        all_ips = set(f.read().splitlines())

    if ip in all_ips:
        print(f"[✔] IP {ip} belongs to a CDN.")
    else:
        print(f"[✘] IP {ip} is NOT in the CDN list.")

def check_file(ip_file, output_file):
    """Check multiple IPs from a file."""
    if not os.path.exists(ip_file):
        print(f"[!] File not found: {ip_file}")
        exit(1)
    
    with open(ip_file, "r") as f:
        ips_to_check = [line.strip() for line in f if line.strip()]

    if not os.path.exists(output_file):
        print("[!] CDN IP list does not exist. Run the script with a range file first.")
        exit(1)

    with open(output_file, "r") as f:
        all_ips = set(f.read().splitlines())

    for ip in ips_to_check:
        if ip in all_ips:
            print(f"[✔] IP {ip} belongs to a CDN.")
        else:
            print(f"[✘] IP {ip} is NOT in the CDN list.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CDN IP Checker")
    parser.add_argument("-f", "--file", help="Check multiple IPs from a file")
    parser.add_argument("-ip", "--ip", help="Check a single IP")

    args = parser.parse_args()

    # Ask for the CDN-Range file when executed
    cdn_range_file = input("Enter the path to your CDN-Range file: ").strip()
    output_file = "all_ips.txt"  # Processed IPs will be stored here

    expand_ranges(cdn_range_file, output_file)  # Extract IPs

    if args.ip:
        check_ip(args.ip, output_file)
    elif args.file:
        check_file(args.file, output_file)
    else:
        print("[!] Please provide an IP (-ip) or file (-f) to check.")
