#!/usr/bin/python3
"""Moduli huu unaelezea sehemu ya kuanzia ya mfasili wa amri.

Unabainisha darasa moja, `HBNBCommand()`, ambalo linaurithi
darasa la `cmd.Cmd`.
Moduli hii inabainisha dhana zinazoturuhusu kudhibiti mfumo wa hifadhi
yenye nguvu (FileStorage / DB). Dhana hii pia itaturuhusu kubadilisha
aina ya hifadhi kwa urahisi bila kusasisha msimbo wote.

Inaturuhusu kufanya kazi kwa njia ya maingiliano na isiyo ya maingiliano:
    - kuunda mfano wa data
    - kudhibiti (kuunda, kusasisha, kufuta, nk) vitu kupitia konsole / mfasili
    - kuhifadhi na kuendelea kuhifadhi vitu katika faili (JSON file)

Mfano wa matumizi ya kawaida:

    $ ./console
    (hbnb)

    (hbnb) help
    Amri zilizoelezwa (andika help <mada>):
    =======================================
    EOF  create  help  quit

    (hbnb)
    (hbnb) quit
    $
"""
import re
import cmd
import json
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.review import Review
from models.amenity import Amenity
from models.place import Place

current_classes = {'BaseModel': BaseModel, 'User': User,
                   'Amenity': Amenity, 'City': City, 'State': State,
                   'Place': Place, 'Review': Review}


class HBNBCommand(cmd.Cmd):
    """Mfasili wa amri.

    Darasa hili linawakilisha mfasili wa amri na kituo cha udhibiti
    cha mradi huu. Inabainisha vishughulishi vya kazi kwa amri zote
    zinazoingizwa kwenye konsole na kuita API zinazofaa za injini
    ya hifadhi kudhibiti data ya programu / mifano.

    Linaurithi darasa la `cmd.Cmd` la Python ambalo hutoa mfumo rahisi
    wa kuandika tafsiri za amri zenye mistari.
    """

    prompt = "(hbnb) "

    def precmd(self, line):
        """Hufafanua maagizo ya kutekelezwa kabla ya <line> kufasiriwa."""
        if not line:
            return '\n'

        pattern = re.compile(r"(\w+)\.(\w+)\((.*)\)")
        match_list = pattern.findall(line)
        if not match_list:
            return super().precmd(line)

        match_tuple = match_list[0]
        if not match_tuple[2]:
            if match_tuple[1] == "count":
                instance_objs = storage.all()
                print(len([v for _, v in instance_objs.items()
                           if type(v).__name__ == match_tuple[0]]))
                return "\n"
            return "{} {}".format(match_tuple[1], match_tuple[0])
        else:
            args = match_tuple[2].split(", ")
            if len(args) == 1:
                return "{} {} {}".format(
                    match_tuple[1], match_tuple[0],
                    re.sub("[\"\']", "", match_tuple[2]))
            else:
                match_json = re.findall(r"{.*}", match_tuple[2])
                if (match_json):
                    return "{} {} {} {}".format(
                        match_tuple[1], match_tuple[0],
                        re.sub("[\"\']", "", args[0]),
                        re.sub("\'", "\"", match_json[0]))
                return "{} {} {} {} {}".format(
                    match_tuple[1], match_tuple[0],
                    re.sub("[\"\']", "", args[0]),
                    re.sub("[\"\']", "", args[1]), args[2])

    def do_help(self, arg):
        """Kupata msaada kwa amri, andika help <mada>."""
        return super().do_help(arg)

    def do_EOF(self, line):
        """Amri ya EOF iliyojengwa ndani kushughulikia makosa kwa neema."""
        print("")
        return True

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """Override tabia ya msingi ya `mstari tupu + kurudi`."""
        pass

    def do_create(self, arg):
        """Huunda mfano mpya."""
        args = arg.split()
        if not validate_classname(args):
            return

        new_obj = current_classes[args[0]]()
        new_obj.save()
        print(new_obj.id)

    def do_show(self, arg):
        """Huchapisha uwakilishi wa mfano."""
        args = arg.split()
        if not validate_classname(args, check_id=True):
            return

        instance_objs = storage.all()
        key = "{}.{}".format(args[0], args[1])
        req_instance = instance_objs.get(key, None)
        if req_instance is None:
            print("** hakuna mfano uliopatikana **")
            return
        print(req_instance)

    def do_destroy(self, arg):
        """Hufuta mfano kulingana na jina la darasa na id."""
        args = arg.split()
        if not validate_classname(args, check_id=True):
            return

        instance_objs = storage.all()
        key = "{}.{}".format(args[0], args[1])
        req_instance = instance_objs.get(key, None)
        if req_instance is None:
            print("** hakuna mfano uliopatikana **")
            return

        del instance_objs[key]
        storage.save()

    def do_all(self, arg):
        """Huchapisha uwakilishi wa maandishi wa mifano yote."""
        args = arg.split()
        all_objs = storage.all()

        if len(args) < 1:
            print(["{}".format(str(v)) for _, v in all_objs.items()])
            return
        if args[0] not in current_classes.keys():
            print("** darasa halipo **")
            return
        else:
            print(["{}".format(str(v))
                  for _, v in all_objs.items() if type(v).__name__ == args[0]])
            return

    def do_update(self, arg: str):
        """Husasisisha mfano kulingana na jina la darasa na id."""
        args = arg.split(maxsplit=3)
        if not validate_classname(args, check_id=True):
            return

        instance_objs = storage.all()
        key = "{}.{}".format(args[0], args[1])
        req_instance = instance_objs.get(key, None)
        if req_instance is None:
            print("** hakuna mfano uliopatikana **")
            return

        match_json = re.findall(r"{.*}", arg)
        if match_json:
            payload = None
            try:
                payload: dict = json.loads(match_json[0])
            except Exception:
                print("** sintaksia batili")
                return
            for k, v in payload.items():
                setattr(req_instance, k, v)
            storage.save()
            return
        if not validate_attrs(args):
            return
        first_attr = re.findall(r"^[\"\'](.*?)[\"\']", args[3])
        if first_attr:
            setattr(req_instance, args[2], first_attr[0])
        else:
            value_list = args[3].split()
            setattr(req_instance, args[2], parse_str(value_list[0]))
        storage.save()


def validate_classname(args, check_id=False):
    """Hufanya ukaguzi kwenye args ili kuthibitisha jina la darasa."""
    if len(args) < 1:
        print("** jina la darasa linakosekana **")
        return False
    if args[0] not in current_classes.keys():
        print("** darasa halipo **")
        return False
    if len(args) < 2 and check_id:
        print("** kitambulisho cha mfano kinakosekana **")
        return False
    return True


def validate_attrs(args):
    """Hufanya ukaguzi kwenye args ili kuthibitisha sifa na maadili."""
    if len(args) < 3:
        print("** jina la sifa linakosekana **")
        return False
    if len(args) < 4:
        print("** thamani inakosekana **")
        return False
    return True


def is_float(x):
    """Huangalia ikiwa `x` ni float."""
    try:
        a = float(x)
    except (TypeError, ValueError):
        return False
    else:
        return True


def is_int(x):
    """Huangalia ikiwa `x` ni int."""
    try:
        a = float(x)
        b = int(a)
    except (TypeError, ValueError):
        return False
    else:
        return a == b


def parse_str(arg):
    """Huchanganua `arg` kuwa `int`, `float` au `string`."""
    parsed = re.sub("\"", "", arg)

    if is_int(parsed):
        return int(parsed)
    elif is_float(parsed):
        return float(parsed)
    else:
        return arg


if __name__ == "__main__":
    HBNBCommand().cmdloop()
