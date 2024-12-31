---
title: "FactioProject"
tags: ""
---

<div id="top"></div>

## 使用技術一覧
<!-- シールド一覧 -->
<!-- 該当するプロジェクトの中から任意のものを選ぶ-->
<p style="display: inline">
  <!-- バックエンドのフレームワーク一覧 -->
  <img src="https://img.shields.io/badge/-Django-092E20.svg?logo=django&style=for-the-badge">
  <!-- バックエンドの言語一覧 -->
  <img src="https://img.shields.io/badge/-Python-F2C63C.svg?logo=python&style=for-the-badge">
<img src="https://img.shields.io/badge/-Javascript-F7DF1E.svg?logo=javascript&style=for-the-badge">
<img src="https://img.shields.io/badge/-Html5-E34F26.svg?logo=html5&style=for-the-badge">
<img src="https://img.shields.io/badge/-Css3-1572B6.svg?logo=css3&style=for-the-badge">
  <img src="https://img.shields.io/badge/-Bootstrap-563D7C.svg?logo=bootstrap&style=for-the-badge">
</p>


## プロジェクト名
### FactioProject

## 目次

1. [プロジェクトについて](#プロジェクトについて)
2. [環境](#環境)
3. [環境構築](#環境構築)
4. [ディレクトリ構成](ディレクトリ構成)
5. [機能発展](#機能発展)



## プロジェクトについて
<br>
自分の好きな組み合わせでファッションを作ったり、共有したりすることが可能なファッションカスタマイズサイトです。アイテム単体を購入することも出来ますが、ユーザーが自分でカスタマイズしたアイテムの組み合わせを購入したり、ユーザー同士で共有することが出来ます。また、コラボ商品以外の他ブランド同士のファッションカスタマイズを可能とすることも目的としています。ファッションの可能性が広がり、より多くのユーザーに楽しんでもらえることを期待しています。
<br><br>ライブラリーが豊富で今後の保守性や開発する際に作業を行いやすいと考え、Djangoで開発しました。</br>


## デモ(図解)
![Factio_Demo2.png](https://boostnote.io/api/teams/ZiDFKbzPj/files/6961a23674c2f79d2c2233c0c35ed3f9179c3d8d9cea3a77d21d2dbed35f9332-Factio_Demo2.png)
![sidekick_GO5MtOqrPz.png](https://boostnote.io/api/teams/ZiDFKbzPj/files/71076c61fbceaa292946cff9cf9f19048c222a60a2ca66ae0d873177abbea345-sidekick_GO5MtOqrPz.png)


## 環境

<!-- 言語、フレームワーク、ミドルウェア、インフラの一覧とバージョンを記載 -->

| 言語・フレームワーク  | バージョン |
| --------------------- | ---------- |
| Python                | 3.12.5     |
| dictknife             | 0.14.1     |
| Django                | 5.1.1      |
| django_allauth        | 65.3.0     |
| Pillow                | 11.0.0     |
| Requests              | 2.32.3     |
| django-bootstrap-datepicker-plus   | 5.0.5  |
| django-cleanup        | 9.0.0      |
| django-widget-tweaks  | 1.5.0      |
| MySQL                 | 8.4.3      |
| Nginx                 | 1.27.3     |
| Gunicorn              | 23.0.0     |
| mysqlclient|2.2.6|


<br>

## 環境構築
### Dockerで環境を構築する場合
Pythonにて以下の設定を行ってください。
## 本番環境
1.設定をする

```
.env.prod

MYSQL_ROOT_PASSWORD=root
MYSQL_DATABASE=movie-db
MYSQL_USER=factio
MYSQL_PASSWORD=movie-prod
# SECRET_KEYについては本番環境では推測されない値に変更しておきましょう
SECRET_KEY=
ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
# 本番環境のためFalse
DEBUG=True
```
2.環境を構築する

```
docker-compose -f docker-compose.prod.yml build
docker-compose -f docker-compose.prod.yml up -d
```

Dockerのdocker-compose.prod.ymlがある階層で上記のコマンドを入力して環境を構築する。


3.スーパーユーザーを作成
まずはコンテナの中へ入る。
```
docker exec -it コンテナ名 bash
(Linuxはbash/bin)
```
その後にmanage.pyのある階層へ移動する
```
cd src
```
そして、下記のコマンドを実行してCIに表示される指示に従ってアカウントを作成する。
(管理者用アカウントが要らない人は飛ばしてもいいです。)
```
pyhton manage.py createsuperuser
```

を入力して完成。


 ## 開発環境
1.設定をする

```
.env

MYSQL_ROOT_PASSWORD=root
MYSQL_DATABASE=movie-db
MYSQL_USER=factio
MYSQL_PASSWORD=movie
# SECRET_KEYに任意の値を入力
SECRET_KEY=
ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
# 開発環境のためTrue
DEBUG=True
```

2.環境を構築する

```
docker-compose -f docker-compose.yml build
docker-compose -f docker-compose.yml up -d
```

Dockerのdocker-compose.ymlがある階層で上記のコマンドを入力して環境を構築する。


3.スーパーユーザーを作成

まずはコンテナの中へ入る。
```
docker exec -it コンテナ名 bash
(Linuxはbash/bin)
```
その後にmanage.pyのある階層へ移動する
```
cd src
```
そして、下記のコマンドを実行してCIに表示される指示に従ってアカウントを作成する。
(管理者用アカウントが要らない人は飛ばしてもいいです。)
```
pyhton manage.py createsuperuser
```

を入力して完成。

<br>

## ディレクトリ構成

└──accounts
    │   ├── __pycache__
    │   ├── migrations
    │   │   └── __pycache__
    │   └── templates
    │       └── accounts
    │           ├── inquiry
    │           ├── login
    │           ├── password
    │           ├── profile
    │           └── register
    │               └── txt
    │                   └── mail_template
    │                       └── create
    ├── app
    │   ├── __pycache__
    │   ├── collected_static
    │   │   ├── admin
    │   │   │   ├── css
    │   │   │   │   └── vendor
    │   │   │   │       └── select2
    │   │   │   ├── fonts
    │   │   │   ├── img
    │   │   │   │   └── gis
    │   │   │   └── js
    │   │   │       ├── admin
    │   │   │       └── vendor
    │   │   │           ├── jquery
    │   │   │           ├── select2
    │   │   │           │   └── i18n
    │   │   │           └── xregexp
    │   │   └── css
    │   ├── migrations
    │   │   └── __pycache__
    │   ├── mysite
    │   │   └── __pycache__
    │   ├── static
    │   │   ├── accounts
    │   │   │   └── css
    │   │   ├── css
    │   │   ├── images
    │   │   └── js
    │   ├── templates
    │   │   └── app
    │   │       ├── blog
    │   │       ├── fashion
    │   │       │   └── review
    │   │       ├── review
    │   │       └── store
    │   └── templatetags
    │       └── __pycache__
    ├── mysite
    │   └── __pycache__
    └── static
        └── accounts
            └── css

59 directories
## 機能発展
AIを使用したユーザーの動向などを分析
<p align="right">(<a href="#top">トップへ</a>)</p>
