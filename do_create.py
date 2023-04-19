def do_create(self, args):
    """ Create an object of any class"""
    tokens = args.split()

    # extract class name and params
    class_name = tokens[0]

    params = tokens[1:]
    if not args:
        print("** class name missing **")
        return
    elif class_name not in HBNBCommand.classes:
        print("** class doesn't exist **")
        return
    # getting new instance object
    new_instance = HBNBCommand.classes[class_name]()

    for param in params:
        try:
            # splitting each params items to key and values
            k, v = param.split("=")
            # relacing the undescore with whitespace
            v = v.replace("_", " ")
            v = v.replace('"', '\\')
            if v[0] == '"' and v[-1] == '"' and len(v) > 1:
                # extract what i need
                v = v[1:-1]
            # if the value contains .
            if "." in v:
                # convert to a float
                v = float(v)
            else:
                # convert to an integer
                v = int(v)
            setattr(new_instance, k, v)

        except ValueError:
            continue
    storage.save()
    print(new_instance.id)
    storage.save()
