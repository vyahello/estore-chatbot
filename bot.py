from estore.bot.handler import bot


def _run() -> None:
    bot.polling(none_stop=True)


if __name__ == '__main__':
    _run()
