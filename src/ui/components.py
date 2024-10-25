"""
再利用可能なUIコンポーネント
"""
import streamlit as st
from typing import List, Tuple
import pandas as pd



##共通の関数
def clean_text(text):
    """辞書型や余分な記号を除去してテキストを整形"""
    if pd.isna(text):
        return ""
    
    # 文字列型への変換
    text = str(text)
    
    # (0, 'text') 形式の文字列から不要な部分を削除
    if text.startswith("(0,"):
        text = text.split("'")[1] if "'" in text else text.split(",", 1)[1]
    
    # 余分な記号を削除
    text = text.replace("{", "").replace("}", "").replace("[", "").replace("]", "")
    text = text.replace("(", "").replace(")", "").replace("'", "")
    
    # 先頭の数字とカンマを削除 (例: "0, " を削除)
    text = text.lstrip("0123456789, ")
    
    return text.strip()

def clean_filename(filename):
    """ファイル名から不要な部分を削除"""
    if pd.isna(filename):
        return ""
    
    # 文字列に変換
    filename = str(filename)
    
    # 拡張子を削除
    filename = filename.split('.')[0]
    
    # "【確定】" を削除
    filename = filename.replace("【確定】", "")
    
    # "-会議の録音" を削除
    filename = filename.replace("-会議の録音", "")
    
    # 日時部分を整形（オプション）
    if "_202" in filename:  # 2024年などの年を含む部分を検出
        filename_parts = filename.split("_")
        main_part = "_".join(filename_parts[:-1])  # 日時部分以外
        # date_part = filename_parts[-1][:8]  # YYYYMMDD部分を取得
        return main_part
    
    return filename.strip()

def split_points(text, max_points=5):
    """テキストを個別のポイントに分割"""
    text = clean_text(text).split("\n")
    # 空の要素を除去し、最大数に制限
    points = [p.strip() for p in points if p.strip()][:max_points]
    return points

def split_text_by_newline(text):
    """テキストを\nで分割し、空の要素を除去"""
    text = clean_text(text)
    if not text:
        return []
    return [t.strip() for t in text.split('\\n') if t.strip()]

