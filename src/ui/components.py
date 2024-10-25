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
    if isinstance(text, str):
        if text.startswith("{0:"):
            text = text.split("'")[1] if "'" in text else text.split(":")[1]
        text = text.replace("{", "").replace("}", "").replace("[", "").replace("]", "")
        return text.strip()
    elif isinstance(text, dict):
        text = text[0]
    return str(text)

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

