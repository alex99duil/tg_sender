#!/usr/bin/env python3

import argparse
import logging
import os
import time
from typing import LiteralString

from dotenv import load_dotenv
from telethon import TelegramClient, errors
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.types import Channel, InputChannel, Message

from tools.tg_groups import chat_list


async def get_message_from_saved(client: TelegramClient) -> Message | None:
    saved_messages_chat = await client.get_me()

    # get latest message from "Saved Messages"
    msg = await client.get_messages(saved_messages_chat, limit=1)
    if not msg[0].message:
        logging.error(
            "There is no message in Saved Messages! You must run the script with the -m option "
            "or paste the message into \"Saved Messages\""
        )
        # client.send_message() #@ok_nope about error
        return None
    else:
        print(msg[0].message)
        return msg[0].message
    # await client.send_message('me', msg[0].message)


async def move_chats_to_folder(client: TelegramClient, ids: list[int], folder_id: int = 1) -> None:
    async for dialog in client.iter_dialogs(folder=0):  # get all dialogs not in archive
        # if isinstance(dialog.entity, Channel) and dialog.entity.megagroup is True:
        if dialog.entity.id in ids:
            await dialog.archive(folder=folder_id)


async def join_to_groups(
    client: TelegramClient, input_chats: list[LiteralString], archive: bool = False
) -> None:
    ids: list[int] = []  # a list of group id's to which client have joined

    async for dialog in client.iter_dialogs():
        # if the user has already joined, removes the group from the list
        if isinstance(dialog.entity, Channel) and dialog.entity.username is not None:
            url = f"https://t.me/{dialog.entity.username}".lower()
            for chat in input_chats:
                if url == chat:
                    input_chats.remove(chat)

            # if url in input_chats:
            #     input_chats.remove(url)

    logging.info(f"length of the list of groups to join - {len(input_chats)}")

    for chat in input_chats:
        try:
            entity_data = await client.get_entity(chat)  # FloodWaitError in this line
            if (
                (isinstance(entity_data, Channel))
                and entity_data.megagroup is True
                and isinstance(entity_data.access_hash, int)
            ):
                await client(
                    JoinChannelRequest(InputChannel(entity_data.id, entity_data.access_hash))
                )
                ids.append(entity_data.id)
                logging.info(f"{chat} - joined successfully.")
                if archive:
                    await move_chats_to_folder(client, [entity_data.id])  # move chat to folder
                    logging.debug("Moved to archive!")
            else:
                logging.error(f"{chat} - is not a group")
        except errors.FloodWaitError as e:
            logging.error(f"{chat} - FloodWaitError. Have to sleep: {e.seconds} seconds")
            # if ids:
            #     await move_chats_to_folder(client, ids)  #while sleep move joined chats to archive
            #     ids.clear()
            time.sleep(e.seconds)
        except Exception as e:
            logging.critical(f"{chat}: {e}")


async def send_message(client: TelegramClient, chats: list[LiteralString], message: str) -> None:
    logging.info("-----sending messages starts now-----")
    for chat in chats:
        try:
            await client.send_message(chat, message)
            print("sent to", chat)
        except Exception as e:
            logging.error(f"send to {chat} - {str(e)}")
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
        "--archive",
        "-a",
        help="move groups to archive",
        action="store_true",
    )
    parser.add_argument(
        "--get_message",
        "-g",
        help="get latest message from saved messages",
        action="store_true",
    )
    parser.add_argument(
        "-m",
        "--message",
        help="specify the message",
        default="Беру МоноБанк⬜️⬛️ \n"
        + "В оренду на 3-5 дней!⏳\n"
        + "Оплата сразу по факту перевязки\n"
        + "300UAH💳\n"
        + "Отзывы в био✅\n"
        + "Писать только сюда в ЛС👉🏾\n"
        + "@IISELEERII",
    )
    return parser


def main(chats: list[LiteralString]) -> None:
    args = get_arguments().parse_args()

    output_logger = logging.StreamHandler()
    output_logger.setLevel("INFO")
    output_logger.setFormatter(fmt=logging.Formatter(fmt="%(levelname)s: %(message)s"))
    logging.basicConfig(
        # filename=f'/tmp/{args.session}.log',
        handlers=[logging.FileHandler("/tmp/tg_sender.log"), output_logger],
        format="%(asctime)s %(levelname)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.DEBUG,
    )
    logging.getLogger("telethon").setLevel(logging.WARNING)

    load_dotenv()
    client = TelegramClient(args.session, int(os.environ["api_id"]), os.environ["api_hash"])

    with client:
        if args.join:
            if args.archive:
                client.loop.run_until_complete(join_to_groups(client, chats, True))
            else:
                client.loop.run_until_complete(join_to_groups(client, chats))
        elif args.archive:
            client.loop.run_until_complete(move_chats_to_folder(client, []))
        elif args.get_message:
            client.loop.run_until_complete(get_message_from_saved(client))
        else:
            client.loop.run_until_complete(send_message(client, chats, args.message))


if __name__ == "__main__":
    main(chat_list)
