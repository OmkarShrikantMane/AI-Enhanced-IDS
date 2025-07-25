import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler

# Sample dummy data for example
data = {
    'duration': [0, 0, 2],
    'protocol_type': ['tcp', 'udp', 'icmp'],
    'src_bytes': [491, 146, 0],
    'dst_bytes': [0, 0, 0],
    'label': ['normal', 'normal', 'attack']
}
df = pd.DataFrame(data)

# Encode categorical
df['protocol_type'] = LabelEncoder().fit_transform(df['protocol_type'])
df['label'] = LabelEncoder().fit_transform(df['label'])

scaler = StandardScaler()
X = scaler.fit_transform(df.drop('label', axis=1))
df_scaled = pd.DataFrame(X, columns=['duration', 'protocol_type', 'src_bytes', 'dst_bytes'])
df_scaled['label'] = df['label']

df_scaled.to_csv('processed.csv', index=False)
print("Data preprocessing complete.")
