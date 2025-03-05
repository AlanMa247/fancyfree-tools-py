import csv
import json
import tkinter as tk
from tkinter import messagebox, scrolledtext
import pandas as pd
from io import StringIO
from itertools import zip_longest


def format_json():
    """
    格式化 JSON 并在文本框中显示，确保 JSON 使用双引号
    """
    try:
        raw_json = text_input.get("1.0", tk.END).strip()
        parsed = json.loads(raw_json)
        formatted_json = json.dumps(parsed, indent=4, ensure_ascii=False)

        text_output.delete("1.0", tk.END)
        text_output.insert(tk.END, formatted_json)
    except json.JSONDecodeError as e:
        messagebox.showerror("JSON 解析错误", f"无效的 JSON 格式:\n{e}")


def extract_from_json(data, keys):
    """
    递归解析 JSON 数据，支持 `.` 分层提取，`[]` 代表数组字段
    """

    def get_value(d, key_chain):
        keys = key_chain.split('.')
        extract_list = False
        if keys[0].startswith('[]'):
            extract_list = True
            keys[0] = keys[0][2:]

        for key in keys:
            if isinstance(d, dict):
                d = d.get(key, "Key not found")
            elif isinstance(d, list):
                if extract_list:
                    d = [item.get(key, "Key not found") for item in d if isinstance(item, dict)]
                else:
                    return "Invalid path"
            else:
                return "Invalid path"
        return d

    extracted_data = {}
    for key in keys:
        extracted_data[key] = get_value(data, key)
    return extracted_data


def extract_json():
    """
    从 JSON 提取指定的字段，并格式化为表格
    """
    try:
        raw_json = text_input.get("1.0", tk.END).strip()
        parsed = json.loads(raw_json)

        extract_keys = extract_key.get().strip()
        if not extract_keys:
            messagebox.showwarning("输入错误", "请输入要提取的键值路径，例如 code|[]list.crt")
            return

        key_list = extract_keys.split('|')
        extracted = extract_from_json(parsed, key_list)

        table_data = list(
            zip_longest(*[extracted[k] if isinstance(extracted[k], list) else [extracted[k]] for k in key_list],
                        fillvalue=""))

        df = pd.DataFrame(table_data, columns=key_list)

        df.replace("", None, inplace=True)
        df.fillna(method="ffill", inplace=True)

        for col in df.columns:
            df[col] = df[col].apply(lambda x: json.dumps(x, ensure_ascii=False) if isinstance(x, dict) else x)

        output = StringIO()

        # 根据勾选状态选择 QUOTE_ALL 或 QUOTE_NONE
        quote_option = csv.QUOTE_ALL if quote_all_var.get() else csv.QUOTE_NONE

        df.to_csv(output, sep='|', index=False, header=False, quoting=quote_option)
        output_value = output.getvalue().strip()

        text_output.delete("1.0", tk.END)
        text_output.insert(tk.END, output_value)
    except json.JSONDecodeError as e:
        messagebox.showerror("JSON 解析错误", f"无效的 JSON 格式:\n{e}")


# 创建 GUI 窗口
root = tk.Tk()
root.title("JSON 格式化 & 提取工具")
root.geometry("700x650")

# JSON 输入框
tk.Label(root, text="输入 JSON:").pack(anchor="w", padx=10, pady=2)
text_input = scrolledtext.ScrolledText(root, height=10)
text_input.pack(fill=tk.BOTH, padx=10, pady=5, expand=True)

# 提取关键字输入框
tk.Label(root, text="输入要提取的键值路径 (例如 code|[]list.crt):").pack(anchor="w", padx=10, pady=2)
extract_key = tk.Entry(root)
extract_key.pack(fill=tk.X, padx=10, pady=5)
extract_key.insert(0, "code|[]list.crt")

# 复选框（控制 QUOTE_ALL 还是 QUOTE_NONE）
quote_all_var = tk.BooleanVar(value=True)  # 默认选中
quote_checkbox = tk.Checkbutton(root, text="CSV 输出使用 QUOTE_ALL", variable=quote_all_var)
quote_checkbox.pack(anchor="w", padx=10, pady=5)

# 按钮区
button_frame = tk.Frame(root)
button_frame.pack(pady=5)

format_button = tk.Button(button_frame, text="格式化 JSON", command=format_json)
format_button.pack(side=tk.LEFT, padx=5)

extract_button = tk.Button(button_frame, text="提取数据", command=extract_json)
extract_button.pack(side=tk.LEFT, padx=5)

# JSON 输出框
tk.Label(root, text="输出:").pack(anchor="w", padx=10, pady=2)
text_output = scrolledtext.ScrolledText(root, height=10)
text_output.pack(fill=tk.BOTH, padx=10, pady=5, expand=True)

# 运行主窗口
root.mainloop()
