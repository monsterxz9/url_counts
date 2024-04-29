import pandas as pd

# 读取CSV文件，指定逗号作为分隔符
df = pd.read_csv('BrowserHistory_2024_4_28.csv', delimiter=',')

# 过滤包含 "bilibili" 的行
bilibili_df = df[df['NavigatedToUrl'].str.contains('pornhub')]

# 将结果保存到新的 CSV 文件中
bilibili_df.to_csv('pornhub_urls.csv', index=False, encoding='utf-16')
