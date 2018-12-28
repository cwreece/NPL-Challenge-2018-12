#!/bin/bash

prog=${1:-check_http_url.py}

function test_url
{
	local url=$1
	python3.7 $prog $url
}

echo "#################################################################"
echo "This bash script tests multiple URLs found in the test.tsv file"
echo "against $prog - either a specified python script or a default script"
echo "and compares the results the against the expected results."
echo "#################################################################"

while read url expected_result
do
	echo "     "
	echo "     "
    echo ".......  testing a new URL"
	echo "######################################################"
	printf "# URL: %-50s \n" $url
	printf "# Expected Result: %-50s \n" $expected_result
	echo "######################################################"
	echo "     "

	test_url $url
done <test.tsv
