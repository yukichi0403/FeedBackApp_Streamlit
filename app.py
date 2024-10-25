"""
メインアプリケーション
"""
import streamlit as st
import pandas as pd
from src.config import load_config
from src.data_providers import FeedbackDataProvider
from src.ui.styles import apply_custom_css
from src.ui.views import display_sales_summary
import logging

# ロギングの設定
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    # カスタムCSSの適用
    apply_custom_css()
    
    try:
        # 設定の読み込みとデータプロバイダーの初期化
        config = load_config()
        data_provider = FeedbackDataProvider(config, logger)
        
        # データの取得
        df = data_provider.get_feedback_data()
    
        
        # サイドバーフィルター
        st.sidebar.markdown('<p class="sub-header">フィルター設定</p>', unsafe_allow_html=True)
        
        # 作成者でフィルタリング
        creators = df['created_by'].unique()
        selected_creator = st.sidebar.selectbox(
            "作成者で絞り込み",
            options=creators
        )
        
        filtered_df = df[df['created_by'] == selected_creator]
        
        selected_record = st.sidebar.selectbox(
            "表示するレコードを選択",
            options=filtered_df.index,
            format_func=lambda x: f"Record {x} - {filtered_df.loc[x, 'file_name']}"
        )
        
        # メインビューの表示
        display_sales_summary(filtered_df, selected_record)
        
    except Exception as e:
        logger.error(f"アプリケーションエラー: {str(e)}", exc_info=True)
        st.error(f"エラーが発生しました: {str(e)}")

if __name__ == "__main__":
    main()