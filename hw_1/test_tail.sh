
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

diff <(tail -n 10 a.txt b.txt ) <(./tail.py a.txt b.txt )
check_ok

diff <(tail -n 10 b.txt a.txt ) <(./tail.py b.txt a.txt )
check_ok

diff <(tail -n 10 a.txt c.txt ) <(./tail.py a.txt c.txt )
check_ok

diff <(tail -n 10 c.txt a.txt ) <(./tail.py c.txt a.txt )
check_ok

diff <(tail -n 10 a.txt b.txt c.txt ) <(./tail.py a.txt b.txt c.txt)
check_ok

diff <(tail -n 10 c.txt b.txt a.txt) <(./tail.py c.txt b.txt a.txt)
check_ok

diff <(tail -n 10 a.txt) <(./tail.py a.txt)
check_ok

diff <(tail -n 10 b.txt) <(./tail.py b.txt)
check_ok

diff <(tail -n 10 c.txt) <(./tail.py c.txt)
check_ok

stdin_test_1='1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18'

expected_1='2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18'

diff <(echo "$expected_1") <(echo "$stdin_test_1" | ./tail.py)
check_ok

stdin_test_2='1
2
3
'

expected_2='1
2
3
'

diff <(echo "$expected_2") <(echo "$stdin_test_2" | ./tail.py)
check_ok

./tail.py a b c > /dev/null 2>&1
check_not_ok

echo OK
