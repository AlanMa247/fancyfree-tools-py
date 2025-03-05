# fancyfree-tools-py

## json_tools.py
**处理json**
1. 支持json格式化
2. 支持json提取内容

**使用方式**
- 运行启动
  ```bash
  python json_tools.py
  ```
- 使用说明
  启动后如图

  <img src="https://github.com/user-attachments/assets/8a288e91-4918-4308-b6f2-7bae8d274eac" width="300px" alt="![image](https://github.com/user-attachments/assets/8a288e91-4918-4308-b6f2-7bae8d274eac)">


---
### 公共操作
#### 输入需要处理的json

```json
{"key1": "value1","keyObj": {"objKey1": "ObjValue1"},"keyArray": [{"arrayKey1": "arrayValue1","arrayKey2": "arrayValue2"},{"arrayKey1": "arrayValue11","arrayKey2": "arrayValue21"},{"arrayKey1": "arrayValue12","arrayKey2": "arrayValue22"},{"arrayKey1": "arrayValue13","arrayKey2": "arrayValue23"},{"arrayKey1": "arrayValue14","arrayKey2": "arrayValue24"},{"arrayKey1": "arrayValue15","arrayKey2": "arrayValue25"}],"key3": "value3"}
```

<img src="https://github.com/user-attachments/assets/947dcbfd-b8e3-4173-8142-7f7c667e7178" width="300px" alt="![image](https://github.com/user-attachments/assets/947dcbfd-b8e3-4173-8142-7f7c667e7178)">



   
---
### 格式化
#### 点解格式化json，格式完成输出

<img src="https://github.com/user-attachments/assets/884ab8df-9a9e-4229-b2c4-455b2e3f33c7" width="300px" alt="![image](https://github.com/user-attachments/assets/884ab8df-9a9e-4229-b2c4-455b2e3f33c7)">



--- 
### 提取内容
#### 输入需要提取的key，提取完成输出

```
key1|[]keyArray.arrayKey1|[]keyArray.arrayKey2
```

<img src="https://github.com/user-attachments/assets/47ca4598-2c7a-4c5d-97c1-121773b20ff4" width="300px" alt="![image](https://github.com/user-attachments/assets/47ca4598-2c7a-4c5d-97c1-121773b20ff4)">


  
