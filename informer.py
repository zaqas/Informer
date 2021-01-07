import webbrowser as browser
import time

websites = ['https://news.gooya.com/',
            'https://www.rfi.fr/fa/',
            'https://per.euronews.com/',
            'https://www.radiofarda.com/',
            'https://aftabnews.ir/',
            'https://www.asriran.com/',
            'https://www.bbc.com/persian',
            'https://www.balatarin.com/',
            'https://baztab.ir/',
            'https://www.dw.com/fa-ir',
            'https://www.pyknet.net/',
            'https://donya-e-eqtesad.com/',
            'https://www.zeitoons.com/',
            'https://www.tasnimnews.com/',
            'https://www.tabnak.ir/',
            'https://ir.sputniknews.com/',
            'https://fa.shafaqna.com/',
            'https://farsi.alarabiya.net/',
            'https://etemadonline.com/',
            'https://www.entekhab.ir/',
            'https://www.peykeiran.com/',
            'https://eslahatnews.com/',
            'https://fararu.com/',
            'https://www.farsnews.ir/',
            'https://www.hamshahrionline.ir/',
            'https://www.ilna.news/',
            'https://www.independentpersian.com/',
            'https://iranwire.com/fa',
            'https://www.irna.ir/',
            'https://www.isna.ir/',
            'https://www.kaleme.com/?theme=fast',
            'https://www.khabaronline.ir/',
            'https://www.alef.ir/',
            'https://kayhan.london/fa/',
            'https://www.mashreghnews.ir/',
            'https://www.mehrnews.com/',
            'https://melimazhabi.com/',
            'https://www.mizanonline.com/',
            'https://www.parsine.com/',
            'https://ir.mondediplo.com/',
            'https://www.pishkhan.com/all']


def main():
    browser.open_new(websites[0])
    for i in websites[1:]:
        browser.open_new_tab(i)
        time.sleep(3)





if __name__ == '__main__':
    main()
