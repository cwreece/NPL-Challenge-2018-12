#!/usr/bin/env python3.7
# NPL Challenge2 code using 3.7 environment by Carole Warner Reece
#
"""
My plan is to check for URL starting with "http://" or "https://",
then verify domain name is in DNS(so is potentially accessible),
then check for reachablility while verifying return code.
If find an invalid HTTP start string, try assuming entry is a fully qualified domain
or a valid IP address entry.

Optionally for testing, I use the bash script "test_url.sh" with examples file
"test.tsv"vto test multiple URLs cases.
"""

import sys
import socket
import requests
import subprocess


# Define functions in this section
#########################################################################
def get_url() -> str:
    """
    get_url either accepts a URL string entered when program is executed
    or prompts user to enter a URL

    :return: url

    """

    try:
        url = str(sys.argv[1])
        return url
    except Exception:
        url = input('Enter a URL to be tested: ')
        return url


def is_valid_url_start(url: str) -> bool:
    """
    is_valid_url_start verfies a URL starts with "http://" or "https://"

    :return: boolean - True or False
    """

    return url.startswith("http://") or url.startswith("https://")


def parse_domain_name(url: str) -> str:
    """
    parse_domain_name extracts a domain name from a valid URL

    :return: domain_name
    """

    assert is_valid_url_start(url)
    testUrl = url.split("//")
    resource = testUrl[1].split("/")
    domain_name = resource[0]
    print("The domain name is: ", domain_name)
    return domain_name


def is_dns_resolvable(domain_name: str) -> bool:
    """
    check_dns verfies that a domain_name can be resolved by DNS,
    or that a valid IP address has been entered.
    check_dns also prints status to the screen.

    Note: if a domain_name is not resolvable, you will never reach it.
    The program will use the python 'requests' module to check http/https status and
    reachability since a ping test may fail for servers that block ping,i.e. www.abs.com.

    :return: boolean - True if resolvable or an IP address, else False
    """

    try:
        # Remove comment in next line as needed for troubleshooting
        # print("Looking for DNS IP")
        # Note: socket.gethostbyname() also validates an IP address
        dns_ip = socket.gethostbyname(domain_name)
        # Comment out next line as needed for troubleshooting if you don't want it
        print("The IP address is", dns_ip)
        return True
    except Exception:
        print("The domain name is unknown in DNS, so is not HTTP reachable.")
        return False


def check_ping(domain_name: str) -> bool:
    """
    check_ping attempts to ping a domain name and returns True if domain_name
    is accessible.
    check_ping uses the subprocess and the platform modules.

    Note: check_ping may help diagnose reachable IP with a server issue.

    :return: boolean - True if domain_name is pingable, else False
    """
    ping_command = ['ping', domain_name, '-c 1']
    ping_output = subprocess.run(ping_command, False, stdout=subprocess.PIPE)
    success = ping_output.returncode
    return True if success == 0 else False


def check_http_status(url: str) -> None:
    """
    check_http_status attempts an HTTP request and prints the status.

    :return: None
    """

    try:
        """
        Need to include a timeout on the request.get so the program will not hang
        indefinitely for non-reachable IPs
        """
        request = requests.get(url, timeout=3)
        if request.status_code == 200:
            print("The request status code is", request.status_code)
            print("Success. The server appears to be online and functioning correctly.")
        elif request.status_code == 400:
            print("The request status code is", request.status_code)
            print("The requested page", url, "is not working.")
        elif request.status_code == 404:
            print("The request status code is", request.status_code)
            print("The requested page", url, "is not available.")
        elif request.status_code == 500:
            print("The request status code is", request.status_code)
            print("Internal server error. The requested page", url, "is not available.")
        elif request.status_code == 502:
            print("The request status code is", request.status_code)
            print("Bad gateway. The requested page", url, "is not available.")
        else:
            print("The request status code is", request.status_code)
    except Exception as e:
        # Handle known errors in the python "requests" module
        # Found by trying URL https://www.abc.com which is invalid
        print("There was an error resolving the URL. The reason was: \n", str(e))


def test_invalid_url_as_fqdn_or_ip(url: str) -> None:
    """
    test_invalid_url_as_fqdn_or_ip attempts to parse input string as a FQDN or an IP

    :return: None
    """

    resource = url.split("/")
    domain_name = resource[0]
    if is_dns_resolvable(domain_name):
        if check_ping(domain_name):
            print("Ping is successful to", domain_name)
        else:
            print("Ping is NOT successful to", domain_name)
        http_url = "http://" + url
        print("Checking HTTP version or", http_url)
        check_http_status(http_url)
        https_url = "https://" + url
        print("\nChecking HTTPS version or", https_url)
        check_http_status(https_url)


def main():
    """
    main function calls other functions to support the program goal of testing URLs

    :return: None
    """

    url = get_url()
    if is_valid_url_start(url):
        domain_name = parse_domain_name(url)
        if check_ping(domain_name):
            print("Ping is successful to", domain_name)
        else:
            print("Ping is NOT successful to", domain_name)
        if is_dns_resolvable(domain_name):
            check_http_status(url)

    else:
        print("Invalid URL syntax. The URL needs to start with http:// or https:// \n")
        print("(Testing for case where a fully qualified domain name or")
        print(" an IP address was entered.) \n")
        test_invalid_url_as_fqdn_or_ip(url)


"""
The main program starts here - previous lines were definitions.
Note: by default, a standalone program has the name '__main__'
Using this structure allows the import of a program to re-use its functions
without running the main program in the loaded .
"""


if __name__ == '__main__':
    main()
