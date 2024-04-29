import pandas as pd
import matplotlib.pyplot as plt
from urllib.parse import urlparse
import seaborn as sns
import numpy as np
def extract_domain(url):
    parsed_uri = urlparse(url)
    domain = '{uri.netloc}'.format(uri=parsed_uri)
    return domain

# 读取CSV文件
df = pd.read_csv('yourcsv', delimiter=',',names=['DateTime', 'NavigatedToUrl', 'PageTitle'])


# 将URL列中的每个URL提取为主域名
df['Domain'] = df['NavigatedToUrl'].apply(extract_domain)

# 计算每个主域名的访问次数
domain_counts = df['Domain'].value_counts()

# 只保留前10个主域名
top_domains = domain_counts.head(10)
# 使用Seaborn设置样式和主题
sns.set_theme(style="whitegrid")  # 设置主题和样式
gradient = np.linspace(0, 1, 100).reshape(1, -1)
plt.imshow([gradient], aspect='auto', cmap='viridis', extent=(0, 10, 0, 1))

# 创建图表
plt.figure(figsize=(12, 8))
sns.barplot(x=top_domains.index, y=top_domains.values, hue=top_domains.index, palette="viridis", legend=False)
plt.title('Top 10 Visited Domains', fontsize=20)
plt.xlabel('Domain', fontsize=16)
plt.ylabel('Number of Visits', fontsize=16)
plt.xticks(rotation=45, ha='right', fontsize=12)
plt.yticks(fontsize=12)
plt.tight_layout()

# 显示图表
plt.show()

