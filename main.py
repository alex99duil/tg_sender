from telethon import TelegramClient, errors
from telethon.tl.functions.channels import JoinChannelRequest
import sys
import time

api_id = 29652078
api_hash = "fe53fd4bb6dd5693234087137dcf69a6"
client = TelegramClient("anon1", api_id, api_hash)


async def join_to_groups(chats: list):
    print(f"{len(chats)} chats, wow")  # 111 chats
    ids = []

    for chat in chats:
        try:
            entity_data = await client.get_entity(chat)
            if not entity_data.megagroup:
                await client(JoinChannelRequest(entity_data.id))
                ids.append(entity_data.id)
                print(f"joined {chat}")
            else:
                print(chats, "- is not group.")
        except errors.FloodWaitError as e:
            print("Have to sleep", e.seconds, "seconds")
            time.sleep(e.seconds)
            continue
        except Exception as e:
            print("ERROR!!!", chat, e)

    print(f"FINAL VER of list({len(ids)}): {ids}")


async def main():
    chat_ids = [
        1855350939,
        1754625717,
        1680618639,
        # 1528899060,
        # 1475949586,
        # 1758049235,
        # 1614717712,
        # 1447881815,
        # 1501665029,
        # 1184724643,
        # 1636967054,
        # 1615009491,
        # 1712913057,
        # 1850702329,
        # 1610766948,
        # 1701646218,
        # 1530690696,
        # 1617771543,
        # 1595794482,
        # 1774164748,
        # 1238938468,
        # 1145981949,
        # 1616485880,
        # 1578304615,
        # 1658834972,
        # 1541456882,
        # 1536736886,
        # 1531438691,
        # 1694473718,
        # 1623343861,
        # 1510659039,
        # 1467238052,
        # 1323807420,
        # 1342224390,
        # 1657227224,
        # 1540491904,
        # 1507179411,
        # 1787445552,
        # 1623020856,
        # 1777401514,
        # 1785186965,
        # 1579705772,
        # 1556387192,
        # 1151723788,
        # 1622272440,
        # 1808837939,
        # 1677820444,
        # 1609471246,
        # 1563484486,
        # 1573875293,
        # 1744724916,
        # 1184828877,
        # 1759788262,
        # 1755120511,
        # 1759028366,
        # 1634075193,
        # 1670925876,
        # 1672846133,
        # 1338914897,
        # 1693155823,
        # 1605157319,
        # 1808798568,
        # 1729303521,
        # 1690002969,
        # 1519725839,
        # 1758088450,
        # 1869929717,
        # 1641247789,
        # 1669089107,
        # 1510946472,
        # 1683368646,
        # 1655030539,
        # 1729361624,
        # 1538000487,
        # 1723445196,
        # 1518626833,
        # 1294093497,
        # 1608390371,
        # 1621779286,
        # 1871218088,
        # 1386040716,
        # 1803761903,
        # 1786913068,
        # 1672143642,
        # 1633165184,
        # 1233915745,
        # 1696618602,
        # 1628653758,
        # 1591908042,
        # 1629485485,
        # 1711979550,
        # 1676656084,
        # 1624627639,
        # 1657352071,
        # 1589262288,
        # 1192035345,
        # 1718925273,
        # 1793891374,
        # 1215895213,
        # 1551423485,
        # 1575775234,
        # 1218529532,
        # 1711979550,
    ]
    while True:
        for chat_id in chat_ids:
            try:
                await client.send_message(
                    chat_id,
                    "✅✅✅Куплю фото айди карты или заграна и выписку из банка на англ языке для pay pal , писать в ЛС, оплата за 1 пак 200грн💰✅✅✅✅✅✅",
                )
                print("sent to", chat_id)
            except Exception as e:
                print(str(e))
                # await client.send_message("me", str(e))
            time.sleep(0.5)
        time.sleep(3600)


chats = [
    "chatsnumberone",
    "Verification_Gold",
    "otc_wl_chat",  # "hom3_ua_chat", # "team_of_azov"
    "secret_room_ru",
    "verifikator_akka",
    "extaazystveriff",
    "veryf_sikachenko",
    "verifikaciya_akkauntov_coinlist",
    "kyckycchat",
    "otc_verifikator",
    "ukraineverificationteam",
    "otc_easymarket",
    "no_scam_verification",
    "JONNYOTC",
    # "IceBergMarketOtc",
    "dropovodiizimani",
    "BafF_otccc",
    "bears_otc",
    "otcmarkt",
    # "btlvrfchat",
    # "OTC_red",
    "otc_blondychain",
    "gjjfv24",
    "Crypto_Mining_Bit",
    "upholdallcountry",
    "piar_chat_ua03",
    "prani_verify",
    "coinlistOCG",
    "High_Skilll",
    "OTC37",
    "verif32",
    "otctopcrypto",
    "different_akk",
    "McDuck_grupp",
    "reger_chat",
    "BJH_CHAT",
    "OTC_DragonMarket",
    "otcp2pnft",
    "veruf02",
    "OTCmarketByChain",
    "verifrubik",
    "nftotc66",
    "verifyaccountcoin",
    "wsSN0wBoYuM0MDM",
    # "Zavod_OTC", no acess
    "chatbugsbunny",
    "zarobotoksxalava",
    "prchat_pr",
    "veriff_yanko",
    "OTC_is_free",
    "piar_chat_ua02",
    "veriffchat",
    "verifma",
    "VerificationsByPilot",
    "VerificstionUK",
    "terncrypto_otc",
    "Market1OTC",
    "coinlistvngroup",
    "OTC_MARKET_EU_RU",
    "WhiteOTC",
    "verefikaciy1",
    "verif_scrooge",
    "zefs3333",
    "verificacia_ch",
    # "otcchinamarket1", no access
    "VERIFFMONEY",
    # "legitBuyerii",
    "darkbuhta",
    "Verif2020",
    "cryptootcc",
    "harrypotter_otc",
    "CloudOTCMARKET",
    # "Otzixuo",
    # "Jackk_chat",
    "account_verification_chatt",
    "drop_visaobnal1",
    "verif_escrow",
    "verif_escre",
    "ahV51D7FQjU1N2F",
    "no_kacap",
    "midas_otc",
    "DETROIT_VERIIIIIF",
    "OHVERIF",
    "buyacclegit",
    "burmalde_verif",
    "VeriFicaTionSJoYs",
    "h1h776",
    "chatkoliamainer",
    "pops_2222",
    "chattpiarchik",
    "otcmarket_drops",
    "KYCFleaMarket",
    "cryptoprchat",
    "izicashchat",
    "agraba_otc_chat",
    "OTC_ANANAS",
    "veriferchat",
    "ncIGO_Bounty",
    "cremindsverif",
    "verifuachat",
    "p2pdropi",
    "otcverifs",
    "truveriff",
    "Kyc_Service_Gor1",
    "coinBomber228",
    "respectromz",
    "bablotok_otc",
    "mediasocialmarket",
    "jobs1ua_free",
    "VEREF_CHAT",
    "work_verif27",
    "mudrevskiy_otc",
    "jobs1ualan",
    "xstoran_verif",
    # "cryptomasonlofficialotc", no access
    "truveriff",
]

with client:
    if len(sys.argv) > 1:
        client.loop.run_until_complete(join_to_groups(chats))
    else:
        client.loop.run_until_complete(main())
