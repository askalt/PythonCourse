Проверка работоспособности:
```sh
$ diff <(wc a.txt b.txt ) <(./wc.py a.txt b.txt )

$ diff <(wc c.txt a.txt ) <(./wc.py c.txt a.txt )

$ diff <(wc c.txt b.txt a.txt) <(./wc.py c.txt b.txt a.txt)

$ diff <(wc b.txt) <(./wc.py b.txt)

$ ./test_wc.sh
OK
```

Автоматические тесты с бОльшим количеством кейсов [тут](../test_wc.sh).
