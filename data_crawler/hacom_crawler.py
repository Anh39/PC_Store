import asyncio
import time,json,os
from playwright.async_api import async_playwright,Playwright,Browser,Page
from asyncio import Task
from bs4 import BeautifulSoup
from backend.common import folder_path
from typing import Literal

class PageManager:
    def __init__(self,page : Page) -> None:
        self.done = True
        self.page : Page = page
class Handler:
    def __init__(self) -> None:
        self.interval = 2.5
        self.driver : Playwright.chromium = None
        self.browser : Browser = None
        self.base_url = "https://hacom.vn"
        self.exception_log = []
        self.max_pool = 4
        self.jobs : list[PageManager] = []
    async def init(self):
        self.playwright_content_manager= async_playwright()
        self.playwright = await self.playwright_content_manager.start()
        self.browser = await self.playwright.chromium.launch(headless=True)
        for i in range(self.max_pool):
            page = await self.browser.new_page()
            page_manger = PageManager(page)
            self.jobs.append(page_manger)
    async def get_page_manager(self) -> PageManager:
        while (True):
            busy_count = 0
            for page_manger in self.jobs:
                if not page_manger.done:
                    busy_count+=1
            for i in range(self.max_pool):
                if (self.jobs[i].done):
                    self.jobs[i].done = False
                    return self.jobs[i]

            await asyncio.sleep(1)
    async def process(self):
        jobs = {
            'pc_game' :  {
                'download_directory' : folder_path.Data.HacomRaw.pc_game,
                'family_url' : 'https://hacom.vn/pc-gaming-streaming'
            },
            'pc_graphic' : {
                'download_directory' : folder_path.Data.HacomRaw.pc_graphic,
                'family_url' : 'https://hacom.vn/pc-workstations'
            },
            'pc_office' : {
                'download_directory' : folder_path.Data.HacomRaw.pc_office,
                'family_url' : 'https://hacom.vn/may-tinh-de-ban'
            },
            'lap_common' :  {
                'download_directory' : folder_path.Data.HacomRaw.lap_common,
                'family_url' : 'https://hacom.vn/laptop-tablet-mobile'
            },
            'lap_game' : {
                'download_directory' : folder_path.Data.HacomRaw.lap_game,
                'family_url' : 'https://hacom.vn/laptop-gaming-do-hoa'
            },
            # 'component' : {
            #     'download_directory' : folder_path.Data.HacomRaw.component,
            #     'family_url' : 'https://hacom.vn/linh-kien-may-tinh'
            # },
            'auxility' : {
                'download_directory' : folder_path.Data.HacomRaw.auxility,
                'family_url' : 'https://hacom.vn/phu-kien'
            },
            'display' : {
                'download_directory' : folder_path.Data.HacomRaw.display,
                'family_url' : 'https://hacom.vn/man-hinh-may-tinh'
            }
        }
        for job_key in jobs:
            job = jobs[job_key]
            self.exception_log = []
            
            raw_links_list = await self._get_urls(job['family_url'])
            links = []
            for raw_links in raw_links_list:
                link_list = self._urls_parser(raw_links)
                links.extend(link_list)
            if (not os.path.exists(job['download_directory'])):
                os.makedirs(job['download_directory'])
            with open(folder_path.join(job['download_directory'],'links.json'),'w') as file:
                file.write(json.dumps(links))
            
            tasks = []
            for link in links:
                task = asyncio.create_task(self.save_spec(link,job['download_directory']))
                tasks.append(task)
            completed = False
            while (not completed):
                completed = True
                for task in tasks:
                    if (not task.done()):
                        completed = False
                await asyncio.sleep(self.interval*2)
            if (self.exception_log != []):
                with open(folder_path.join(job['download_directory'],'exception.json'),'w') as file:
                    file.write(json.dumps(self.exception_log)) 
    async def close(self):
        await self.browser.close()
        await self.playwright_content_manager.__aexit__()
    async def _get_urls(self,family_url):
        stop_value = '\n          \n  '
        results = []
        i = 1
        while (True):
            page = await self.browser.new_page()
            await page.goto(family_url+'/{}/'.format(str(i)))
            i+=1
            result = None
            try:
                case_list = await page.query_selector('.cate-list-prod')
                result = await case_list.inner_html()
                if (result == stop_value):
                    await page.close()
                    break
            except:
                pass
            await page.close()
            results.append(result)
        return results
    def _urls_parser(self,content : str):
        soup = BeautifulSoup(content,'html.parser')
        elements = soup.select('.p-img a')
        result = []
        for element in elements:
            result.append(element['href'])
        return result
    async def _try_get(self,page : Page,select_arguments : list[str] = [],auto_parse : Literal['html','text',''] = ''):
        for select_argumnt in select_arguments:
            result = await page.query_selector(select_argumnt)
            if result != None:
                if (auto_parse == 'html'):
                    return await result.inner_html()
                elif (auto_parse == 'text'):
                    return await result.inner_text()
                else:
                    return result
    async def _try_get_all(self,page : Page,select_arguments : list[str] = [],auto_parse : Literal['html','text',''] = ''):
        for select_argumnt in select_arguments:
            result = await page.query_selector_all(select_argumnt)
            if result != None:
                if (auto_parse != ''):
                    final_result = []
                    for ele in result:
                        if (auto_parse=='html'):
                            inner = await ele.inner_html()
                        else:
                            inner = await ele.inner_text()
                        final_result.append(inner)
                    return final_result
                else:
                    return result
    async def _get_info(self,url : str):        
        url = self.base_url + url
        page_manager = await self.get_page_manager()
        page = page_manager.page
        await page.goto(url)
        #start
        result = {
            'name' : None,
            'full_price' : None,
            'price' : None,
            'discount' : None,
            'notices' : None,
            'info' : '',
            'detail_info' : '',
            'view_count' : None,
            'images' : None,
            'url' : url
        }
        
        result['name'] = await self._try_get(
            page=page,
            select_arguments=[
                '.product_detail-title'
            ],
            auto_parse='text'
        )
        result['full_price'] = await self._try_get(
            page=page,
            select_arguments=[
                '.giany'
            ],
            auto_parse='text'
        )
        price_element = await self._try_get(
            page=page,
            select_arguments=[
                '.giakm'
            ]
        )
        result['discount'] = await self._try_get(
            page=page,
            select_arguments=[
                '.tietkiem'
            ],
            auto_parse='text'
        )
        result['info'] = await self._try_get(
            page=page,
            select_arguments=[
                '.product-summary-item-ul'
            ],
            auto_parse='text'
        )
        result['detail_info'] = await self._try_get(
            page=page,
            select_arguments=[
                '//html/body/div[6]/div[4]/div[3]/div[1]/div[2]/div[1]/div/div[1]/table/tbody'
            ],
            auto_parse='text'
        )
        result['notices'] = await self._try_get_all(
            page=page,
            select_arguments=[
                '.yellow-ribbon'
            ],
            auto_parse='text'
        )
        result['view_count'] = await self._try_get(
            page=page,
            select_arguments=[
                '//html/body/div[6]/div[4]/div[1]/div[3]/div/div[1]/div[1]/div[5]/span'
            ],
            auto_parse='text'
        )
        images = []
        image_element = await self._try_get(
            page=page,
            select_arguments=[
                '//html/body/div[6]/div[4]/div[1]/div[2]/div/div/div/a/img'
            ]
        )
        if (image_element != None):
            src = await image_element.get_attribute('src')
            images.append(src)
        i=1
        while (True):
            image_element = await self._try_get(
                page=page,
                select_arguments=[
                    '//html/body/div[6]/div[4]/div[1]/div[2]/div/div/div[1]/div/div[{}]/div/a/img'.format(i)
                ]
            )
            i+=1
            if (image_element != None):
                src = await image_element.get_attribute('src')
                images.append(src)
            else:
                break
        result['images'] = images
        result['price'] = await price_element.evaluate('(element) => element.getAttribute("data-price")')   
        #end
        for key in result:
            if (key != 'detail_info'):
                if (result == None):
                    print(key, ' null')
                    print(url)
        page_manager.done = True
        return result
    async def save_spec(self,url,download_directory):
        path = os.path.join(download_directory,url.split('/')[-1]+'.json')
        if (not os.path.exists(path)):
            try:
                info = await self._get_info(url)
                with open(path,'w') as file:
                    file.write(json.dumps(info))
            except Exception as e:
                print(e)
                self.exception_log.append({
                    'url' : url,
                    'exception' : str(e)
                })
        else:
            print('File {} aldready exits.'.format(url.split('/')[-1]+'.json'))