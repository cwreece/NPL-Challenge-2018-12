# NPL-Challenge-2018-12
Dec 2018 NPL Challenge

This is my response to the Dec 2018 NPL challenge to create a python program to troubleshoot HTTP/HTTPS reachability to a URL that is input by the user from a prompt.

The program is named "http_url_checker.py".

My basic plan was to check for a URL starting with "http://" or "https://".
http_url_checker.py will either accept a string as an argument when ran (preferred), or ask the user to enter a URL.

If the URL is valid, the program next will verify domain name is in DNS (so is potentially accessible).
Then the prgram will check for reachablility to the URL while verifying return code.

If the program finds invalid HTTP, it will re-try the inputted string assuming entry is a fully qualified domain 
or a valid IP address entry.

I also set up a bash script called "test_url.sh" with examples file "test.tsv" that can be used to test multiple URLs cases.

I decided to work in the 3.x Python environment, and so am using Python3.7.

Program notes: 
I use three Python modules: sys, socket, and requests. The sys and socket are Python defaults, but I had to install requests so that it could be used.

I focused on using more functions for this program, including a main() fuction. I included doc strings for each function. 
Here's the self-documenting description of my functions from running help on them interactively:

>>> sys.argv
['http_url_checker.py']
>>>

>>> help(get_url)
Help on function get_url in module __main__:

get_url() -> str
    get_url either accepts a URL string entered when program is executed 
    or prompts user to enter a URL
    
        :return: url

>>> 
>>> help(is_valid_url_start)
Help on function is_valid_url_start in module __main__:

is_valid_url_start(url: str) -> bool
    is_valid_url_start verfies a URL starts with "http://" or "https://"
    
        :return: boolean - True or False

>>> 
>>> help(parse_domain_name)
Help on function parse_domain_name in module __main__:

parse_domain_name(url: str) -> str
    parse_domain_name extracts a domain name from a valid URL
    
        :return: domain_name

>>> 
>>> help(is_dns_resolvable)
Help on function is_dns_resolvable in module __main__:

is_dns_resolvable(domain_name: str) -> bool
    check_dns verfies that a domain_name can be resolved by DNS,
    or that a valid IP address has been entered.
    check_dns also prints status to the screen.
    
    Note: if a domain_name is not resolvable, you will never reach it, so no need to check further.
    The program will use the python 'requests' module to check http/https status and reachability,
    since a ping test may fail for servers that block ping such as www.abs.com.
    
        :return: boolean - True if resolvable or an IP address, else False

>>> 
>>> help(check_http_status)
Help on function check_http_status in module __main__:

check_http_status(url: str) -> None
    check_http_status attempts an HTTP request and prints the status.
    
        :return: None

>>> 
>>> help(test_invalid_url_as_fqdn_or_ip)
Help on function test_invalid_url_as_fqdn_or_ip in module __main__:

test_invalid_url_as_fqdn_or_ip(url: str) -> None
    test_invalid_url_as_fqdn_or_ip attempts to parse input string as a FQDN or an IP
    
        :return: None

>>> 
>>> help(main)
Help on function main in module __main__:

main()
    main function calls other functions to support the program goal of testing URLs
    
        :return: None

>>> 

