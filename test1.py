import requests

cookies = {
    '_ga': 'GA1.1.1015550465.1777190708',
    '_ga_JB8X4ZTQZX': 'GS2.1.s1777190708$o1$g1$t1777191341$j34$l0$h0',
    'session': 'b8668e07-aa27-4699-878d-8e20d49b7734',
    'session.sig': '5m39BuiRyp2dNVSbG6aPVjS_xDk',
    '_ga_9HJV4PGNGJ': 'GS2.1.s1777191370$o1$g1$t1777191684$j29$l0$h0',
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,az;q=0.4',
    'priority': 'u=1, i',
    'referer': 'https://kientuong.lienquan.garena.vn/trang-chu',
    'sec-ch-ua': '"Google Chrome";v="147", "Not.A/Brand";v="8", "Chromium";v="147"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36',
    # 'cookie': '_ga=GA1.1.1015550465.1777190708; _ga_JB8X4ZTQZX=GS2.1.s1777190708$o1$g1$t1777191341$j34$l0$h0; session=b8668e07-aa27-4699-878d-8e20d49b7734; session.sig=5m39BuiRyp2dNVSbG6aPVjS_xDk; _ga_9HJV4PGNGJ=GS2.1.s1777191370$o1$g1$t1777191447$j57$l0$h0',
}

response = requests.get('https://kientuong.lienquan.garena.vn/api/player/get', cookies=cookies, headers=headers)
print(response.json())