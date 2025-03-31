import requests
import csv
import time
from datetime import datetime, timedelta

# ====================== 配置区域 ======================
API_URL = "https://wap.api.banglail.com:62021/api-entrance/productcategory/officialWebsite"
CATEGORIES = ["蔬菜类", "果品类", "水产类", "畜禽蛋品", "粮油", "副食"]  # 目标品类列表
DAYS = 30  # 数据抓取时间范围(天)
OUTPUT_FILE = "../data/农产品数据.csv"  # 输出文件路径
REQUEST_DELAY = 1  # 请求间隔(秒，防封禁)
TIMEOUT = 15  # 请求超时时间(秒)


# =====================================================

def generate_timestamps(days):
    """生成过去N天的开始和结束时间戳(13位毫秒级)"""
    end_time = datetime.now()
    start_time = end_time - timedelta(days=days)
    return (
        int(start_time.timestamp() * 1000),
        int(end_time.timestamp() * 1000)
    )


def process_location(location):
    """处理产地字段：保留/前的内容"""
    if not location:
        return ""
    return location.split("/")[0].strip() if "/" in location else location


def process_timestamp(ts):
    """将13位时间戳转为YYYY-MM-DD格式"""
    if not ts:
        return ""
    try:
        return datetime.fromtimestamp(int(ts) / 1000).strftime('%Y-%m-%d')
    except:
        return ""


def fetch_all_data(category, days):
    """获取指定品类全量数据"""
    start_ts, end_ts = generate_timestamps(days)
    all_data = []
    page = 1
    limit = 1000  # 单页最大数量

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
        "Content-Type": "application/json"
    }

    while True:
        try:
            # 构造请求参数
            payload = {
                "page": page,
                "limit": limit,
                "categoryName": category,
                "startTime": start_ts,
                "endTime": end_ts
            }

            # 发送请求
            resp = requests.post(
                API_URL,
                json=payload,
                headers=headers,
                timeout=TIMEOUT
            )

            # 处理HTTP错误
            if resp.status_code != 200:
                print(f"[{category}] 请求失败，状态码: {resp.status_code}")
                break

            data = resp.json()

            # 处理业务错误
            if data.get("code") != 0:
                print(f"[{category}] 接口返回错误: {data.get('msg')}")
                break

            current_data = data["data"]["list"]
            if not current_data:
                break  # 无更多数据

            all_data.extend(current_data)
            print(f"[{category}] 已获取第 {page} 页，累计 {len(all_data)} 条")
            page += 1

            time.sleep(REQUEST_DELAY)  # 请求间隔

        except requests.exceptions.Timeout:
            print(f"[{category}] 请求超时，已重试")
            continue
        except Exception as e:
            print(f"[{category}] 发生异常: {str(e)}")
            break

    return all_data


def save_to_csv(data, filename):
    """保存处理后的数据到CSV"""
    if not data:
        print("警告：没有需要保存的数据")
        return

    with open(filename, 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        # 写入表头（与数据库字段对应）
        writer.writerow([
            "categoryName", "productName", "priceMax",
            "priceAvg", "priceMin", "unit",
            "productSize", "productPlace", "recordDate"
        ])

        count = 0
        for item in data:
            # 处理产地字段
            raw_place = item.get("productPlace", "")
            processed_place = process_location(raw_place)

            # 处理时间戳
            raw_ts = item.get("recordDate", "")
            processed_date = process_timestamp(raw_ts)

            # 写入处理后的数据
            writer.writerow([
                item.get("categoryName", ""),
                item.get("productName", ""),
                item.get("priceMax", ""),
                item.get("priceAvg", ""),
                item.get("priceMin", ""),
                item.get("unit", ""),
                item.get("productSize", ""),
                processed_place,
                processed_date
            ])
            count += 1
        print(f"成功保存 {count} 条数据到 {filename}")


if __name__ == "__main__":
    all_products = []

    print("====== 农产品数据采集系统启动 ======")
    print(f"目标品类: {', '.join(CATEGORIES)}")
    print(f"时间范围: 最近{DAYS}天")
    print(f"输出文件: {OUTPUT_FILE}\n")

    for category in CATEGORIES:
        start_time = time.time()
        print(f"\n=== 开始采集 [{category}] 数据 ===")

        try:
            category_data = fetch_all_data(category, DAYS)
            all_products.extend(category_data)
            print(f"[{category}] 完成采集，共获得 {len(category_data)} 条数据")
            print(f"[{category}] 耗时: {time.time() - start_time:.2f}秒")
        except Exception as e:
            print(f"[{category}] 采集失败: {str(e)}")

        time.sleep(REQUEST_DELAY * 2)  # 品类间间隔

    print("\n=== 数据保存阶段 ===")
    save_to_csv(all_products, OUTPUT_FILE)

    print("\n====== 系统运行完成 ======")
    print(f"总计获取品类数: {len(CATEGORIES)}")
    print(f"总计获取数据量: {len(all_products)}")
    print(f"输出文件路径: {OUTPUT_FILE}")