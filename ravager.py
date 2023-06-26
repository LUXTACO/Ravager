import os
import sys
import art
import time
import ctypes
import random
import logging
import threading
from pystyle import Colorate, Colors, Center, Col, Add

logs = []
dark = Col.dark_gray
light = Col.light_gray
blue = Colors.StaticMIX((Col.light_blue, Col.blue))
bblue = Colors.StaticMIX((Col.blue, Col.blue, Col.white))
red = Colors.StaticMIX((Col.red, Col.red, Col.white))
green = Colors.StaticMIX((Col.green, Col.green, Col.white))
reset = Colors.reset

date = time.strftime("%d-%m-%Y")
logging.basicConfig(filename=f"./logs/logs{date}.log", level=1, format="%(asctime)s - %(levelname)s - %(message)s")

def main():
    
    def clear():
        os.system("cls" if os.name == "nt" else "clear")
    
    text = r""" 
    ██▀███   ▄▄▄    ██▒   █▓ ▄▄▄        ▄████ ▓█████  ██▀███  
    ▓██ ▒ ██▒▒████▄ ▓██░   █▒▒████▄     ██▒ ▀█▒▓█   ▀ ▓██ ▒ ██▒
    ▓██ ░▄█ ▒▒██  ▀█▄▓██  █▒░▒██  ▀█▄  ▒██░▄▄▄░▒███   ▓██ ░▄█ ▒
    ▒██▀▀█▄  ░██▄▄▄▄██▒██ █░░░██▄▄▄▄██ ░▓█  ██▓▒▓█  ▄ ▒██▀▀█▄  
    ░██▓ ▒██▒ ▓█   ▓██▒▒▀█░   ▓█   ▓██▒░▒▓███▀▒░▒████▒░██▓ ▒██▒
    ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░ ▐░   ▒▒   ▓▒█░ ░▒   ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
    ░▒ ░ ▒░  ▒   ▒▒ ░░ ░░    ▒   ▒▒ ░  ░   ░  ░ ░  ░  ░▒ ░ ▒░
    ░░   ░   ░   ▒     ░░    ░   ▒   ░ ░   ░    ░     ░░   ░ 
    ░           ░  ░   ░        ░  ░      ░    ░  ░   ░     
                        ░                                     """[:-1]

    banner = """
                                ...                   
                     .:^^^^^^^^^^7^               
                   ^~^:.        ~^                
                :~?^           ^!                 
               !^..:.          ~?                 
              !: .  : .        7~~                
             ~^~?~:^77!!^7   .~: ?                
            .J?&?YY7P7JG?P:  . .!~                
            ^~7P~!P5Y!YY?YBY: :!7:                
             ^~^GY7!5! ^P?~&P.~  ?                
             !^ G57J?7?J5?:BP   77                
              7:PBJ~~^~~^5:&7::^::!.              
            .^~^Y&@P^!G&#~!#?5.  .GJ^.            
           ~~. :JP&@@@@P! :.^. ^?BG!.7:           
           !: .J??G@@@#J^   ^Y##5~ ~7:            
           .7. 7?~ ~7~.   :P&G7.  JY^             
            7!^.!:    :!?JBY^   .GG!              
            !~.. ~^.~JJ?!~. :~7YBB?^              
             ~7:  :~^    ^JB##GY!:.               
              :Y7:    :?#@&P?^.                   
               .!7!. !G&G?^.                      
                 ^JPGBP7:                         
                   ^J7.                           
                                                  """[1:]

    banner = Add.Add(text, banner, center=True)
    
    clear()
    print(Colorate.Diagonal(Colors.DynamicMIX((blue, dark)), Center.XCenter(banner)))
    ctypes.windll.kernel32.SetConsoleTitleW("Ravager")
    
    logs.append(f"(#) Succesfully printed the banner")
    
    try:
        amount_acc = int(input(f"{dark}[{light}?{dark}] {bblue}How many accounts do you want to generate per thread {dark}->{reset} "))
        logs.append(f"(#) Set var amount_acc to [{amount_acc}]")
    except Exception as e:
        print(f"\n{dark}[{light}!{dark}] {red}Please enter a number{reset}")
        logs.append(f"(*) Got error while setting the value of amount_acc [{e}]")
        os.system("pause >nul")
        exit()
        
    try:
        amount_thread = int(input(f"\n{dark}[{light}?{dark}] {bblue}How many threads do you want to use {dark}->{reset} "))
        logs.append(f"(#) Set var amount_thread to [{amount_thread}]")
    except Exception as e:
        print(f"\n{dark}[{light}!{dark}] {red}Please enter a number{reset}")
        logs.append(f"(*) Got error while setting the value of amount_thread [{e}]")
        os.system("pause >nul")
        exit()
    
    """    
    try:
        proxies_use = input(f"\n{dark}[{light}?{dark}] {bblue}Do you want to use proxies? {dark}[{light}Y{dark}/{light}N{dark}]{dark}->{reset} ").lower()
        if proxies_use == 'y':
            logs.append(f"(#) Set var proxies_use to [True]")
            proxies_use = True
        elif proxies_use == 'n':
            logs.append(f"(#) Set var proxies_use to [False]")
            proxies_use = False
        else:
            print(f"\n{dark}[{light}!{dark}] {red}Please enter a valid option{reset}")
            logs.append(f"(*) Got error while setting the value of proxies_use [{proxies_use}]")
            os.system("pause >nul")
            exit()
    except Exception as e:
        print(f"\n{dark}[{light}!{dark}] {red}Got an unexpected error!{reset}")
        logs.append(f"(*) Got error while setting the value of proxies_use [{e}]")
        exit()
    """
    
    proxies_use = False
    
    try:
        driver_choice = input(f"\n{dark}[{light}?{dark}] {bblue}Do you want to use Selenium or Undetected? {dark}[{light}S{dark}/{light}U{dark}]{dark}->{reset} ").lower()
        if driver_choice == 's':
            logs.append(f"(#) Set var driver_choice to [Selenium]")
            driver_choice = 'selenium'
        elif driver_choice == 'u':
            logs.append(f"(#) Set var driver_choice to [Undetected]")
            driver_choice = 'undetected'
        else:
            print(f"\n{dark}[{light}!{dark}] {red}Please enter a valid option{reset}")
            logs.append(f"(*) Got error while setting the value of driver_choice [{driver_choice}]")
            os.system("pause >nul")
            exit()
    except Exception as e:
        print(f"\n{dark}[{light}!{dark}] {red}Got an unexpected error (driver_choice)!{reset}")
        logs.append(f"(*) Got error while setting the value of driver_choice [{e}]")
        exit()

    return amount_acc, amount_thread, proxies_use, driver_choice
    

