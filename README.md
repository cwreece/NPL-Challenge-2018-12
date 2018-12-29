# NPL-Challenge-2018-12
Dec 2018 NPL Challenge

This is my response to the Dec 2018 NPL challenge to create a python program to troubleshoot HTTP/HTTPS reachability to a URL that is input by the user. I combined the base challenge and the bonus tasks together.

The program is named "check_http_url.py".

I decided this time to work in the 3.x Python environment, so I am using Python 3.7.

I use four Python modules: sys, socket, subprocess, and requests. (I had to install requests so that it could be used.)

I focused on using mostly functions for this program, including a main() function. I included a docstring for each function to document how the functions should be used and for help in interactive mode.

The high level program flow is as follows:
  1) The program check_http_url.py will accept a URL string as an argument when run.
  (If the check_http_url.py is run without a provided URL, it will prompt the user to input a URL.)
  Program note: The function get_url is used.

  2) The program will check for a URL starting with "http://" or "https://" as a protocol identifier.
  Program note: The function is_valid_url_start is used.

  3) If the URL is valid (starts with "http://" or "https://"), the program next will parse the domain name in the URL resource name
  then check if it is in DNS (and so is potentially accessible).
  Program note: The functions parse_domain_name and is_dns_resolvable are used.

  4) If the domain name is potentially accessible (or is DNS resovable), the program will check for reachablility to the URL
  while verifying the HTTP return code using the requests module.
  Note 1: To handle known errors in the python "requests" module, I included a timeout with requests.get.
  Note 2: I do include a ping check for general reachability,but some sites such as www.abs.com block ping.
  Program note: The functions check_ping and check_http_status are used.

  5) If the program finds an invalid HTTP protocol identifier was entered, the program will re-test the string under the assumption that
  the input may be either a fully qualified domain or a valid IP address entry. This test will look for both port 80 (HTTP) and
  port 443 (HTTPS) accessible.
  Program notes: The function test_invalid_url_as_fqdn_or_ip is used, and it also uses is_dns_resolvable, and may use check_ping 
  and check_http_status.




I also set up a bash script called "test_url.sh" that tests many examples in the file "test.tsv".

Here's the self-documenting description of my functions from running help on them interactively:

        >>> sys.argv
		['check_http_url.py', '0.0.0.0']
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
	
			Note: if a domain_name is not resolvable, you will never reach it.
			The program will use the python 'requests' module to check http/https status and
			reachability since a ping test may fail for servers that block ping,i.e. www.abs.com.
	
			:return: boolean - True if resolvable or an IP address, else False

		>>> 
		>>> help(check_ping)
		Help on function check_ping in module __main__:

		check_ping(domain_name: str) -> bool
			check_ping attempts to ping a domain name and returns True if domain_name
			is accessible.
			check_ping uses the subprocess and the platform modules.
	
			Note: check_ping may help diagnose reachable IP with a server issue.
	
			:return: boolean - True if domain_name is pingable, else False

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
