# このアプリについて

gitbookでビルドされたhtmlファイルを編集するアプリケーションです

## 仮想環境

```txt
textfile == 0.1.5
```

## 使用上の注意

- .exeファイルの配置先

```txt
.
├── build
├── gitbook
│   ├── README.md
│   └── SUMMARY.md
└── main.exe : ここに配置する
```

- 置き換え対象は、gitbook直下のmdファイル（=ビルド後のhtmlファイル）と、gitbook配下に作成されたディレクトリ内のmdファイル

```txt
├── build
├── gitbook
│   ├── Chapter1
│   │    ├── Chapter1-1
│   │    │    └── About.md : 置き換え対象ではない
│   │    └── Abstract.md : 置き換え対象
│   ├── README.md : 置き換え対象
│   └── SUMMARY.md : 置き換え対象
└── main.exe : ここに配置する
```
