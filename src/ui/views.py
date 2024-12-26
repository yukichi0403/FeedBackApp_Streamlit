"""
メインビューの定義
"""
import streamlit as st
import pandas as pd
from .components import (
    clean_text,
    split_text_by_newline,
    clean_filename
)
import pyperclip
import json

#各セクションごとの関数
def display_summary_section(text, label):
    """概要セクションの表示"""
    st.markdown(f"""
        <div class="summary-card">
            <div class="summary-label">{label}</div>
            <div class="summary-content">{clean_text(text)}</div>
        </div>
    """, unsafe_allow_html=True)

def display_kintone_copy_section(text: str):
    """Kintoneコピー用テキストセクションの表示（スタイル適用版）"""
    # テキストとコピーボタンを含むコンテナ
    with st.container():
        col1, col2 = st.columns([10, 1])
        
        with col1:
            # スタイル適用済みのテキストエリア
            st.markdown(f"""
                <div class="kintone-copy-text">
                    {clean_text(text)}
                </div>
            """, unsafe_allow_html=True)
        
        # with col2:
        #     # コピーボタンを上寄せで配置
        #     st.markdown('<div style="margin-top: 12px;">', unsafe_allow_html=True)
        #     if st.button("📋", key="copy_kintone_text", help="クリックでコピー"):
        #         pyperclip.copy(clean_text(text))
        #         st.toast("コピーしました！", icon="✅")
        #     st.markdown('</div>', unsafe_allow_html=True)

def display_point_details(points, point_type="positive"):
    """ポイントの詳細表示"""
    for i, point in enumerate(points, 1):
        if ":" in point:  # タイトルと内容が:で区切られている場合
            title, content = point.split(":", 1)
        else:
            title = f"{point_type=='positive' and '良かった点' or '改善点'} {i}"
            content = point
            
        st.markdown(f"""
            <div class="point-card {point_type}-point">
                <div class="point-title">{title}</div>
                <div class="point-content">{content}</div>
            </div>
        """, unsafe_allow_html=True)


def display_point_card(point, index, point_type="positive"):
    """個別のポイントカードを表示"""
    class_name = "positive-point" if point_type == "positive" else "improvement-point"
    st.markdown(f"""
        <div class="point-card {class_name}">
            <div class="point-title">{point_type == "positive" and "良かった点" or "改善点"} {index + 1}</div>
            <div class="point-content">{point}</div>
        </div>
    """, unsafe_allow_html=True)


def display_date_section(df, selected_record):
    """重要な日程セクションの表示"""
    st.markdown('<div class="section-container">', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">重要な日程</div>', unsafe_allow_html=True)
    
    dates_html = f"""
    <div class="grid-container">
        <div class="info-card">
            <div class="label">トライアル開始日</div>
            <div class="value">{df.loc[selected_record, 'trial_start']}</div>
        </div>
        <div class="info-card">
            <div class="label">契約開始日</div>
            <div class="value">{df.loc[selected_record, 'contract_start']}</div>
        </div>
        <div class="info-card">
            <div class="label">次回ミーティング</div>
            <div class="value">{df.loc[selected_record, 'next_meeting']}</div>
        </div>
    </div>
    """
    st.markdown(dates_html, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

def display_other_info(df, selected_record):
    """その他の情報セクションの表示"""
    st.markdown('<div class="section-container">', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">その他の情報</div>', unsafe_allow_html=True)
    
    info_html = f"""
    <div class="other-info-section">
        <div class="info-card">
            <div class="label">期待ARR</div>
            <div class="value">{clean_text(df.loc[selected_record, 'expected_arr'])}</div>
        </div>
        <div class="info-card">
            <div class="label">議論された課題</div>
            <div class="value">{clean_text(df.loc[selected_record, 'customer_issues_discussed'])}</div>
        </div>
        <div class="info-card">
            <div class="label">ROI説明</div>
            <div class="value">{clean_text(df.loc[selected_record, 'roi_explanation'])}</div>
        </div>
        <div class="info-card">
            <div class="label">差別化ポイント</div>
            <div class="value">{clean_text(df.loc[selected_record, 'differentiation_explained'])}</div>
        </div>
        <div class="info-card">
            <div class="label">特記事項</div>
            <div class="value">{clean_text(df.loc[selected_record, 'notable_item'])}</div>
        </div>
    </div>
    """
    st.markdown(info_html, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)


def display_sales_summary(df, selected_record):
    st.markdown('<p class="main-header">商談サマリー</p>', unsafe_allow_html=True)
    
    # 商談名の表示
    filename = clean_filename(df.loc[selected_record, 'file_name'])
    st.markdown(f'<p class="sub-header" style="color: #666; font-size: 16px; margin-top: -10px;">{filename}</p>', 
               unsafe_allow_html=True)
    
    # 商談概要セクション
    st.markdown('<p class="sub-header">商談概要</p>', unsafe_allow_html=True)
    
    # 各項目を縦に表示
    st.markdown('<div class="summary-section">', unsafe_allow_html=True)
    for label, field in [
        ("概要", "main_points"),
        ("進捗", "overall_progress"),
        ("成功確率", "success_probability")
    ]:  
        display_summary_section(df.loc[selected_record, field], label)
    
    # Kintoneコピー用テキストセクション
    st.markdown('<div class="summary-section">', unsafe_allow_html=True)
    st.markdown('<p class="section-header">Kintoneコピー用テキスト</p>', unsafe_allow_html=True)
    display_kintone_copy_section(df.loc[selected_record, 'summary_for_kintone'])
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # 以下は既存のコードと同じ
    # 良かった点と改善点
    st.markdown('<p class="sub-header">良かった点と改善点</p>', unsafe_allow_html=True)
    cols = st.columns(2)    
    with cols[0]:
        st.markdown('<p class="section-header">良かった点</p>', unsafe_allow_html=True)
        positive_points = split_text_by_newline(df.loc[selected_record, 'positive_aspects'])
        display_point_details(positive_points, "positive")

    with cols[1]:
        st.markdown('<p class="section-header">改善点</p>', unsafe_allow_html=True)
        improvement_points = split_text_by_newline(df.loc[selected_record, 'areas_for_improvement'])
        display_point_details(improvement_points, "improvement")
    
    display_date_section(df, selected_record)
    display_other_info(df, selected_record)