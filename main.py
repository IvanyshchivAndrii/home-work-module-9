PHONEB00K = {}


def add_contact():
    with open('phonebook.txt', 'r') as fd:
        for user in fd:
            users = user.split()
            PHONEB00K[users[0]] = users[1]


def input_error(func):
    def inner(*args):
        try:
            if 1 < len(args) <= 2 and args[0] != 'phone':
                print('Enter telephone number')
            elif len(args) <= 1 and args[0] == 'phone':
                print('Enter Username')
            elif len(args) <= 1 and args[0] in ['change', 'add']:
                print('Enter Username and telephone number')
            else:
                return func(*args)
        except KeyError:
            print('Enter existing or correct username')
        # except IndexError as e:
        #     print(e)

    return inner


def say_hallo(*args):
    print("How can I help you?")
    return ''


@input_error
def add_contact(*args):
    PHONEB00K[args[1].title()] = args[2]
    return ''


@input_error
def change_contact(*args):
    if args[1].title() in list(PHONEB00K):
        PHONEB00K[args[1].title()] = args[2]
    else:
        print(f'There is no {args[1]} in phonebook!')
    return ''


@input_error
def show_phone(*args):
    print(f'The number you have searched: {PHONEB00K[args[1].title()]}')
    return ''


def show_all_contacts(*args):
    num, name, tel = '№', 'Name', 'Phone'
    print(f'|{num:^5}|{name:^10}|{tel:^15}|')
    for k, v in enumerate(PHONEB00K):
        print(f'|{k:^5}|{v:^10}|{PHONEB00K[v]:^15}|')
    return ''


OPERATIONS = {
    'hello': say_hallo,
    'add': add_contact,
    'change': change_contact,
    'phone': show_phone,
    'show all': show_all_contacts
}


def get_hendler(*args):
    return OPERATIONS[args[0]]


def main():
    flag = True
    print('Hello!! This is your phonebook assistant. Let\'s start!!')
    while flag:
        request = input('Enter request>>>').lower()
        request_list = request.split()
        if request_list[0] in list(OPERATIONS):
            get_hendler(*request.split())(*request.split())
        elif ' '.join(request_list[0:2]) == 'show all':
            show_all_contacts()
        elif request in ['exit', 'close', 'good bye']:
            flag = False
        else:
            print('Please, write one of the command')

if __name__ == '__main__':
    main()
