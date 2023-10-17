# 絵描き詠み

表示される和歌のイメージを絵にしていろんな人と共有するWebアプリ(現在は非公開)

![image](https://github.com/nakaji-nandaina/EkakiYomi/assets/65334953/958b65c4-2ffd-45a7-8d49-46ccac749b1e)


![image](https://github.com/nakaji-nandaina/EkakiYomi/assets/65334953/55d0e165-2a34-4717-9d11-bb1533fb5cb3)

## colab＆localtonelで公開できます

colabとlocaltonelを使うことでサーバを借りる必要も自分のPCをサーバにする必要もなくウェブアプリの公開ができます。

colabのセッションが切れると非公開になる上URLも変化してしまいますが、サーバ費用が掛からないのでハッカソンなど短い期間だけアプリを公開したい場合は有効だと思います。


### ウェブアプリ（絵描き詠み）の公開方法

EkakiYomiフォルダーをダウンロードしてGoogleDriveのMyDriveに保存

EkakiYomi.ipynbを開いて上から順に実行する

以上！

app.pyの中身を書き換えれば自由にウェブアプリが出来ます。

（元々はFireBaseStorage等をデータベースとして使っていましたが、今回は他の人がすぐ動かせる様にdriveに設置したdataフォルダー内に他の人が描いた絵を直接ぶち込む仕様に。）
