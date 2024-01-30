#!./env//bin/python3
import argparse
import logging
import os
import time
from typing import LiteralString
from tools.tg_groups import chat_list

from dotenv import load_dotenv
from telethon import TelegramClient, errors
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.types import Channel, InputChannel


async def join_to_groups(client: TelegramClient, chats: list[LiteralString]) -> None:
    print(f"{len(chats)} chats, wow")  # 207 chats
    logging.info(f"length of the list of groups to join - {len(chats)}")
    not_groups: list[LiteralString] = []

    for chat in chats:
        try:
            entity_data = await client.get_entity(chat)
            if (isinstance(entity_data, Channel) and type(entity_data.access_hash) == int):
                await client(JoinChannelRequest(InputChannel(entity_data.id, entity_data.access_hash)))
                print(f"joined {chat}")
            else:
                not_groups.append(chat)
                logging.info(f"chat {chat} is not a group")
                print(chat, "- is not a group.")
        except errors.FloodWaitError as e:
            print("Have to sleep", e.seconds, "seconds")
            logging.error(f"{chat} chat. have to sleep: {e.seconds}")
            time.sleep(e.seconds)
        except Exception as e:
            logging.error(f"{chat} chat: {e}")
            print("ERROR!!!", chat, e)

    print(f"FINAL VER of list({len(not_groups)}): {not_groups}")
    logging.info(f"list of groups to which you have successfully joined({len(not_groups)}) - {not_groups}")


async def send_message(client: TelegramClient, chats: list[LiteralString], message: str) -> None:
    logging.info("sending messages starts now")
    for chat in chats:
        try:
            await client.send_message(chat, message)
            print("sent to", chat)
        except Exception as e:
            print(str(e))
            logging.error(f"{chat} - {str(e)}")
            # await client.send_message("me", str(e)) #send log to saved messages.
    logging.info("sending messages has finished")


def get_arguments() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="script for sending messages to groups in telegram"
    )
    parser.add_argument(
        "-s",
        "--session",
        help="name for session file",
        type=str,
        default="sessions/ya.session",
    )
    # parser.add_argument('--log', help='path to log')
    parser.add_argument(
        "--join",
        "-j",
        help="join to groups and then send messages",
        action="store_true",
    )
    parser.add_argument(
        "-m",
        "--message",
        help="specify the message",
        default="⚪️КУПЛЮ⚪️\n🏦IziBANK - 200грн💳\n🏦MONOBANK - 300грн💳\n🏦Возьму на вериф PayPal, только те кто не делал, мануал даю и помогу пройти вериф, оплата 400грн💳\n☯️Отзывы в Био☯️\n✅Гарант+✅\n✍️ПИСАТЬ В ЛС✍️",
    )
    return parser


def main(chats: list[LiteralString]) -> None:
    args = get_arguments().parse_args()

    logging.basicConfig(
        # filename=f'/tmp/{args.session}.log',
        filename="/tmp/tg_sender.log",
        # filemode='a',
        format="%(asctime)s %(levelname)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.INFO,
    )

    load_dotenv()
    client = TelegramClient(args.session, int(os.environ["api_id"]), os.environ["api_hash"])

    with client:
        if args.join == True:
            client.loop.run_until_complete(join_to_groups(client, chats))
        else:
            client.loop.run_until_complete(send_message(client, chats, args.message))



if __name__ == "__main__":
    main(chat_list)
