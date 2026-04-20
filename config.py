from dotenv import load_dotenv
import os

# 加载环境变量
load_dotenv()

# ============== 读取配置 ==============
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
PRODUCT_API_KEY = os.getenv("PRODUCT_API_KEY")
LLM_API_KEY = os.getenv("LLM_API_KEY")

USE_MOCK_DATA = os.getenv("USE_MOCK_DATA", "true").lower() == "true"
USE_LLM = os.getenv("USE_LLM", "false").lower() == "true"
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")


# ============== 配置校验函数（关键） ==============
def validate_config():
    print("正在检查配置...")

    # 只有在需要真实API时才检查
    if not USE_MOCK_DATA:
        if not NEWS_API_KEY:
            raise Exception("错误：缺少 NEWS_API_KEY（关闭Mock数据时必须提供）")

    # 只有开启LLM才检查
    if USE_LLM:
        if not LLM_API_KEY:
            raise Exception("错误：USE_LLM=true 但未配置 LLM_API_KEY")

    # 提醒但不报错
    if not USE_MOCK_DATA and not USE_LLM:
        print("警告：未使用Mock数据，也未开启LLM，系统功能可能受限")

    print("配置检查通过")

validate_config()