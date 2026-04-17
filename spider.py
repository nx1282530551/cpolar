from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.options import Options
import datetime

def login_and_get_text():
    edge_options = Options()
    edge_options.add_argument("--headless=new")
    edge_options.add_argument("--disable-gpu")
    edge_options.add_argument("--no-sandbox")
    edge_options.add_argument("--disable-dev-shm-usage")
    edge_options.add_argument("--disable-extensions")
    edge_options.add_argument("--disable-popup-blocking")
    edge_options.add_argument("--remote-debugging-port=9222")

    driver = webdriver.Edge(options=edge_options)
    driver.implicitly_wait(10)

    try:
        
        url = "http://7e8b56d5.r17.cpolar.top/#/status/online"
        driver.get(url)

        # 账号
        username_input = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div/form/div[2]/div/div/input"))
        )
        username_input.clear()
        username_input.send_keys("102477511@qq.com")

        # 密码
        password_input = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div/form/div[3]/div/div/input"))
        )
        password_input.clear()
        password_input.send_keys("19")

        # 登录
        login_btn = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/form/button"))
        )
        login_btn.click()

        # 抓取内容
        target_td = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[2]/section/div/div/div[3]/table/tbody/tr[2]/td[3]/div"))
        )
        text_content = target_td.text
        return text_content

    except Exception as e:
        return f"抓取失败：{str(e)}"
    finally:
        driver.quit()

if __name__ == "__main__":
    content = login_and_get_text()
    now = datetime.datetime.utcnow() + datetime.timedelta(hours=8)
    update_time = now.strftime("%Y-%m-%d %H:%M:%S")

    final = f"""
# 自动更新

当前内容：
{content}

最后更新：{update_time}
    """

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(final.strip())
