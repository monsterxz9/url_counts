# Browser History Analyzer

分析浏览器历史记录的命令行工具，已在 Edge 导出的浏览记录上测试。

## 使用方法

将浏览历史 CSV 文件放到此目录，然后运行对应命令。

### 查看 Top N 域名图表

```bash
python main.py top-domains history.csv
python main.py top-domains history.csv --top-n 20
```

### 按关键词过滤 URL

```bash
python main.py filter history.csv bilibili
python main.py filter history.csv youtube --output youtube_urls.csv
```

### 统计 URL 访问次数

```bash
python main.py count history.csv
python main.py count history.csv --output my_counts.csv
```

## CSV 格式

支持 Edge 导出的浏览记录格式，列名为：`DateTime`, `NavigatedToUrl`, `PageTitle`。
