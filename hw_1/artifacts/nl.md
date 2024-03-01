Проверка работоспособности:
```sh
$ ./nl.py
rlrl
     1	rlrl
relrelrel;rerle;
     2	relrelrel;rerle;

     3
rwlerlew;
     4	rwlerlew;
^C
Aborted!

$ ./nl.py test.txt
     1	1
     2
     3	a
     4
     5	fdlf;dl
     6
     7
     8	3444313
     9
    10	lol

$ diff <(./nl.py test.txt) <(nl -b a test.txt)

$ echo $?
0

$ ./test_nl.sh
OK
```

Автоматические тесты с бОльшим количеством кейсов [тут](../test_nl.sh).
