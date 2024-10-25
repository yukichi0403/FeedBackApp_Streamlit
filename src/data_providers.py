"""
データ取得ロジックモジュール
"""
from logging import Logger
import pandas as pd
from .database import DatabricksConnection
from .config import DatabricksConfig

class DataProvider:
    def __init__(self, config: DatabricksConfig, logger: Logger):
        self.connection = DatabricksConnection(config, logger)
        self.logger = logger

class FeedbackDataProvider(DataProvider):
    def get_feedback_data(self) -> pd.DataFrame:
        """
        フィードバックデータを取得し、適切なデータ型に変換
        """
        query = """
        SELECT *
        FROM common.sharepoint.feedback_app
        """
        df = self.connection.execute_query(query)
        
        # データ型を明示的に指定
        string_columns = ['main_points', "overall_progress", "success_probability", "positive_aspects", "areas_for_improvement", "expected_arr", 
                          "customer_tasks", "customer_issues_discussed", "roi_explanation", "differentiation_explained", "cross_department_expansion_discussed",
                          "notable_item", "trial_start", "contract_start", "next_meeting"]  # 文字列として扱うカラムのリスト
        for col in string_columns:
            if col in df.columns:
                df[col] = df[col].astype(str)
        
        return df