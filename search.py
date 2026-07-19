import os

def find_and_open_student():
    print("=== 學生專屬資料夾極速開啟工具 ===")
    
    # 預設的母資料夾路徑 (前面的 r 代表 raw string，可以避免斜線 \ 造成程式誤判)
    target_directory = r"G:\.shortcut-targets-by-id\170yYzxYJNk8qHJPuKu-1EWWd0cesjLi2\補習班事宜\行政相關\永福收費相關\學費單"
    
    print("目前預設搜尋路徑：")
    print(target_directory)
    print("-" * 30)
    
    keyword = input("請輸入要搜尋的學號或姓名 (例如 s0069) 並按 Enter: ")
    print("\n搜尋結果：")
    
    try:
        # 取得資料夾內的所有項目
        all_items = os.listdir(target_directory)
        found_count = 0
        
        for item in all_items:
            # 檢查項目名稱是否包含我們輸入的關鍵字
            if keyword in item:
                # 組合出完整的絕對路徑
                full_path = os.path.join(target_directory, item)
                
                # 確保找到的是資料夾，而不是單純的檔案
                if os.path.isdir(full_path):
                    print(f"找到並開啟目標: {item}")
                    # 直接呼叫 Windows 系統開啟該資料夾
                    os.startfile(full_path)
                    found_count += 1
        
        if found_count == 0:
            print("沒有找到符合的資料夾。")
        else:
            print(f"\n總共自動開啟了 {found_count} 個資料夾視窗。")
            
    except FileNotFoundError:
        print("找不到預設的母資料夾路徑！")
        print("請確認公司電腦的 Google 雲端硬碟已經開啟並連線，且代號為 G: 槽。")
    except Exception as e:
        print(f"發生未知的錯誤: {e}")
        
    print("-" * 30)
    input("請按 Enter 鍵結束程式...")

if __name__ == "__main__":
    find_and_open_student()
