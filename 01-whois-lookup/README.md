# WhoIsLookUp

A small Python WHOIS client, written as a first reconnaissance exercise. `whois.py` opens a TCP socket to IANA's WHOIS server, sends a domain name, and prints the reply.

## What you'll use

- Python 3 (standard library `socket` only)
- Outbound access to `whois.iana.org` on TCP port 43

## Steps

1. Open a terminal in this repository folder and run the script.

   ```bash
   python3 whois.py
   ```

   Expected result: the script queries `example.com` and prints IANA's record, starting with `% IANA WHOIS server` and including lines such as `domain: EXAMPLE.COM`, `organisation: Internet Assigned Numbers Authority`, and `source: IANA`.

2. To look up another domain, change the argument in the last line of `whois.py`, for example `print(whois_lookup("<your-domain>"))`, and run the script again.

   Expected result: IANA answers with the record it holds for that name. For most domains under a top-level domain like `.com`, IANA's reply points to the registry's own WHOIS server (a `refer:` line) instead of the full registration details.

3. Read `whois_lookup()` to see the three socket steps: connect to port 43, send the domain followed by `\r\n`, and read up to 4096 bytes of the response.

## What I learned

- WHOIS is a plain-text protocol over TCP port 43, so a raw socket is enough to query it.
- IANA is the top of the WHOIS chain and refers queries down to each registry.
- A single `recv(4096)` call can cut off long replies; a loop until the server closes the connection would read the whole response.
