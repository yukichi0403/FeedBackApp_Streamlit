import streamlit as st
import pandas as pd
import os


CUSTOM_CSS="""
<style>
    /* ベーススタイル */
    .section-container {
        margin: 30px 0;
        padding: 20px;
        background-color: white;
        border-radius: 8px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }
    
    /* ヘッダースタイル */
    .main-header {
        display: flex;
        font-weight: bold;
        flex-direction: column;
        gap: 10px;
        margin-bottom: 20px;
        font-size: 24px;
    }
    
    .sub-header {
        display: flex;
        font-weight: bold;
        flex-direction: column;
        gap: 10px;
        margin-bottom: 20px;
        font-size: 18px;
        color: #333;
        padding-bottom: 10px;
        border-bottom: 2px solid #f0f0f0;
    }

    /* コピー用テキストエリアのスタイル更新 */
    .kintone-copy-text {
        background-color: #f5f5f5;
        border: 1px solid #ddd;
        border-radius: 4px;
        padding: 12px;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
        font-size: 14px;
        line-height: 1.5;
        margin: 5px 0;
        color: #333;
    }
    
    /* 概要セクションのスタイル */
    .summary-section {
        display: flex;
        flex-direction: column;
        gap: 15px;
        margin-bottom: 25px;
    }
    
    .summary-card {
        background-color: white;
        padding: 15px;
        border-radius: 5px;
        border: 1px solid #ddd;
        margin: 5px 0;
    }
    
    .summary-label {
        font-size: 14px;
        font-weight: bold;
        color: #666;
        margin-bottom: 8px;
    }
    
    .summary-content {
        font-size: 14px;
        color: #333;
        line-height: 1.4;
    }
    
    /* ポイントカードのスタイル（既存を維持） */
    .point-card {
        background-color: white;
        padding: 15px;
        margin: 10px 0;
        border-radius: 5px;
        border: 1px solid #ddd;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    .positive-point {
        border-left: 4px solid #4CAF50;
    }
    
    .improvement-point {
        border-left: 4px solid #FF5722;
    }
    
    .point-title {
        font-size: 16px;
        font-weight: bold;
        margin-bottom: 10px;
        color: #333;
    }
    
    .point-content {
        font-size: 14px;
        color: #666;
        line-height: 1.6;
    }
    
    /* 情報グリッドのスタイル */
    .grid-container {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 20px;
        margin: 15px 0;
    }
    
    /* 情報カードのスタイル */
    .info-card {
        background-color: white;
        padding: 15px;
        margin: 15px 0;
        border-radius: 6px;
        border: 1px solid #e0e0e0;
    }
    
    .label {
        font-size: 14px;
        font-weight: bold;
        color: #666;
        margin-bottom: 8px;
    }
    
    .value {
        font-size: 14px;
        color: #333;
        line-height: 1.6;
        padding: 8px;
        background-color: #f8f9fa;
        border-radius: 4px;
    }
    
    /* その他の情報セクション */
    .other-info-section {
        display: grid;
        grid-template-columns: 1fr;
        gap: 15px;
        margin: 20px 0;
    }
</style>
"""

def apply_custom_css():
    """カスタムCSSをアプリケーションに適用"""
    st.markdown(CUSTOM_CSS, unsafe_allow_html=True)