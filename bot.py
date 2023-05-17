import re
from pyrogram import Client, filters
from telegram import Chat, ChatMember
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

api_id = 24977504
api_hash = '431a1ec75b188d6d3d46dabe99126c6e'
bot_token = '5688019347:AAGk2Gi2krOhbuOeV1r3hQH6ZdvX56A3wys'

app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)
EXEMPTED_GROUP_ID = [-1001675452200, -1001872496207, -1001972957095]
# Daftar karakter huruf yang tidak diinginkan
UNWANTED_CHARS = [
'𝔨', '𝔩', '𝔪', '𝔫', '𝔬', '𝔭', '𝔮', '𝔯', '𝔱', '𝔲', '𝔣', '𝔴', '𝔵', '𝔶', 
'𝔷', '𝖆', '𝖇', '𝖈', '𝖉', '𝖊', '𝖋', '𝖌', '𝖍', '𝖎', '𝖏', '𝖐', '𝖑', '𝖒', 
'𝖓', '𝖔', '𝖕', '𝖖', '𝖗', '𝖘', '𝖙', '𝖚', '𝖋', '𝖜', '𝖝', '𝖞', '𝖟', '𝓪', 
'𝓫', '𝓬', '𝓭', '𝓮', '𝓯', '𝓰', '𝓱', '𝓲', '𝓳', '𝓴', '𝓵', '𝓶', '𝓷', '𝓸', 
'𝓹', '𝓺', '𝓻', '𝓼', '𝓽', '𝓾', '𝓯', '𝔀', '𝔁', '𝔂', '𝔃', '𝒶', '𝒷', '𝒸', 
'𝒹', '𝑒', '𝒻', '𝑔', '𝒽', '𝒾', '𝒿', '𝓀', '𝓁', '𝓂', '𝓃', '𝑜', '𝓅', '𝓆', 
'𝓇', '𝓈', '𝓉', '𝓊', '𝒻', '𝓌', '𝓍', '𝓎', '𝓏', '𝕒', '𝕓', '𝕔', '𝕕', '𝕖', 
'𝕗', '𝕘', '𝕙', '𝕚', '𝕛', '𝕜', '𝕝', '𝕞', '𝕟', '𝕠', '𝕡', '𝕢', '𝕣', '𝕤', 
'𝕥', '𝕦', '𝕗', '𝕨', '𝕩', '𝕪', '𝕫', 'ａ ', 'ｂ ', 'ｃ ', 'ｄ ', 'ｅ ', 
'ｆ ', 'ｇ ', 'ｈ ', 'ｉ ', 'ｊ ', 'ｋ ', 'ｌ ', 'ｍ ', 'ｎ', 'ｏ ', 'ｐ'
 'ｑ ', 'ｒ ', 'ｓ ', 'ｔ ', 'ｕ ', 'ｆ ', 'ｗ ', 'ｘ ', 'ｙ ', 'ｚ ', 
'𝒶', '𝒷', '𝒸', '𝒹', '𝑒', '𝒻', '𝑔', '𝒽', '𝒾', '𝒿', '𝓀', '𝓁', '𝓂', '𝓃', 
'𝓅', '𝓆', '𝓇', '𝓈', '𝓉', '𝓊', '𝒻', '𝓌', '𝓍', '𝓎', '𝓏', 'ᴀ', 'ʙ', 'ᴄ', 
'ᴅ', 'ᴇ', 'ꜰ', 'ɢ', 'ʜ', 'ɪ', 'ᴊ', 'ᴋ', 'ʟ', 'ᴍ', 'ɴ', 'ᴏ', 'ᴘ', 'ǫ', 
'ʀ', 'ᴛ', 'ᴜ', 'ꜰ', 'ᴡ', 'ʏ', 'ᴢ', '𝐚', '𝐛', '𝐜', '𝐝', '𝐞', '𝐟', '𝐠', 
'𝐡', '𝐢', '𝐣', '𝐤', '𝐥', '𝐦', '𝐧', '𝐨', '𝐩', '𝐪', '𝐫', '𝐭', '𝐮', '𝐟', 
'𝐰', '𝐱', '𝐲', '𝐳', '𝘢', '𝘣', '𝘤', '𝘥', '𝘦', '𝘧', '𝘨', '𝘩', '𝘪', '𝘫', 
'𝘬', '𝘭', '𝘮', '𝘯', '𝘰', '𝘱', '𝘲', '𝘳', '𝘴', '𝘵', '𝘶', '𝘧', '𝘸', '𝘹', 
'𝘺', '𝘻', 
'̶a','̶','̶b','̶','̶c','̶','̶d','̶','̶e','̶','̶f','̶','̶g','̶','̶h','̶','̶i','̶','̶j','̶','̶k','̶','̶l','̶','̶m','̶','̶n','̶','̶o','̶','̶p','̶','̶q','̶','̶r','̶','̶','̶t','̶','̶','̶f','̶','̶w','̶','̶','̶y','̶','̶z', 
'ᗩ', 'ᗷ', 'ᑕ', 'ᗞ', 'ᗴ', 'ᖴ', 'Ꮐ', 'ᕼ', 'Ꮖ', 'ᒍ', 'Ꮶ', 'Ꮮ', 'ᗰ', 'ᑎ', 
'ᝪ', 'ᑭ', 'ᑫ', 'ᖇ', 'ᔑ', 'Ꭲ', 'ᑌ', 'ᖴ', 'ᗯ', '᙭', 'Ꭹ', 'Ꮓ', '𝓪', '𝓫', 
'𝓬', '𝓭', '𝓮', '𝓯', '𝓰', '𝓱', '𝓲', '𝓳', '𝓴', '𝓵', '𝓶', '𝓷', '𝓸', '𝓹', 
'𝓺', '𝓻', '𝓼', '𝓽', '𝓾', '𝓯', '𝔀', '𝔁', '𝔂', '𝔃', '𝚊', '𝚋', '𝚌', '𝚍', 
'𝚎', '𝚏', '𝚐', '𝚑', '𝚒', '𝚓', '𝚔', '𝚕', '𝚖', '𝚗', '𝚘', '𝚙', '𝚚', '𝚛', 
'𝚜', '𝚝', '𝚞', '𝚏', '𝚠', '𝚡', '𝚢', '𝚣', 'ⓐ', 'ⓑ', 'ⓒ', 'ⓓ', 'ⓔ', 'ⓕ', 
'ⓖ', 'ⓗ', 'ⓘ', 'ⓙ', 'ⓚ', 'ⓛ', 'ⓜ', 'ⓝ', 'ⓞ', 'ⓟ', 'ⓠ', 'ⓡ', 'ⓢ', 'ⓣ', 
'ⓤ', 'ⓕ', 'ⓦ', 'ⓧ', 'ⓨ', 'ⓩ', '𝘼', '𝘽', '𝘾', '𝘿', '𝙀', '𝙁', '𝙂', '𝙃', 
'𝙄', '𝙅', '𝙆', '𝙇', '𝙈', '𝙉', '𝙊', '𝙋', '𝙌', '𝙍', '𝙎', '𝙏', '𝙐', '𝙁', 
'𝙒', '𝙓', '𝙔', '𝙕', '𝙖', '𝙗', '𝙘', '𝙙', '𝙚', '𝙛', '𝙜', '𝙝', '𝙞', '𝙟', 
'𝙠', '𝙡', '𝙢', '𝙣', '𝙤', '𝙥', '𝙦', '𝙧', '𝙨', '𝙩', '𝙪', '𝙫', '𝙬', '𝙭', 
'𝙮', '𝙯', '𝗮', '𝗯', '𝗰', '𝗱', '𝗲', '𝗳', '𝗴', '𝗵', '𝗶', '𝗷', '𝗸', '𝗹', 
'𝗺', '𝗻', '𝗼', '𝗽', '𝗾', '𝗿', '𝘀', '𝘁', '𝘂', '𝘃', '𝘄', '𝘅', '𝘆', '𝘇', 
'𝘢', '𝘣', '𝘤', '𝘥', '𝘦', '𝘧', '𝘨', '𝘩', '𝘪', '𝘫', '𝘬', '𝘭', '𝘮', '𝘯', 
'𝘰', '𝘱', '𝘲', '𝘳', '𝘴', '𝘵', '𝘶', '𝘷', '𝘸', '𝘹', '𝘺', '𝘻', '𝒂', '𝒃', 
'𝒄', '𝒅', '𝒆', '𝒇', '𝒈', '𝒉', '𝒊', '𝒋', '𝒌', '𝒍', '𝒎', '𝒏', '𝒐', '𝒑', 
'𝒒', '𝒓', '𝒔', '𝒕', '𝒖', '𝒗', '𝒘', '𝒙', '𝒚', '𝒛', '𝐚', '𝐛', '𝐜', '𝐝', 
'𝐞', '𝐟', '𝐠', '𝐡', '𝐢', '𝐣', '𝐤', '𝐥', '𝐦', '𝐧', '𝐨', '𝐩', '𝐪', '𝐫', 
'𝐬', '𝐭', '𝐮', '𝐯', '𝐰', '𝐱', '𝐲', '𝐳', '𝑎', '𝑏', '𝑐', '𝑑', '𝑒', '𝑓', 
'𝑔', 'ℎ', '𝑖', '𝑗', '𝑘', '𝑙', '𝑚', '𝑛', '𝑜', '𝑝', '𝑞', '𝑟', '𝑠', '𝑡', 
'𝑢', '𝑣', '𝑤', '𝑥', '𝑦', '𝑧', '𝕒', '𝕓', '𝕔', '𝕕', '𝕖', '𝕗', '𝕘', '𝕙', 
'𝕚', '𝕛', '𝕜', '𝕝', '𝕞', '𝕟', '𝕠', '𝕡', '𝕢', '𝕣', '𝕤', '𝕥', '𝕦', '𝕧', 
'𝕨', '𝕩', '𝕪', '𝕫', '𝓪', '𝓫', '𝓬', '𝓭', '𝓮', '𝓯', '𝓰', '𝓱', '𝓲', '𝓳', 
'𝓴', '𝓵', '𝓶', '𝓷', '𝓸', '𝓹', '𝓺', '𝓻', '𝓼', '𝓽', '𝓾', '𝓿', '𝔀', '𝔁', 
'𝔂', '𝔃', '𝒶', '𝒷', '𝒸', '𝒹', '𝑒', '𝒻', '𝑔', '𝒽', '𝒾', '𝒿', '𝓀', '𝓁', 
'𝓂', '𝓃', '𝑜', '𝓅', '𝓆', '𝓇', '𝓈', '𝓉', '𝓊', '𝓋', '𝓌', '𝓍', '𝓎', '𝓏', 
'𝗔', '𝗕', '𝗖', '𝗗', '𝗘', '𝗙', '𝗚', '𝗛', '𝗜', '𝗝', '𝗞', '𝗟', '𝗠', '𝗡', 
'𝗢', '𝗣', '𝗤', '𝗥', '𝗦', '𝗧', '𝗨', '𝗩', '𝗪', '𝗫', '𝗬', '𝗭', '𝘈', '𝘉', 
'𝘊', '𝘋', '𝘌', '𝘍', '𝘎', '𝘏', '𝘐', '𝘑', '𝘒', '𝘓', '𝘔', '𝘕', '𝘖', '𝘗', 
'𝘘', '𝘙', '𝘚', '𝘛', '𝘜', '𝘝', '𝘞', '𝘟', '𝘠', '𝘡', '𝑨', '𝑩', '𝑪', '𝑫', 
'𝑬', '𝑭', '𝑮', '𝑯', '𝑰', '𝑱', '𝑲', '𝑳', '𝑴', '𝑵', '𝑶', '𝑷', '𝑸', '𝑹', 
'𝑺', '𝑻', '𝑼', '𝑽', '𝑾', '𝑿', '𝒀', '𝒁', '𝐀', '𝐁', '𝐂', '𝐃', '𝐄', '𝐅', 
'𝐆', '𝐇', '𝐈', '𝐉', '𝐊', '𝐋', '𝐌', '𝐍', '𝐎', '𝐏', '𝐐', '𝐑', '𝐒', '𝐓', 
'𝐔', '𝐕', '𝐖', '𝐗', '𝐘', '𝐙', '𝐴', '𝐵', '𝐶', '𝐷', '𝐸', '𝐹', '𝐺', '𝐻', 
'𝐼', '𝐽', '𝐾', '𝐿', '𝑀', '𝑁', '𝑂', '𝑃', '𝑄', '𝑅', '𝑆', '𝑇', '𝑈', '𝑉', 
'𝑊', '𝑋', '𝑌', '𝑍', '🅐', '🅑', '🅒', '🅓', '🅔', '🅕', '🅖', '🅗', '🅘', '🅙', 
'🅚', '🅛', '🅜', '🅝', '🅞', '🅟', '🅠', '🅡', '🅢', '🅣', '🅤', '🅕', '🅦', '🅧', 
'🅨', '🅩', '🅃', '🄴', '🄺', '🄼', '🄸', '🅄', '🅃', '🄲', '🄰', '🅁', '🅂', '🄻', 
'🄽', '🄶', '🄷', '🄽', '🄳', '🄱', '🅈', '🄾', '🄷', '𝕋', '𝕄', '𝕆', 'ℂ', '𝕌', 
'𝔸', 'ℕ', '𝕂', '𝕃', '𝔾', '𝕊', '𝕌', '𝕁', '𝕀', '𝔻' 'L', 'E', 'P', 'H', 
'N', 'G', 'W', 'D', 'B',
'Y', '0',
'T','A','K','E','M','I','Y','O','T',
'S','P','G','D'
]
@app.on_message(filters.command(["start"]))
async def start_command_handler(client, message):
    keyboard = [
        [
            InlineKeyboardButton("Add To Group", url='https://t.me/v1BNUnGcastbot?startgroup=true'),
        ],
        [
            InlineKeyboardButton("Channel", url='https://t.me/rexc0de'),
            InlineKeyboardButton("Developer",url='https://t.me/eldipion'),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await message.reply_text("Hai Tongmet Lovers\nini adalah bot penghapus gcast yang dimana menghapus per Karakter.\nuntuk menjalankan, baiknya beri akses bot menjadi admin.\n\nJika Ingin Menggunakan Bot ini Silahkan Chat Developer", reply_markup=reply_markup)

# Define a callback query handler
@app.on_callback_query()
async def callback_query_handler(client, query):
    if query.data == "button1":
        await query.message.edit_text("Anda memilih Button 1")
    elif query.data == "button2":
        await query.message.edit_text("Anda memilih Button 2")
    else:
        await query.answer()
# Tambahkan filter agar fungsi hanya dipanggil saat pesan teks baru diterima
# Fungsi untuk menghapus karakter yang tidak diinginkan dari string
def remove_unwanted_chars(text):
    for char in UNWANTED_CHARS:
        text = re.sub(char, '', text, flags=re.IGNORECASE)
    return text
# Fungsi untuk menghapus pesan yang mengandung karakter tidak diinginkan
@app.on_message(filters.text & ~filters.edited)
async def delete_messages_with_unwanted_chars(client, message):
    chat_id = message.chat.id
    # Cek apakah pesan berasal dari admin grup yang ditentukan
    chat_member = await client.get_chat_member(chat_id, message.from_user.id)
    if chat_member.status in ("administrator", "creator") and chat_member.chat.id == EXEMPTED_GROUP_ID:
        return
    # Hapus pesan yang mengandung karakter yang tidak diinginkan
    if any(char in message.text.lower() for char in UNWANTED_CHARS):
        await message.delete()
if __name__ == '__main__':
    app.run()
