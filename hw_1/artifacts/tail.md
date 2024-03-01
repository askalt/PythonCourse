Проверка работоспособности:
```sh
$ diff <(tail -n 10 a.txt b.txt ) <(./tail.py a.txt b.txt )

$ diff <(tail -n 10 b.txt a.txt ) <(./tail.py b.txt a.txt )

$ diff <(tail -n 10 a.txt) <(./tail.py a.txt)

$ ./test_tail.sh
OK
```

Автоматические тесты с бОльшим количеством кейсов [тут](../test_tail.sh).
