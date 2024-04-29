import pandas as pd

# 读取CSV文件，指定逗号作为分隔符
df = pd.read_csv('your_csv', delimiter=',')

# 过滤包含 "bilibili" 的行
bilibili_df = df[df['NavigatedToUrl'].str.contains('bilibili')]

# 将结果保存到新的 CSV 文件中
bilibili_df.to_csv('bilibili_urls.csv', index=False, encoding='utf-16')
