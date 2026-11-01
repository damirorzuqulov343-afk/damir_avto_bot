import requests, time, os
BOT_TOKEN = os.environ.get("BOT_TOKEN")
TEXT = "Salom! Hozir bandman, birozdan keyin albatta javob beraman. Rahmat!"
API = f"https://api.telegram.org/bot{BOT_TOKEN}"
def main():
    print("Bot started")
    off=0
    while True:
        try:
            r=requests.get(f"{API}/getUpdates", params={"offset":off,"timeout":30}, timeout=35).json()
            for u in r.get("result",[]):
                off=u["update_id"]+1
                if "business_message" in u:
                    m=u["business_message"]
                    if m.get("from",{}).get("is_bot"): continue
                    requests.post(f"{API}/sendMessage", json={"chat_id":m["chat"]["id"],"text":TEXT,"business_connection_id":m.get("business_connection_id")})
        except: time.sleep(5)
if __name__=="__main__": main()
