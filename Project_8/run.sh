# zsh code for my mac :)
n=2000000
k=2000000

perl -p -e "s/# Wersja2 //" Ułamek.py > Ułamek2.py

echo "With __slots__"
/usr/bin/time -al -p python3 Ułamek.py $n $k 2>&1 1>/dev/null | grep  -E "real|max"
/usr/bin/time -al -p python3 Ułamek.py $n $k 2>&1 1>/dev/null | grep  -E "real|max"
/usr/bin/time -al -p python3 Ułamek.py $n $k 2>&1 1>/dev/null | grep  -E "real|max"
/usr/bin/time -al -p python3 Ułamek.py $n $k 2>&1 1>/dev/null | grep  -E "real|max"
echo "Without __slots__"
/usr/bin/time -al -p python3 Ułamek2.py $n $k 2>&1 1>/dev/null | grep  -E "real|max"
/usr/bin/time -al -p python3 Ułamek2.py $n $k 2>&1 1>/dev/null | grep  -E "real|max"
/usr/bin/time -al -p python3 Ułamek2.py $n $k 2>&1 1>/dev/null | grep  -E "real|max"
/usr/bin/time -al -p python3 Ułamek2.py $n $k 2>&1 1>/dev/null | grep  -E "real|max"

