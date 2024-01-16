#!/usr/bin/python3
from telethon import TelegramClient, errors
from telethon.tl.functions.channels import JoinChannelRequest
import logging
import argparse
import time

api_id = 29652078
api_hash = 'fe53fd4bb6dd5693234087137dcf69a6'

parser = argparse.ArgumentParser(
    description='script for sending messages to groups in telegram'
)
parser.add_argument(
    '-s',
    '--session',
    help='name for session file',
    type=str,
    default='sessions/ya.session',
)
# parser.add_argument('--log', help='path to log')
parser.add_argument(
    '--join',
    '-j',
    help='join to groups and then send messages',
    action='store_true',
)
parser.add_argument(
    '-m',
    '--message',
    help='specify the message',
    default='⚪️КУПЛЮ⚪️\n🏦IziBANK - 200грн💳\n🏦MONOBANK - 300грн💳\n🏦Возьму на вериф PayPal, только те кто не делал, мануал даю и помогу пройти вериф, оплата 400грн💳\n☯️Отзывы в Био☯️\n✅Гарант+✅\n✍️ПИСАТЬ В ЛС✍️',
)
args = parser.parse_args()

logging.basicConfig(
    # filename=f'/tmp/{args.session}.log',
    filename='/tmp/tg_sender.log',
    # filemode='a',
    format='%(asctime)s %(levelname)s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.INFO,
)

client = TelegramClient(args.session, api_id, api_hash)
# anon - swiatiymykolay 3.0 ###osnova
# anon1 - zeitgeist
# anon3 - swiatiymykilay 2.0
# anon_second_acc - swiatiymykolay 1.0


async def join_to_groups(chats: list):
    print(f'{len(chats)} chats, wow')  # 111 chats
    logging.info(f'length of the list of groups to join - {len(chats)}')
    ids = []

    for chat in chats:
        try:
            entity_data = await client.get_entity(chat)
            if not getattr(entity_data, 'gigagroup'):
                # if not entity_data.gigagroup:
                await client(JoinChannelRequest(entity_data.id))
                ids.append(entity_data.id)
                print(f'joined {chat}')
            else:
                logging.info(f'chat {chat} is not a group')
                print(chats, '- is not group.')
        except errors.FloodWaitError as e:
            print('Have to sleep', e.seconds, 'seconds')
            logging.error(f'{chat} chat. have to sleep: {e.seconds}')
            time.sleep(e.seconds)
        except Exception as e:
            logging.error(f'{chat} chat: {e}')
            print('ERROR!!!', chat, e)

    print(f'FINAL VER of list({len(ids)}): {ids}')
    logging.info(
        f'list of groups to which you have successfully joined({len(ids)}) - {ids}'
    )


async def send_message():
    chat_ids = [
        1855350939,
        1754625717,
        1680618639,
        1528899060,
        1475949586,
        1758049235,
        1614717712,
        1447881815,
        1501665029,
        1184724643,
        1636967054,
        1615009491,
        1712913057,
        1850702329,
        1610766948,
        1701646218,
        1530690696,
        1617771543,
        1595794482,
        1774164748,
        1238938468,
        1616485880,
        1578304615,
        1658834972,
        1541456882,
        1536736886,
        1531438691,
        1694473718,
        1623343861,
        1510659039,
        1467238052,
        1323807420,
        1732649784,
        1342224390,
        1657227224,
        1540491904,
        1432401094,
        1507179411,
        1787445552,
        1777401514,
        1785186965,
        1579705772,
        1556387192,
        1151723788,
        1622272440,
        1808837939,
        1677820444,
        1609471246,
        1563484486,
        1573875293,
        1744724916,
        1184828877,
        1759788262,
        1755120511,
        1759028366,
        1634075193,
        1670925876,
        1672846133,
        1338914897,
        1693155823,
        1605157319,
        1577121069,
        1808798568,
        1729303521,
        1690002969,
        1519725839,
        1758088450,
        1869929717,
        1641247789,
        1669089107,
        1510946472,
        1683368646,
        1655030539,
        1729361624,
        1538000487,
        1723445196,
        1518626833,
        1608390371,
        1621779286,
        1871218088,
        1386040716,
        1803761903,
        1786913068,
        1672143642,
        1844254394,
        1633165184,
        1233915745,
        1696618602,
        1628653758,
        1591908042,
        1629485485,
        1711979550,
        1676656084,
        1624627639,
        1657352071,
        1589262288,
        1192035345,
        1718925273,
        1793891374,
        1215895213,
        1551423485,
        1575775234,
        1218529532,
        1711979550,
    ]
    logging.info('sending messages starts now')
    for chat_id in chat_ids:
        try:
            await client.send_message(
                chat_id,
                args.message,
                # "✅Куплю документы под pay pal✅\n✅Нужно фото айди или заграна и выписка из привата, моно или а банка на УКР языке✅\n✅Оплата 200грн✅\n✅НУЖНО МНОГО✅\n✅Писать в ЛС, отзывы в БИО✅",
            )
            print('sent to', chat_id)
        except Exception as e:
            print(str(e))
            logging.error(f'{chat_id} - {str(e)}')
            # await client.send_message("me", str(e))
        logging.info('sending messages is over')


