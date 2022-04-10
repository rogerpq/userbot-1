#  قبل لا تفكر تخمط هذا الملف ترا الملف متعوب عليه لا تخمط واني حذرتك
# حسب قوانين موقع github https://github.com/VFF35-AR/JM-THON/blob/master/LICENSE
# تنص على انه اي شخص ياخذ الملف بدون ذكر حقوق طبع والنشر سيتم حذف حسابه من قبل صاحب الملف اقتضى التنوي
# Copyright ©️ 2021 VFF34 . All Rights Reserved
# You are free to use this code in any of your project, but you MUST include the following in your README.md (Copy & paste)
# ##Credits -  (  @RR7PP  - @VFF35  )

from userbot import *
from userbot import VFF35
from ..Config import Config
from ..sql_helper.globals import gvarstatus

VFF35_CMD = Config.SCPIC_CMD or "جلب الصورة"
VFF35_caption = gvarstatus("TEX_SEC") or "..."

@VFF35.on(admin_cmd(pattern=f"VFF35"))
async def dato(event):
    if not event.is_reply:
        return await event.edit("..")
    VFF34 = await event.get_reply_message()
    pic = await VFF34.download_media()
    await bot.send_file(
        "me",
        pic,
        caption=f"""
-تـم جـلب الصـورة بنجـاح ✅
- CH: @VFF35
- Dev: @VFF34
  """,
    )
    await event.edit(VFF35_caption)
