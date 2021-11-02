import webbrowser as browser


def abrir(trigger):
    if 'instagram' in trigger:
        browser.open('https://www.instagram.com/?hl=pt-br')

    elif 'facebook' in trigger:
        browser.open('https://pt-br.facebook.com/')

    elif 'google' in trigger:
        browser.open('https://www.google.com.br/')

    elif 'youtube' in trigger:
        browser.open('https://www.youtube.com/')

    elif 'spotify' in trigger:
        browser.open('https://accounts.spotify.com/en/login/?continue=https:%2F%2Fwww.spotify.com%2Fapi%2Fgrowth%2Fl2l'
                     '-redirect&_locale=pt-BR')

    elif 'twitter' in trigger:
        browser.open('https://twitter.com/login?lang=pt')

    elif 'tik tok' in trigger:
        browser.open('https://www.tiktok.com/foryou?lang=pt_BR')

    elif 'outlook' in trigger:
        browser.open('https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1607531749&rver=7.0.6737.0&wp=MBI'
                     '_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26RpsCsrfState%3d65aa56c7-f222'
                     '-d247-0817-d89c5003042a&id=292841&aadredir=1&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid='
                     '90015')

    elif 'gmail' in trigger:
        browser.open('https://accounts.google.com/ServiceLogin/signinchooser?service=mail&passive=true&rm=false&'
                     'continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr='
                     '1&osid=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin')

    elif 'pinterest' in trigger:
        browser.open('https://br.pinterest.com/')

    elif 'twitch' in trigger:
        browser.open('https://www.twitch.tv/')

    elif 'netflix' in trigger:
        browser.open('https://www.netflix.com/br/login')

    elif 'mercado livre' in trigger:
        browser.open('https://www.mercadolivre.com.br/')

    elif 'netshoes' in trigger:
        browser.open('https://www.netshoes.com.br/?campaign=gglepqbdg&gclid=EAIaIQobChMI6pDzmqzB7QIVi4eRCh381wQnEAA'
                     'YASAAEgL2SPD_BwE&gclsrc=aw.ds')

    elif 'mercado pago' in trigger:
        browser.open('https://www.mercadolivre.com/jms/mlb/lgz/login?platform_id=MP&go=https%3A%2F%2Fwww.mercadopago'
                     '.com.br%2Fpaid%3Futm_term%3DCAMPANHA_HOME_INSTITUCIONAL_PURO%26utm_term%3DEXTENSAO_'
                     'PRECO%26gclid%3DEAIaIQobChMI59G2sqzB7QIVCYGRCh2hDAjcEAAYASAAEgJe__D_BwE%26utm_content%3DINST_'
                     'HOME_MP%26matt_tool%3D34485376%26utm_campaign%3DMLB_MP_G_AO_BKW_X_SEARCH_INST_TXS_HOME%26utm_'
                     'medium%3Dsearch%26matt_word%3DMLB_MP_G_AO_BKW_X_SEARCH_INST_TXS_HOME%26utm_source%3Dgoogle%26'
                     'code%3DS3ARCHGO&loginType=explicit')

    elif 'renner' in trigger:
        browser.open('https://www.lojasrenner.com.br/')

    elif 'marisa' in trigger:
        browser.open('https://www.marisa.com.br/')

    elif 'discord' in trigger:
        browser.open('https://discord.com/login?redirect_to=%2Fchannels%2F753222488850432040%2F753222488850432042')

    elif 'casas bahia' in trigger:
        browser.open('https://www.casasbahia.com.br/')

    elif 'magazine luiza' in trigger:
        browser.open('https://www.magazineluiza.com.br/')

    elif 'whatsapp' in trigger:
        browser.open('https://web.whatsapp.com/')

    elif 'ifood' in trigger:
        browser.open('https://www.ifood.com.br/')

    elif 'riachuelo' in trigger:
        browser.open('https://www.riachuelo.com.br/')

    elif 'uber' in trigger:
        browser.open('https://www.uber.com/global/pt-br/sign-in/')

    elif 'cea' in trigger:
        browser.open('https://www.cea.com.br/')

    elif 'americanas' in trigger:
        browser.open('https://www.americanas.com.br/')

    elif 'apple' in trigger:
        browser.open('https://www.apple.com/br/?afid=p238%7CsikJb1MHC-dc_mtid_1870765e38482_pcrid_482040369839_pgrid'
                     '_17049243418_&cid=aos-br-kwgo-brand--slid---product-')

    elif 'motorola' in trigger:
        browser.open('https://www.motorola.com.br/')

    elif 'samsung' in trigger:
        browser.open('https://www.samsung.com/br/')

    elif 'leroymerlin' in trigger:
        browser.open('https://www.leroymerlin.com.br/')

    elif 'sodimac' in trigger:
        browser.open('https://www.sodimac.com.br/sodimac-br/')

    elif 'telhanorte' in trigger:
        browser.open('https://www.telhanorte.com.br/')

    elif 'telegram' in trigger:
        browser.open('https://web.telegram.org/#/login')

    elif 'xiaomi' in trigger:
        browser.open('https://www.mi.com/br/')

    elif 'tesla' in trigger:
        browser.open('https://www.tesla.com/')

    elif 'disneyplus' in trigger:
        browser.open('https://www.disneyplus.com/pt-br/login')

    elif 'cinépolis' in trigger:
        browser.open('https://www.cinepolis.com.br/')

    elif 'cinemark' in trigger:
        browser.open('https://www.cinemark.com.br/')

    elif 'telecine' in trigger:
        browser.open('https://www.telecineplay.com.br/entrar')

    elif 'prime vídeo' in trigger:
        browser.open('https://www.primevideo.com/?ref_=dvm_pds_amz_br_dc_s_g_mkw_s2Hv03IvM-dc_pcrid_388732931008&'
                     'mrntrk=slid__pgrid_62046161446_pgeo_1001731_x__ptid_kwd-296527732991')

    elif 'amazon' in trigger:
        browser.open('https://www.amazon.com.br/')
