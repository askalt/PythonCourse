#!/bin/bash

check_ok() {
    if [ $? -ne 0 ]; then
        echo "Error"
        exit 1
    fi
}

check_not_ok() {
    if [ $? -eq 0 ]; then
        echo "Error expected"
        exit 1
    fi
}

diff <(./nl.py test.txt) <(nl -b a test.txt)
check_ok

diff <(echo "a\nb\n\nc\lala" | ./nl.py) <(echo "a\nb\n\nc\lala" | nl -b a)
check_ok

./nl.py a b c > /dev/null 2>&1
check_not_ok

./nl.py test.txt test.txt > /dev/null 2>&1
check_not_ok

echo OK
