
import csv

file_path = 'D:/gameplace/code第三學期初階/week_01/nfl_offensive_stats.csv'
player_to_find = "Aaron Rodgers"
total_pass_yds = 0

try:
    with open(file_path, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['player'] == player_to_find:
                total_pass_yds += int(row['pass_yds'])
    print(f"球員 {player_to_find} 的總傳球碼數 (pass_yds) 為: {total_pass_yds}")
except Exception as e:
    print(f"發生錯誤: {e}")
