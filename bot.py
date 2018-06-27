from estore.bot.runner import bot


def _run() -> None:
    bot.polling()


if __name__ == '__main__':
    _run()
