#  قبل لا تفكر تخمط هذا الملف ترا الملف متعوب عليه لا تخمط واني حذرتك
# حسب قوانين موقع github https://github.com/VFF35-AR/JM-THON/blob/master/LICENSE
# تنص على انه اي شخص ياخذ الملف بدون ذكر حقوق طبع والنسر سيتم حذف حسابه من قبل صاحب الملف اقتضى التنوي
# Copyright ©️ 2021 RR9R7 . All Rights Reserved
# You are free to use this code in any of your project, but you MUST include the following in your README.md (Copy & paste)
# ##Credits -  (  @RR7PP  - @VFF35  )
#

# 𝗧𝗲𝗹𝗲𝗚𝗿𝗮𝗠 : @EITHON  ~ @RR7PPimport re
# 𝗧𝗲𝗹𝗲𝗚𝗿𝗮𝗠 : @EITHON  ~ @RR7PP

import re

from telethon import Button
from telethon.events import CallbackQuery, InlineQuery

from userbot import VFF35

# 𝗧𝗲𝗹𝗲𝗚𝗿𝗮𝗠 : @VFF35  ~ @RR7PP
from ..core.decorators import check_owner

CALC = {}

plugin_category = "utils"

m = [
    "AC",
    "C",
    "⌫",
    "%",
    "7",
    "8",
    "9",
    "+",
    "4",
    "5",
    "6",
    "-",
    "1",
    "2",
    "3",
    "x",
    "00",
    "0",
    ".",
    "÷",
]
tultd = [Button.inline(f"{x}", data=f"calc{x}") for x in m]
lst = list(zip(tultd[::4], tultd[1::4], tultd[2::4], tultd[3::4]))
lst.append([Button.inline("=", data="calc=")])


@EITHON.on(admin_cmd(pattern="حاسبة(?:\s|$)([\s\S]*)"))
async def icalc(e):
    if e.client._bot:
        return await e.reply(
            "**الحـاسبة العـلمية لسـورس ايثون\n @VFF35**", buttons=lst
        )
    results = await e.client.inline_query(Config.TG_BOT_USERNAME, "calc")
    await results[0].click(e.chat_id, silent=True, hide_via=True)
    await e.delete()


@EITHON.tgbot.on(InlineQuery)
async def inlinecalc(event):
    query_user_id = event.query.user_id
    query = event.text
    string = query.lower()
    if (
        query_user_id == Config.OWNER_ID or query_user_id in Config.SUDO_USERS
    ) and string == "calc":
        event.builder
        calc = event.builder.article(
            "Calc", text="**الحـاسبة العـلمية لسـورس ايثون\n @EITHON**", buttons=lst
        )
        await event.answer([calc])


# 𝗧𝗲𝗹𝗲𝗚𝗿𝗮𝗠 : @EITHON  ~ @RR7PP
@EITHON.tgbot.on(CallbackQuery(data=re.compile(b"calc(.*)")))
@check_owner
async def _(e):  # sourcery no-metrics
    x = (e.data_match.group(1)).decode()
    user = e.query.user_id
    get = None
    if x == "AC":
        if CALC.get(user):
            CALC.pop(user)
        await e.edit(
            "**الحـاسبة العـلمية لسـورس ايثون\n @EITHON**",
            buttons=[Button.inline("افتح مره اخرى", data="recalc")],
        )
    elif x == "C":
        if CALC.get(user):
            CALC.pop(user)
        await e.answer("تم الحذف")
    elif x == "⌫":
        if CALC.get(user):
            get = CALC[user]
        if get:
            CALC.update({user: get[:-1]})
            await e.answer(str(get[:-1]))
    elif x == "%":
        if CALC.get(user):
            get = CALC[user]
        if get:
            CALC.update({user: get + "/100"})
            await e.answer(str(get + "/100"))
    elif x == "÷":
        if CALC.get(user):
            get = CALC[user]
        if get:
            CALC.update({user: get + "/"})
            await e.answer(str(get + "/"))
    elif x == "x":
        if CALC.get(user):
            get = CALC[user]
        if get:
            CALC.update({user: get + "*"})
            await e.answer(str(get + "*"))
    elif x == "=":
        if CALC.get(user):
            get = CALC[user]
        if get:
            if get.endswith(("*", ".", "/", "-", "+")):
                get = get[:-1]
            out = eval(get)
            try:
                num = float(out)
                await e.answer(f"▾∮ الجـواب : {num}", cache_time=0, alert=True)
            except BaseException:
                CALC.pop(user)
                await e.answer("خـطأ", cache_time=0, alert=True)
        await e.answer("غير معروف")
    else:
        if CALC.get(user):
            get = CALC[user]
        if get:
            CALC.update({user: get + x})
            return await e.answer(str(get + x))
        CALC.update({user: x})
        await e.answer(str(x))


# 𝗧𝗲𝗹𝗲𝗚𝗿𝗮𝗠 : @EITHON  ~ @RR7PP
@EITHON.tgbot.on(CallbackQuery(data=re.compile(b"recalc")))
@check_owner
async def _(e):
    m = [
        "AC",
        "C",
        "⌫",
        "%",
        "7",
        "8",
        "9",
        "+",
        "4",
        "5",
        "6",
        "-",
        "1",
        "2",
        "3",
        "x",
        "00",
        "0",
        ".",
        "÷",
    ]
    tultd = [Button.inline(f"{x}", data=f"calc{x}") for x in m]
    lst = list(zip(tultd[::4], tultd[1::4], tultd[2::4], tultd[3::4]))
    lst.append([Button.inline("=", data="calc=")])
    await e.edit("**الحـاسبة العـلمية لسـورس ايثون\n @EITHON**", buttons=lst)


# 𝗧𝗲𝗹𝗲𝗚𝗿𝗮𝗠 : @EITHON  ~ @RR7PP

CMD_HELP.update(
    {"الحسابة": ".حاسبة" "\n فقط اكتب الامر لعرض حاسبة علميه تحتاج الى تفعيل وضع الانلاين اولا\n\n"}
)