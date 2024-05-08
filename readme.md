# Process Checker

Process Checker is a Python script that monitors a specified process on Windows and sends a notification to a Telegram chat if the process is not active.

## Requirements

- Python 3.x
- `requests` library (install via `pip install requests`)
- `python-dotenv` library (install via `pip install python-dotenv`)
- Windows operating system

## Installation

1. Clone or download this repository to your local machine.
2. Install the required Python libraries:
3. Create a `.env` file in the same directory as the Python script (`process_checker.py`) and add the following variables:
Replace `YOUR_BOT_TOKEN` and `YOUR_CHAT_ID` with your Telegram bot token and chat ID respectively.

## Usage

### Running as a Windows Service

To run the script as a Windows service:

1. Open Command Prompt as administrator.
2. Navigate to the directory containing the Python script.
3. Install the service:
4. Start the service:

The service will now run in the background and periodically check if the specified process is running. If the process is not active, a notification will be sent to the specified Telegram chat.

### Running with Task Scheduler

Alternatively, you can schedule the script to run with the Windows Task Scheduler. Follow the instructions in the script or README to set up a scheduled task.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

