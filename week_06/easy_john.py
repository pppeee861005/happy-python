from collections import namedtuple

# 使用 namedtuple 讓資料結構一目了然，取代難記的 [year, rev, pro, mar]
Record = namedtuple('Record', ['year', 'revenue', 'profit', 'margin'])

# 集中管理格式設定，未來要調整欄寬只要改這裡
QUIT_COMMAND = 'q'
PROMPT = f">> (輸入 '{QUIT_COMMAND}' 結束) "
INPUT_HINT = "格式：年度,營業額,利潤（例如：112,1550000,47895）"


def parse_input(raw: str) -> Record:
    """解析使用者輸入，回傳 Record；格式錯誤時拋出 ValueError。"""
    parts = raw.split(',')
    if len(parts) != 3:
        raise ValueError("需要三個以逗號分隔的欄位")
    
    year = parts[0].strip()
    revenue = int(parts[1].strip())
    profit = int(parts[2].strip())
    
    if revenue == 0:
        raise ValueError("營業額不能為 0")
    
    margin = profit / revenue
    return Record(year, revenue, profit, margin)


def collect_records() -> list[Record]:
    """持續收集使用者輸入，直到輸入結束指令。"""
    records = []
    print(INPUT_HINT)
    
    while True:
        raw = input(PROMPT).strip()
        
        if raw.lower() == QUIT_COMMAND:
            break
        
        try:
            records.append(parse_input(raw))
        except ValueError as e:
            print(f"⚠️  輸入錯誤：{e}")
            print(f"   {INPUT_HINT}")
    
    return records


def print_report(records: list[Record]) -> None:
    """輸出格式化報表。"""
    if not records:
        print("\n（無資料）")
        return
    
    # 表頭
    header = f"{'年度':>8} {'營業額':>18} {'利潤':>17} {'獲利率':>12}"
    print(f"\n{header}")
    print("=" * 60)
    
    # 資料列
    # :>N  靠右對齊 N 欄寬
    # :,d  整數加千分位逗號
    # :.2% 轉百分比並保留兩位小數
    for r in records:
        print(f"{r.year:>8} {r.revenue:>18,d} {r.profit:>17,d} {r.margin:>12.2%}")


def main() -> None:
    records = collect_records()
    print_report(records)


if __name__ == "__main__":
    main()