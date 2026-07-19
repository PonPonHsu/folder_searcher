import os

def find_and_open_student():
    print("=== 學生專屬資料夾極速開啟工具 ===")
    
    target_directory = r"G:\.shortcut-targets-by-id\170yYzxYJNk8qHJPuKu-1EWWd0cesjLi2\補習班事宜\行政相關\永福收費相關\學費單"
    
    print("目前預設搜尋路徑：")
    print(target_directory)
    print("-" * 30)
    
    # 建立一個無窮迴圈，讓程式可以不斷接受新的搜尋指令
    while True:
        # 提示文字加入「輸入 q 離開」的說明
        keyword = input("\n請輸入要搜尋的學號或姓名 (輸入 q 離開程式) 並按 Enter: ")
        
        # 設定防呆與離開機制
        if keyword.lower() == 'q':
            print("結束搜尋，關閉小工具。")
            break  # 觸發 break，正式跳出迴圈並結束程式
            
        if keyword.strip() == "":
            print("關鍵字不能為空白，請重新輸入！")
            continue # 觸發 continue，跳過這次搜尋，直接回到上方要求重新輸入
        
        try:
            all_items = os.listdir(target_directory)
            found_count = 0
            
            for item in all_items:
                if keyword in item:
                    full_path = os.path.join(target_directory, item)
                    
                    if os.path.isdir(full_path):
                        print(f"找到並開啟目標: {item}")
                        os.startfile(full_path)
                        found_count += 1
            
            if found_count == 0:
                print("沒有找到符合的資料夾。")
            else:
                print(f"--> 總共自動開啟了 {found_count} 個資料夾視窗。")
                
        except FileNotFoundError:
            print("找不到預設的母資料夾路徑！")
            print("請確認公司電腦的 Google 雲端硬碟已經開啟並連線，且代號為 G: 槽。")
        except Exception as e:
            print(f"發生未知的錯誤: {e}")
            
        print("-" * 30)

if __name__ == "__main__":
    find_and_open_student()
