import requests
import re
import json
import hashlib
import random
import time
import os
from datetime import datetime, timezone, timedelta
from bs4 import BeautifulSoup
from urllib.parse import urljoin

class ProxyCollector:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
        })

        self.proxy_sources = [
            "https://t.me/s/iSeqaro",
            "https://t.me/s/SOSkeyNET", 
            "https://t.me/s/irancpi_vpn",
            "https://t.me/s/times_config",
            "https://t.me/s/PewezaVPN",
            "https://t.me/s/dadavpnn",
            "https://t.me/s/vpn_openet",
            "https://t.me/s/AR14N24b",
            "https://t.me/s/ConfigsHub",
            "https://t.me/s/oneclickvpnkeys",
            "https://t.me/s/V2rayCollector",
            "https://t.me/s/Porteqal3",
            "https://t.me/s/Knightshieldgroup",
            "https://t.me/s/injector_1401Ehi",
            "https://t.me/s/filembad",
            "https://t.me/s/Daily_Configs",
            "https://t.me/s/Bestproxy_24",
            "https://t.me/s/v2ra_config",
            "https://t.me/s/sogoandfuckyourlove",
            "https://t.me/s/Blank_Vpn",
            "https://t.me/s/brayirani",
            "https://t.me/s/DarcProxy",
            "https://t.me/s/proxy_mardomkhiaban",
            "https://t.me/s/textplanetorg", 
            "https://t.me/s/starlinkvatan",
            "https://t.me/s/duckvp_n",
            "https://t.me/s/shankamil",
            "https://t.me/s/chat_nakone",
            "https://t.me/s/irproxy",
            "https://t.me/s/KnightShield",
            "https://t.me/s/MARAMBASHI1",
            "https://t.me/s/V2rayNG_Cila",
            "https://t.me/s/king_v2raay",
            "https://t.me/s/shahincrafto",
            "https://t.me/s/DailyV2Config",
            "https://t.me/s/rxv2ray",
            "https://t.me/s/as12rgh",
            "https://t.me/s/Pro_v2rayShop",
            "https://t.me/s/WorldVPN6",
            "https://t.me/s/free_servers1",
            "https://t.me/s/skypro_vpn",
            "https://t.me/VayNora",
            "https://t.me/V2ray_khabar",
            "https://t.me/+3qTKfGn3u1EzOWQ8",
            "https://t.me/surfboardv2ray",
            "https://t.me/subHiddify",
            "https://t.me/s/rojproxy",
            "https://t.me/v2nodes",
            "https://t.me/hack_proxy1",
            "https://t.me/s/v2ray_configs_pool",
            "https://t.me/s/XpnTeam",
            "https://t.me/v2rayNGcloud",
            "https://t.me/s/ZibaNabz",
            "https://t.me/s/FreakConfig",
            "https://t.me/s/V_2rey",
            "https://t.me/s/V2ray_Alpha",
            "https://t.me/s/PROXY_MTM",
            "https://t.me/s/SiNABiGO",
            "https://t.me/s/v2rayng12023",
            "https://t.me/s/vlessconfig",
            "https://t.me/s/piazshekan",
            "https://t.me/s/Free_Internet_Iran",
            "https://t.me/s/ARv2ray",
            "https://t.me/s/VPNCUSTOMIZE",
            "https://t.me/s/UnlimitedDev",
            "https://t.me/s/MARAMBASHI",
            "https://t.me/s/PrivateVPNs",
            "https://t.me/s/client_proo",
            "https://t.me/s/nufilter",
            "https://t.me/s/icv2ray",
            "https://t.me/s/Vpn_Mikey",
            "https://t.me/s/v2rayngvpn",
            "https://t.me/s/kingspeedchanel",
            "https://t.me/s/VPN_Xpace",
            "https://t.me/s/SVNTEAM",
            "https://t.me/s/WPSNET",
            "https://t.me/s/v2rayng_fa2",
            "https://t.me/s/Hope_Net",
            "https://t.me/s/ServerNett",
            "https://t.me/s/alfred_config",
            "https://t.me/s/allv2ray",
            "https://t.me/s/alo_v2rayng",
            "https://t.me/s/angus_vpn",
            "https://t.me/s/antifilterservice",
            "https://t.me/s/asak_vpn",
            "https://t.me/s/asintech",
            "https://t.me/s/astrovpn_official",
            "https://t.me/s/awlix_ir",
            "https://t.me/s/azarbayjab1",
            "https://t.me/s/bermudavpn24",
            "https://t.me/s/bigsmoke_config",
            "https://t.me/s/blueberrynetwork",
            "https://t.me/s/bored_vpn",
            "https://t.me/s/catvpns",
            "https://t.me/s/cconfig_v2ray",
            "https://t.me/s/city_v2rayng",
            "https://t.me/s/configforvpn",
            "https://t.me/s/configpositive",
            "https://t.me/s/configt",
            "https://t.me/s/configv2rayforfree",
            "https://t.me/s/custom_config",
            "https://t.me/s/customizev2ray",
            "https://t.me/s/cvrnet",
            "https://t.me/s/dailyv2ry",
            "https://t.me/s/daredevill_404",
            "https://t.me/s/deragv2ray",
            "https://t.me/s/digiv2ray",
            "https://t.me/s/directvpn",
            "https://t.me/s/donald_vpn",
            "https://t.me/s/drvpn_net",
            "https://t.me/s/easy_free_vpn",
            "https://t.me/s/entrynet",
            "https://t.me/s/ev2rayy",
            "https://t.me/s/expressvpn_420",
            "https://t.me/s/external_net",
            "https://t.me/s/farahvpn",
            "https://t.me/s/fasst_vpn",
            "https://t.me/s/fast_2ray",
            "https://t.me/s/fastkanfig",
            "https://t.me/s/fastshadow_vpn",
            "https://t.me/s/filterk0sh",
            "https://t.me/s/flyv2ray",
            "https://t.me/s/freakconfig1",
            "https://t.me/s/freakconfig2",
            "https://t.me/s/free1_vpn",
            "https://t.me/s/free_vpn02",
            "https://t.me/s/freeconfig01",
            "https://t.me/s/freeconfigvpns",
            "https://t.me/s/freeiranweb",
            "https://t.me/s/freenapsternetv",
            "https://t.me/s/freev2raym",
            "https://t.me/s/freevirgoolnet",
            "https://t.me/s/fsv2ray",
            "https://t.me/s/ghalagyann",
            "https://t.me/s/godv2ray_ng",
            "https://t.me/s/golestan_vpn",
            "https://t.me/s/grizzlyvpn",
            "https://t.me/s/hajimamadvpn",
            "https://t.me/s/hamster_vpnn",
            "https://t.me/s/hatunnel_vpn",
            "https://t.me/s/hopev2ray",
            "https://t.me/s/hormozvpn",
            "https://t.me/s/hose_io",
            "https://t.me/s/imrv2ray",
            "https://t.me/s/ios_v2",
            "https://t.me/s/ipcloudflaretamiz",
            "https://t.me/s/ipv2ray",
            "https://t.me/s/iranbaxvpn",
            "https://t.me/s/iraniv2ray_config",
            "https://t.me/s/irv2rey",
            "https://t.me/s/isvvpn",
            "https://t.me/s/kafing_2",
            "https://t.me/s/kingofilter",
            "https://t.me/s/lightning6",
            "https://t.me/s/ln2ray",
            "https://t.me/s/lombo_channel",
            "https://t.me/s/mahdiserver",
            "https://t.me/s/manzariyeh_rasht",
            "https://t.me/s/maznet",
            "https://t.me/s/meli_proxyy",
            "https://t.me/s/mester_v2ray",
            "https://t.me/s/mgvpnsale",
            "https://t.me/s/mikasavpn",
            "https://t.me/s/miov2ray",
            "https://t.me/s/moftinet",
            "https://t.me/s/msv2ray",
            "https://t.me/s/msv2raynp",
            "https://t.me/s/n2vpn",
            "https://t.me/s/netmellianti",
            "https://t.me/s/new_proxy_channel",
            "https://t.me/s/noforcedheaven",
            "https://t.me/s/npvv2rayfilter",
            "https://t.me/s/ohvpn",
            "https://t.me/s/orange_vpns",
            "https://t.me/s/outline_ir",
            "https://t.me/s/outline_vpn",
            "https://t.me/s/pars_vpn3",
            "https://t.me/s/parsashonam",
            "https://t.me/s/pashmam_vpn",
            "https://t.me/s/pishiserver",
            "https://t.me/s/pqv2ray",
            "https://t.me/s/proprojec",
            "https://t.me/s/proxiiraniii",
            "https://t.me/s/proxy_n1",
            "https://t.me/s/proxyfull",
            "https://t.me/s/proxystore11",
            "https://t.me/s/prroxyng",
            "https://t.me/s/puni_shop_v2rayng",
            "https://t.me/s/qeshmserver",
            "https://t.me/s/realvpnmaster",
            "https://t.me/s/rnrifci",
            "https://t.me/s/satoshivpn",
            "https://t.me/s/savagev2ray",
            "https://t.me/s/selinc",
            "https://t.me/s/shadowproxy66",
            "https://t.me/s/shokhmiplus",
            "https://t.me/s/sinavm",
            "https://t.me/s/sobi_vpn",
            "https://t.me/s/special_net8",
            "https://t.me/s/spikevpn",
            "https://t.me/s/srcvpn",
            "https://t.me/s/summertimeus",
            "https://t.me/s/superv2rang",
            "https://t.me/s/tehranargo",
            "https://t.me/s/tehranargo1",
            "https://t.me/s/thexconfig",
            "https://t.me/s/thunderv2ray",
            "https://t.me/s/tv_v2ray",
            "https://t.me/s/ultrasurf_12",
            "https://t.me/s/v2_city",
            "https://t.me/s/v2aryng_vpn",
            "https://t.me/s/v2boxvpnn",
            "https://t.me/s/v2graphy",
            "https://t.me/s/v2net_iran",
            "https://t.me/s/v2ngfast",
            "https://t.me/s/v2pedia",
            "https://t.me/s/v2ra2",
            "https://t.me/s/v2raand",
            "https://t.me/s/v2rang00",
            "https://t.me/s/v2range",
            "https://t.me/s/v2raxx",
            "https://t.me/s/v2ray1_ng",
            "https://t.me/s/v2ray6388",
            "https://t.me/s/v2ray_alpha07",
            "https://t.me/s/v2ray_fark",
            "https://t.me/s/v2ray_ng",
            "https://t.me/s/v2ray_one1",
            "https://t.me/s/v2ray_raha",
            "https://t.me/s/v2ray_rolly",
            "https://t.me/s/v2rayargon",
            "https://t.me/s/v2raych",
            "https://t.me/s/v2rayfast",
            "https://t.me/s/v2rayfast_7",
            "https://t.me/s/v2rayfree_irr",
            "https://t.me/s/v2rayiman",
            "https://t.me/s/v2raylandd",
            "https://t.me/s/v2rayn2g",
            "https://t.me/s/v2rayng3",
            "https://t.me/s/v2rayng_city",
            "https://t.me/s/v2rayng_madam",
            "https://t.me/s/v2rayng_prime",
            "https://t.me/s/v2rayngv",
            "https://t.me/s/v2rayngvpnn",
            "https://t.me/s/v2rayngzendegimamad",
            "https://t.me/s/v2rayprotocol",
            "https://t.me/s/v2rayyngvpn",
            "https://t.me/s/v2rez",
            "https://t.me/s/v2rray_ng",
            "https://t.me/s/v2ry_proxy",
            "https://t.me/s/v2ryng01",
            "https://t.me/s/v2ryng_vpn",
            "https://t.me/s/v2ryngfree",
            "https://t.me/s/v2safe",
            "https://t.me/s/v2safee",
            "https://t.me/s/v_2rayngvpn",
            "https://t.me/s/vip_vpn_2022",
            "https://t.me/s/vipv2rayngnp",
            "https://t.me/s/vipv2rey",
            "https://t.me/s/vipvpn_v2ray",
            "https://t.me/s/vistav2ray",
            "https://t.me/s/vmesc",
            "https://t.me/s/vmess_ir",
            "https://t.me/s/vmess_iran",
            "https://t.me/s/vmesskhodam",
            "https://t.me/s/vmesskhodam_vip",
            "https://t.me/s/vmessprotocol",
            "https://t.me/s/vp22ray",
            "https://t.me/s/vpfreen",
            "https://t.me/s/vpn_accounti",
            "https://t.me/s/vpn_free_v2ray5",
            "https://t.me/s/vpn_ioss",
            "https://t.me/s/vpn_kanfik",
            "https://t.me/s/vpn_proxy_custom",
            "https://t.me/s/vpn_tehran",
            "https://t.me/s/vpn_vip_nor",
            "https://t.me/s/vpnazadland",
            "https://t.me/s/vpnconfignet",
            "https://t.me/s/vpnfail_v2ray",
            "https://t.me/s/vpnhubmarket",
            "https://t.me/s/vpnkanfik",
            "https://t.me/s/vpnmasi",
            "https://t.me/s/vpnowl",
            "https://t.me/s/vpnstorefast",
            "https://t.me/s/vpnv2rayngv",
            "https://t.me/s/vpnxyam_ir",
            "https://t.me/s/wedbaztel",
            "https://t.me/s/wsbvpn",
            "https://t.me/s/xvproxy",
            "https://t.me/s/zede_filteri",
            "https://t.me/s/zibanabz",
            "https://t.me/s/zohalserver",
            "https://t.me/s/vpnaloo",
            "https://t.me/s/godot404",
            "https://t.me/s/prrofile_purple",
            "https://t.me/s/vpnsaint",
            "https://t.me/s/azadnet",
            "https://t.me/s/appsooner",
            "https://t.me/s/V2SayFreeArchive",
            "https://t.me/s/shadoowvpnn",
            "https://t.me/s/v2fre",
            "https://t.me/s/ConfigsHubPlus",
            "https://t.me/s/imtproxy_ir",
            "https://t.me/s/PASARGAD_V2rayNG",
            "https://t.me/s/Outline_ir",
            "https://t.me/s/club_profsor",
            "https://t.me/s/Speeds_vpn1",
            "https://t.me/s/Airdorap_Free",
            "https://t.me/s/VPN_SOLVE",
            "https://t.me/s/bglvps",
            "https://t.me/s/mrsoulb",
            "https://t.me/s/config_fre",
            "https://t.me/s/AchaVPN",
            "https://t.me/s/Artemisvpn1",
            "https://t.me/s/heyatserver",
            "https://t.me/s/Capoit",
            "https://t.me/s/SimChin_ir",
            "https://t.me/s/abiidar_server",
            "https://t.me/s/Marambashi2",
            "https://t.me/s/nim_vpn_ir",
            "https://t.me/s/keysOutline",
            "https://t.me/s/ai_duet",
            "https://t.me/s/amirinventor2010",
            "https://t.me/s/ana_service",
            "https://t.me/s/apple_x1",
            "https://t.me/s/argo_vpn1",
            "https://t.me/s/argooo_vpn",
            "https://t.me/s/armodvpn",
            "https://t.me/s/avaalvpn",
            "https://t.me/s/bislullproxy",
            "https://t.me/s/black_vpn1",
            "https://t.me/s/canfing_vpn",
            "https://t.me/s/chanel_v2ray_2",
            "https://t.me/s/change_ip1",
            "https://t.me/s/config_proxy",
            "https://t.me/s/configasli",
            "https://t.me/s/configfa",
            "https://t.me/s/configms",
            "https://t.me/s/configology",
            "https://t.me/s/configpluse",
            "https://t.me/s/configscenter",
            "https://t.me/s/configx2ray",
            "https://t.me/s/confing_chanel",
            "https://t.me/s/connect_sho",
            "https://t.me/s/cook_vpn",
            "https://t.me/s/customv2ray",
            "https://t.me/s/customvpnserver",
            "https://t.me/s/daily_configs",
            "https://t.me/s/dailytek",
            "https://t.me/s/dalton_ping",
            "https://t.me/s/dargiiriis",
            "https://t.me/s/darkfiilter",
            "https://t.me/s/deamnet_proxy",
            "https://t.me/s/dextoken_10x",
            "https://t.me/s/ehsawn8",
            "https://t.me/s/eliteproxyv2",
            "https://t.me/s/elitevpnv2",
            "https://t.me/s/evay_vpn",
            "https://t.me/s/farstar_vpn",
            "https://t.me/s/fastvpnorummobile",
            "https://t.me/s/father_vpn",
            "https://t.me/s/filtershekan_channel",
            "https://t.me/s/flystoreir",
            "https://t.me/s/free1ss",
            "https://t.me/s/free_outline_keys",
            "https://t.me/s/free_serverir",
            "https://t.me/s/freeconfigsplus",
            "https://t.me/s/freevpnatm",
            "https://t.me/s/g0dv2ray",
            "https://t.me/s/getconfigir",
            "https://t.me/s/gh_v2rayng",
            "https://t.me/s/ghalagyann2",
            "https://t.me/s/ghotb_scarf",
            "https://t.me/s/goldenshiinevpn",
            "https://t.me/s/green_config",
            "https://t.me/s/hacknashid",
            "https://t.me/s/imhdiyvp",
            "https://t.me/s/info_2it_channel",
            "https://t.me/s/ip_cf_config",
            "https://t.me/s/ipstatic1",
            "https://t.me/s/iranmedicalvpn",
            "https://t.me/s/iransoftware90",
            "https://t.me/s/iseqaro",
            "https://t.me/s/jd_vpn",
            "https://t.me/s/jeyksatan",
            "https://t.me/s/jiedianf",
            "https://t.me/s/jiedianssr",
            "https://t.me/s/jiujied",
            "https://t.me/s/kesslervpn",
            "https://t.me/s/key_outline",
            "https://t.me/s/kilid_stor",
            "https://t.me/s/komail315",
            "https://t.me/s/kurdistan_vpn_perfectt",
            "https://t.me/s/kurdvpn1",
            "https://t.me/s/lakvpn1",
            "https://t.me/s/lexernet",
            "https://t.me/s/lranonline_new",
            "https://t.me/s/mahanvpn",
            "https://t.me/s/mahxray",
            "https://t.me/s/masterserver1",
            "https://t.me/s/mdvpn184",
            "https://t.me/s/megavpn_link",
            "https://t.me/s/mehduox_vpn",
            "https://t.me/s/mehrosaboran",
            "https://t.me/s/melov2ray",
            "https://t.me/s/mimitdl",
            "https://t.me/s/minovpnch",
            "https://t.me/s/moein_insta",
            "https://t.me/s/mood_tarinhaa",
            "https://t.me/s/mowjproxy",
            "https://t.me/s/mpproxy",
            "https://t.me/s/msv2flyng",
            "https://t.me/s/mt_proxy",
            "https://t.me/s/mtproxy22_v2ray",
            "https://t.me/s/mtproxy_lists",
            "https://t.me/s/mtpv2ray",
            "https://t.me/s/narco_nett",
            "https://t.me/s/nationalproxytelegram",
            "https://t.me/s/netaccount",
            "https://t.me/s/netfreedom0",
            "https://t.me/s/nitroserver_ir",
            "https://t.me/s/nofilter_v2rayng",
            "https://t.me/s/noviin_tel",
            "https://t.me/s/ntconfig",
            "https://t.me/s/ntgreenplus",
            "https://t.me/s/oonfig",
            "https://t.me/s/orgempirenet",
            "https://t.me/s/outlineopenkey",
            "https://t.me/s/outlinereleasedkey",
            "https://t.me/s/outlinev2rayng",
            "https://t.me/s/outlinevpn_ru",
            "https://t.me/s/payam_nsi",
            "https://t.me/s/pistachiovpn",
            "https://t.me/s/proxie",
            "https://t.me/s/proxse11",
            "https://t.me/s/proxy_hiddfy",
            "https://t.me/s/proxy_kafee",
            "https://t.me/s/proxy_mtproto_vpns_free",
            "https://t.me/s/proxy_v2box",
            "https://t.me/s/proxyandvpnofficial1",
            "https://t.me/s/proxycrone",
            "https://t.me/s/proxygodratmand",
            "https://t.me/s/proxygrizzly",
            "https://t.me/s/proxyvpnvip",
            "https://t.me/s/psiphonf",
            "https://t.me/s/pubg_vpn_ir",
            "https://t.me/s/pydriclub",
            "https://t.me/s/qafor_1",
            "https://t.me/s/qrv2ray",
            "https://t.me/s/rayanconf",
            "https://t.me/s/redfree8",
            "https://t.me/s/rockettunnel",
            "https://t.me/s/rojproxy",
            "https://t.me/s/rsv2ray",
            "https://t.me/s/satarvpn1",
            "https://t.me/s/satellitenewspersian",
            "https://t.me/s/savagenet",
            "https://t.me/s/server444",
            "https://t.me/s/server_nekobox",
            "https://t.me/s/serverii",
            "https://t.me/s/serversiran11",
            "https://t.me/s/seven_ping",
            "https://t.me/s/shadowsockskeys",
            "https://t.me/s/sharecentrepro",
            "https://t.me/s/shh_proxy",
            "https://t.me/s/singbox1",
            "https://t.me/s/skivpn",
            "https://t.me/s/sobyv2ray",
            "https://t.me/s/socks5tobefree",
            "https://t.me/s/speedconfig00",
            "https://t.me/s/srovpn",
            "https://t.me/s/sstpvpn",
            "https://t.me/s/strongprotocol",
            "https://t.me/s/tawanaclub",
            "https://t.me/s/tgvpn6",
            "https://t.me/s/tiny_vpn_official",
            "https://t.me/s/turboo_server",
            "https://t.me/s/ultranett",
            "https://t.me/s/uvpn_org",
            "https://t.me/s/v222ray",
            "https://t.me/s/v2box_free",
            "https://t.me/s/v2ra_ng_iran",
            "https://t.me/s/v2rang_da",
            "https://t.me/s/v2ray03",
            "https://t.me/s/v2ray_83",
            "https://t.me/s/v2ray_cartel",
            "https://t.me/s/v2ray_collector",
            "https://t.me/s/v2ray_extractor",
            "https://t.me/s/v2ray_fd",
            "https://t.me/s/v2ray_free_conf",
            "https://t.me/s/v2ray_god",
            "https://t.me/s/v2ray_melli",
            "https://t.me/s/v2ray_sos",
            "https://t.me/s/v2ray_sub",
            "https://t.me/s/v2ray_tz",
            "https://t.me/s/v2ray_v_vpn",
            "https://t.me/s/v2ray_vmes",
            "https://t.me/s/v2ray_vmess_free",
            "https://t.me/s/v2ray_youtube",
            "https://t.me/s/v2raycrow",
            "https://t.me/s/v2rayexpress",
            "https://t.me/s/v2rayfree",
            "https://t.me/s/v2rayfree_server",
            "https://t.me/s/v2raying",
            "https://t.me/s/v2raymelliii",
            "https://t.me/s/v2rayn5",
            "https://t.me/s/v2rayng_1378",
            "https://t.me/s/v2rayng_fars",
            "https://t.me/s/v2rayng_fast",
            "https://t.me/s/v2rayng_matsuri",
            "https://t.me/s/v2rayngb",
            "https://t.me/s/v2rayngconfiig",
            "https://t.me/s/v2rayngn",
            "https://t.me/s/v2rayngraisi",
            "https://t.me/s/v2rayngrit",
            "https://t.me/s/v2rayngseven",
            "https://t.me/s/v2rayngte",
            "https://t.me/s/v2rayngvpn_1",
            "https://t.me/s/v2rayopen",
            "https://t.me/s/v2rayproxy",
            "https://t.me/s/v2rayroz",
            "https://t.me/s/v2rayvlp",
            "https://t.me/s/v2rayvpn2",
            "https://t.me/s/v2rayvpnchannel",
            "https://t.me/s/v2rayweb",
            "https://t.me/s/v2reay",
            "https://t.me/s/v2ret",
            "https://t.me/s/v2source",
            "https://t.me/s/v2trayproxy",
            "https://t.me/s/vaslvip",
            "https://t.me/s/vaynora",
            "https://t.me/s/vip_fragment_v2ray",
            "https://t.me/s/vipoutline",
            "https://t.me/s/vipv2rayvip",
            "https://t.me/s/vmessiran",
            "https://t.me/s/vmess_vless_v2rayng",
            "https://t.me/s/vmessorg",
            "https://t.me/s/vp_n1",
            "https://t.me/s/vpn451",
            "https://t.me/s/vpn4ir_1",
            "https://t.me/s/vpn_arta",
            "https://t.me/s/vpn_bal0uch",
            "https://t.me/s/vpn_kade01",
            "https://t.me/s/vpn_kadeh_iran",
            "https://t.me/s/vpn_meliii",
            "https://t.me/s/vpn_storm",
            "https://t.me/s/vpnaiden",
            "https://t.me/s/vpnepic",
            "https://t.me/s/vpnfastservice",
            "https://t.me/s/vpnfree85",
            "https://t.me/s/vpnhouse_official",
            "https://t.me/s/vpnmeg",
            "https://t.me/s/vpnod",
            "https://t.me/s/vpnplusee_free",
            "https://t.me/s/vpnserverrr",
            "https://t.me/s/vpnstable",
            "https://t.me/s/vpnv2raytop",
            "https://t.me/s/vpnx1x",
            "https://t.me/s/vtworay_wolf",
            "https://t.me/s/wancloudfa",
            "https://t.me/s/wedbazvpn",
            "https://t.me/s/wolf_vpn02",
            "https://t.me/s/xiv2ray",
            "https://t.me/s/xyzquantvpn",
            "https://t.me/s/yejoriconfig",
            "https://t.me/s/zdyz2",
            "https://t.me/s/ZedBaz_vpn",
            "https://t.me/s/zedmodeonvpn",
            "https://t.me/s/zerov2shop",
            "https://t.me/s/zvpnn",
            "https://t.me/s/FreeNetPlus1",
            "https://t.me/s/Express_freevpn",
            "https://t.me/s/manVPN",
            "https://t.me/s/vpnv2r4y",
            "https://t.me/s/V2All",
            "https://t.me/s/V2ConfigGB",
            "https://t.me/s/ittechnoland",
            "https://t.me/s/NET2PROXY",
            "https://t.me/s/Vpn_Sky",
            "https://t.me/s/Proxy_v2ry",
            "https://t.me/s/sorenab2",
            "https://t.me/s/configproxyy",
            "https://t.me/s/Tweety_Proxy",
            "https://t.me/s/SPARTAN_YT",
            "https://t.me/s/v2rayngtn",
            "https://t.me/s/tazaxy",
            "https://t.me/s/networld_vpn",
            "https://t.me/s/V2HUBIR",
            "https://t.me/s/Leecher56",
            "https://t.me/s/v2ray313",
            "https://t.me/s/persianvpnhub",
            "https://t.me/s/SSRSUB",
            "https://t.me/s/YeBeKhe",
            "https://t.me/s/Proxymelimon",
            "https://t.me/s/Gp_Config",
            "https://t.me/s/v2ray_unit",
            "https://t.me/s/npvv2rayn",
            "https://t.me/s/Abeautifulnumber",
            "https://t.me/s/v2proxfree",
            "https://t.me/s/N3TWRK",
            "https://t.me/s/v2dogs_n"
        ]

        self.dead_cache = {}
        self.failed_counter = {}
        self.cache_file = "configs/proxies/dead_cache.json"
        self.load_dead_cache()

        self.proxy_patterns = [
            r'(\d{1,3}(?:\.\d{1,3}){3}:\d{2,5})',
            r'(mtproto://[^\s"<]+)',
            r'(tg://proxy\?[^\s"<]+)',
            r'(https://t\.me/proxy\?[^\s"<]+)',
        ]

    def load_dead_cache(self):
        try:
            if os.path.exists(self.cache_file):
                with open(self.cache_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    for url, t in data.items():
                        self.dead_cache[url] = datetime.fromisoformat(t)
        except:
            self.dead_cache = {}

    def save_dead_cache(self):
        try:
            os.makedirs(os.path.dirname(self.cache_file), exist_ok=True)
            with open(self.cache_file, 'w', encoding='utf-8') as f:
                json.dump(
                    {k: v.isoformat() for k, v in self.dead_cache.items()},
                    f, ensure_ascii=False, indent=2
                )
        except:
            pass

    def update_dead_cache(self, url):
        now = datetime.now(timezone.utc)
        self.failed_counter[url] = self.failed_counter.get(url, 0) + 1
        if self.failed_counter[url] >= 3:
            self.dead_cache[url] = now
            self.save_dead_cache()
            print(f"  → Added to dead cache (failed {self.failed_counter[url]} times)")

    def should_skip_source(self, url):
        if url in self.dead_cache:
            diff = datetime.now(timezone.utc) - self.dead_cache[url]
            if diff < timedelta(hours=48):
                print(f"  → Skipped (dead cache {int(diff.total_seconds()/3600)}h ago)")
                return True
            del self.dead_cache[url]
            self.failed_counter.pop(url, None)
            self.save_dead_cache()
        return False

    def get_last_post_time(self, html):
        try:
            soup = BeautifulSoup(html, 'html.parser')
            time_tag = soup.find('time')
            if not time_tag:
                return None
            dt_str = time_tag.get('datetime')
            if not dt_str:
                return None
            return datetime.fromisoformat(dt_str.replace('Z', '+00:00'))
        except:
            return None

    def adaptive_delay(self):
        time.sleep(random.uniform(0.6, 1.5))

    def fetch_page(self, url):
        try:
            r = self.session.get(url, timeout=20, allow_redirects=True)
            r.raise_for_status()
            return r.text
        except:
            return ""

    def extract_from_html(self, html, base_url=None):
        proxies = []
        soup = BeautifulSoup(html, 'html.parser')
        elements = soup.find_all(['textarea', 'code', 'pre', 'div', 'span', 'p'])
        for el in elements:
            text = el.get_text()
            for pattern in self.proxy_patterns:
                matches = re.findall(pattern, text, re.IGNORECASE)
                proxies.extend(matches)
        links = soup.find_all('a', href=True)
        for a in links:
            label = a.get_text(strip=True).lower()
            href = a['href']
            if any(k in label for k in ['proxy', 'پروکسی', 'mtproto', 'telegram', 'connect']):
                full_url = urljoin(base_url, href)
                html2 = self.fetch_page(full_url)
                if html2:
                    for pattern in self.proxy_patterns:
                        matches = re.findall(pattern, html2, re.IGNORECASE)
                        proxies.extend(matches)
        return proxies

    def clean_proxy(self, p):
        return p.strip().replace('\n', '').replace('\r', '')

    def validate_proxy(self, p):
        p = self.clean_proxy(p)
        if p.startswith(('mtproto://', 'tg://proxy', 'https://t.me/proxy')):
            return True
        if ':' in p:
            try:
                parts = p.split(':', 1)
                ip_parts = parts[0].split('.')
                if len(ip_parts) == 4:
                    for part in ip_parts:
                        if not part.isdigit() or int(part) < 0 or int(part) > 255:
                            return False
                port = int(parts[1])
                return 1 <= port <= 65535
            except:
                return False
        return False

    def deduplicate(self, proxies):
        seen = set()
        result = []
        for p in proxies:
            h = hashlib.md5(p.encode()).hexdigest()
            if h not in seen:
                seen.add(h)
                result.append(p)
        return result

    def categorize(self, proxies):
        cat = {'http': [], 'https': [], 'socks4': [], 'socks5': [], 'mtproto': [], 'other': []}
        for p in proxies:
            p = self.clean_proxy(p)
            if p.startswith(('mtproto://', 'tg://proxy', 'https://t.me/proxy')):
                cat['mtproto'].append(p)
            elif p.startswith('socks4://'):
                cat['socks4'].append(p)
            elif p.startswith('socks5://'):
                cat['socks5'].append(p)
            elif p.startswith('https://'):
                cat['https'].append(p)
            elif p.startswith('http://'):
                cat['http'].append(p)
            else:
                if ':' in p:
                    cat['http'].append(p)
                else:
                    cat['other'].append(p)
        return cat

    def process_sources(self, limit_per_channel=10):
        proxies_per_source = {}
        failed = []
        dead_skipped = 0
        skipped_inactive = 0

        print(f"Processing {len(self.proxy_sources)} sources...\n")

        for i, url in enumerate(self.proxy_sources, 1):
            print(f"[{i}/{len(self.proxy_sources)}] {url}")
            
            if self.should_skip_source(url):
                dead_skipped += 1
                continue

            html = self.fetch_page(url)
            if not html:
                self.update_dead_cache(url)
                failed.append(url)
                self.adaptive_delay()
                continue

            if 't.me/s/' in url:
                last_post_time = self.get_last_post_time(html)
                if last_post_time and datetime.now(timezone.utc) - last_post_time > timedelta(days=2):
                    self.update_dead_cache(url)
                    skipped_inactive += 1
                    self.adaptive_delay()
                    continue

            raw = self.extract_from_html(html, url)
            valid = [p for p in raw if self.validate_proxy(p)]

            if valid:
                if limit_per_channel and 't.me/s/' in url:
                    proxies_per_source[url] = valid[:limit_per_channel]
                else:
                    proxies_per_source[url] = valid
                self.failed_counter[url] = 0

            self.adaptive_delay()

        collected = []
        for lst in proxies_per_source.values():
            collected.extend(lst)

        unique = self.deduplicate(collected)
        categories = self.categorize(unique)

        return categories, len(unique), len(failed), dead_skipped, skipped_inactive

    def save_results(self, categories):
        ts = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        os.makedirs('configs/proxies', exist_ok=True)

        all_items = []
        for k, v in categories.items():
            if v:
                path = f"configs/proxies/{k}.txt"
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(
                        f"# {k.upper()} Proxies\n# Updated: {ts}\n# Count: {len(v)}\n\n" +
                        "\n".join(v)
                    )
                all_items.extend(v)

        if all_items:
            with open("configs/proxies/all.txt", 'w', encoding='utf-8') as f:
                f.write(
                    f"# All Proxies\n# Updated: {ts}\n# Total: {len(all_items)}\n\n" +
                    "\n".join(all_items)
                )

        return len(all_items)

def main():
    print("=" * 60)
    print("ARISTA PROXY COLLECTOR v1.3 | Telegram Focused Edition")
    print("=" * 60)

    collector = ProxyCollector()
    categories, total, failed, dead_skipped, inactive_skipped = collector.process_sources(limit_per_channel=10)
    saved = collector.save_results(categories)

    print("\n✅ PROCESSING COMPLETE")
    print(f"Total unique proxies: {total}")
    print(f"Saved: {saved}")
    print(f"Failed sources: {failed}")
    print(f"Dead-cache skipped: {dead_skipped}")
    print(f"Inactive channels skipped: {inactive_skipped}")

if __name__ == "__main__":
    main()
