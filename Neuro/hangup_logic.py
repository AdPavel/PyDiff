import NeuroNetLibrary as nn
import NeuroVoiceLibrary as nv


def hangup(result) -> None:
    """
    Функция завершения разговора
    :param result:
    :return:
    """
    hangup_logic_dict = {
        'hangup_positive': {
            'mes': 'Отлично!  Большое спасибо за уделенное время! Всего вам доброго!',
            'status': 'высокая оценка'},
        'hangup_negative': {
            'mes': 'Я вас понял. В любом случае большое спасибо за уделенное время!  Всего вам доброго.',
            'status': 'низкая оценка'},
        'hangup_wrong_time': {
            'mes': 'Извините пожалуйста за беспокойство. Всего вам доброго',
            'status': 'нет времени для разговора'},
        'hangup_null': {
            'mes': 'Вас все равно не слышно, будет лучше если я перезвоню. Всего вам доброго',
            'status': 'проблемы с распознаванием'}}

    nv.say(hangup_logic_dict[result]['mes'])
    # nn.env('result', hangup_logic_dict[result]['status'])
    nn.log('condition', hangup_logic_dict[result]['status'])
    nn.dialog.result = nn.RESULT_DONE


# def hangup_positive():
# 	nv.say('Отлично!  Большое спасибо за уделенное время! Всего вам доброго!')
# 	nn.log('condition', 'высокая оценка')
# 	nn.dialog.result = nn.RESULT_DONE
#
# def hangup_negative():
# 	nv.say('Я вас понял. В любом случае большое спасибо за уделенное время!  Всего вам доброго.')
# 	nn.log('condition', 'низкая оценка')
# 	nn.dialog.result = nn.RESULT_DONE
#
# def hangup_wrong_time():
# 	nv.say('Извините пожалуйста за беспокойство. Всего вам доброго')
# 	nn.log('condition', 'нет времени для разговора')
# 	nn.dialog.result = nn.RESULT_DONE
#
# def hangup_null():
# 	nv.say('Вас все равно не слышно, будет лучше если я перезвоню. Всего вам доброго')
# 	nn.log('condition', 'проблемы с распознаванием')
# 	nn.dialog.result = nn.RESULT_DONE
