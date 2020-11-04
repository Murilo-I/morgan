import webbrowser as browser


def whato_play(trigger):
    if 'eletrônica' in trigger:
        playlists('eletrônica')

    elif 'funk' in trigger:
        playlists('funk')

    elif 'sertanejo' in trigger:
        playlists('sertanejo')

    elif 'rock' in trigger:
        playlists('rock')

    elif 'rap' in trigger:
        playlists('rap')

    elif 'pop smoke' in trigger:
        playlists('pop smoke')

    elif 'post malone' in trigger:
        playlists('post malone')

    elif 'kevinho' in trigger:
        playlists('kevinho')

    elif 'luan santana' in trigger:
        playlists('luan santana')

    elif 'marshmello' in trigger:
        playlists('marshmello')

    elif 'eminem' in trigger:
        playlists('eminem')

    elif 'wesley safadão' in trigger:
        playlists('wesley safadão')

    elif 'mc livinho' in trigger:
        playlists('mc livinho')

    elif 'ed sheeran' in trigger:
        playlists('ed sheeran')

    elif 'shawn mendes' in trigger:
        playlists('shawn mendes')

    elif 'samba' in trigger:
        playlists('samba')

    elif 'pagode' in trigger:
        playlists('pagode')


def playlists(album):
    if album == 'pop smoke':
        browser.open('https://www.youtube.com/watch?v=Q9pjm4cNsfc&list=PLrqfOeU4oaWzrCWvuyju4wuGjaJ0N5L3A&index=1')

    elif album == 'eletrônica':
        browser.open('https://www.youtube.com/watch?v=2zToEPpFEN8&list=PL_Q15fKxrBb5d4FzxegXGGkW2eAgtukpi&index=1')

    elif album == 'funk':
        browser.open('https://www.youtube.com/watch?v=Tun92VU2OkU&list=PLCwAHfhr-Gc82BO57__8Y-wEvZz8ytlHG&index=1')

    elif album == 'sertanejo':
        browser.open('https://www.youtube.com/watch?v=M76qUQTt_Sw&list=RDQMaN3fxIo2Kwk&index=1')

    elif album == 'rock':
        browser.open('https://www.youtube.com/watch?v=kXYiU_JCYtU&list=PLZ1dJqY6KWOXGGeIlZqleztqta23wHMGG&index=1')

    elif album == 'rap':
        browser.open('https://www.youtube.com/watch?v=JFm7YDVlqnI&list=PL-FVH5VWgRPHNz24zZ5_FLHQWoidN6O1d&index=1')

    elif album == 'post malone':
        browser.open('https://www.youtube.com/watch?v=ApXoWvfEYVU&list=PLegvV8yC11jbsUdqKEkIazprdTm71fU1z&index=1')

    elif album == 'kevinho':
        browser.open('https://www.youtube.com/watch?v=WAb1xxYzycw&list=PLbnysjjM_VIm3wMCA6_sBs5wkefVBTfG8&index=1')

    elif album == 'luan santana':
        browser.open('https://www.youtube.com/watch?v=PcXtzbdCd-E&list=PL952uGL-ahB_MvfTLvExCr1nrLKsONuQQ&index=1')

    elif album == 'marshmello':
        browser.open('https://www.youtube.com/watch?v=ALZHF5UqnU4&list=PLEMoDqX-7M9Ro8XuRRmprhNO2_4_rj7nP&index=1')

    elif album == 'eminem':
        browser.open('https://www.youtube.com/watch?v=_Yhyp-_hX2s&list=PLC0w3lEHx2SEisFu76dsAC1JxqjWZOYr1&index=1')

    elif album == 'wesley safadão':
        browser.open('https://www.youtube.com/watch?v=Jtler_CFqHI&list=PL92KYhulRUL9K3eITtBpqDPvb5hFa0Tx8&index=1')

    elif album == 'mc livinho':
        browser.open('https://www.youtube.com/watch?v=Sn0wA_ERHVU&list=PL4dYBPEeVh609FNO7_0aLefydncIDdGHr&index=1')

    elif album == 'ed sheeran':
        browser.open('https://www.youtube.com/watch?v=JGwWNGJdvx8&list=PLaq655wqcKDlaw569c2frEOlsF_S5HYZl&index=1')

    elif album == 'shawn mendes':
        browser.open('https://www.youtube.com/watch?v=Pkh8UtuejGw&list=PLOYP-X0Ialymfu4X9sl4skhNRh8K2GoRz&index=1')

    elif album == 'samba':
        browser.open('https://www.youtube.com/watch?v=eHSIhLG-Clw&list=PLfmShFzlmLLE0onNn2yxUP6VnHm-ufRIs&index=1')

    elif album == 'pagode':
        browser.open('https://www.youtube.com/watch?v=c4XeTP11EI8&list=PLws-Q6lwJkI1jq4kJbugdcAJryK2u_vi1&index=1')