def selenium(amount_acc, proxies_use, thread_id):
    print(f"\n{dark}[{light}Thread {thread_id+1}{dark}] {green}Starting thread{reset}")
    
    from selenium.webdriver.common.by import By
    from selenium.webdriver import ChromeOptions
    from selenium_profiles.webdriver import Chrome
    from selenium_profiles.profiles import profiles
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.common.action_chains import ActionChains
    from selenium.webdriver.support import expected_conditions as EC
    
    from selenium_injector.injector import mv3_injector as injector

    fail = False
    path = os.getcwd() + "/solver"
    emailchoice = 0

    def get_email(emailchoice):
        try:
            with open("email.txt", "r") as f:
                emails = f.readlines()
                tempmail = emails[emailchoice].strip()
                f.close()
            return tempmail
        except IndexError:
            print(f"{dark}[{light}Thread {thread_id+1}{dark}] {red}No more emails in the list{reset}")
            
    def pass_gen():
        chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
        password = ""
        for c in range(16):
            password += random.choice(chars)
        return password
        
    def user_gen():
        suffix = ['Best', 'Ratchet', 'Baller', 'Big', 'Money']
        name_list = ['Lil', 'Big', 'Young', 'Old', 'Dope', 'Savage', 'Crazy', 'Swag', 'Dank', 'Lit', 'Savage', 'Crazy']
        prefix = ['Swag', 'Dank', 'Lit', 'Savage', 'Crazy']
        
        name = random.choice(suffix) + random.choice(name_list) + random.choice(suffix)
        
        return name    
    
    profile = profiles.Windows()
    options = ChromeOptions()
    options.add_argument("--window-size=700,800")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-crash-reporter")
    options.add_argument("--disable-in-process-stack-traces")
    options.add_argument("--disable-logging")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--log-level=3")
    options.add_argument("--output=/dev/null")
    options.add_argument(fr"--load-extension={path}")
    mydriver = Chrome(profile, options=options, uc_driver=True)
    
    driver = mydriver.start()
    wait = WebDriverWait(driver, 120)
    
    print(f"{dark}[{light}Thread {thread_id+1}{dark}] {green}Succesfully started the driver{reset}")
    
    while amount_acc > 0:
        driver.get("https://discord.com/register")
    
        try: 
            wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='email']")))
            print(f"{dark}[{light}Thread {thread_id+1}{dark}] {green}Successfully loaded the page{reset}")
        except:
            print(f"{dark}[{light}Thread {thread_id+1}{dark}] {red}Failed to load the page{reset}")
            fail = True
        
        email = get_email(emailchoice)
        password = pass_gen()
        username = user_gen()
        
        print(f"{dark}[{light}Thread {thread_id+1}{dark}] {green}Using email {light}{email}{reset}")
        print(f"{dark}[{light}Thread {thread_id+1}{dark}] {green}Using password {light}{password}{reset}")
        print(f"{dark}[{light}Thread {thread_id+1}{dark}] {green}Using username {light}{username}{reset}")
        
        if fail == False:
            try:
                driver.find_element(By.NAME, 'email').send_keys(email)
                print(f"{dark}[{light}Thread {thread_id+1}{dark}] {green}Successfully entered the email{reset}")
                time.sleep(random.uniform(1.5, 3.5))
                driver.find_element(By.NAME, 'username').send_keys(username)
                print(f"{dark}[{light}Thread {thread_id+1}{dark}] {green}Successfully entered the username{reset}")
                time.sleep(random.uniform(0.5, 1.5))
                driver.find_element(By.NAME, 'password').send_keys(password)
                print(f"{dark}[{light}Thread {thread_id+1}{dark}] {green}Successfully entered the password{reset}")
                time.sleep(random.uniform(0.5, 1.5))
            except Exception as e:
                print(f"{dark}[{light}Thread {thread_id+1}{dark}] {red}Failed to enter the information{reset}")
                print(e)
                fail = True
                
        if fail == False:
            try:
                #Birthday
                action = ActionChains(driver)
                driver.find_elements(By.CLASS_NAME, 'css-1hwfws3')[0].click()
                action.send_keys(str(random.randint(1,12))).pause(random.uniform(0.5, 1.5)).perform()
                action.send_keys(Keys.ENTER).pause(random.uniform(0.5, 1.5)).perform()
                driver.find_elements(By.CLASS_NAME, 'css-1hwfws3')[1].click()
                action.send_keys(str(random.randint(1,28))).pause(random.uniform(0.5, 1.5)).perform()
                driver.find_elements(By.CLASS_NAME, 'css-1hwfws3')[2].click()
                action.send_keys(str(random.randint(1990,2005))).pause(random.uniform(0.5, 1.5)).perform()
                
                print(f"{dark}[{light}Thread {thread_id+1}{dark}] {green}Successfully entered the birthday{reset}")
                time.sleep(random.uniform(0.5, 1.5))
                driver.find_element(By.CLASS_NAME, 'button-1cRKG6').click()
                print(f"{dark}[{light}Thread {thread_id+1}{dark}] {green}Successfully clicked the continue button{reset}")
            except Exception as e:
                print(f"{dark}[{light}Thread {thread_id+1}{dark}] {red}Failed to enter the information{reset}")
                print(e)
                fail = True
                
        if fail == False:
            try:
                time.sleep(5)
                wait.until(EC.url_to_be("https://discord.com/channels/@me"))
                wait.until(EC.presence_of_element_located((By.XPATH, 'html/body')))
                print(f"{dark}[{light}Thread {thread_id+1}{dark}] {green}Successfully created the account{reset}")
                print(f"{dark}[{light}Thread {thread_id+1}{dark}] {green}Successfully loaded the dashboard{reset}")
                js_code ="(webpackChunkdiscord_app.push([[''],{},e=>{m=[];for(let c in e.c)m.push(e.c[c])}]),m).find(m=>m?.exports?.default?.getToken!==void 0).exports.default.getToken()"
                token = driver.execute_script(f"return {js_code};")
                print(f"{dark}[{light}Thread {thread_id+1}{dark}] {green}Successfully got the token{reset}")
                time.sleep(random.uniform(1.5, 2.5))
            except Exception as e:
                print(f"{dark}[{light}Thread {thread_id+1}{dark}] {red}Failed to create the account{reset}")
                print(e)
                fail = True
        
    if fail == False:
        with open('accounts.txt', 'a') as f:
            f.write(f"{email}:{password}:{token}\n")    
        emailchoice += 1
        driver.delete_all_cookies()
        driver.quit()
    sys.exit()
    
