import os

def find_student():
    print("=== 學生資料夾極速搜尋工具 ===")
    # 讓使用者手動輸入路徑與關鍵字
    directory = input("請貼上學生資料夾的完整路徑 (例如 C:\\Users\\...) 並按 Enter: ")
    keyword = input("請輸入要搜尋的學號或姓名 (例如 s0069) 並按 Enter: ")
    
    print("\n搜尋結果：")
    print("-" * 30)
    
    try:
        all_items = os.listdir(directory)
        found = False
        for item in all_items:
            if keyword in item:
                print(f"找到目標: {item}")
                found = True
        
        if not found:
            print("沒有找到符合的資料夾。")
            
    except FileNotFoundError:
        print("找不到該路徑，請檢查路徑是否輸入正確。")
    except Exception as e:
        print(f"發生未知的錯誤: {e}")
        
    print("-" * 30)
    # 這行非常重要，避免 .exe 執行完畢後視窗瞬間關閉
    input("請按 Enter 鍵結束程式...")

if __name__ == "__main__":
    find_student()
