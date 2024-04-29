import pandas as pd

# 读取CSV文件，指定逗号作为分隔符
df = pd.read_csv('BrowserHistory_2024_4_28.csv', delimiter=',')

# 统计每个URL的访问次数
url_counts = df['NavigatedToUrl'].value_counts()

# 将统计结果写入CSV文件
url_counts.to_csv('url_counts.csv', header=['Count'])