def undetected(amount_acc, proxies_use, thread_id):
    import undetected_chromedriver as uc
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.common.action_chains import ActionChains
    from selenium.webdriver.support import expected_conditions as EC
    
    fail = False
    path = os.getcwd() + "/solver"
    emailchoice = 0
    
    def get_email(emailchoice):
        try:
            with open("email.txt", "r") as f:
                emails = f.readlines()
                tempmail = emails[emailchoice].strip()
                f.close()
            return tempmail
        except IndexError:
            print(f"{dark}[{light}Thread {thread_id+1}{dark}] {red}No more emails in the list{reset}")
            
    def pass_gen():
        chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
        password = ""
        for c in range(16):
            password += random.choice(chars)
        return password
        
    def user_gen():
        suffix = ['Best', 'Ratchet', 'Baller', 'Big', 'Money']
        name_list = ['Lil', 'Big', 'Young', 'Old', 'Dope', 'Savage', 'Crazy', 'Swag', 'Dank', 'Lit', 'Savage', 'Crazy']
        prefix = ['Swag', 'Dank', 'Lit', 'Savage', 'Crazy']
        
        name = random.choice(suffix) + random.choice(name_list) + random.choice(suffix)
        
        return name    
    
    options = uc.ChromeOptions()
    options.add_argument("--window-size=700,800")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-crash-reporter")
    options.add_argument("--disable-in-process-stack-traces")
    options.add_argument("--disable-logging")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--log-level=3")
    options.add_argument("--output=/dev/null")
    options.add_argument(fr"--load-extension={path}")
    
    driver = uc.Chrome(options=options)
    wait = WebDriverWait(driver, 120)
    
    print(f"{dark}[{light}Thread {thread_id+1}{dark}] {green}Succesfully started the driver{reset}")
    
    while amount_acc > 0:
        driver.get("https://discord.com/register")
    
        try: 
            wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='email']")))
            print(f"{dark}[{light}Thread {thread_id+1}{dark}] {green}Successfully loaded the page{reset}")
        except:
            print(f"{dark}[{light}Thread {thread_id+1}{dark}] {red}Failed to load the page{reset}")
            fail = True
        
        email = get_email(emailchoice)
        password = pass_gen()
        username = user_gen()
        
        print(f"{dark}[{light}Thread {thread_id+1}{dark}] {green}Using email {light}{email}{reset}")
        print(f"{dark}[{light}Thread {thread_id+1}{dark}] {green}Using password {light}{password}{reset}")
        print(f"{dark}[{light}Thread {thread_id+1}{dark}] {green}Using username {light}{username}{reset}")
        
        if fail == False:
            try:
                driver.find_element(By.NAME, 'email').send_keys(email)
                print(f"{dark}[{light}Thread {thread_id+1}{dark}] {green}Successfully entered the email{reset}")
                time.sleep(random.uniform(1.5, 3.5))
                driver.find_element(By.NAME, 'username').send_keys(username)
                print(f"{dark}[{light}Thread {thread_id+1}{dark}] {green}Successfully entered the username{reset}")
                time.sleep(random.uniform(0.5, 1.5))
                driver.find_element(By.NAME, 'password').send_keys(password)
                print(f"{dark}[{light}Thread {thread_id+1}{dark}] {green}Successfully entered the password{reset}")
                time.sleep(random.uniform(0.5, 1.5))
            except Exception as e:
                print(f"{dark}[{light}Thread {thread_id+1}{dark}] {red}Failed to enter the information{reset}")
                print(e)
                fail = True
                
        if fail == False:
            try:
                #Birthday
                action = ActionChains(driver)
                driver.find_elements(By.CLASS_NAME, 'css-1hwfws3')[0].click()
                action.send_keys(str(random.randint(1,12))).pause(random.uniform(0.5, 1.5)).perform()
                action.send_keys(Keys.ENTER).pause(random.uniform(0.5, 1.5)).perform()
                driver.find_elements(By.CLASS_NAME, 'css-1hwfws3')[1].click()
                action.send_keys(str(random.randint(1,28))).pause(random.uniform(0.5, 1.5)).perform()
                driver.find_elements(By.CLASS_NAME, 'css-1hwfws3')[2].click()
                action.send_keys(str(random.randint(1990,2005))).pause(random.uniform(0.5, 1.5)).perform()
                
                print(f"{dark}[{light}Thread {thread_id+1}{dark}] {green}Successfully entered the birthday{reset}")
                time.sleep(random.uniform(0.5, 1.5))
                driver.find_element(By.CLASS_NAME, 'button-1cRKG6').click()
                print(f"{dark}[{light}Thread {thread_id+1}{dark}] {green}Successfully clicked the continue button{reset}")
            except Exception as e:
                print(f"{dark}[{light}Thread {thread_id+1}{dark}] {red}Failed to enter the information{reset}")
                print(e)
                fail = True
                
        if fail == False:
            try:
                time.sleep(5)
                wait.until(EC.url_to_be("https://discord.com/channels/@me"))
                wait.until(EC.presence_of_element_located((By.XPATH, 'html/body')))
                print(f"{dark}[{light}Thread {thread_id+1}{dark}] {green}Successfully created the account{reset}")
                print(f"{dark}[{light}Thread {thread_id+1}{dark}] {green}Successfully loaded the dashboard{reset}")
                js_code ="(webpackChunkdiscord_app.push([[''],{},e=>{m=[];for(let c in e.c)m.push(e.c[c])}]),m).find(m=>m?.exports?.default?.getToken!==void 0).exports.default.getToken()"
                token = driver.execute_script(f"return {js_code};")
                print(f"{dark}[{light}Thread {thread_id+1}{dark}] {green}Successfully got the token{reset}")
                time.sleep(random.uniform(1.5, 2.5))
            except Exception as e:
                print(f"{dark}[{light}Thread {thread_id+1}{dark}] {red}Failed to create the account{reset}")
                print(e)
                fail = True
        
    if fail == False:
        with open('accounts.txt', 'a') as f:
            f.write(f"{email}:{password}:{token}\n")    
        emailchoice += 1
        driver.delete_all_cookies()
        driver.quit()
    sys.exit()
    
    
    
    
if __name__ == '__main__':
    try:
        data = main()
        amount_acc = data[0]
        amount_thread = data[1]
        proxies_use = data[2]
        driver_choice = data[3]
    except:
        pass
    
    try:
        if driver_choice == 'selenium':
            for i in range(amount_thread):
                threading.Thread(target=selenium, args=(amount_acc, proxies_use, i)).start()
        elif driver_choice == 'undetected':
            for i in range(amount_thread):
                threading.Thread(target=undetected, args=(amount_acc, proxies_use, i)).start()
    except:
        pass