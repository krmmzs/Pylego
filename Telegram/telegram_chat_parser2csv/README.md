# telegram chat parese to csv

No extra packages required, only Python 3.x!

## Usage

```bash
python3 telegram-chat-parser.py results.json
```

results is the json file you exported from Telegram Desktop.

## The output format

Once the script is done parsing, the result CSV file will have the format bellow:

-   `msg_id`: the unique identifier of the message
-   `sender`: the literal name of the sender
-   `sender_id`: the unique identifier of the sender
-   `reply_to_mesg_id`: if the message is a reply, this column will store the id of that message, or -1 otherwise
-   `date`: date time stamp of the message
-   `msg_type`: can be one of the following: `text, sticker, file, photo, poll, location or link`
-   `msg_content`: the text content the message, already cleaned in terms of newline and spaces; if the message was not a text (sticker, media, etc) this field will store the path pointing to the media
-   `has_mention`: it will be `1` if there's a mention in the text, `0` otherwise
-   `has_email`: it will be `1` if there's a email in the text, `0` otherwise
-   `has_phone`: it will be `1` if there's a phone contact in the message, `0` otherwise
-   `has_hashtag`: it will be `1` if there's a hashtag in the text, `0` otherwise
-   `is_bot_command`: it will be `1` if the message is a bot command, `0` otherwise
