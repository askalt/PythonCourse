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

diff <(wc a.txt b.txt ) <(./wc.py a.txt b.txt )
check_ok

diff <(wc b.txt a.txt ) <(./wc.py b.txt a.txt )
check_ok

diff <(wc a.txt c.txt ) <(./wc.py a.txt c.txt )
check_ok

diff <(wc c.txt a.txt ) <(./wc.py c.txt a.txt )
check_ok

diff <(wc a.txt b.txt c.txt ) <(./wc.py a.txt b.txt c.txt)
check_ok

diff <(wc c.txt b.txt a.txt) <(./wc.py c.txt b.txt a.txt)
check_ok

diff <(wc a.txt) <(./wc.py a.txt)
check_ok

diff <(wc b.txt) <(./wc.py b.txt)
check_ok

diff <(wc c.txt) <(./wc.py c.txt)
check_ok

test_input='laallal
tralalal
string and string
и русский текст
'

diff <(echo " 5  8 65") <(echo "$test_input" | ./wc.py)
check_ok

echo OK