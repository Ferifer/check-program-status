import subprocess
import win32serviceutil
import win32service
import win32event
import win32timezone
import requests
import logging
import time

class ProcessChecker(win32serviceutil.ServiceFramework):
    _svc_name_ = "ProcessChecker"
    _svc_display_name_ = "Process Checker"
    
    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        self.stop_requested = False
        self.process_name = os.getenv("PROCESS_NAME")
        self.bot_token = os.getenv("BOT_TOKEN")
        self.chat_id = os.getenv("CHAT_ID")
        
    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)
        self.stop_requested = True
    
    def send_telegram_message(self, message):
        try:
            url = f"https://api.telegram.org/bot{self.bot_token}/sendMessage"
            params = {"chat_id": self.chat_id, "text": message}
            response = requests.post(url, params=params)
            if response.status_code == 200:
                logging.info("Message sent successfully.")
            else:
                logging.error("Failed to send message. Status code:", response.status_code)
        except Exception as e:
            logging.error("An error occurred while sending message:", e)
    
    def check_process_status(self):
        try:
            result = subprocess.run(['tasklist', '/FI', f'IMAGENAME eq {self.process_name}.exe'], capture_output=True, text=True)
            if self.process_name.lower() not in result.stdout.lower():
                logging.info(f"The process {self.process_name}.exe is not running. Sending notification to Telegram.")
                message = f"The process {self.process_name}.exe is not running."
                self.send_telegram_message(message)
        except Exception as e:
            logging.error("An error occurred:", e)
    
    def SvcDoRun(self):
        self.ReportServiceStatus(win32service.SERVICE_RUNNING)
        logging.info("Process Checker service is running.")
        while True:
            self.check_process_status()
            if self.stop_requested:
                break
            time.sleep(60)  # Check process status every 60 seconds

if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(ProcessChecker)
