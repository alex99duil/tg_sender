from telethon import TelegramClient
from random import randint
import json
import time

api_id = 29652078
api_hash = "fe53fd4bb6dd5693234087137dcf69a6"
client = TelegramClient("anon", api_id, api_hash)


async def parse_users():
    user_ids = []
    chats = [
        "chatsnumberone",
        "Verification_Gold",
        # "hom3_ua_chat",
        "otc_wl_chat",
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
        "IceBergMarketOtc",
        "dropovodiizimani",
        "BafF_otccc",
        "bears_otc",
        "otcmarkt",
        "btlvrfchat",
        "OTC_red",
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
        "Zavod_OTC",
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
        "otcchinamarket1",
        "VERIFFMONEY",
        "legitBuyerii",
        "darkbuhta",
        "Verif2020",
        "cryptootcc",
        "harrypotter_otc",
        "CloudOTCMARKET",
        "Otzixuo",
        "Jackk_chat",
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
        "team_of_azov",
        "mudrevskiy_otc",
        "jobs1ualan",
        "xstoran_verif",
        "cryptomasonlofficialotc",
        "truveriff",
    ]
    for chat in chats:
        try:
            count = 0
            contacts = await client.get_participants(chat)
            for contact in contacts:
                if (
                    contact.deleted
                    == contact.bot
                    == contact.fake
                    == contact.support
                    == False
                ):
                    if contact.id not in user_ids:
                        user_ids.append(contact.id)
                    count += 1
                    # print(user_ids)
            print(f"{count} users in {chat}")
            # print(f"{j} users from group {chat} already in array")
        except Exception as e:
            print("!!!", e)

    with open("user_ids.json", "w") as f:
        json.dump(user_ids, f)


async def main():
    # async for dialog in client.iter_dialogs():
    #     print(dialog.name, "has ID", dialog.id)

    with open("user_ids.json", "r") as f:
        ids = json.load(f)

    print(f"{len(ids)} users, wow")
    while True:
        random = randint(0, len(ids) - 1)
        await client.send_message(
            ids[random],
            "✅✅✅Куплю фото айди карты или заграна и выписку из банка на англ языке для pay pal , писать в ЛС, оплата за 1 пак 200грн💰✅✅✅СРОЧНО!!!✅✅✅ Отзывы в био!!!",
        )
        time.sleep(3)


with client:
    # client.loop.run_until_complete(parse_users())
    client.loop.run_until_complete(main())
