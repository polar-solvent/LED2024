# LED2024
## 概要
画像を右から左に流すためのコマンドです。
## インストール方法
[python公式ダウンロードページ](https://www.python.org/downloads/)からpythonをダウンロードして、pipをインストールしてからターミナルに
```sh
pip install git+https://github.com/polar-solvent/LED2024
```
と入力するとインストールできます。
## 使い方
### ledmaking
`ledmaking`は指定した画像ファイルを任意のpxずつずらしていき、そのすべての画像をbmp画像群として保存します。

複数の画像のファイルを指定することで、並列に並べた画像を保存することができます。

最初は真っ黒な画像から始まり、指定した画像が通り過ぎた後、真っ黒な画像となって終わります。

使用できるオプションは以下の通りです。
* `--upright`, `-u` …画像をずらす向きを90度変えます。デフォルトは横向きにずれていきますが、このオプションを入れると縦向きにずらすことができます。
* `--reverse`, `-r` …画像をずらす向きを逆転させます。デフォルトは枠の中で画像が右から左あるいは下から上にずれていきますが、このオプションを入れると左から右あるいは上から下にずらすことができます。
* `--arrange`, `-a` …画像を配置する場所を変えます。デフォルトは枠の上側にそろえ、1を入力すると枠の真ん中にそろえ、2を入力すると枠の下側にそろえます。なお、0はデフォルトと同じです。0~2以外を入力するとエラーとなります。
* `--width`, `-W` …出力する画像の横幅(ずらす方向)をpxで指定します。デフォルトは入力した画像全ての横幅の和となります。1以上の整数での入力を受け付けています。
* `--height`, `-H` …出力する画像の縦幅(ずらさない方向)をpxで指定します。デフォルトは入力した画像のうち最も縦幅が大きいものの縦幅となります。1以上の整数での入力を受け付けています。

    ※widthオプション、heightオプションで指定する「横幅」、「縦幅」は、uprightオプションによる向きの変更があった場合縦横が逆になります。つまり、widthは画像を**ずらす**方向、heightは画像を**ずらさない**方向の出力画像の幅を指定します。

* `--interval`, `-I` …出力する画像1枚ごとにずらす幅を指定します。デフォルトは1pxで、1以上出力する横幅(`--width`で指定)以下の整数での入力を受け付けています。
* `--dest`, `-d` …画像の出力先のディレクトリを指定します。デフォルトはカレントディレクトリ内の`assets/dest`です。仮に指定したディレクトリが存在しない場合でも、自動的にディレクトリが作成されます。
* `--name`, `-n` …出力する画像の名前を指定します。デフォルトは`frame_(0以上の数字).bmp`です。このオプションでは`frame`の部分だけを変えられます。


使用例：
```sh
ledmaking ./assets/src/snow.bmp -W 192 -I 3 -n snow -d ./assets/dest/snow
```
上記の例で実行すると、カレントディレクトリ内の`assets/src/snow.bmp`という画像を読み込み、横幅192pxの枠の中で指定した画像が3pxずつ右から左へとずれた画像群が保存されます。場所はカレントディレクトリ内の`assets/dest/snow`で、`snow_0.bmp`～`snow_xxx.bmp`という名前で保存されています。
![snow192_i3](./docs/snow192_i3.mp4)


また、次のような使い方をすることもできます。
```sh
ledmaking ./assets/src/snow.bmp -W 192 -I 192 -n snow_p192 -d ./assets/dest/snow_p192
```
上記の例で実行すると、`snow.bmp`という画像を左から192pxずつ切り取った画像が保存されます。
![snow_p192](./docs/snow_p192.mp4)


そして、このような使い方をすることもできます。
```sh
ledmaking ./assets/src/rapid.bmp -u -r -n rapid_ur -d ./assets/dest/rapid_ur
```
上記の例で実行すると、`rapid.bmp`という画像を、画像と同じ大きさの枠内で上から下へ1pxずつずらした画像が保存されます。
![rapid_ur](./docs/rapid_ur.mp4)


さらに、次のような使い方をすることもできます。
```sh
ledmaking ./assets/src/special_rapid.bmp ./assets/src/rapid.bmp ./assets/src/local.bmp -u -a 1 -W 32 -H 144 -n curtain
```
上記の例で実行すると、`special_rapid.bmp`、`rapid.bmp`、`local.bmp`の3つの画像を縦に並べ、縦32px、横144pxの枠の中央で下から上へ1pxずつずらした画像が保存されます。

---

### ledshowing
ledshowingは、ledmakingで保存した画像群のうち1枚を指定し、同じディレクトリ内の名前部分が同じ画像を右から左へ流れるように表示します。

qのキーが押された場合、そこで表示が終了されます。

使用できるオプションは以下の通りです。
* `--fps`, `-f` …画像を表示する速さを指定します。デフォルトは1秒に60枚の表示で、入力する数字が大きいほど速く表示され、小さいほど遅く表示されます。1秒に1枚未満、あるいは1秒に1000枚より多い数の画像を表示することはできません。
* `--save`, `-s` …表示された画像群をmp4形式の動画にして保存します。`(保存するディレクトリ)/(保存する名前).mp4`と入力すると、指定したディレクトリ内で指定した名前で保存されます。デフォルトはカレントディレクトリ内の`assets/dest`で`video.mp4`と言う名前で保存されます。

使用例：
```sh
ledshowing ./assets/dest/snow/snow_0.bmp -f 30
```
上記の例で実行すると、カレントディレクトリ内の`assets/dest/snow`内にある、`snow_(数字).bmp`という名前の画像を読み込み、`snow_0.bmp`から`snow_xxx.bmp`までのすべての画像を1秒に30枚の速さで表示します。

また、次のような使い方をすることもできます。
```sh
ledshowing ./assets/dest/snow/snow_0.bmp -f 180 -s ./assets/dest/videos/snow.mp4
```
上記の例で実行すると、カレントディレクトリ内の`assets/dest/videos`というフォルダに`snow.mp4`という名前で、1秒に180枚の速さで表示される画像群がmp4形式で保存されます。
![snow192_i3_180](./docs/snow192_i3_180fps.mp4 "保存される動画")

