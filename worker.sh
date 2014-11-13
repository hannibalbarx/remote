cd
wget -O config.ini http://pastebin.com/raw.php?i=7Zr3Fnbt
if [ -d "tradeSwift" ]; then
 rm -rf tradeSwift
fi
if [ -p "pipe0" ]; then
 rm  pipe*
fi
git clone git://github.com/hannibalbarx/tradeSwift.git
for ((i=0;i<`nproc`;i++))
do
        mkfifo pipe$i
        python tradeSwift/messenger.py<pipe$i |pypy tradeSwift/search_fast.py>pipe$i &
done