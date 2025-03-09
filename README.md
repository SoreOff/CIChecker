# CDN-IP-Checker

A simple and efficient tool to process CDN IP ranges, expand them into individual IPs, and check if a given IP belongs to a CDN.

## Features

- **Processes CDN IP Ranges**: Expands CIDR and IP range formats into individual IPs.
- **IPv4 Only**: Automatically ignores IPv6 addresses.
- **Check Single IP or File**: Verify if an IP or a list of IPs belong to a CDN.
- **Persistent Storage**: Saves expanded IPs to avoid redundant processing.
- **Error Handling**: Skips invalid entries and continues execution.


## Requirements

- Python 3.x
- No external dependencies (uses built-in Python libraries)


## Installation & Usage

### 1️⃣ Clone the repository:
```sh
git clone https://github.com/yourusername/CDN-IP-Checker.git
cd CDN-IP-Checker
```


## 2️⃣ Run the script and provide CDN range file:
```sh
python3 CDN_IP.py
```
It will prompt you to enter the CDN range file, which will be processed and stored.


## 3️⃣ Check a single IP:
```sh
python3 CDN_IP.py -ip 192.168.1.1
```


## 4️⃣ Check multiple IPs from a file:
```sh
python3 CDN_IP.py -f ips.txt
```

---

#### 5️⃣ ****Required Input File Format** (Input File Format)**

## Input File Format

The CDN range file (`ranges.txt`) should contain IP ranges in the following formats:

192.168.1.0/24 10.0.0.1-10.0.0.255 203.0.113.42

- CIDR notation (`x.x.x.x/xx`)
- Dash-separated range (`x.x.x.x-x.x.x.x`)
- Single IPs

The IP list file (`ips.txt`) should contain one IP per line for checking.



## How It Works

1. The script asks for the CDN range file.
2. It processes the file, expanding ranges into individual IPs.
3. All unique IPv4 addresses are stored in `all_ips.txt`.
4. When checking an IP, it searches in the stored file for a match.


## Limitations

- Only supports IPv4 (IPv6 addresses are ignored).
- Performance may decrease with extremely large datasets.


## Contributing

Feel free to submit issues or pull requests to improve the tool! 🛠️

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit changes (`git commit -m "Added a new feature"`)
4. Push to your branch (`git push origin feature-branch`)
5. Open a pull request


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.