chat_list = [
    'chatsnumberone',
    'Verification_Gold',
    'otc_wl_chat',  # "hom3_ua_chat", # "team_of_azov"
    'secret_room_ru',
    'verifikator_akka',
    'extaazystveriff',
    'veryf_sikachenko',
    'verifikaciya_akkauntov_coinlist',
    'kyckycchat',
    'otc_verifikator',
    'ukraineverificationteam',
    'otc_easymarket',
    'no_scam_verification',
    'JONNYOTC',
    # "IceBergMarketOtc",
    'dropovodiizimani',
    'BafF_otccc',
    'bears_otc',
    'otcmarkt',
    # "btlvrfchat",
    # "OTC_red",
    'otc_blondychain',
    'gjjfv24',
    'Crypto_Mining_Bit',
    'upholdallcountry',
    'piar_chat_ua03',
    'prani_verify',
    'coinlistOCG',
    'High_Skilll',
    'OTC37',
    'verif32',
    'otctopcrypto',
    'different_akk',
    'McDuck_grupp',
    'reger_chat',
    'BJH_CHAT',
    'OTC_DragonMarket',
    'otcp2pnft',
    'veruf02',
    'OTCmarketByChain',
    'verifrubik',
    'nftotc66',
    'verifyaccountcoin',
    'wsSN0wBoYuM0MDM',
    # "Zavod_OTC", no acess
    'chatbugsbunny',
    'zarobotoksxalava',
    'prchat_pr',
    'veriff_yanko',
    'OTC_is_free',
    'piar_chat_ua02',
    'veriffchat',
    'verifma',
    'VerificationsByPilot',
    'VerificstionUK',
    'terncrypto_otc',
    'Market1OTC',
    'coinlistvngroup',
    'OTC_MARKET_EU_RU',
    'WhiteOTC',
    'verefikaciy1',
    'verif_scrooge',
    'zefs3333',
    'verificacia_ch',
    # "otcchinamarket1", no access
    'VERIFFMONEY',
    # "legitBuyerii",
    'darkbuhta',
    'Verif2020',
    'cryptootcc',
    'harrypotter_otc',
    'CloudOTCMARKET',
    # "Otzixuo",
    # "Jackk_chat",
    'account_verification_chatt',
    'drop_visaobnal1',
    'verif_escrow',
    'verif_escre',
    'ahV51D7FQjU1N2F',
    'no_kacap',
    'midas_otc',
    'DETROIT_VERIIIIIF',
    'OHVERIF',
    'buyacclegit',
    'burmalde_verif',
    'VeriFicaTionSJoYs',
    'h1h776',
    'chatkoliamainer',
    'pops_2222',
    'chattpiarchik',
    'otcmarket_drops',
    'KYCFleaMarket',
    'cryptoprchat',
    'izicashchat',
    'agraba_otc_chat',
    'OTC_ANANAS',
    'veriferchat',
    'ncIGO_Bounty',
    'cremindsverif',
    'verifuachat',
    'p2pdropi',
    'otcverifs',
    'truveriff',
    'Kyc_Service_Gor1',
    'coinBomber228',
    'respectromz',
    'bablotok_otc',
    'mediasocialmarket',
    'jobs1ua_free',
    'VEREF_CHAT',
    'work_verif27',
    'mudrevskiy_otc',
    'jobs1ualan',
    'xstoran_verif',
    # "cryptomasonlofficialotc", no access
    'truveriff',
    # list #1
    'otc_easymarket',
    'OTC37',
    'terncrypto_otc',
    'otcp2pnft',
    'RisingStarOTC',
    'otcship',
    'ProfitOTC',
    'otc_youngapp',
    'otc_cryptonft',
    'OTCBlack_Market',
    'cake_otc_market',
    'otc_market_nft_crypto',
    'mediasocialmarket',
    'KING_OTC',
    'WTSotc',
    'OTC_DragonMarket',
    'OTCmarketByChain',
    'OTCtrust1',
    'chornyy_rynok',
    'MuskOTC',
    'TVS_OTC',
    'otctopcrypto',
    'SCryptOTC',
    'mudrevskiy_otc',
    'Zavod_OTC',
    'OTC_FANTASY',
    'otc_Family',
    'OTC_red',
    'churchillotc',
    'boOm_Zyc',
    'OTC_lowFee',
    'OTCTlPMARKET',
    'WhiteOTC',
    'otc_market_cryptos',
    'otc_crypto_markt',
    'whales_otc',
    'otc_wl_chat',
    'NFTMarketSOL',
    'otc_marketgucci',
    'otc_verifikator',
    'otc_nft_community',
    'crpt_otc',
    'VietNamOTCWhitelist',
    'otcmarket3',
    'otcchinamarket1',
    'OTC_number_one',
    'nftotc',
    'otc_service_ban',
    'cryptomarket_otc',
    'otc_market_usdt',
    'otccryptopushka',
    'tokensale_otc',
    'market_community',
    'toptrustchat_otc',
    'otc_narnia',
    'sbotc',
    'nft_otc_community',
    'worldwide_otc',
    'poseidon_otc',
    'otc_market1',
    'topclab_otc',
    'otcescrow',
    'tcvnotc',
    'otc_mediaopt',
    'otcmarkt',
    'buyyercoinlist30',
    'otcmarketcryptoukr',
    'otccryptonftvietnam',
    'coinlistvietnamgroup',
    'veriffmoney',
    'OTCISOIDOMARKET',
    'otccryptoglobal',
    'newly_trading_otc_qx',
    'otctokensalemarket',
    'CoinlistOtcEscrow',
    'market1otc',
    'otc_investorhub',
    'coinlist_account1',
    'upholdallcountry',
    'smartbuyerandseller',
    'theotcroom',
    'bears_otc',
    'wts_wtb_accs',
    'tytopotcmarket',
    'otc_14',
    'exchangecoinlist',
    'otc_europe',
    'supplyotc',
    'coinlistvngroup',
    'plus4accountbar',
    'swoptoky_exchange',
    'otc_market_eu_ru',
    'nftmarkettotc',
    'otc_market_europe',
    'buyacclegit',
    'otc_premium',
    'otc_is_free',
    'cryptosotc',
    'otc_blondychain',
    'OTC_Bull',
    'crypto_accounts',
    'doubletop_otc',
    'nike_otc',
    'escrowschat',
    'coinlist_allcountry',
    'web_investors',
    'smartrubby',
    'otc_marketcrypto',
    # list #2
    'ObshchenieR',
    'otc_Family',
    'Swoptoky_exchange',
    'GR_Verifications',
    'otcp2pnft',
    'verifikacii_dropy_dropovody',
    'cryptosotc',
    'zarabotok_na_verifikaciyah0',
    'VEREF_CHAT',
    'prani_verify',
    'arendaprodajabankcard',
    'bdsverivication',
    'verif_worrk',
    'bossveref',
    'crypto_exclusiv1',
    'chatiki0',
    'verifyaccountcoin',
    'no_scam_verification',
]

with client:
    if args.join == True:
        client.loop.run_until_complete(join_to_groups(chat_list))
        client.loop.run_until_complete(send_message())
    else:
        client.loop.run_until_complete(send_message())
