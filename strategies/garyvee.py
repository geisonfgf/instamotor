from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time, random, sys

class GaryVeeStrategy:
    username = "your_username"
    password = "your_password"

    hashtags = [
        #"negocios", "dinheiro", "empreendedorismo", "liderança",
        #"empreendedor", "vendedor", "atitude", "negociosonline",
        "viverdevendas", "trabalhoduro"
    ]

    comments = [
        ("Estava procurando inspiração e encontrei seus posts, "
        "gostei muito, espero que encontre valor no meu perfil também!"),
        "Seu post me motivou, espero que encontre motivação no meu perfil também!",
        "Ótimo post, espero que goste do meu perfil também!",
        ("Vendo teus posts acredito que temos coisas em comum, "
        "espero que gosto do meu perfil também!")
    ]

    links = []

    def __init__(self):
        self.price = 0.0
        self.browser = webdriver.Firefox()

    def login(self):
        self.browser.get("https://www.instagram.com/accounts/login?source=auth_switcher")
        time.sleep(10)

        username_field = self.browser.find_element_by_xpath("//input[@name='username']")
        username_field.clear()
        username_field.send_keys(self.username)
        time.sleep(1)

        password_field = self.browser.find_element_by_xpath("//input[@name='password']")
        password_field.clear()
        password_field.send_keys(self.password)
        time.sleep(1)

        login_button = self.browser.find_element_by_xpath("//button[@type='submit']")
        login_button.click()
        time.sleep(2)

    def get_top_10_posts_of_each_hashtag(self):
        for hashtag in self.hashtags:
            self.browser.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
            time.sleep(5)

            links = self.browser.find_elements_by_xpath("//a[@href]")
            condition = lambda link: ".com/p/" in link.get_attribute("href")
            valid_links = list(filter(condition, links))

            for i in range(0, 9):
                link = valid_links[i].get_attribute("href")
                if link not in self.links:
                    self.links.append(link)

    def interact(self):
        for link in self.links:
            self.browser.get(link)
            time.sleep(5)

            self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)

            self.comment()
            time.sleep(2)

            self.like()
            time.sleep(1)

            print("Comment and liked the link: " + link + "\n")

            self.price += 0.02

            sleeptime = random.randint(18, 28)
            time.sleep(sleeptime)

    def comment(self):
        comment_input = lambda: self.browser.find_element_by_tag_name("textarea")
        comment_input().click()
        comment_input().clear()

        comment = random.choice(self.comments)
        for letter in comment:
            comment_input().send_keys(letter)
            delay = random.randint(1, 7) / 30
            time.sleep(delay)

        comment_input().send_keys(Keys.RETURN)

    def like(self):
        like_button = lambda: self.browser.find_element_by_xpath(
            '//button[@class="dCJp8 afkep _0mzm-"]'
        )
        like_button().click()

    def finalize(self):
        print("You gave $" + str(self.price) + " back to the community!")
        self.browser.close()
        sys.exit()

    def run(self):
        self.login()
        self.get_top_10_posts_of_each_hashtag()
        self.interact()
        self.finalize()

if __name__ == "__main__":
    strategy = GaryVeeStrategy()
    strategy.run()