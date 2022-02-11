import NeuroNetLibrary as nn
import NeuroVoiceLibrary as nv
from Neuro import hangup_logic
from Neuro import hello_logic

def main() -> object:
    """
    Функция для опроса при положительном ответе респондента
    :return:
    """
    recommend_main()
    pass

def recommend_main() -> object:
    """
    Функция начального сообщения модуля
    :return:
    """
    with nv.listen((None, None, 500, 'AND'), entities=entity_list()) as listen_result:
        nv.say('Скажите, а готовы ли вы рекомендовать нашу компанию своим друзьям? Оцените, пожалуйста, по шкале от '
               '«0» до «10», где «0» - не буду рекомендовать, «10» - обязательно порекомендую.')
     return main_rules(listen_result)

def main_rules(listen_result: object):
    """
    Функция с логикой работы модуля
    :param listen_result:
    :return:
    """
    if not listen_result:
        nn.log('condition', 'NULL')
        return recommend_null()
    elif listen_result.has_entity('recommendation_score')\
         and listen_result.entity('recommendation_score') in range(9):
        return hello_logic.message_pattern('recommendation_score=[0…8]', listen_result.entity(
            'recommendation_score'), 'hangup_negative')
    elif listen_result.has_entity('recommendation_score')\
         and listen_result.entity('recommendation_score') in range(9,11):
        return hello_logic.message_pattern('recommendation_score=[9…10]', listen_result.entity(
            'recommendation_score'), 'hangup_positive')
    elif listen_result.has_entity('recommendation') and listen_result.entity('recommendation') == 'positive':
        return recommend_score('positive', 'recommendation=positive', 'Да')
        # return recommend_score_positive()
    elif listen_result.has_entity('recommendation') and listen_result.entity('recommendation') == 'negative':
        return recommend_score('negative', 'recommendation=negative', 'Нет')
        # return recommend_score_negative()
    elif listen_result.has_entity('recommendation') and listen_result.entity('recommendation') == 'neutral':
        return recommend_score('neutral', 'recommendation=neutral', 'Возможно')
        # return recommend_score_neutral()
    elif listen_result.has_entity('repeat') and listen_result.entity('repeat') == 'true':
        return recommend_score('repeat', 'repeat=true', 'Еще раз')
        # return recommend_repeat()
    elif listen_result.has_entity('recommendation') and listen_result.entity('recommendation') == 'dont_know':
        return recommend_score('dont_know', 'recommendation=dont_know', 'Не знаю')
        # return recommend_repeat_2()
    elif listen_result.has_entity('wrong_time') and listen_result.entity('wrong_time') == 'true':
        return hello_logic.message_pattern('wrong_time=true', 'Занят', 'hangup_wrong_time')
    elif listen_result.has_entity('question') and listen_result.entity('question') == 'true':
        nn.log('condition', 'question=true')
        nn.env('result', 'Вопрос')
        return forward()
    else:
        return recommend_default()


def recommend_null() -> object:
    """
        Функция для обработки: "NULL - не сказано ни одного слова"
    :return:
    """
    with nv.listen((None, None, 500, 'AND'), entities=entity_list()) as listen_result:
        nv.say('Извините вас совсем не слышно,  повторите пожалуйста?')
        if not listen_result:
            nn.log('condition', 'NULL')
            hangup_logic.hangup('hangup_null')
            return None
        else:
            return main_rules(listen_result)

def recommend_score(status: str, *args) -> object:
    """
    Общая функция обработки ответов
    :type args: tuple(str, str)
    :param status:
    :param args:
    :return:
    """
    condition, result = args
    nn.log('condition', condition)
    nn.env('result', result)
    message_dict = {'positive': 'Хорошо,  а по 10-ти бальной шкале как бы вы оценили 8-9 или может 10 ?',
                    'negative': 'Ну а от 0 до 10 как бы вы оценили бы: 0, 5 или может 7 ?',
                    'neutral': 'Ну а от 0 до 10 как бы вы оценили ?',
                    'repeat': 'Как бы вы оценили возможность порекомендовать нашу компанию своим знакомым по шкале от 0'
                              ' до 10, где 0 - точно не порекомендую, 10 - обязательно порекомендую.',
                    'dont_know': 'Ну если бы вас попросили порекомендовать нашу компанию друзьям или знакомым, '
                                 'вы бы стали это делать? Если «да» - то оценка «10», если точно нет – «0».'
                    }

    with nv.listen((None, None, 500, 'AND'), entities=entity_list()) as listen_result:
        nv.say(message_dict[status])
        return main_rules(listen_result)

def forward() -> object:
    """
    Функция перевода на оператора
    :return:
    """
    with nv.listen((None, None, 500, 'AND'), entities=entity_list()) as listen_result:
            nv.say('Чтобы разобраться в вашем вопросе, я переключу звонок на моих коллег. Пожалуйста оставайтесь на линии.')
     nn.env('result', 'перевод на оператора')
     pass

def recommend_default() -> object:
    """
    Функция при не подходящих ответах
    :return:
    """
    with nv.listen((None, None, 500, 'AND'), entities=entity_list()) as listen_result:
        nv.say('повторите пожалуйста ')
        return main_rules(listen_result)

# def recommend_score_positive():
#     with nv.listen((None, None, 500, 'AND'), entities=entity_list()) as listen_result:
#         nv.say('Хорошо,  а по 10-ти бальной шкале как бы вы оценили 8-9 или может 10 ?')
#         return recommend_main(listen_result)

# def recommend_score_negative():
#     with nv.listen((None, None, 500, 'AND'), entities=entity_list()) as listen_result:
#         nv.say('Ну а от 0 до 10 как бы вы оценили бы: 0, 5 или может 7 ?')
#         return recommend_main(listen_result)

# def recommend_score_neutral():
#     with nv.listen((None, None, 500, 'AND'), entities=entity_list()) as listen_result:
#             nv.say('Ну а от 0 до 10 как бы вы оценили ?')
#             return recommend_main(listen_result)

# def recommend_repeat():
#     with nv.listen((None, None, 500, 'AND'), entities=entity_list()) as listen_result:
#             nv.say('Как бы вы оценили возможность порекомендовать нашу компанию своим знакомым по шкале от 0 до 10, '
#                    'где 0 - точно не порекомендую, 10 - обязательно порекомендую.')
#             return recommend_main(listen_result)

# def recommend_repeat_2():
#     with nv.listen((None, None, 500, 'AND'), entities=entity_list()) as listen_result:
#                 nv.say('Ну если бы вас попросили порекомендовать нашу компанию друзьям или знакомым, вы бы стали это '
#                        'делать? Если «да» - то оценка «10», если точно нет – «0».')
#                 return recommend_main(listen_result)
