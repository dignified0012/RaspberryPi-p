#!/bin/sh

# LCDの初期化
i2cset -y 2 0x3e 0 0x38 0x39 0x14 0x78 0x5f 0x6a i
#   -y: 確認メッセージをパス
#    1: I2Cバスを指定
# 0x3e: アドレスを指定 0x3eに対してのデータ
#    0: RS=0で、データではなくコマンド？
# 以下コマンド（詳細は後ろのLCD取扱説明書の制御コマンド一覧を参照）
# 0x38: 機能設定コマンド 8bitモード、2行表示、通常フォント、命令テーブル0
# 0x39: 機能設定コマンド 8bitモード、2行表示、通常フォント、命令テーブル1
#       → ビットモードは、2度設定しないと反映されないらしい
#       → 命令テーブル1のコマンドを仕様するため、命令テーブル1を選択
# 0x14: 内部OSC周波数セット
# 0x78: コントラストセット
# 0x5f: コントラストセット
# 0x6a: フォロアコントロール
#    i: 連続書き込みモード

sleep 0.3
i2cset -y 2 0x3e 0 0xc 0x1 i
# 0x0c: ディスプレイ表示ON
# 0x01: ディスプレイ表示内容をクリア DDRAMメモリに0を設定

sleep 0.3
i2cset -y 2 0x3e 0 0x6 i
# 0x06: エントリモード設定 書き込み後にカーソルを右へ移動するように設定
sleep 0.3

# 文字を出力（1行目）
i2cset -y 2 0x3e 0 0x80 b
# 0x80: Write Data to RAM
# b: バイトでの通常書き込みモード

i2cset -y 2 0x3e 0x40 0x48 0x65 0x6c 0x6c 0x6f 0x2c i
# 0x40: RS=1でコマンドではなくデータ？
# 以下データ（詳細は後ろのLCD取扱説明書の表示文字コード表を参照）
# 0x48: H
# 0x65: e
# 0x6c: l
# 0x6c: l
# 0x6f: o
# 0x2c: ,

# 文字を出力（2行目）
i2cset -y 2 0x3e 0 0xc0 b
# 0xc0: Read Data from RAM リードしたら改行される？

i2cset -y 2 0x3e 0x40 0x57 0x6f 0x72 0x6c 0x64 0x21 i
# 0x57: W
# 0x6f: o
# 0x72: r
# 0x6c: l
# 0x64: d
# 0x21: !
