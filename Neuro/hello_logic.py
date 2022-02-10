import NeuroNetLibrary as nn
import NeuroVoiceLibrary as nv
from Neuro import hangup_logic
from Neuro import main_logic



def hello_main():
    """
    Функция входа для модуля
    :return:
    """
    nn.env('result', 'сброс на приветствии')
    with nv.listen((None, None, 500, 'AND'), entities=entity_list()) as listen_result:
        nv.say('Добрый день! Вас беспокоит компания X, мы проводим опрос удовлетворенности нашими услугами.\
                  Подскажите, вам удобно сейчас говорить?')
    return hello_rules(listen_result)


def hello_rules(listen_result):
    """
    Функция с логикой работы модуля
    :param listen_result:
    :return:
    """
    if not listen_result:
        nn.log('condition', 'NULL')
        return hello_null()
    elif listen_result.has_entity('voicemail') and listen_result.entity('voicemail') == 'true':
        return message_pattern('voicemail=true', 'автоответчик', 'hangup_null')
    elif listen_result.has_entity('confirm') and listen_result.entity('confirm') == 'true':
        main_logic.main()
        return message_pattern('confirm=true', 'да', None)
    elif listen_result.has_entity('confirm') and listen_result.entity('confirm') == 'false':
        return message_pattern('confirm=false', 'нет', 'hangup_wrong_time')
    elif listen_result.has_entity('wrong_time') and listen_result.entity('wrong_time') == 'true':
        return message_pattern('wrong_time=true', 'Занят', 'hangup_wrong_time')
    elif listen_result.has_entity('repeat') and listen_result.entity('repeat') == 'true':
        nn.log('condition', 'repeat=true')
        nn.env('result', 'Еще раз')
        return hello_repeat()
    else:
        return main_logic.recommend_main()


def message_pattern(*args):
    """
    Функция шаблона записи в лог и изменения окружения (env), отправляет сообщение для hangup
    :param args:
    :return:
    """
    condition, result, mes = args
    nn.log('condition', condition)
    nn.env('result', result)
    if mes: hangup_logic.hangup(mes)
    return condition


def hello_null():
    """
    Функция для обработки: "NULL - не сказано ни одного слова"
    :return:
    """
    with nv.listen((None, None, 500, 'AND'), entities=entity_list()) as listen_result:
        nv.say('Извините, вас не слышно. Вы могли бы повторить?')
        if not listen_result:
            nn.log('condition', 'NULL')
            hangup_logic.hangup('hangup_null')
            return 'NULL'
        else:
            return hello_rules(listen_result)


def hello_repeat():
    """
     Функция для обработки: "Еще раз", повтор
    :return:
    """
    with nv.listen((None, None, 500, 'AND'), entities=entity_list()) as listen_result:
        nv.say('Это компания X  Подскажите, вам удобно сейчас говорить?')
        return hello_rules(listen_result)
