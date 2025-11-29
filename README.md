# Internship Browser Automation Agent 🤖

A Python-based automation tool designed to perform sequential email operations (Login → Compose → Send) using Selenium WebDriver. This agent is built to handle dynamic page loading and includes specific logic to safely navigate Google's security prompts.

## 📋 Assignment Objective
The goal of this project is to create an executable agent that:
1.  Accepts user credentials and email content via the command prompt.
2.  Logs into a Gmail account.
3.  Composes an email with a specific subject and body.
4.  Sends the email to a designated recipient (`scittest@auditram.com`).

## 🛠️ Prerequisites

Before running the agent, ensure you have the following installed:
* **Python 3.7+**: [Download Python](https://www.python.org/downloads/)
* **Google Chrome Browser**: Ensure it is updated to the latest version.

## ⚙️ Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/selenium-email-agent.git](https://github.com/YOUR_USERNAME/selenium-email-agent.git)
    cd selenium-email-agent
    ```

2.  **Install Dependencies:**
    This project requires the `selenium` library. Install it using pip:
    ```bash
    pip install -r requirements.txt
    ```
    *(Note: If you don't have a requirements.txt file, you can run `pip install selenium`)*

## 🚀 How to Run

1.  Open your command prompt or terminal in the project folder.
2.  Run the agent:
    ```bash
    python agent.py
    ```
3.  **Enter Inputs:** Follow the on-screen prompts to enter:
    * Your Gmail Address
    * Your Password
    * Email Subject
    * Email Body

## ⚠️ Important: Handling 2FA / Login Security

Google often blocks automated login attempts or requires Two-Factor Authentication (2FA). To handle this, **the script includes a 20-second manual intervention pause** after entering the password.

**When the script says:**
> *"⚠️ IMPORTANT: CHECK YOUR PHONE/SCREEN NOW ⚠️"*

1.  **Watch the browser window.**
2.  If Google asks for a verification code or sends a prompt to your phone ("Is this you?"), **approve it immediately**.
3.  If Google asks to add a recovery email/phone, click **"Not Now"**.
4.  **Goal:** Ensure the **Gmail Inbox** is visible on the screen before the 20-second timer ends. The script will resume automatically once the timer finishes to compose and send the email.

## 🔧 Troubleshooting

* **"WinError 6" / "The handle is invalid":**
    * This usually occurs if you are using an unstable version of `undetected-chromedriver`. This repository uses standard Selenium to ensure stability. Ensure you are running the `agent.py` provided in this repo.
* **Script crashes after login:**
    * Ensure you successfully completed the manual 2FA step within the allocated time.
    * Check your internet connection speed; you may need to increase the `time.sleep()` duration in the code if your inbox loads slowly.
* **Chrome closes immediately:**
    * This is normal behavior. The script is designed to close the browser automatically after the email is sent successfully.

## 📄 License & Disclaimer
This project is for educational and testing purposes only. Ensure you have permission to automate the email account you are using.
