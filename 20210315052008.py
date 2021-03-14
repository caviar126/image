from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


from lxml import etree
import json



"""
#加启动配置
    option = webdriver.ChromeOptions()
    #关闭“chrome正受到自动测试软件的控制”
    #V75以及以下版本
    #option.add_argument('disable-infobars')
    #V76以及以上版本
    option.add_experimental_option('useAutomationExtension', False)
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    #不自动关闭浏览器
    option.add_experimental_option("detach", True)
    # 打开chrome浏览器
    driver = webdriver.Chrome(chrome_options=option)
    return driver

"""


l_season = [
 

    'https://zhwikizmz.cn/往期剧集/第十七季/', 


    ]

"""

l_season = [
 
    'https://zhwikizmz.cn/往期剧集/第一季/', 
    'https://zhwikizmz.cn/往期剧集/第二季/', 
    'https://zhwikizmz.cn/往期剧集/第三季/', 
    'https://zhwikizmz.cn/往期剧集/第四季/', 
    'https://zhwikizmz.cn/往期剧集/第五季/', 
    'https://zhwikizmz.cn/往期剧集/第六季/', 
    'https://zhwikizmz.cn/往期剧集/第七季/', 
    'https://zhwikizmz.cn/往期剧集/第八季/', 
    'https://zhwikizmz.cn/往期剧集/第九季/', 
    'https://zhwikizmz.cn/往期剧集/第十季/', 
    'https://zhwikizmz.cn/往期剧集/第十一季/', 
    'https://zhwikizmz.cn/往期剧集/第十二季/', 
    'https://zhwikizmz.cn/往期剧集/第十三季/', 
    'https://zhwikizmz.cn/往期剧集/第十四季/', 
    'https://zhwikizmz.cn/往期剧集/第十五季/', 
    'https://zhwikizmz.cn/往期剧集/第十六季/', 
    'https://zhwikizmz.cn/往期剧集/第十七季/', 
    'https://zhwikizmz.cn/往期剧集/第十八季/', 
    'https://zhwikizmz.cn/往期剧集/第十九季/', 
    'https://zhwikizmz.cn/往期剧集/第二十季/', 
    'https://zhwikizmz.cn/往期剧集/第二十一季/', 
    'https://zhwikizmz.cn/往期剧集/第二十二季/'
   
    ]

"""


def main():
    options = Options()
    options.add_experimental_option("detach", True)

    # 不加载图片
    prefs = {"profile.managed_default_content_settings.images":2}
    options.add_experimental_option("prefs",prefs)

    
    # Page loading strategy
    options.page_load_strategy = 'none'

    """
    Page loading strategy: 

    normal - This will make Selenium WebDriver to wait for the entire page is loaded. When set to normal, Selenium WebDriver waits until the load event fire is returned.
    By default normal is set to browser if none is provided.

    eager - This will make Selenium WebDriver to wait until the initial HTML document has been completely loaded and parsed, and discards loading of stylesheets, images and subframes.

    none - When set to none Selenium WebDriver only waits until the initial page is downloaded.

    """


    #设置成用户自己的数据目录: "chrome://version/" # （原用户参数为复制以为"Default"，另复制一份为"DefaultCopy"程序才不会报错）
    # options.add_argument('--user-data-dir=C:\\Users\\Caviar\\AppData\\Local\\Temp\\scoped_dir3768_856195622\\DefaultCopy') 

    # options.binary_location指定360极速浏览器路径
    options.binary_location = 'C:\\Users\\Caviar\\AppData\\Local\\360Chrome\\Chrome\\Application\\360chrome.exe'
    
    # 创建Chrome驱动实例，executable_path指定chromedriver路径
    driver = webdriver.Chrome(options=options, executable_path='C:\\Users\\Caviar\\AppData\\Local\\360Chrome\\Chrome\\Application\\chromedriver.exe')
    
    # 最小化浏览器
    #driver.minimize_window() 









    for url_season in l_season:

        dict_season = {}
        josn_fn = url_season.split('/')[-2]
        print([josn_fn])

        #driver ---- class WebDriver(selenium.webdriver.remote.webdriver.WebDriver)
        driver.get(url_season)

        # 经过浏览器渲染以及标签清洗过后的HTML页面
        html_season_ = driver.page_source
        #'''
        with open('经过浏览器渲染以及标签清洗过后的HTML页面.html', 'w', encoding='utf-8') as f:
            f.write(html_season_)
        #'''
        html_season = etree.HTML(html_season_)
        # 每集描述

        for a in html_season.xpath('//*[@id="default-page"]/div/div/div/div/figure/ul/li/figure/a'):
            #print(a)
            #print([etree.tounicode(a)])
            #print()

            try:
                figcaption = a.xpath('./following-sibling::*[1]')[0]
                img_episode = a.xpath('./img/@src')[0]
                url_episode = a.xpath('./@href')[0]

                #print(etree.tounicode(figcaption))
                strong_eng = figcaption.xpath('./div/a[1]/div/strong')[0]
                strong_chn = figcaption.xpath('./div/a[1]/strong')[0]
                discription_eng = strong_eng.text
                discription_chn = strong_chn.text
                
                # 进入二级网页
                # 如果二级页面使用requests从服务器直接获取的HTML源数据标签规范，那么可以直接使用requests访问，抓取效率更高
                driver.get(url_episode)
                #driver.set_page_load_timeout(time_to_wait=10)
                driver.implicitly_wait(time_to_wait=0)
                html_episode_ = driver.page_source
                html_episode = etree.HTML(html_episode_)
                a_mp4 = html_episode.xpath('//*[@id="default-page"]/div/div/div/div/div[1]/div/div/section[2]/div/div/div[1]/div/div/div/div/div/a')[0]
                mp4_url = a_mp4.xpath('./@href')[0]
                print(mp4_url)

                d = {mp4_url:[discription_eng, discription_chn, img_episode]}
                dict_season.update(d)
                print(d)
            except:
                #### 将python_data写入data.json文件
                with open(f'{josn_fn}【无】.txt', 'w', encoding='utf-8') as f:
                    f.write('')
                break
        
        if dict_season != {}:
            #### 将python_data写入data.json文件
            with open(f'{josn_fn}.json', 'w', encoding='utf-8') as f:
                json.dump(dict_season, f, sort_keys=True, indent=4, ensure_ascii=False)
        else:
            pass




"""



    # WebElement(builtins.object)
    a_elements = driver.find_elements_by_xpath('//*[@id="default-page"]/div/div/div/div/figure/ul/li/figure/a')
    for a_element in a_elements:
        episode_url = a_element.get_attribute('href')
        img_element = a_element.find_element_by_xpath('./img')
        img_url = img_element.get_attribute('src')
        #print(episode_url)

        figcaption_element = a_element.find_element_by_xpath('./following-sibling::*[1]')
        strong_element = figcaption_element.find_element_by_xpath('./div[1]/a/strong')
        chn = strong_element.text
        eng = strong_element.find_element_by_xpath('./following-sibling::*[1]/strong').text

        
        # 进入二级网页（新标签）
        cmd = f'window.open("{episode_url}")'
        print(cmd)
        driver.execute_script(cmd)

        #driver.get(episode_url)
        a_mp4_element = driver.find_elements_by_xpath('//a[@class="elementor-button-link elementor-button elementor-size-sm"]')[0]
        mp4_url = a_mp4_element.get_attribute('href')
        #print(a_mp4_element.tag_name)
        #break
        


"""




    
    #driver.quit()








if __name__ == '__main__':

    main()
