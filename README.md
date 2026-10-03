# WhoIsLookUp

A simple Python WHOIS client used as a first step in reconnaissance.

## What It Does

`whois.py` opens a raw socket to `whois.iana.org` on port 43, sends a
domain name, and prints the WHOIS response.

## Usage

```
python3 whois.py
```

Edit the domain passed to `whois_lookup()` in the script to look up a
different domain.
