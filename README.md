# pythonでpip installでinstallできるlibraryを作成する。

下記参照
https://qiita.com/icoxfog417/items/edba14600323df6bf5e0
https://qiita.com/xecus/items/49cbceacae97fb2a078f

# libraryの使い方
```shell script
pip install <this directory path>
```
or for exitable
```shell script
pip install -e <this directory path>
```
or
```shell script
pip install git+<url>
```

```python
import mylib
mylib.generate_random(123)
```